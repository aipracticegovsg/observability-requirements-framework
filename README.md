# Observability Requirements Framework (ORF)

A structured, **risk-tiered telemetry specification** for generative and agentic
AI systems in the public sector, published as a static [MkDocs](https://www.mkdocs.org/)
site. The framework organises telemetry into six operational categories, pairs
each requirement with a mathematical metric definition, and maps every item to a
four-tier priority matrix keyed to system risk level.

This repository mirrors the architecture of GovTech's
[Agentic Risk & Capability (ARC) framework](https://github.com/govtech-responsibleai/agentic-risk-capability-framework):
**YAML data files** drive the content, MkDocs (Material theme) renders the site,
and an interactive table (Tabulator.js) makes the requirements browsable.

## Repository layout

```
orf-framework/
├── mkdocs.yml                 # site config, nav, theme, Tabulator assets
├── requirements.txt           # Python deps (mkdocs, mkdocs-material, PyYAML)
├── data/                      # ← single source of truth (edit here)
│   ├── categories.yaml        # the six operational categories
│   ├── risk_tiers.yaml        # Low / Medium / High system risk tiers
│   ├── priority_tiers.yaml    # Tier 1–4 telemetry priority
│   ├── matrix.yaml            # the requirements matrix (Table 1)
│   └── requirements.yaml      # every risk → impact → control → item (Tables 2 + 3)
├── docs/                      # MkDocs content
│   ├── index.md
│   ├── framework/             # introduction, categories, tiering, matrix, table, definitions
│   ├── implementation/        # adoption strategy
│   ├── assets/                # generated requirements.json (do not edit by hand)
│   ├── javascripts/           # Tabulator table renderer
│   └── stylesheets/           # tier / action styling
└── scripts/
    ├── build_json.py          # data/*.yaml → docs/assets/requirements.json
    ├── gen_pages.py           # data/*.yaml → docs/framework/metric-definitions.md
    ├── gen_crosswalk.py       # data/*.yaml → docs/framework/crosswalk.md (ORF↔ARC)
    └── validate.py            # schema / unique-id / tier / crosswalk + JS guards
```

## Quick start

```bash
python -m pip install -r requirements.txt

python scripts/validate.py      # sanity-check the data
python scripts/build_json.py    # regenerate the interactive table data
python scripts/gen_pages.py     # regenerate the static metric-definitions page

mkdocs serve                    # preview at http://127.0.0.1:8000
mkdocs build                    # produce ./site for deployment
```

## Editing the framework

All content lives in `data/`. To add or change a telemetry item, edit
`data/requirements.yaml`, then re-run `validate.py`, `build_json.py`, and
`gen_pages.py`. Item IDs follow `ORF-<CATEGORY>-<nn>`.

## Deployment (GitHub Pages)

```bash
mkdocs gh-deploy            # builds and pushes to the gh-pages branch
```

Set the repo's Pages source to the `gh-pages` branch.

## Provenance

Content transcribed from *"An Observability Requirements Framework for Generative
AI Systems in the Public Sector"* (Low, Yan, Ong & Ng; AI Practice, GovTech
Singapore), Tables 1–3 and Sections 7.3–7.7.
