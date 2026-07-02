# Metric Definitions

Mathematical definitions for every metric, log, and trace in the [Requirements Table](requirements-table.md), so that any two agencies following the specification compute numerically comparable values. The tier marker (1–4) maps to the [requirements matrix](requirements-matrix.md).

!!! note "Generated file"
    This page is generated from `data/requirements.yaml` by `scripts/gen_pages.py`. Do not edit it by hand.

## Agent-Level Observability `AGT`

| Tier | Type | Telemetry Item | Mathematical Definition |
| --- | --- | --- | --- |
| 1 | log | **ORF-AGT-01** — LLM prompt and response pairs with intermediate reasoning steps (where available), timestamps, and token usage. | For each turn i, log r_i = (timestamp_i, prompt_i, response_i, tokens_in_i, tokens_out_i, intermediate_steps_i). |
| 1 | log | **ORF-AGT-02** — Tool / API call events with parameters, outcomes, and retries. | For each call event e_j, log e_j = (timestamp_j, tool_j, parameter_j, outcome_j, retry_attempt_j). |
| 2 | log | **ORF-AGT-03** — Knowledge base / memory access logs (queries, retrieved documents, memory writes). | For each access event e_k, log e_k = (timestamp_k, query_k, retrieved_docs_k, memory_write_k). |
| 2 | trace | **ORF-AGT-04** — Unique trace IDs per query–task–tool call chain (end-to-end distributed tracing). | Assign trace IDs for all events e in a query–task–tool chain: trace_id_e = constant. Coverage: trace_coverage = \|{e : trace_id_e present}\| / \|{e}\|. |
| 1 | log | **ORF-AGT-05** — Error and exception logs. | error_log = {(timestamp, trace_id, error_type, error_message, stack_hash)}; error_count = \|error_log\| over the observation window. |
| 2 | trace | **ORF-AGT-06** — Subtask decomposition. | Represent a task as a tree D whose nodes are subtasks and whose edges capture parent–child relations. decomposition_size = \|nodes(D)\|. |
| 2 | trace | **ORF-AGT-07** — Retrieval-to-response traces. | Trace graph G = (V, E) linking retrieved items d to response spans y; edge (d → y) exists if d was used to generate y. |
| 1 | metric | **ORF-AGT-08** — Tool usage count per task/session with thresholds for abnormal spikes. | tool_counts = #tool calls in s. Alert if tool_counts > threshold. |
| 1 | metric | **ORF-AGT-09** — Task duration and step count per task/session. | task_duration_T = task_end_T − task_start_T; step_count_T = #actions in T. |
| 2 | trace | **ORF-AGT-10** — Error lineage traces linking repeated failures. | Build a retry-lineage graph whose nodes are attempts and whose edges link attempt k → k+1 when a failure triggers a retry. |
| 1 | metric | **ORF-AGT-11** — Request retry counts per tool call. | #retries = #attempts − 1; retry_rate = #retries / #calls. |
| 2 | log | **ORF-AGT-12** — Model deployment / change logs (who, what, when). | deployment_log = {(timestamp, actor, model_id, model_version, environment)}. |
| 2 | log | **ORF-AGT-13** — Configuration / prompt / policy change logs with approver identity. | change_log = {(timestamp, change_type, artifact_id, description, owner, approver)}. |
| 4 | metric | **ORF-AGT-14** — Side-by-side performance metrics pre- and post-change (hallucination rate, refusal rate, etc.). | For any metric m: Δm = m_after − m_before; relative change = (m_after − m_before) / m_before. |

## Agent Performance `PERF`

