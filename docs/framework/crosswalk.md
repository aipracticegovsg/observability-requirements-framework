# ARC Control Crosswalk

This page maps each ORF risk group — and the telemetry items beneath it —
to the controls in GovTech's [Agentic Risk & Capability (ARC) framework](https://github.com/govtech-responsibleai/agentic-risk-capability-framework)
that the telemetry supports or evidences. ORF is the *evidentiary substrate*:
its metrics, logs, and traces are the data that demonstrates ARC controls are
actually working.

!!! warning "How to read the *basis* column"
    **explicit** — the ORF Technical Paper references this ARC theme or control directly in the risk text or mitigations.  
    **thematic** — a reasoned alignment by this repo; it is *not* stated verbatim in the ORF paper and should be treated as interpretive.

## Agent-Level Observability `AGT`

### AGT-R1 — Agent actions and decision steps are not logged in sufficient detail to reconstruct specific sessions when necessary.

*ORF items:* ORF-AGT-01, ORF-AGT-02, ORF-AGT-03, ORF-AGT-04, ORF-AGT-05, ORF-AGT-06, ORF-AGT-07

> ORF states this telemetry exists to satisfy "the ARC framework's baseline requirements for monitoring and traceability and for tamper-evident audit trails."

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-043` | Record comprehensive logs | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-027` | Implement distributed tracing | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-028` | Write immutable audit logs | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-042` | Implement real-time monitoring | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-049` | Log all task assignments | <span class="orf-basis orf-basis-thematic">thematic</span> |

### AGT-R2 — Runaway or looping behaviour by the agent (e.g., infinite tool calls, repeated failures).

*ORF items:* ORF-AGT-08, ORF-AGT-09, ORF-AGT-10, ORF-AGT-11

> ORF mitigations for runaway/looping behaviour are described as "aligned with ARC's architecture controls."

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-026` | Apply circuit-breakers | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-007` | Reasoning time limit | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-083` | Ensure immediate interruptability | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-112` | Set minimum and maximum limits for system resources | <span class="orf-basis orf-basis-thematic">thematic</span> |

### AGT-R3 — Silent regressions after model, tool, or prompt changes.

*ORF items:* ORF-AGT-12, ORF-AGT-13, ORF-AGT-14

> Change/deployment logging supports ARC change-management and audit controls; ARC has no dedicated deployment-change-log control, so this is thematic.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-099` | Human approval for data changes | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-096` | Review all generated code before execution | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-010` | Conduct periodic audits | <span class="orf-basis orf-basis-thematic">thematic</span> |

## Agent Performance `PERF`

### PERF-R1 — Undetected model performance drift on critical tasks or domains.

*ORF items:* ORF-PERF-01, ORF-PERF-02, ORF-PERF-03

> Drift detection evidences ARC's periodic-audit and human-oversight controls.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-010` | Conduct periodic audits | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-021` | Run periodic audits | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-003` | Maintain human-in-the-loop approval | <span class="orf-basis orf-basis-thematic">thematic</span> |

### PERF-R2 — Hallucinations or ungrounded responses leading to harmful advice (e.g., policy advice).

*ORF items:* ORF-PERF-04, ORF-PERF-05, ORF-PERF-06

> Groundedness/hallucination telemetry maps directly onto ARC's hallucination and source-verification controls.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-056` | Implement methods to reduce hallucination rates | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-058` | Implement features for answer verification | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-057` | Implement UI/UX cues for hallucination risk | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-081` | Prioritise verified domains | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-082` | Require cross-source validation | <span class="orf-basis orf-basis-thematic">thematic</span> |

### PERF-R3 — Biased or unfair outputs across demographic-related inputs.

*ORF items:* ORF-PERF-07, ORF-PERF-08

> ARC has no dedicated fairness control; the closest analogue is its multi-objective success criteria (which include ethics). Fairness/parity telemetry is an ORF extension beyond ARC.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-016` | Define multi-objective success criteria | <span class="orf-basis orf-basis-thematic">thematic</span> |

## User Interaction & Behaviour `UX`

### UX-R1 — Abusive or malicious user behaviour (e.g., prompt injection, scams, probing for sensitive data) goes undetected.

*ORF items:* ORF-UX-01, ORF-UX-02, ORF-UX-03

> ORF notes that without this telemetry "the ARC 'monitoring and traceability' risk is not properly mitigated"; the listed input-defence controls are thematic.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-042` | Implement real-time monitoring | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-027` | Implement distributed tracing | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-078` | Implement input guardrails for prompt injection | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-005` | Implement input sanitisation | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-033` | Sanitise messages | <span class="orf-basis orf-basis-thematic">thematic</span> |

### UX-R2 — High rate of human handover or override but no structured tracking.

*ORF items:* ORF-UX-04, ORF-UX-05, ORF-UX-06, ORF-UX-07, ORF-UX-08

