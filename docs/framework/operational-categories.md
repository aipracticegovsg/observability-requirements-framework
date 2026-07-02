# Operational Categories

The framework organises telemetry requirements into six categories that jointly
cover the artefacts necessary to reconstruct, evaluate, and govern an agentic
system.

## 1. Agent-Level Observability `AGT`

Supports debugging of individual queries, provides visibility into agent decision
pathways, surfaces anomalies in output, supports root-cause analysis, and
provides an audit trail for accountability.

## 2. Agent Performance `PERF`

Tracks changes in input and output distributions, measures groundedness and
factual accuracy, captures human oversight and intervention rates, and quantifies
safety and fairness indicators.

## 3. User Interaction & Behaviour `UX`

Assesses user satisfaction and engagement, identifies common intents and usage
patterns, surfaces UX pain points, detects abuse and misuse, and supports
feedback-driven improvement.

## 4. System Performance, Health & Reliability `SYS`

Tracks availability, efficiency, regression, anomaly detection, SRE readiness,
post-incident analysis, and SLA conformance.

## 5. Safety & Security Compliance `SEC`

Monitors policy enforcement, boundary containment, responsible-AI compliance,
sensitive-data handling, and threat detection.

## 6. Product Lifecycle & Governance `GOV`

Captures the maturity and effectiveness of the agency's LLMOps and AgentOps
processes, change and audit controls, and the cadence of structured review.

---

See the [Requirements Table](requirements-table.md) for the full set of telemetry
items in each category, and [Metric Definitions](metric-definitions.md) for their
mathematical definitions.
