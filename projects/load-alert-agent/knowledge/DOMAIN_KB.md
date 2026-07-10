# Domain Knowledge Base — Substation Load Monitoring & Alerting

_Compiled by functional-agent at Intake. Scope: brief, per-project research pass
(this project is a verification exercise for the roster-dropping mechanism, not
a production deployment) — real but not exhaustive._

## What signals actually matter

The load-alert-agent's real job is turning raw substation telemetry into alerts
an operator can trust. The signal that matters most is not raw current/kVA
alone but **transformer winding hotspot temperature**, since that's what
determines safe continuous loading, permissible short-term overload multiplier,
and maximum emergency-overload duration (per IEC 60076-7 / IEEE C57.91 thermal
aging guidance). A well-designed alert should reason about load relative to
rated capacity *and* duration/thermal trend, not just an instantaneous
threshold crossing — e.g. a brief spike during switching transients is normal;
sustained loading above ~90-105% of nameplate for minutes-to-hours is what
actually threatens equipment life. Other signals worth surfacing: phase
imbalance (uneven loading across phases causes localized heating), cooling
system state (fan/pump stages should escalate before a hard alarm fires), and
rate-of-change of load (fast ramps are more often a data/comms glitch than a
real event).

## Common false-alarm / failure modes

This is the area most likely to burn trust in an automated alerting agent, so
it's the most important thing to get right architecturally:

- **Alarm flooding**: SCADA-literature convention treats >10 alarms in 10
  minutes as a flood — once operators are flooded they stop reading alarms
  individually and react to none. An LLM-based alert agent must not amplify
  this (e.g. re-alerting on every polling cycle while a condition persists).
- **Chattering alarms**: a value oscillating near a threshold (e.g. load
  hovering right at 100%) causes rapid active/clear/active cycling. Needs
  hysteresis (distinct set/clear thresholds) or a debounce window, not a
  single instantaneous threshold check.
- **Stale/standing alarms**: conditions that trip once and are never
  cleared/acknowledged reduce attention to genuinely new problems.
- **Comms/sensor glitches masquerading as load events**: a dropped or noisy
  reading can look like a spike; distinguishing "real overload" from "bad
  data" typically requires cross-checking against a second signal (e.g.
  temperature trend, or plausibility bounds) before alerting.
- **Alerting without actionability**: an alert that doesn't state why it
  fired, what threshold was crossed, and what the plausible operator action
  is tends to get ignored — same failure mode as generic SCADA alarm
  configuration.

## Implication for this project

Given the template's placeholder `lookup_status` tool, the real tool(s) this
project needs will likely be a load/telemetry lookup (current load vs. rated
capacity, ideally with recent trend) plus an alerting/threshold-evaluation
step that applies hysteresis and duration logic rather than a naive
instantaneous compare. This is a devil's-advocate point worth raising if
Plan & Backlog scopes a bare "if load > X, alert" without addressing
chattering/flooding.

Sources:
- https://electrical-engineering-portal.com/substation-transformer-alarms
- https://link.springer.com/article/10.1007/s40866-024-00227-z
- https://www.pteinc.com/scada-alarm-management-isa-18-2-best-practices/
- https://industrialmonitordirect.com/blogs/knowledgebase/scada-alarm-management-strategy-summary-suppression-priority
