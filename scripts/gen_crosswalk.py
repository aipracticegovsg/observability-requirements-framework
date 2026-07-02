#!/usr/bin/env python3
"""Generate the ORF↔ARC crosswalk page from the YAML sources.

    python scripts/gen_crosswalk.py

Output: docs/framework/crosswalk.md
"""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "framework" / "crosswalk.md"
ARC_REPO = "https://github.com/govtech-responsibleai/agentic-risk-capability-framework"


def load(name: str):
    with (DATA / name).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def collapse(text: str) -> str:
    return " ".join((text or "").split())


def basis_badge(basis: str) -> str:
    return f'<span class="orf-basis orf-basis-{basis}">{basis}</span>'


def main() -> None:
    categories = load("categories.yaml")
    requirements = load("requirements.yaml")
    arc = load("arc_controls.yaml")
    crosswalk = {row["orf_risk"]: row for row in load("crosswalk.yaml")}

    lines = [
        "# ARC Control Crosswalk",
        "",
        "This page maps each ORF risk group — and the telemetry items beneath it —",
        f"to the controls in GovTech's [Agentic Risk & Capability (ARC) framework]({ARC_REPO})",
        "that the telemetry supports or evidences. ORF is the *evidentiary substrate*:",
        "its metrics, logs, and traces are the data that demonstrates ARC controls are",
        "actually working.",
        "",
        "!!! warning \"How to read the *basis* column\"",
        '    **explicit** — the ORF Technical Paper references this ARC theme or control'
        " directly in the risk text or mitigations.  ",
        '    **thematic** — a reasoned alignment by this repo; it is *not* stated verbatim'
        " in the ORF paper and should be treated as interpretive.",
        "",
    ]

    # Index risk groups by category, preserving paper order.
    for block in requirements:
        cat = block["category"]
        lines.append(f"## {categories[cat]['name']} `{cat}`")
        lines.append("")
        for risk in block["risks"]:
            rid = risk.get("id")
            cw = crosswalk.get(rid)
            item_ids = ", ".join(item["id"] for item in risk["items"])
            lines.append(f"### {rid} — {collapse(risk['risk'])}")
            lines.append("")
            lines.append(f"*ORF items:* {item_ids}")
            lines.append("")
            if not cw or not cw.get("controls"):
                lines.append("_No ARC control mapping recorded._")
                lines.append("")
                continue
            if cw.get("note"):
                lines.append(f"> {collapse(cw['note'])}")
                lines.append("")
            lines.append("| ARC Control | Name | Basis |")
            lines.append("| --- | --- | --- |")
            for c in cw["controls"]:
                cid = c["control"]
                name = arc.get(cid, "(unknown control)")
                lines.append(f"| `{cid}` | {name} | {basis_badge(c['basis'])} |")
            lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    n = sum(len(c.get("controls", [])) for c in crosswalk.values())
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(crosswalk)} risk groups, {n} control links)")


if __name__ == "__main__":
    main()
