# Domain Knowledge Base: Utility Regulatory/Compliance Policy Lookup

Owner: functional-agent (standing SME + devil's advocate)
Domain question answered at Intake: "Utility regulatory/compliance policy lookup"
Scope: retrieval and explanation of official utility maintenance and
renewable-incentive policy content, with correct citations.

## 1. Domain Overview

This system sits at the intersection of two utility-sector document worlds
that this project's own sample docs make concrete:

- **Grid maintenance / reliability policy** (`grid_maintenance_policy.txt`):
  operational rules with hard numeric thresholds (90% capacity for 2+ hours,
  48-hour inspection window, 15-minute customer notification, 24-hour
  completion report). These numbers are exactly the kind of detail that
  matters for NERC/FERC-style reliability compliance — in the real world,
  utilities operate under overlapping **federal** (FERC sets rules, NERC
  develops and enforces reliability standards under FERC oversight, with
  penalties that can run over $1M per day per violation for the most
  serious/cascading-failure violations) and **state** (Public Utility
  Commission / PUC) regimes, plus their own internal operating procedures
  that go beyond what regulators strictly require. A real deployment of
  this assistant would need to know which "policy" document is federal
  mandate, which is state PUC rule, and which is the utility's own
  internal standard — because only some of these are legally binding on
  external parties. (Source: FERC Reliability Explainer,
  https://www.ferc.gov/reliability-explainer; NERC/FERC compliance
  overviews, https://www.thinkpowersolutions.com/blogs/nerc-and-ferc-compliance-2025/,
  https://www.gdsassociates.com/rates-regulatory/nerc-compliance/)

- **Renewable incentive programs** (`renewable_incentives_faq.txt`): dollar
  caps, percentage rebates, processing-day counts, and eligibility windows
  (e.g., "installed within 12 months of approval") framed as an FAQ, not a
  regulation. Real-world renewable incentive policy is notoriously
  fast-moving and multi-layered: federal tax credit rules (e.g., IRS
  guidance on "beginning construction" safe harbors for clean electricity
  credits), state-level programs, and municipal/utility-specific rebate
  programs all stack or interact, and eligibility windows and credit
  phase-outs change on short notice via new IRS notices or state PUC
  dockets. DSIRE (Database of State Incentives for Renewables &
  Efficiency, https://dsireusa.org/) exists specifically because no single
  source of truth covers all layers — that fragmentation is a structural
  feature of this domain, not an edge case. (Sources: IRS Notice 2025-42
  on "beginning construction" for Sec. 45Y/48E credits, referenced via
  Grant Thornton summary, https://www.grantthornton.com/insights/alerts/tax/2025/insights/energy-incentives-under-obbba-what-you-need-to-know;
  Federal Register renewable energy incentive notices,
  https://www.federalregister.gov/documents/2025/05/16/2025-08569/renewable-energy-production-incentives;
  DSIRE, https://dsireusa.org/)

- **Document authority levels differ and are not interchangeable.**
  Administrative law draws a real, load-bearing line between a
  **regulation** (legally binding, has force of law, went through
  notice-and-comment), **guidance** (an agency's stated interpretation or
  policy intent — explicitly *not* binding on the public), and an **FAQ**
  (informal, often the least authoritative, fastest to go stale, and
  sometimes not even reviewed by legal/policy staff before publication).
  This project's own sample corpus mixes a policy-style document with an
  FAQ-style document, which is realistic — but it also means a system that
  treats every retrieved chunk as equally authoritative is already
  misrepresenting the domain. (Sources: DOJ Justice Manual on guidance
  documents, https://www.justice.gov/jm/1-19000-limitation-issuance-guidance-documents-1;
  CRS "Agency Use of Guidance Documents," https://www.congress.gov/crs-product/LSB10591;
  ACUS Statement of Principles for Agency Guidance,
  https://www.acus.gov/sites/default/files/documents/Agency-Guidance-Documents-SOP.pdf)

- **Wrong answers in this domain have demonstrated real legal/financial
  consequences**, not just reputational ones. In *Moffatt v. Air Canada*
  (BC Civil Resolution Tribunal, Feb 2024), the airline was held liable
  for negligent misrepresentation after its chatbot invented a bereavement
  refund policy that didn't exist; the tribunal explicitly rejected the
  argument that the chatbot was a separate legal entity from the company.
  The same reasoning would apply directly to a utility's compliance
  assistant misstating a notification deadline or an incentive eligibility
  window. (Source: ABA Business Law Today,
  https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/;
  see also FTC v. DoNotPay for a regulator-side enforcement example of an
  AI tool giving unsupervised legal/compliance-adjacent output)

## 2. Key Risks / Edge Cases (devil's-advocate material for Plan & Architecture gates)

1. **Citation to the wrong authority level.** A confident, well-formatted
   citation that points to an internal FAQ when the user actually needed
   the binding regulation (or vice versa) is worse than no citation,
   because it *looks* authoritative. The system needs some notion of
   document type/authority tagging (regulation vs. guidance vs. FAQ vs.
   internal policy) surfaced to the user, not just a source filename.

2. **Staleness / versioning is invisible in a vector store by default.**
   Nothing about a Chroma embedding tells you if the source document was
   superseded last month. Renewable incentive rules in particular change
   on short notice (new IRS notices, expiring safe-harbor deadlines, PUC
   docket rulings). Without an explicit "as-of" date and a re-ingestion /
   staleness-check process, the assistant will confidently answer with
   out-of-date numbers (e.g., a rebate cap or a credit phase-out date that
   has since changed) and have no way to know it's wrong.

3. **Numeric precision cannot be "approximately right."** Both sample docs
   are dense with exact thresholds (90% capacity, 48 hours, 15 minutes, 30
   minutes, 24 hours, 20%, $4,000, 12 months, 1 MW, 10 years, 30/90/120
   business days). An LLM that paraphrases "within about a day" instead of
   "within 24 hours," or blends two similar-sounding numbers from adjacent
   chunks, produces a plausible-sounding but factually wrong compliance
   answer. This is a much higher-stakes failure mode here than in a
   generic RAG FAQ bot.

4. **Overlapping/conflicting jurisdictions produce genuinely ambiguous
   "correct" answers.** A question like "how long do I have to report an
   outage" could have different answers at the federal reliability-standard
   level, the state PUC level, and the individual utility's internal
   policy level — all simultaneously "correct" depending on which entity
   is asking and why. A system that returns a single authoritative-sounding
   number without surfacing "this depends on which regulatory layer
   applies" is oversimplifying a domain where that ambiguity is the norm,
   not the exception.

5. **"FAQ" framing invites informal user questions the source docs don't
   actually answer**, and the tempting failure mode is to have the LLM
   fill the gap by extrapolating from adjacent facts (e.g., inferring a
   commercial solar rebate cap by analogy to the residential one). The
   system needs a well-defined "insufficient evidence in corpus" refusal
   path, not silent extrapolation — this matters more here than in
   low-stakes RAG use cases because an extrapolated compliance number can
   drive real financial/operational decisions.

6. **Combining/stacking rules is a common real question and a common
   correctness trap.** The sample FAQ explicitly allows stacking with
   "most municipal-level programs unless explicitly stated otherwise in
   the municipal program's terms" — an answer that requires checking a
   *second, external* document this system may not have ingested. A
   confident "yes, incentives stack" answer that omits the
   corpus-doesn't-cover-municipal-terms caveat is a realistic and costly
   failure mode.

7. **Emergency/exception clauses override normal rules and are easy to
   miss in retrieval.** The grid maintenance doc's emergency-maintenance
   carve-out (different timing rules, different notification trigger)
   is the kind of clause that a chunking strategy tuned for the "normal
   case" paragraph can easily separate from the base rule it modifies,
   leading to answers that quote the general rule while missing the
   exception that actually applies to the user's scenario.

8. **Liability exposure is not hypothetical.** As established by
   *Moffatt v. Air Canada*, courts have already held a company responsible
   for its chatbot's factual misstatement of a company policy, rejecting
   the "AI said it, not us" defense. For a compliance-lookup tool that
   utility staff, regulators, or the public might rely on for actual
   maintenance-notification or incentive-eligibility decisions, an
   incorrect or badly-cited answer is a plausible source of real
   regulatory or legal exposure for whoever deploys this system — this
   should inform how confidently the product surfaces answers (e.g.,
   disclaimers, "verify with the source document" prompts, confidence
   signaling) at the Architecture and Plan gates.

## Sources
- FERC Reliability Explainer — https://www.ferc.gov/reliability-explainer
- NERC and FERC Compliance 2025: Utility Guide — https://www.thinkpowersolutions.com/blogs/nerc-and-ferc-compliance-2025/
- Utility Contractor Guide to NERC and FERC Compliance — https://www.thinkpowersolutions.com/blogs/nerc-and-ferc-compliance/
- GDS Associates, NERC & FERC Compliance — https://www.gdsassociates.com/rates-regulatory/nerc-compliance/
- V-Comply, Best Practices for Electric Utility Regulatory Compliance — https://www.v-comply.com/blog/best-practices-electric-utility-regulatory-compliance/
- DSIRE (Database of State Incentives for Renewables & Efficiency) — https://dsireusa.org/
- Grant Thornton, Energy incentives under OBBBA — https://www.grantthornton.com/insights/alerts/tax/2025/insights/energy-incentives-under-obbba-what-you-need-to-know
- Federal Register, Renewable Energy Production Incentives — https://www.federalregister.gov/documents/2025/05/16/2025-08569/renewable-energy-production-incentives
- EPA, Summary of Inflation Reduction Act provisions related to renewable energy — https://www.epa.gov/green-power-markets/summary-inflation-reduction-act-provisions-related-renewable-energy
- DOJ Justice Manual, Principles for Issuance and Use of Guidance Documents — https://www.justice.gov/jm/1-19000-limitation-issuance-guidance-documents-1
- Congressional Research Service, Agency Use of Guidance Documents — https://www.congress.gov/crs-product/LSB10591
- ACUS, Statement of Principles for Agency Guidance Documents — https://www.acus.gov/sites/default/files/documents/Agency-Guidance-Documents-SOP.pdf
- CRS, General Policy Statements: Legal Overview — https://crsreports.congress.gov/product/pdf/R/R44468
- ABA Business Law Today, "BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot" (Moffatt v. Air Canada) — https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
- ABA, "The legal risks of AI speaking for your business" — https://www.americanbar.org/news/abanews/aba-news-archives/2025/06/legal-risks-ai-speaking-for-business/
