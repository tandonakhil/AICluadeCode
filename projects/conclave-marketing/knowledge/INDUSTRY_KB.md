# INDUSTRY_KB: conclave-marketing

**Industry**: Energy (utilities, grid operators, energy companies) — specifically their buyers of AI software: digital/innovation, operations, compliance/security, and IT leaders.
**Researched**: 2026-07-17 by industry-expert (Intake gate; content returned to orchestrator, file written by orchestrator per KB-write policy). All statistics below verified against real, published sources; no fabricated attributions.

## 1. Who the buyer is and how they buy

- Utility software purchases are committee decisions run through formal RFP processes with weighted scoring on technical capability, financial stability, references, and price — not impulse buys off a landing page. The marketing site's real job is to survive being forwarded to a skeptical evaluation committee ([TechTarget RFP guide](https://www.techtarget.com/searchcio/tip/How-to-write-an-RFP-for-a-software-purchase-with-template), [Energy Central RFP checklist](https://www.energycentral.com/intelligent-utility/post/your-utility-program-software-vendor-rfp-checklist-snmmn2l2rBTGbCJ)).
- Buyers shortlist vendors with **proven references in their exact vertical and operating model**; the biggest perceived risks are choosing a vendor without utility-specific references and low frontline adoption ([RFP.wiki energy/utilities](https://www.rfp.wiki/specialty-industries/energy-utilities-software)).
- The four persona lenses already on the v5 seed (product owner, operations, compliance/security, IT) map well to real utility buying committees. Keep them; deepen them on the Solutions page.
- Reliability culture matters: utilities are conservative adopters whose institutional reflex is "prove it won't break anything." Language that acknowledges this ("decision support, not autonomous control"; "human holds final say") aligns with NERC's own stated posture ([NERC AI/ML in Real-Time System Operations whitepaper, Nov 2024](https://www.nerc.com/pa/rrm/bpsa/Documents/Whitepaper-AI%20and%20ML%20in%20Real-Time%20System%20Operations.pdf), [Ampyx Cyber summary](https://ampyxcyber.com/blog/embracing-ai-for-the-electric-grid-insights-from-nerc)).

## 2. What energy-sector buyers care about when evaluating AI vendors

- **Auditability**: comprehensive audit trails for automated decisions are now table stakes — for regulatory compliance and for operational forensics after incidents. Conclave's append-only decision record is a direct answer; lead with it ([AI x Energy: governance architecture](https://www.aixenergy.io/utilities-need-an-ai-governance-architecture-not-another-framework/)).
- **Human oversight**: NERC guidance emphasizes AI as decision support with the operator holding final input. Conclave's "explicit human decision at every gate" is the same principle applied to the SDLC — say so explicitly ([HSI: AI in the control room](https://hsi.com/blog/ai-improving-grid-operations-without-losing-nerc-compliance)).
- **Regulatory scrutiny of AI + OT**: AI agents touching systems without defined access scopes/audit trails create exposure that NERC and state regulators increasingly scrutinize; NERC CIP applies where AI affects BES reliability, though customer-facing and analytics apps (Conclave's actual portfolio) typically sit outside CIP scope. Be precise about this boundary — overclaiming "NERC CIP compliant" would be a red flag ([APPIT: NERC CIP + AI](https://www.appitsoftware.com/blog/nerc-cip-ai-cybersecurity-compliance-grid-systems)).
- **Governance frameworks buyers recognize**: ISO/IEC 42001 (AI management systems), NIST AI RMF, and for EU-exposed buyers the EU AI Act's high-risk classification of critical-infrastructure AI (conformity assessments, documentation, human oversight — obligations phasing in through August 2026) ([Baker Botts on the EU AI Act](https://www.bakerbotts.com/thought-leadership/publications/2026/march/the-eu-ai-act)). Name-checking these frameworks accurately (as "aligned with the expectations of," not "certified") earns credibility.
- **Vendor supply-chain security**: NIS2-style expectations (incident reporting, vendor security assessment) mean security posture belongs on the site, not just in the RFP response.

## 3. Industry trends worth reflecting on the site (2025–2026)

- **AI adoption is mainstream, expertise is the bottleneck**: Itron's 2025 Resourcefulness Report (500 NA utility executives) found 81% already use AI — 41% fully integrated, 40% with mature projects underway — and the #1 hurdle is lack of in-house expertise (43%) ([Itron, Oct 2025](https://investors.itron.com/news-releases/news-release-details/itron-report-reveals-81-north-american-utilities-already-use-ai)). Positioning implication: the market is past "should we use AI?" — the pitch is *governed, supportable* AI a lean team can own. The "IT leader / no priesthood" card on the seed hits this; amplify it.
- **Load growth and grid strain dominate the agenda**: Deloitte's 2026 outlook projects peak demand could rise 26% by 2035 (fastest growth in 30 years, driven by data centers/electrification), with "smarter systems — integrating analytics and AI" as one of five core utility strategies ([Deloitte 2026 Power & Utilities Outlook](https://www.deloitte.com/us/en/insights/industry/power-and-utilities/power-and-utilities-industry-outlook.html)). Utility buyers' attention is on reliability, affordability, and capacity — frame Conclave-built apps (outage chatbots, agentic workflows, RAG) as relieving workload on stretched teams.
- **Data readiness is utilities' urgent AI gap** per EPRI's 2025 research ([EPRI: AI Readiness in Utilities](https://www.epri.com/research/products/000000003002033653), [EPRI Journal](https://eprijournal.com/why-data-readiness-is-one-of-utilities-most-urgent-ai-challenges/)) — a natural hook for the RAG/knowledge-base solution story.
- **Outage communication** remains the flagship customer-facing use case (the seed's gate-by-gate walkthrough already uses an outage-status chatbot — this is the right choice; keep it as the canonical narrative).
- **AI governance expectations are formalizing**: no US state PUC had issued formal operational-AI guidance as of early 2026, but utilities are adapting federal (OMB M-25-22) and ISO 42001 patterns voluntarily — meaning governance is a differentiator *now*, before it becomes a mandate.

## 4. Language that resonates vs. reads as hype

**Resonates**: audit trail, decision record, human-in-the-loop / final say, test evidence including failures, independent review, defined scope, reference architecture, portable stack, "decision support not autonomous control," named frameworks used accurately.
**Reads as hype to utility buyers**: "revolutionary," "autonomous," "10x," unquantified ROI promises, "AI-powered" as a feature in itself (FTC calls this AI-washing), any implication of touching grid operations/OT, vanity metrics without methodology.
The seed's honest register ("You're shown a real failure, and asked what to do about it") is unusually well matched to reliability culture — preserve it through the redesign.

## 5. Compliance considerations for the site itself

- **Claims substantiation (FTC)**: Operation AI Comply (launched Sept 2024, continuing under the current administration with 12+ Section 5 actions) requires every explicit *and implied* AI capability claim to be substantiated by competent, reliable evidence ([Benesch](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/), [FTC](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)). This site markets an AI product — it is squarely in scope.
- **Accessibility**: target WCAG 2.1 AA (ADA-exposure baseline; utility buyers often carry public-sector accessibility procurement requirements). The seed already honors `prefers-reduced-motion` — carry that forward; add semantic landmarks, contrast checks on copper-on-dark, keyboard nav for tab modules and marquees (marquees need pause/reduced-motion behavior).
- **No external requests / no tracking** (existing constraint) is itself a sellable trust point to security-conscious buyers — consider stating it.
- **Verified-real citations on the current seed** (both check out; keep exact wording and years): Gartner 2024 — "at least 30% of generative AI projects will be abandoned after proof of concept by end of 2025"; Gartner 2025 — "over 40% of agentic AI projects will be canceled by end of 2027," inadequate risk controls among cited causes.
- **Claims on the seed needing substantiation or hedging before external use**:
  - "Six independent test suites" and "Eight platform capabilities since launch" — verifiable internally, but keep counts synced to `admin/MAS_REGISTRY.md`/changelog or they'll silently drift false.
  - "0 lines of code shipped without a human having approved the plan" / "100% human-approved" — defensible as a *process description*, but phrase as design guarantee ("by design, nothing advances without approval"), not an audited outcome metric.
  - "No lock-in… LLM providers switchable by configuration — no code changes" — verify this holds for every template before shipping the sentence.
  - `hello@conclave.example` — already flagged; must be real before external sharing.
  - Do not add "NERC CIP compliant," "ISO 42001 certified," or customer counts/testimonials unless literally true.

## 6. Suggested backlog (trend-informed)

1. **Solutions page structured by the three portfolio use cases** (GenAI chatbot / agentic workflow / RAG knowledge app), each anchored to a real utility pain: outage communication & customer self-service; workflow relief for stretched ops teams amid record load growth; institutional-knowledge retrieval addressing EPRI-documented data-readiness gaps. (High priority — this is the page evaluation committees will read.)
2. **"Governance, on the record" trust section/page**: audit-trail artifact samples (decision record excerpt, test-evidence excerpt), human-oversight model, accurate framework alignment language (NIST AI RMF / ISO 42001 expectations / NERC decision-support posture). Directly answers 2026 vendor-evaluation criteria.
3. **Persona-tabbed value module (THRED CxO-style)** mapped to the four utility buying-committee roles — carry over from seed, deepen with role-specific proof artifacts.
4. **"Evaluation-ready" resource block**: security/architecture one-pager framing, reference-architecture diagram, stack portability statement — content shaped for being pasted into an RFP scoring matrix.
5. **Verified-stats strip** (Gartner 30%/40%+, optionally Itron 81%/43%-expertise-gap with exact attribution) with a house rule: every number carries source + year, rendered adjacent, never in a footnote.
6. **Accessibility hardening as an explicit feature**: WCAG 2.1 AA pass on all pages, reduced-motion parity for the new always-moving THRED components (looping hero, marquee), visible-focus states.
7. **Claims-substantiation checklist in the repo** (each marketing claim → its evidence source) so Review/Test gates can verify drift — makes the site itself a demonstration of Conclave's governance story.
8. **"Built by Conclave" proof section** retained and strengthened: for a references-driven buyer with no customer logos available, self-hosted dogfooding evidence is the most credible proof point this site can honestly make.
9. Lower priority: outage-chatbot narrative kept as the canonical gate-by-gate walkthrough; optional EU AI Act note only if non-US buyers become a target.

---

Sources:
- [Deloitte 2026 Power and Utilities Industry Outlook](https://www.deloitte.com/us/en/insights/industry/power-and-utilities/power-and-utilities-industry-outlook.html)
- [Itron 2025 Resourcefulness Report press release](https://investors.itron.com/news-releases/news-release-details/itron-report-reveals-81-north-american-utilities-already-use-ai)
- [EPRI: AI Readiness in Utilities](https://www.epri.com/research/products/000000003002033653) and [EPRI Journal on data readiness](https://eprijournal.com/why-data-readiness-is-one-of-utilities-most-urgent-ai-challenges/)
- [NERC whitepaper: AI/ML in Real-Time System Operations](https://www.nerc.com/pa/rrm/bpsa/Documents/Whitepaper-AI%20and%20ML%20in%20Real-Time%20System%20Operations.pdf) and [Ampyx Cyber summary](https://ampyxcyber.com/blog/embracing-ai-for-the-electric-grid-insights-from-nerc)
- [APPIT: NERC CIP + AI compliance](https://www.appitsoftware.com/blog/nerc-cip-ai-cybersecurity-compliance-grid-systems), [HSI: AI in the control room](https://hsi.com/blog/ai-improving-grid-operations-without-losing-nerc-compliance)
- [Baker Botts: EU AI Act for energy executives](https://www.bakerbotts.com/thought-leadership/publications/2026/march/the-eu-ai-act), [AI x Energy: governance architecture](https://www.aixenergy.io/utilities-need-an-ai-governance-architecture-not-another-framework/)
- [FTC Operation AI Comply announcement](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes), [Benesch: one year of Operation AI Comply](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)
- [RFP.wiki energy/utilities software](https://www.rfp.wiki/specialty-industries/energy-utilities-software), [Energy Central utility RFP checklist](https://www.energycentral.com/intelligent-utility/post/your-utility-program-software-vendor-rfp-checklist-snmmn2l2rBTGbCJ), [TechTarget software RFP guide](https://www.techtarget.com/searchcio/tip/How-to-write-an-RFP-for-a-software-purchase-with-template)

---

## 2026-07-20 — Market positioning research (industry-agnostic repositioning + FDE model)

Supersedes the energy-sector buyer research above for positioning purposes.
Full deliverable returned to orchestrator; decision-ready summary:

**White space:** no player occupies (multi-agent build system) × (human-gated
governance with audit evidence) × (FDE delivery in customer environment).
- Cluster A vibe-coding (Lovable ~$200M ARR, Bolt, Replit Agent, v0, Cursor):
  win on speed-to-demo; fail enterprise security review; documented incidents.
- Cluster B agentic delivery (Cognition/Devin, Factory, GitHub Agent HQ):
  task autonomy inside existing eng orgs; governance bolt-on via SIs
  (Cognizant/Infosys partnerships prove the platform alone doesn't close).
- Cluster C FDE-led (Palantir +85% YoY, OpenAI Deployment Company $4B+,
  Distyl $1.8B, SIs): outcome ownership, but no governed build pipeline as
  the shipped artifact; FDE job postings +729% YoY.

**Recommended primary positioning:** "Conclave is governed AI software
delivery: forward-deployed engineers run a multi-agent build pipeline inside
your environment, a human approves every gate, and the audit trail ships
with the application." Short form: "AI-built software you can defend."
Pillars: (1) human-in-command by design; (2) the audit trail is a
deliverable; (3) forward-deployed, outcome-owned delivery.

**Claims evidence tiers (for CITATIONS.md if used on site):**
- STRONG (website-grade): Veracode 2025/2026 (45% of AI-generated code has
  OWASP Top-10 vulns); GitClear 2025/2026 (8x duplication, −70% refactoring,
  +47% error-masking); Replit prod-DB deletion incident (Jul 2025, since
  safeguarded); CVE-2025-48757 (Lovable RLS, ~170 apps exposed); MIT NANDA
  2025 (95% of GenAI pilots no P&L impact; external partners ~2x internal);
  EU AI Act Art. 12–14 logging/oversight, penalties from Aug 2026.
- MEDIUM (attribute explicitly, not headlines): CodeRabbit 1.7x issues;
  Escape.tech scan; Gartner 40%-of-apps-agents-by-2026.
- WEAK (never use): Creatr rebuild-cost stat; unverified CVE-count and
  adoption/trust aggregator numbers; MindStudio "640% returns".

**Hedge rules for FDE copy:** no named-customer implication; always pair
"FDE" with the governed pipeline (never bare "we provide FDEs"); no scale
claims (boutique/high-touch); competitor-failure claims must cite dated
incidents/CVEs or be omitted; preempt "nine gates = slow" with
time-to-trusted-production framing; keep WEAK-tier stats out entirely.

**GTM signal:** fixed-price gated pilot (one application through all 9
gates, audit trail as deliverable) → portfolio retainer; bootcamp-style
wedge motion validated by Palantir AIP Bootcamps (1,300+).

---

## 2026-07-23 — /what redesign research (Conclave builds a wide range of software)

Current /what wrongly caps Conclave at 3 template types. Market reality:
custom-software market ~22% CAGR ($53.95B 2025 → $65.85B 2026 → $141B 2030,
The Business Research Company 2026). Demand spans a dozen+ categories, not 3.

**9 concrete illustrative example applications (domain-neutral, no invented
customers — "Conclave CAN build," never "we built X for Y"):**
1. Contract & Document Intelligence Platform — extract terms/obligations/
   renewals, route exceptions to a human. (doc-AI payback ~10-14mo, SQ Mag 2026)
2. Customer/Partner Self-Service Portal — external access under account rules.
   (portals = most common web commission; 82% found over-broad agent access,
   Gravitee 2026)
3. Internal Operations Console — replace spreadsheets/admin panels.
   (JPMorgan 450+ internal-ops AI use cases, Acuvate 2026)
4. Compliance & Audit-Trail System — regulator-ready tamper-evident records.
   (EU AI Act Aug 2026, ISO 42001)
5. Decision-Support / Analytics App — surface drivers, recommend with reasoning.
6. Agentic Process Automation Workflow — multi-step, escalates to human.
   (~171% ROI on successful deploys; 88% of pilots die pre-prod on governance)
7. System Integration / Middleware Layer — custom APIs across systems.
8. Knowledge & Retrieval Assistant — reframed as ONE option (was a template).
9. Customer-Facing Support Assistant — reframed as ONE option (was a template).
Presentation: lead with #1-#7 (new breadth); demote the original chatbot/
knowledge/workflow trio to "three of many accelerators, not the menu."

**Recommended breadth framing (honest, survives claims manifest):**
"From an idea to a production-grade platform — across the software your
business actually runs on." Sub: the 16 agents / 9 gates aren't tied to one
app type; the 3 templates are accelerators, not limits; examples below are
illustrative. Capability-spine claim: every app shares the same backbone
(human-in-command gates, tamper-evident audit trail, security+design review,
FDE delivery). One-line: "Not three app types — a general-purpose way to build
software, shown through concrete examples of what it can produce."

**Governance-matters-across-all-software evidence (citable):** 88% of agent
pilots never reach prod, blocker = governance/controls not model quality
(Northflank/AnAr 2026); >40% agentic canceled by 2027 on inadequate risk
controls (Gartner); only 13% of enterprises believe they have adequate AI
governance despite 76% having a CAIO (getagentid 2026) — the vacuum Conclave's
gates fill.

**OVERCLAIM FLAGS (must avoid):** (1) "build literally anything" — use "wide
range" + anchors; (2) any named customer/logo/delivery — illustrative only;
(3) market ROI figures (171%/2.4x/5.1x) as CONCLAVE's results — attribute to
sources as "why governed delivery matters," never own track record; (4) no
implied shipped client portfolio; (5) no compliance-guarantee language ("makes
you EU AI Act compliant") — "produces the audit trail these frameworks require";
(6) no banned industries — domain-neutral. Full source list in the research
deliverable (transcript 2026-07-23).

---

## 2026-07-25 — /what example ORDER research (serial-position effect)

Research-backed sequence for the 8 example cards (flat, curated — NOT grouped;
grouping would bury the governance differentiator and surface the technical
integration card under a header). Serial-position effect: first + last remembered,
middle skimmed (F-pattern). Lead with broadest/most-relatable; anchor value last.

RECOMMENDED ORDER:
1. Contract & document intelligence — OPENER (broadest hook: every org has
   contracts; embodies "governed clarity" — extract value, route exceptions to a
   human — without opening on the pessimistic compliance note).
2. Internal operations console — most universally-felt pain ("kill the spreadsheet").
3. Customer & partner portals — customer-facing, revenue-adjacent, easy to picture.
4. Decision-support & analytics — more abstract → skimmed middle.
5. Integration & middleware — most technical/least relatable → deepest buried slot.
6. Agentic process automation — aspirational 2026 peak, rising to recency zone.
7. Compliance & audit — RECENCY trust anchor; the last CONCRETE example, answers
   #6's autonomy with a guardrail; governance = closing reassurance, not a brake.
8. "…software you haven't scoped yet" — LAST, open-ended closer that converts a
   finite list into an unbounded promise; the implicit CTA.
Arc: concrete value → more value → intelligence → autonomy → all governed → whatever's next.
Do NOT lead with compliance/audit (over-indexes on the "brake" story). Sources:
Laws of UX / CXL / abtasty / LogRocket (serial position), Unbounce (F-pattern),
Forbes Tech Council Jan 2026 (governance demand). Full list in transcript 2026-07-25.

---

## 2026-07-25 — Visual-engagement research (text-heavy fix + "imagery")

Human wants imagery + less text ("very text heavy"). Research on how LEADING
comparable products engage users. BOTTOM LINE: for serious/trust-led technical
products (our peer set: Anthropic, Palantir, Glean, Writer, Sierra), the leading
move is NOT "add images" — it's rationed restraint + product/system clarity +
editorial text-breaking. Anthropic built its brand on "warmth, restraint, trust,"
skips symbolism, one rationed accent. Consumer AI builders (v0/Replit/Lovable)
lead with generated-output eye-candy, but that's the WRONG register for us.

WHAT WORKS on text-heavy B2B (cited): real product/UI over illustration (abstract
hero art declining); interactive demos (+63% lead-gen conv); scrollytelling for
complex stories (+85% engagement, +40% product-page conv); scroll-triggered
stat/charts; split layouts (text|visual); pull-quotes + callouts (10-20 words).
WHAT HURTS: generic stock / AI imagery = banner blindness + credibility red flag
(worst possible for a trust brand); animation without a job (NN/g: 100-300ms,
purposeful, give agency). Honesty note: can't show fake product screenshots —
our labeled "sample UI" cards are the honest substitute; lean on diagram/system
visuals.

RECOMMENDATION (impact→risk):
- P1 editorial text-breaking kit (stat callouts, pull-quotes, split cards) —
  highest ROI, zero risk, directly fixes text-heaviness. Apply to Home, /why, /what.
- P2 scroll-reveal the visuals we ALREADY own (Council Mark, replay, hierarchy,
  sample-UI) — activate, don't add; fast/purposeful, respect reduced-motion.
- P3 the honest answer to "imagery": a restrained ON-BRAND, LOCALLY-GENERATED
  abstract "council network" texture (richer ambient canvas) as sparse section
  backing/dividers — monochrome-paper + one rationed teal/gold accent. Generative-
  from-code guarantees zero external requests. NO stock, NO people, NO fake screens.
- P4 thin custom line-icon/seal-motif spot-graphics for section heads.
AVOID: stock/AI photography, human imagery, fake screenshots-as-real, heavy 3D/
scroll-jacking. Per page: /why (top priority) = heavy P1 + P2; Home = stat
callouts + pull-quotes + scroll-reveal Council Mark + ambient hero backing;
/what = more split cards; /how,/who already visual (add scroll choreography +
section icons). Sources: Mantlr, Figma trends 2026, Nebutra, Studio Siraj,
SaaSFrame, Maglr, NN/g, Webbiquity, Rewarx (full list in transcript 2026-07-25).
