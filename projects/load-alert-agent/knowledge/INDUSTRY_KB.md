# Industry Knowledge Base — Utilities/Energy

_Compiled by industry-expert at Intake. Scope: brief, per-project research pass
(this project is a verification exercise for the roster-dropping mechanism, not
a production deployment) — real but not exhaustive._

## Industry context

Utilities are actively moving AI grid tools from pilot to production: industry
coverage of DTECH 2026 notes the strongest success stories are the ones tied
to concrete operational KPIs (outage prediction accuracy, restoration time,
crew dispatch efficiency) rather than generic "AI monitoring." Vendors are
converging on the "copilot for the operator" pattern rather than autonomous
control — e.g. Itron's IEOS Connector for Microsoft 365 Copilot, Schneider
Electric's One Digital Grid Platform, ThinkLabs' Grid Copilot, and Argonne's
GridMind research platform all position AI as a decision-support layer that
augments a human operator's situational awareness, not a system that acts
unsupervised. Southern California Edison's "Project Orca" is a concrete
production example: a GenAI incident-management assistant that lets network
operations staff pull up relevant documents, past incidents, and real-time
telemetry in seconds during an event.

This matters directly for load-alert-agent: the credible industry framing for
an LLM-based alerting agent is "assistant that surfaces and explains an
alert-worthy condition for a human to act on," not "autonomous alarm/trip
authority." NERC guidance explicitly frames AI as decision-support, not an
autonomous controller, and emphasizes audit trails/traceability — relevant if
this tool's alerts ever need to be explainable after the fact.

## Compliance considerations

NERC (grid reliability) sets the bar most likely to be relevant even for an
internal/local-scope tool: alerting systems that touch operational data
should be able to justify *why* an alert fired (traceable reasoning, not a
black box), consistent with NERC's stated preference for auditable
decision-support tooling. This is worth flagging even though this project is
explicitly local/dev-scoped and not being built for real compliance sign-off.

## Suggested feature backlog (for Plan & Backlog to consider)

1. **Explain-the-alert trace** — since utilities are adopting AI as
   decision-support (not autonomous control), the agent's response to a
   load-alert query should include *why* (which signal, which threshold,
   trend direction), not just a verdict — mirrors the Project Orca /
   copilot pattern of surfacing telemetry + context together in one place.
2. **Alert-fatigue guardrail (dedupe/cooldown)** — given the industry's own
   documented struggle with nuisance/flooded alarms (see DOMAIN_KB.md), a
   feature that suppresses repeat alerts for an already-acknowledged/ongoing
   condition would track current utility-side alarm-management practice.
3. **Incident-history lookup** — a lightweight "has this substation/feeder
   alarmed before, and how was it resolved" query, echoing the
   incident-history-retrieval pattern utilities are adopting in
   production copilots (SCE's Orca) — useful even at small scale for this
   project's context window.

Sources:
- https://www.deloitte.com/us/en/insights/industry/power-and-utilities/power-and-utilities-industry-outlook.html
- https://gridwise.org/ai-and-the-grid-unlocking-the-potential-of-artificial-intelligence-for-electric-utilities/
- https://www.microsoft.com/en-us/industry/blog/energy-and-resources/power-and-utilities/2026/02/17/dtech-2026-how-microsoft-and-our-partners-are-accelerating-ai-innovation-for-utilities/
- https://www.renewableenergyworld.com/power-grid/smart-grids/from-pilots-to-production-where-ai-is-delivering-real-value-in-utility-field-operations/
- https://www.anl.gov/article/gridmind-powering-the-control-room-of-the-future-with-ai-agents
