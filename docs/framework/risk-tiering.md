# Risk Tiering

The framework defines three **system risk tiers**. Risk tier is the primary
determinant of mandatory telemetry.

## Low-Risk Operations

Beta testing, internal pilots, and proofs of concept where the impact of failure
is limited and human-in-the-loop oversight is strong. *Example:* internal
experimentation by a single team to prototype a new use case, where outputs are
not used to inform downstream decisions.

## Medium-Risk Operations

Internal agency usage with minimal impact on operations, and low-impact
public-facing use cases with strong human-in-the-loop oversight. *Example:* an
internal scoping assistant used by public officers to draft documents, with all
outputs reviewed before use.

## High-Risk Operations

Systems with significant operational impact and high-impact public-facing
deployments. *Example:* public-facing chatbots that answer questions on
consequential domains such as housing, taxation, or social support, and agentic
systems that take actions against external services on behalf of citizens.

!!! note "Data classification interacts with risk"
    A low-risk system that processes high-classification data inherits stricter
    handling requirements for its telemetry, and a high-risk system that handles
    only public information may have stricter logging needs but laxer storage
    requirements. Agencies should conduct a parallel data-handling assessment
    alongside the risk-tier determination.