> Structured handover/override tracking evidences ARC's human-in-the-loop and logging controls; the structured-annotation requirement is an ORF extension.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-003` | Maintain human-in-the-loop approval | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-043` | Record comprehensive logs | <span class="orf-basis orf-basis-thematic">thematic</span> |

## System Performance, Health & Reliability `SYS`

### SYS-R1 — System outages, timeouts, or partial failures that produce unsafe states (e.g., an external tool action completed but its response is lost).

*ORF items:* ORF-SYS-01, ORF-SYS-02, ORF-SYS-03, ORF-SYS-04, ORF-SYS-05, ORF-SYS-06, ORF-SYS-07, ORF-SYS-08, ORF-SYS-09, ORF-SYS-10

> ARC's coverage of system reliability is limited; these are architecture/monitoring analogues for safe-fail and recovery behaviour.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-026` | Apply circuit-breakers | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-024` | Insert validation checkpoints | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-025` | Design feedback loops | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-091` | Monitor code runtime and memory consumption | <span class="orf-basis orf-basis-thematic">thematic</span> |

### SYS-R2 — Unexpected traffic spikes or abuse.

*ORF items:* ORF-SYS-11, ORF-SYS-12, ORF-SYS-13

> Capacity/abuse telemetry supports ARC's resource-limit controls.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-112` | Set minimum and maximum limits for system resources | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-113` | Limit concurrent queries to external systems | <span class="orf-basis orf-basis-thematic">thematic</span> |

## Safety & Security Compliance `SEC`

### SEC-R1 — Harmful, toxic, or policy-violating outputs that are not detected or not logged.

*ORF items:* ORF-SEC-01, ORF-SEC-02, ORF-SEC-03, ORF-SEC-04

> Harmful-output telemetry evidences ARC's safety-layer and output-guardrail controls.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-002` | Integrate safety constraint layer | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-052` | Implement output safety text guardrails | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-053` | Implement input text guardrails for specialized domains | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-054` | Implement input text guardrails for controversial content | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-078` | Implement input guardrails for prompt injection | <span class="orf-basis orf-basis-thematic">thematic</span> |

### SEC-R2 — Data privacy or confidentiality breaches (e.g., PII or sensitive organisational data exposed in outputs or logs).

*ORF items:* ORF-SEC-05, ORF-SEC-06, ORF-SEC-07, ORF-SEC-08

> Privacy telemetry maps onto ARC's PII guardrails and memory-encryption controls.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-103` | Implement input guardrails for PII | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-055` | Implement output text guardrails for PII | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-104` | Do not allow access to PII unless required | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-022` | Encrypt memory and restrict access | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-030` | Use guardrails | <span class="orf-basis orf-basis-thematic">thematic</span> |

### SEC-R3 — Unauthorised tool usage or privilege escalation by agents or users.

*ORF items:* ORF-SEC-09, ORF-SEC-10, ORF-SEC-11

> ORF mitigations are described as "aligned with ARC's Roles & Access Controls."

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-034` | Agent role isolation | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-036` | Apply Principle of Least Privilege | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-039` | Authenticate and validate agent roles | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-040` | Use fine-grained credentials | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-041` | Use time-bound credentials | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-015` | Conduct least-privilege reviews | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-037` | No admin privileges | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-038` | No privilege modification | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-077` | Use separate authentication service | <span class="orf-basis orf-basis-thematic">thematic</span> |

### SEC-R4 — Incomplete or mutable audit trails for safety incidents.

*ORF items:* ORF-SEC-12, ORF-SEC-13

> ORF mitigations specify "append-only log stores or log encryption (per ARC guidance)."

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-028` | Write immutable audit logs | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-043` | Record comprehensive logs | <span class="orf-basis orf-basis-explicit">explicit</span> |
| `CTRL-022` | Encrypt memory and restrict access | <span class="orf-basis orf-basis-thematic">thematic</span> |

## Product Lifecycle & Governance `GOV`

### GOV-R1 — Model, prompt, or policy changes are made without audit, safety assessment, or rollback path.

*ORF items:* ORF-GOV-01, ORF-GOV-02, ORF-GOV-03

> Pre-change governance telemetry supports ARC's change-management, code-review, and rollback controls.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-099` | Human approval for data changes | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-096` | Review all generated code before execution | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-010` | Conduct periodic audits | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-025` | Design feedback loops | <span class="orf-basis orf-basis-thematic">thematic</span> |

### GOV-R2 — Limited or ad hoc safety audits and incident post-mortems.

*ORF items:* ORF-GOV-04, ORF-GOV-05

> Audit-cadence and incident-recurrence telemetry evidences ARC's periodic-audit controls; the review-cadence and recurrence metrics are ORF extensions.

| ARC Control | Name | Basis |
| --- | --- | --- |
| `CTRL-010` | Conduct periodic audits | <span class="orf-basis orf-basis-thematic">thematic</span> |
| `CTRL-021` | Run periodic audits | <span class="orf-basis orf-basis-thematic">thematic</span> |
