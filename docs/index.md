# Observability Requirements Framework (ORF)

A structured, **risk-tiered telemetry specification** for generative and agentic
AI systems in the public sector. The ORF organises telemetry into **six
operational categories**, pairs each requirement with a **mathematical metric
definition**, and maps every item to a **four-tier priority matrix** keyed to
system risk level.

The framework is the *evidentiary substrate* that connects high-level governance
principles — Singapore's Model AI Governance Framework for Generative AI, the
Model AI Governance Framework for Agentic AI, and GovTech's Agentic Risk &
Capability (ARC) framework — to concrete engineering practice.

## How to navigate

| Section | What you'll find |
| --- | --- |
| [Introduction](framework/introduction.md) | The observability gap and what the framework is for |
| [Operational Categories](framework/operational-categories.md) | The six categories of telemetry |
| [Risk Tiering](framework/risk-tiering.md) | Low / Medium / High system risk tiers |
| [Requirements Matrix](framework/requirements-matrix.md) | Tier × risk → Mandatory / Waivable / Good-to-Have |
| [Requirements Table](framework/requirements-table.md) | **Interactive** table of every telemetry item |
| [Metric Definitions](framework/metric-definitions.md) | Mathematical definition of every item |
| [Adoption Strategy](implementation/strategy.md) | The three-phase implementation path |

## Source of truth

All framework content lives as YAML under `data/` and is rendered into these
pages:

```
data/
├── categories.yaml      # the six operational categories
├── risk_tiers.yaml      # Low / Medium / High system risk tiers
├── priority_tiers.yaml  # Tier 1–4 telemetry priority
├── matrix.yaml          # the requirements matrix (Table 1)
└── requirements.yaml    # every risk → impact → control → telemetry item (Tables 2 + 3)
```

To regenerate the interactive table after editing the data, run
`python scripts/build_json.py`.