| Tier | Type | Telemetry Item | Mathematical Definition |
| --- | --- | --- | --- |
| 3 | metric | **ORF-PERF-01** — Performance / model-drift metrics on critical tasks (context- and agency-specific). | drift = diff(performance_current, performance_baseline). |
| 2 | log | **ORF-PERF-02** — Human override / edit logs and counts, especially for harmful or incorrect outputs. | edit_counts = #edited outputs in s; edit_rates = edit_counts / #outputs in s. |
| 4 | metric | **ORF-PERF-03** — Task completion rate per session, with explicit labelling of safe failure (the agent declines and the task is not completed) versus unsafe success (the task is completed but the agent emits unsafe or policy-violating content). | For each session, label its outcome outcome ∈ {safe_failure, unsafe_failure, unsafe_success, safe_success}. Report, for each label ℓ, P(outcome = ℓ) = #{outcome = ℓ} / #outcomes. |
| 4 | metric | **ORF-PERF-04** — Hallucination rate on sampled outputs (number of materially incorrect answers). | hallucination_rate = #materially_incorrect_responses / #sampled_responses. |
| 4 | metric | **ORF-PERF-05** — Number of ungrounded responses (no sources or weak citations) for high-risk domains. | ungrounded_count = #high-risk outputs with missing or weak citations; ungrounded_rate = ungrounded_count / #high-risk outputs. |
| 3 | metric | **ORF-PERF-06** — Retrieval metrics (e.g., top-K recall, retrieval accuracy, embedding drift) where retrieval is supposed to ground responses. | drift = diff(performance_current, performance_baseline), where performance ∈ {top-K recall, retrieval accuracy, embedding drift}. |
| 4 | metric | **ORF-PERF-07** — Bias and fairness indicators (e.g., parity metrics) on representative test sets. | parity_gap = max_g \|performance_g − performance_ref\|, where performance ∈ {approval rate, refusal rate, hallucination rate}. |
| 4 | metric | **ORF-PERF-08** — Segment-wise hallucination or refusal rates by sensitive attribute. | For group g: rate_g = #hallucination/refusal events for g / #outputs for g. Report max_g rate_g. |

## User Interaction & Behaviour `UX`

| Tier | Type | Telemetry Item | Mathematical Definition |
| --- | --- | --- | --- |
| 2 | log | **ORF-UX-01** — Logs of detected unexpected or out-of-scope query types and topics. | OOS_log = {(timestamp, session_id, oos_label)}; oos_rate = #out-of-scope queries / #queries. |
| 1 | metric | **ORF-UX-02** — Content policy violation attempts and model refusals per user/session. | Per user u or session s: violation_attempt_rate = #attempts / #queries; refusal_rate = #refusals / #queries. |
| 1 | trace | **ORF-UX-03** — Session traces for flagged abusive sessions. | For flagged session s, store the ordered sequence of events {(timestamp_e, prompt_e, tool_call_e, output_e)} for reconstruction. |
| 2 | metric | **ORF-UX-04** — Number of sessions requiring human handover or override. | override_count = #sessions requiring handover/override; override_rate = override_count / #sessions. |
| 3 | log | **ORF-UX-05** — Human annotations on the reason for handover (safety, quality, capability gap, policy issue). | handover_annotation = {(timestamp, session_id, handover_reason, description)}, where handover_reason ∈ {safety, quality, capability gap, policy}. |
| 2 | metric | **ORF-UX-06** — User feedback (thumbs up/down) tied to specific responses. | satisfaction_rate = #thumbs up / (#thumbs up + #thumbs down). |
| 3 | metric | **ORF-UX-07** — Repeat queries / user retry rates (number of repeated queries per session). | repeat_rate = #repeated queries in session / #queries in session. |
| 3 | metric | **ORF-UX-08** — Number of users abandoning their sessions. | abandon_rate = #inactive sessions that timed out / #sessions started. |

## System Performance, Health & Reliability `SYS`

| Tier | Type | Telemetry Item | Mathematical Definition |
| --- | --- | --- | --- |
| 2 | metric | **ORF-SYS-01** — System uptime / availability. | availability = (total runtime − downtime) / total runtime. |
| 2 | metric | **ORF-SYS-02** — Error rates (e.g., HTTP 5xx, tool invocation failures). | error_rate = #errors / #requests. |
| 2 | metric | **ORF-SYS-03** — Timeout / abort counts per request and per tool. | Per request or tool: timeout_count = #timeouts and aborts in the period. |
| 1 | log | **ORF-SYS-04** — System request logs. | request_log = {(timestamp, request_id, service_id, endpoint_id, status, latency_ms, bytes)}. |
| 1 | log | **ORF-SYS-05** — System timeout / abort logs. | timeout_log = {(timestamp, request_id, tool_id, timeout_reason)}. |
| 1 | log | **ORF-SYS-06** — System error logs and crash reports. | error_log = {(timestamp, service_id, error_code, stack_hash, crash_id)}; crash_count = #system crashes in the period. |
| 2 | metric | **ORF-SYS-07** — System throughput and queue length. | throughput = #requests / Δt; q̄ = (1/Δt) ∫ q(t) dt, where Δt is the observation window and q(t) is the number of requests waiting in the queue at time t. |
| 2 | metric | **ORF-SYS-08** — GPU / CPU / memory utilisation (for capacity risk). | ū = (1/Δt) ∫ util(t) dt, where Δt is the observation window and util(t) is the utilisation of GPU / CPU / memory at time t. |
| 2 | trace | **ORF-SYS-09** — Distributed request traces across services (where multi-service flows exist). | A trace is a set of spans across services; each span = (trace_id, span_id, parent_id, service_id, timestamp_start, timestamp_end). |
| 3 | metric | **ORF-SYS-10** — Redundancy and failover success rates. | failover_success_rate = #successful failovers / #failover attempts. |
| 2 | metric | **ORF-SYS-11** — Traffic volume per user. | For user u: traffic_volume_u is the number of requests, or bytes transferred, per period. |
| 2 | metric | **ORF-SYS-12** — Error and latency distribution during spikes. | latency_quantiles = {q_p : P(latency ≤ q_p) = p} for p ∈ {0.5, 0.95, 0.99}. |
| 3 | metric | **ORF-SYS-13** — Cost per query, task, or session. | cost = total cost / #queries / tasks / sessions. |

