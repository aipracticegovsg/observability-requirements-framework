# Introduction

As generative AI moves from pilots to production-facing services across the
public sector, agencies face a systemic **observability gap**: telemetry
practices inherited from earlier machine-learning operations do not capture the
artefacts that matter for generative AI oversight — reasoning traces, tool
invocations, retrieval provenance, refusal events, and groundedness signals.

Public sector deployments must answer to citizens, regulators, parliamentary
oversight, and internal audit, all of which expect detailed evidence about how a
system behaved over time — not only what it did, but what it chose *not* to do,
what alternatives it considered, what data it retrieved, and which guardrails
were activated.

## What the framework provides

The ORF is **risk-tiered**, **implementation-agnostic**, and designed to be
adopted by agencies at very different levels of technical maturity. It:

1. Organises telemetry into **six operational categories** that jointly cover the
   artefacts needed to reconstruct, evaluate, and govern an agentic system.
2. Pairs each category with a table of **metrics, logs, and traces**.
3. Provides a **mathematical definition** for each metric, so two agencies
   following the spec compute numerically comparable values.
4. Maps each item to a **four-tier priority matrix** keyed to system risk level.

## Terminology: session, query, task, request

The framework defines a hierarchy of execution units, consistent with the
OpenTelemetry GenAI agent semantic conventions:

- **Query** — a user-issued natural-language prompt that initiates a session or
  task.
- **Task** — a discrete goal the agent attempts in response to a query, which may
  require multiple reasoning steps, subtasks, or tool invocations.
- **Request** — a specific operation or API call performed by the agent during a
  task; multiple requests make up the actions of a single task.
- **Session** — a complete unit of interaction encompassing one or more queries
  and all downstream tasks and requests.
