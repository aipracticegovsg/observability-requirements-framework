#!/usr/bin/env python3
"""Generate the static Metric Definitions page from the YAML sources.

    python scripts/gen_pages.py

Output: docs/framework/metric-definitions.md
"""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "framework" / "metric-definitions.md"


def load(name: str):
    with (DATA / name).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def collapse(text: str) -> str:
    return " ".join(text.split())


def main() -> None:
    categories = load("categories.yaml")
    requirements = load("requirements.yaml")

    lines = [
        "# Metric Definitions",
        "",
        "Mathematical definitions for every metric, log, and trace in the "
        "[Requirements Table](requirements-table.md), so that any two agencies "
        "following the specification compute numerically comparable values. The "
        "tier marker (1–4) maps to the [requirements matrix](requirements-matrix.md).",
        "",
        "!!! note \"Generated file\"",
        "    This page is generated from `data/requirements.yaml` by "
        "`scripts/gen_pages.py`. Do not edit it by hand.",
        "",
    ]

    for block in requirements:
        cat = block["category"]
        lines.append(f"## {categories[cat]['name']} `{cat}`")
        lines.append("")
        lines.append("| Tier | Type | Telemetry Item | Mathematical Definition |")
        lines.append("| --- | --- | --- | --- |")
        for risk in block["risks"]:
            for item in risk["items"]:
                name = collapse(item["name"]).replace("|", "\\|")
                defn = collapse(item["definition"]).replace("|", "\\|")
                lines.append(
                    f"| {item['tier']} | {item['type']} | "
                    f"**{item['id']}** — {name} | {defn} |"
                )
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