## Safety & Security Compliance `SEC`

| Tier | Type | Telemetry Item | Mathematical Definition |
| --- | --- | --- | --- |
| 3 | metric | **ORF-SEC-01** — Toxic / harmful output rate (flagged by filters or human review). | toxic_rate = #outputs flagged by guardrails / human review / #outputs. |
| 2 | metric | **ORF-SEC-02** — Number of policy violations detected versus refused. | refused_share = #refusals due to policy violations / #policy violations per period. |
| 2 | log | **ORF-SEC-03** — Model refusal events and categories (e.g., safety, privacy). | For category c: refusal_count_c = #refusals attributable to c. Report the distribution refusal_count_c / Σ_c refusal_count_c across all categories. |
| 3 | metric | **ORF-SEC-04** — Distribution of content categories requested (especially sensitive topics). | distribution(c) = #requests of category c / #requests. |
| 2 | metric | **ORF-SEC-05** — Privacy incident count (PII exposure events). | privacy_incident_count = #PII exposure events detected in the period. |
| 2 | log | **ORF-SEC-06** — Privacy breach incident logs (records of detected personal or sensitive data leaks). | privacy_incident_log = {(timestamp, incident_id, exposure_type, severity_level, trace_id)}. |
| 2 | metric | **ORF-SEC-07** — Classified information leakage incidents. | classified_leak_count = #classified-data exposure events detected in the period. |
| 2 | log | **ORF-SEC-08** — Memory / KB access logs with classification of data sensitivity. | For KB / memory accesses: access_log = {(timestamp, agent_id, resource_id, sensitivity_level)}. |
| 2 | metric | **ORF-SEC-09** — Unauthorised or failed privileged tool usage attempts. | unauthorised_rate = #unauthorised privileged attempts / #privileged attempts. |
| 2 | log | **ORF-SEC-10** — Audit logs of role / permission changes and token issuance. | authorised_change_log = {(timestamp, actor, role/permission change, target principal)}. |
| 2 | log | **ORF-SEC-11** — Agent identity / credential usage logs. | credential_use_log = {(timestamp, agent_id, credential_id, scope, tool_id)}. |
| 2 | trace | **ORF-SEC-12** — Full conversation traces retained for flagged safety and security incidents. | For each flagged incident i, retain the full transcript c_i = (timestamp, messages, tool_id, agent_id) as an immutable record. |
| 2 | log | **ORF-SEC-13** — Audit logs for prompts, responses, tool calls, and memory operations. | With append-only integrity controls: audit_log = {(timestamp, session_id, prompt, response, tool_id, memory_ops)}. |

## Product Lifecycle & Governance `GOV`

| Tier | Type | Telemetry Item | Mathematical Definition |
| --- | --- | --- | --- |
| 3 | metric | **ORF-GOV-01** — Deployment metrics: rollout frequency and percentage of changes with safety evaluation. | rollout_frequency = #deployments / Δt; safety_evaluation_percent = #changes with safety evaluation / #changes. |
| 3 | metric | **ORF-GOV-02** — Audit metrics: percentage of audited sessions and number of audit findings per period. | audited_session_percent = #audited sessions / #sessions; findings_rate = #audit findings / Δt. |
| 2 | log | **ORF-GOV-03** — Configuration change logs with owners and approvers. | change_log = {(timestamp, change_type, artifact_id, description, owner, approver)}. |
| 3 | log | **ORF-GOV-04** — Audit logs for reviewed sessions and findings. | review_log = {(timestamp, session_id, reviewer, finding_label, description, severity)}; findings_count = #findings in the period. |
| 3 | metric | **ORF-GOV-05** — Incident count and severity over time, with recurrence indicators. | incident_count = #incidents in the period; recurrence_rate = #recurrences / #incidents. |
