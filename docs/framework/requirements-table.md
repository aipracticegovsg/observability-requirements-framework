# Observability Requirements Table

The full requirements table, organised by operational category. Each telemetry
item is annotated with its **priority tier** (1–4) and the **action** required at
each system risk level (read from the [requirements matrix](requirements-matrix.md)).

Use the column header filters to narrow by type, tier, or text. **Click any row**
to see its mathematical definition, the risk it mitigates, the impact, and the
mitigations.

<div id="orf-requirements-table"></div>

!!! tip "Regenerating this table"
    The table is rendered from `docs/assets/requirements.json`, generated from the
    YAML in `data/`. After editing the data, run `python scripts/build_json.py`.

---

If JavaScript is disabled, see [Metric Definitions](metric-definitions.md) for the
same items in static form, or read [`data/requirements.yaml`](https://github.com/)
directly.
