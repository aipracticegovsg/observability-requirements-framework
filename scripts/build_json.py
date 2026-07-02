#!/usr/bin/env python3
"""Flatten the YAML sources in data/ into a single JSON file that the
interactive Tabulator table (docs/javascripts/requirements-table.js) consumes.

Run this whenever data/*.yaml changes:

    python scripts/build_json.py

Output: docs/assets/requirements.json
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "assets" / "requirements.json"


def load(name: str):
    with (DATA / name).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main() -> None:
    categories = load("categories.yaml")
    matrix = load("matrix.yaml")
    requirements = load("requirements.yaml")

    action_labels = {k: v["label"] for k, v in matrix["actions"].items()}
    tier_matrix = matrix["matrix"]

    rows = []
    for block in requirements:
        cat_key = block["category"]
        cat_name = categories[cat_key]["name"]
        for risk in block["risks"]:
            for item in risk["items"]:
                tier = item["tier"]
                actions = tier_matrix[tier]
                rows.append(
                    {
                        "id": item["id"],
                        "category": cat_key,
                        "category_name": cat_name,
                        "tier": tier,
                        "type": item["type"],
                        "name": " ".join(item["name"].split()),
                        "definition": " ".join(item["definition"].split()),
                        "risk": " ".join(risk["risk"].split()),
                        "impact": " ".join(risk["impact"].split()),
                        "mitigations": " ".join(risk["mitigations"].split()),
                        "high": action_labels[actions["high"]],
                        "medium": action_labels[actions["medium"]],
                        "low": action_labels[actions["low"]],
                    }
                )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)

    print(f"Wrote {len(rows)} telemetry items to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
