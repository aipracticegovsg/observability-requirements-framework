# Telemetry Requirements Matrix

The matrix separates two ideas that are often conflated. The **tier** of a
telemetry item is an intrinsic property of the item — how foundational it is,
independent of any deployment. The **action** required of an agency is the
intersection of that tier with the system's risk level.

## The three actions

- **Mandatory** — must be implemented, with no waiver permitted.
- **Mandatory but Waivable** — must be implemented unless a waiver is obtained
  from the agency's responsible-AI oversight function with a documented risk
  acceptance.
- **Good-to-Have** — strongly encouraged but not required; agencies may implement
  it based on their specific needs and constraints.

## Table 1 — Requirements Matrix

| Priority tier | High-Risk System | Medium-Risk System | Low-Risk System |
| --- | --- | --- | --- |
| **Tier 1** | Mandatory | Mandatory | Good-to-Have |
| **Tier 2** | Mandatory | Mandatory but Waivable | Good-to-Have |
| **Tier 3** | Mandatory but Waivable | Good-to-Have | Good-to-Have |
| **Tier 4** | Good-to-Have | Good-to-Have | Good-to-Have |

The matrix is deliberately **proportional**: as risk decreases, the action
attaches one step lower on the same item, so low-risk pilots are not held to the
same evidentiary standard as high-impact citizen-facing deployments.

## Priority tiers

- **Tier 1** — the most foundational telemetry: prompt/response logs, tool-call
  logs, basic error logs.
- **Tier 2** — incident investigation and accountability: knowledge-base access
  logs, distributed traces, override tracking.
- **Tier 3** — deeper performance and safety analysis: drift detection,
  override-reason annotations, segment-wise fairness measures.
- **Tier 4** — research-grade or aspirational: hallucination rate on labelled
  samples, bias auditing on representative test sets.
