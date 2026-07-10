# Industry Knowledge Base: Utilities / Energy

Owner: industry-expert
Industry answered at Intake: "Utilities / Energy"
Scope: this KB covers industry/business-trend context (where and why utilities
are actually deploying GenAI/RAG today, and industry-specific compliance
considerations) as a companion to functional-agent's `DOMAIN_KB.md`, which
covers domain/technical risk (regulatory content structure, citation-authority
risk, staleness, liability precedent). Read both before Plan & Backlog.

## 1. Industry Trends

### 1.1 Adoption is real and accelerating, but concentrated in a few use cases
Energy-sector executives report broad digitization intent — 92% plan to
expand AI-powered automation, and roughly a third of energy enterprises have
already adopted generative AI in some form (Aimultiple / SmartDev industry
surveys, 2026). Adoption clusters into four repeatable use cases, and this
project's "policy lookup assistant" sits squarely inside the second one:

1. **Customer service** — contact-center copilots and self-service chatbots
   that answer billing, outage, and program-eligibility questions.
2. **Internal knowledge management** — retrieval assistants that let field
   technicians, engineers, and contact-center reps instantly pull safety
   protocols, outage-response steps, and regulatory/policy content out of
   manuals and siloed document stores instead of paging through PDFs or
   asking a senior colleague. This is the direct precedent for this
   project's own use case. (masterofcode.com; smartdev.com)
3. **Regulatory/rate-case compliance assistance** — GenAI tools that help
   compliance and regulatory-affairs teams draft and validate rate-case
   filings and track requirement changes (e.g., SAP's "Rate Case Normalizer,"
   cited by ve3.global, reduces rate-case prep time by automating
   cross-referencing against current requirements).
4. **Field/predictive operations** — copilots trained on manuals and incident
   logs that guide technicians in real time and boost first-time fix rates;
   NextEra Energy's push to integrate proprietary asset data with predictive
   AI for crew deployment is a concrete industry example (Google Cloud
   industry blog, 2026).

A concrete deployed example directly on point: **Ontario Power Generation's
"ChatOPG"** (built with Microsoft) lets field technicians and customer-service
reps retrieve safety protocols and regulatory updates in real time, which OPG
credits with reduced delays and improved compliance consistency — this is
essentially the same shape of tool as this project, deployed at a real
utility. (Sources below)

### 1.2 What's driving adoption — three forces, all present in this project's own framing
- **Workforce attrition / knowledge loss.** This is the single most-cited
  driver in current utility-sector coverage, not a generic buzzword: roughly
  a quarter of the utility workforce is eligible to retire within five years,
  and estimates run as high as half the workforce retiring within a decade
  (Performance Services; Power Magazine; geo-nexus.com, 2026 industry
  reporting). The concern isn't just headcount — it's "the way things work
  around here" walking out the door with veteran staff who hold undocumented
  institutional knowledge of policy interpretation and edge cases. A RAG
  assistant over official policy/incentive documents is a direct, plausible
  mitigation utilities are actively pursuing for exactly this reason, not a
  speculative benefit.
- **Regulatory complexity increasing.** Compliance teams face standards that
  change faster than staff can track manually (NERC CIP standard revisions,
  state PUC dockets, IRS notices on renewable credit eligibility — as
  functional-agent's DOMAIN_KB.md documents in detail for this project's own
  sample corpus). GenAI-assisted compliance tooling is being adopted
  specifically to keep filings and internal guidance current against that
  moving target (ve3.global; IBM regulatory-compliance grounding writeup).
- **Customer/employee self-service expectations.** Both external customers
  (asking about incentive programs) and internal staff (asking about
  maintenance procedures) increasingly expect instant, conversational answers
  rather than manual-lookup or escalation to a subject-matter expert — this
  is the general trend RAG-for-employee-experience vendors (HCLTech, Squirro)
  are selling directly into.

### 1.3 Implication for this project
The industry precedent (OPG's ChatOPG) and the top adoption driver (workforce
knowledge loss) both point at the *internal-knowledge-management* framing of
this tool — technicians and compliance/CS staff looking up policy — as the
higher-precedent, higher-adoption use case, more so than a fully public
customer-facing chatbot. This should inform how the human scopes the MVP
audience at Plan & Backlog (internal staff tool vs. public-facing) since the
compliance bar (see below) differs substantially between the two.

## 2. Compliance Considerations

These are specific to utilities as a *regulated critical-infrastructure*
sector, distinct from functional-agent's domain-content risks (authority
level, staleness, citation correctness) already covered in DOMAIN_KB.md.

