# Adoption Strategy

Agencies running **Medium-** or **High-Risk** systems should adopt the framework
through three implementation phases. Agencies running **Low-Risk** pilots are not
expected to follow the full phasing, but are encouraged to adopt Tier 1 items as
good practice and to revisit the matrix when the system progresses toward
production.

## Phase 1 — Tier 1 substrate + offline batch evaluation

Concentrates on **Tier 1** items and stands up offline batch evaluation. This
phase establishes the trace and log substrate — prompts, responses, tool calls,
error logs, refusals, system telemetry — and ensures data flows are captured
before any analysis is layered on top.

## Phase 2 — Tier 2 + incident-investigation workflows

Adds **Tier 2** items and incident-investigation workflows, including
knowledge-base access logs, distributed request traces, override and handover
tracking, and privacy-incident logging.

## Phase 3 — Tier 3 & Tier 4 analytics

Introduces the **Tier 3 and Tier 4** items that require more sophisticated
infrastructure — drift metrics, hallucination evaluation, fairness indicators,
and bias auditing on representative test sets.

## Lean on existing instrumentation

At each phase, lean on existing instrumentation where it exists:

- **OpenTelemetry**-based distributed tracing for system telemetry.
- Structured logging pipelines for security telemetry.
- LLM-specific observability platforms such as **Langfuse** or **Arize Phoenix**
  for prompt–response and trace logging.

The phasing recommends a *sequence* in which to address items; the
[requirements matrix](../framework/requirements-matrix.md) determines what is
actually *required* of the agency at each step for its risk level.
