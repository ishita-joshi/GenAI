# Platform Team — Interview Specifics

The platform team builds the infrastructure that other engineering teams depend on: feature flag system, internal authentication, data ingestion pipelines, internal developer tooling. Platform interviews adjust the standard Staff loop to emphasize the skills that matter for this work.

## System Design Adjustments

For platform candidates, the system design round always involves a multi-tenant component. Example problems:
- Design a feature flag service supporting 100k QPS with sub-10ms latency
- Design an internal API gateway with per-team rate limiting
- Design a config service that supports gradual rollouts and instant rollbacks

The interviewer should probe for: blast radius reasoning, backward compatibility, versioning strategy, and how the candidate would migrate existing consumers off a legacy system.

## Technical Deep Dive Focus

For the deep dive round, prefer candidates who can speak to:
- Operating a system in production (on-call, incident response)
- API design decisions and their consequences
- Migrating other teams off a deprecated system

Platform engineers spend significant time on developer experience. Candidates who only have product-engineering background often struggle at Staff level on platform — flag this early.

## Bar Raiser Selection

For platform Staff candidates, the bar raiser should come from a *consumer* team, not another infrastructure team. The point is to test whether the candidate communicates well with their internal customers — that signal is lost if the bar raiser is also a platform engineer.

## Round Order for Platform Loops

Run System Design before Coding. Strong platform candidates often have rusty coding speed but excellent system design instincts; if Coding goes first and goes poorly, the rest of the loop is biased. System Design first surfaces the Staff-level signal earlier.
