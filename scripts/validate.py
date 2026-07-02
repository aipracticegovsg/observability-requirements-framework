#!/usr/bin/env python3
"""Sanity-check the ORF data files: schema, unique IDs, valid tiers/categories.

    python scripts/validate.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS_JS = ROOT / "docs" / "javascripts"
VALID_TYPES = {"metric", "log", "trace"}
_SELECTOR_RE = re.compile(r'script\[src\$="javascripts/([^"]+)"\]')


def load(name: str):
    with (DATA / name).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _unterminated_string(line: str) -> bool:
    """True if a single-line JS string literal is left open at end of line.

    Walks the line tracking quote state with backslash escaping, and stops at a
    `//` line comment when outside a string. This is robust to apostrophes inside
    double-quoted strings (and vice versa), so it flags the real bug class
    (a string opened with " but closed with ') without false-positiving on
    contractions. Assumes no template literals / block comments (none are used).
    """
    state = None  # None | '"' | "'"
    escaped = False
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if state is not None:
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == state:
                state = None
        elif c in ('"', "'"):
            state = c
        elif c == "/" and i + 1 < n and line[i + 1] == "/":
            break  # line comment outside a string
        i += 1
    return state is not None


def check_js(errors: list[str]) -> int:
    """Guard the interactive scripts against the two errors that previously
    reached the browser: unterminated string literals, and a self-locator
    selector that no longer matches the file's own name (e.g. after a rename).
    """
    checked = 0
    for path in sorted(DOCS_JS.glob("*.js")):
        checked += 1
        text = path.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            if _unterminated_string(line):
                errors.append(f"[{path.name}:{n}] unterminated string literal")
        m = _SELECTOR_RE.search(text)
        if m and m.group(1) != path.name:
            errors.append(
                f"[{path.name}] self-locator selector points to "
                f"'javascripts/{m.group(1)}' but file is named '{path.name}'"
            )
    return checked


def main() -> int:
    categories = load("categories.yaml")
    priority_tiers = {int(k) for k in load("priority_tiers.yaml")}
    requirements = load("requirements.yaml")
    arc = load("arc_controls.yaml")
    crosswalk = load("crosswalk.yaml")

    errors: list[str] = []
    seen_ids: set[str] = set()
    risk_ids: set[str] = set()
    count = 0

    for block in requirements:
        cat = block["category"]
        if cat not in categories:
            errors.append(f"Unknown category: {cat}")
        for risk in block["risks"]:
            if risk.get("id"):
                risk_ids.add(risk["id"])
            for field in ("id", "risk", "impact", "mitigations", "items"):
                if not risk.get(field):
                    errors.append(f"[{cat}] risk missing '{field}'")
            for item in risk.get("items", []):
                count += 1
                iid = item.get("id", "<no-id>")
                if iid in seen_ids:
                    errors.append(f"Duplicate item id: {iid}")
                seen_ids.add(iid)
                if item.get("tier") not in priority_tiers:
                    errors.append(f"[{iid}] invalid tier: {item.get('tier')}")
                if item.get("type") not in VALID_TYPES:
                    errors.append(f"[{iid}] invalid type: {item.get('type')}")
                if not item.get("definition"):
                    errors.append(f"[{iid}] missing definition")

    # Crosswalk integrity: every referenced ORF risk and ARC control must exist.
    for row in crosswalk:
        rid = row.get("orf_risk")
        if rid not in risk_ids:
            errors.append(f"[crosswalk] unknown ORF risk id: {rid}")
        for c in row.get("controls", []):
            if c.get("control") not in arc:
                errors.append(f"[crosswalk {rid}] unknown ARC control: {c.get('control')}")
            if c.get("basis") not in {"explicit", "thematic"}:
                errors.append(f"[crosswalk {rid}] invalid basis: {c.get('basis')}")

    js_checked = check_js(errors)

    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {count} telemetry items across {len(requirements)} categories, "
          f"all IDs unique and well-formed; {js_checked} JS file(s) clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