1. **NERC CIP / BCSI handling, if this tool ever touches operational data.**
   NERC CIP-004-7 and CIP-011-3 (effective 2024) govern how "BES Cyber System
   Information" (BCSI) — sensitive operational/grid-security information —
   can be stored and processed, including in the cloud. The revised standards
   *do* permit BCSI in third-party cloud/SaaS systems (including LLM/RAG
   pipelines) provided encryption at rest/in transit, access management, and
   vendor (cloud service provider) compliance controls are in place. This
   project's current sample corpus (public-facing maintenance policy and
   incentive FAQ text) is **not** BCSI, but the distinction matters at scope
   time: if a future ingestion pipeline is pointed at internal grid-operation
   procedures rather than public policy documents, this becomes a hard
   compliance gate, not an optional hardening step. Recommend the Plan gate
   explicitly scope the corpus as "public-facing policy/incentive content
   only, not operational/BES data" to keep NERC CIP out of MVP scope, and
   flag it as a re-scoping trigger if that changes later. (NERC CIP-004-7/
   CIP-011-3 guidance; AWS/Microsoft NERC CIP compliance guides)

2. **AI disclosure and "you are talking to an AI" requirements are
   proliferating at the state level and will likely apply if this is
   customer-facing.** Multiple 2025–2026 state laws (Utah's AI Policy Act,
   Colorado's AI Act effective June 2026, California SB 243) require
   disclosure that a user is interacting with GenAI, and some single out
   "high-risk" or regulated-service interactions for stricter disclosure
   timing. A utility incentive/policy lookup tool plausibly qualifies as
   touching a "regulated service" interaction in some state frameworks. This
   argues for a persistent, visible "this is an AI assistant, verify against
   the source document" disclosure baked into the UI from the start, not
   added later — cheap now, and consistent with the liability precedent
   (Moffatt v. Air Canada) already flagged in DOMAIN_KB.md. (DLA Piper,
   Cooley, Gunderson Dettmer 2026 AI-law trackers)

3. **PUCs are increasingly active AI regulators/watchers for utilities
   specifically**, per NYU CSMAP's "Hidden Regulators" analysis of Public
   Utility Commissions and AI governance — utilities are a sector where the
   *industry regulator itself* (not just general consumer-protection law) is
   paying attention to AI-driven customer interactions. This raises the bar
   above a generic chatbot-disclosure requirement: a utility deploying this
   tool should expect that its own PUC, not just a state attorney general,
   could scrutinize how AI-generated compliance/incentive guidance is
   presented to customers.
4. **Data handling/privacy is a named non-negotiable in utility GenAI
   deployments even for non-BCSI data** — industry guidance calls out data
   lineage tracking, access controls, and PII masking as baseline
   requirements for utility GenAI tools generally, plus a preference for
   on-prem/private-cloud/hybrid deployment options to preserve data
   sovereignty in "harshly regulated" sectors. Even though this project's
   docs contain no customer PII today, any future feature that lets a user
   submit their own account/eligibility details for a personalized incentive
   answer would cross into this requirement immediately.

## 3. Proposed Feature Backlog (industry-trend-informed)

For the human to fold into MVP scope at Plan & Backlog alongside their own
must-haves. Ordered roughly by how directly each maps to the trends above.

1. **Document authority/type badge and "as-of" date surfaced per answer**
   (e.g., "Internal Policy," "Regulation," "FAQ — informal guidance," each
   with a visible source date). Directly addresses the #1 adoption driver
   (replacing informal tribal knowledge) without recreating its failure
   mode — an assistant that looks authoritative but is silently wrong is
   worse than the manual-lookup process it replaces. Cheap to build now
   (metadata tagging at ingestion), expensive to retrofit later.

2. **Persistent "AI-generated — verify against source" disclosure + direct
   source-document link/excerpt on every answer.** Addresses the
   proliferating state AI-disclosure laws (#2 in compliance) and the
   Moffatt v. Air Canada liability precedent in one feature; also builds
   user trust, which industry writeups (Squirro, IBM) identify as the actual
   adoption blocker for utility GenAI tools, not model capability.

3. **"Insufficient evidence in corpus" explicit refusal path**, distinct from
   a generic fallback answer — when a question falls outside ingested
   documents (e.g., asks about a program/jurisdiction not in the corpus),
   the assistant should say so rather than extrapolate. This is the single
   highest-leverage feature for the credibility a regulated-utility deployment
   needs, per both DOMAIN_KB's risk #5 and the industry liability trend.

4. **Corpus scope declaration + re-scoping flag for BCSI.** Not a runtime UI
   feature but a Plan-gate deliverable: an explicit, written statement that
   the MVP corpus is public-facing policy/incentive content only (not
   operational/grid-security data), so NERC CIP BCSI controls are correctly
   out of scope for v1 — with a documented trigger for revisiting this if a
   later phase ingests internal operational procedures.

5. **Staleness/re-ingestion alerting for time-sensitive incentive content**
   (e.g., a visible "last verified" timestamp per document, plus a
   lightweight process — even manual at MVP — for periodic re-check against
   source-of-truth sites like DSIRE or IRS notices). Renewable-incentive
   rules change fast (functional-agent's DOMAIN_KB documents this
   structurally); this is the feature that keeps the "knowledge management"
   value proposition from becoming a liability six months post-launch.

6. **Audience-scoped MVP (internal staff tool first, public-facing later).**
   A backlog/scoping recommendation, not a UI feature: the strongest industry
   precedent (OPG's ChatOPG) and the lowest compliance bar both point to
   launching as an internal tool for technicians/compliance/CS staff before
   opening it to the public, since state AI-disclosure laws and PUC scrutiny
   bear most heavily on customer-facing deployments.

## Sources
- Masterofcode, Generative AI in Energy and Utilities Sector Use Cases — https://masterofcode.com/blog/generative-ai-in-energy-and-utilities
- SmartDev, AI in Utilities: Top Use Cases — https://smartdev.com/ai-use-case-in-utilities/
- Aimultiple, AI Utilities: Top 15 Use Cases & Case Studies (2026) — https://research.aimultiple.com/ai-utilities/
- Google Cloud, How 7 power & energy companies are innovating with cloud and AI in 2026 — https://cloud.google.com/transform/power-energy-companies-innovating-with-ai-and-cloud-2026-industry-tech-trends
- Deloitte, 2026 Power and Utilities Industry Outlook — https://www.deloitte.com/us/en/insights/industry/power-and-utilities/power-and-utilities-industry-outlook.html
- PwC, Generative AI for energy and utilities: 5 surprising facts — https://www.pwc.com/us/en/tech-effect/ai-analytics/generative-ai-for-energy-and-utilities.html
- HCLTech, GenAI for Smarter Employee Experience in Utilities — https://www.hcltech.com/blogs/genai-for-smarter-employee-experience-in-utilities
- VE3, GenAI for Utility Contact Centres & Customer Experience — https://ve3.global/blog/genai-for-utility-contact-centres-customer-experience-driving-next-generation-process-automation-in-energy
- Squirro, RAG in 2026: Bridging Knowledge and Generative AI — https://squirro.com/squirro-blog/state-of-rag-genai
- IBM, Enhancing regulatory compliance in the AI age by grounding documents with generative AI — https://www.ibm.com/think/insights/enhancing-regulatory-compliance-ai-age
- Performance Services, The Disappearing Utility Workforce — https://www.performanceservices.com/resources/the-disappearing-utility-workforce/
- Power Magazine, Addressing the Challenges Presented by a Retiring Utility Workforce — https://www.powermag.com/addressing-the-challenges-presented-by-a-retiring-utility-workforce/
- geo-nexus, Retirement Boom Leading to Knowledge Loss? — https://geo-nexus.com/retirement-boom-leading-to-knowledge-loss-transition-to-an-off-the-shelf-solution/
- EnergyCentral, How Workforce Retirement Is Quietly Slowing Utility Modernization — https://www.energycentral.com/energy-biz/post/how-workforce-retirement-is-quietly-slowing-utility-modernization-ARo0A32pscACfJH
- AssurX, BCSI Data in the Cloud – A Field Guide to NERC Compliance — https://www.assurx.com/bcsi-data-in-the-cloud-a-field-guide-to-nerc-compliance/
- NERC, Reliability and Security Technical Committee Implementation Guidance (CIP-004-7 R6 / CIP-011-3 R1, cloud/BCSI) — https://www.nerc.com/globalassets/programs/compliance/compliance-guidance/implementation/cip-004-7-r6-and-cip-011-3-r1---cloud-solutions-for-bcsi-rstc.pdf
- AWS, NERC CIP Standards for BES Cyber System Information Compliance Guide — https://aws.amazon.com/blogs/industries/new-compliance-guide-nerc-cip-standards-for-bes-cyber-system-information-on-aws/
- Microsoft, NERC CIP compliance in Azure — https://www.microsoft.com/en-us/security/blog/2020/02/12/nerc-cip-compliance-azure/
- DLA Piper, AI disclosure laws on commercial chatbot interactions are on the rise — https://www.dlapiper.com/en-us/insights/publications/2026/01/ai-disclosure-laws-on-chatbots-are-on-the-rise-key-takeaways-for-companies
- Cooley, AI Chatbots at the Crossroads: Navigating New Laws and Compliance Risks — https://www.cooley.com/news/insight/2025/2025-10-21-ai-chatbots-at-the-crossroads-navigating-new-laws-and-compliance-risks
- Gunderson Dettmer, 2026 AI Laws Update: Key Regulations and Practical Guidance — https://www.gunder.com/en/news-insights/insights/2026-ai-laws-update-key-regulations-and-practical-guidance
- Arnall Golden Gregory, AI Chatbot Compliance: Key Legal Risks and Regulatory Considerations for Businesses in 2026 — https://www.agg.com/news-insights/publications/ai-chatbot-compliance-key-legal-risks-and-regulatory-considerations-for-businesses-in-2026/
- NYU CSMAP, The Hidden Regulators: Public Utility Commissions and AI Governance — https://csmapnyu.org/impact/policy/the-hidden-regulators-public-utility-commissions-and-ai-governance
