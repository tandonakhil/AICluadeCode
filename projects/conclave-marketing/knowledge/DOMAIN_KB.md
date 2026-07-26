# DOMAIN_KB: B2B AI-Platform Marketing Websites (Conversion-Focused Marketing Site Engineering)

**Project**: conclave-marketing | **Researched**: 2026-07-17 | **Agent**: functional-agent (content returned to orchestrator; file written by orchestrator per KB-write policy)

## 1. Domain framing

The functional domain is B2B product-marketing websites for AI/software platforms: small, fast, credibility-dense sites whose job is (a) explain what the platform does in seconds, (b) make an enterprise-skeptical buyer trust it, (c) route the visitor to one clear next action. For Conclave the "buyer" is anyone evaluating a governed multi-agent SDLC approach for energy-industry AI apps. The site itself is also a proof artifact: it was built *by* the platform it markets — that self-referential proof is the strongest asset available and should be treated as a first-class messaging element.

## 2. Messaging architecture and conversion patterns

- **Hero thesis**: 2026 standard is story-driven, outcome-first heroes that demonstrate value within 3–5 seconds — short headline (guideline: under ~44 characters), one subline naming the problem, one primary CTA. Feature-list heroes underperform problem/outcome framing. Micro-animation showing the product working (Conclave's looping council/pipeline diagram fits this pattern exactly — animation as *explanation*, not decoration).
- **One primary CTA per page.** Competing CTAs measurably depress conversion. Secondary links are fine but visually subordinate. For a local/no-backend-form context, the "conversion" is the Contact page — every page should end by routing there (the planned giant typographic closing CTA is the right pattern).
- **Narrative order that converts** (Home): problem → thesis → how it works (progressive disclosure, since MAS is a complex product) → proof → value-by-persona → closing CTA. Numbered sections (already in the v5 seed and THRED reference) aid scannability.
- **Persona segmentation**: tabbed value-by-role modules (CxO / architect / delivery lead style) let multi-stakeholder buying committees self-select. Multi-stakeholder messaging is explicitly a 2026 hero/homepage best practice — B2B AI purchases average 5+ evaluators. Each tab needs a *distinct* value statement, not the same claim reworded.
- **Social proof hierarchy**: named customer outcomes > quantified anonymous outcomes > analyst citations > logos > self-description. Conclave has no external customers; do not simulate having them. Usable honest proof: the platform's own artifacts (registry, gates, real projects built, test evidence), plus properly attributed analyst research (Gartner citations, per the project's hard rule).
- **Copy discipline**: concrete verbs, no "revolutionary/cutting-edge" filler; buyers pattern-match AI hype and discount it. Specificity is the credibility currency.

## 3. What enterprise buyers of AI platforms need to see (trust signals)

Buyer trust in vendor AI claims has *fallen* (TrustRadius: trust in vendor AI ethics 58% → 42%, 2023–2025); evidence now beats claims decisively.

- **Transparency about what the AI actually does**: buyers want to see why a decision was made, what data/rules applied, and where humans intervene. Conclave's human-in-the-loop gates and orchestrator-with-final-human-say model is precisely what "guarded autonomy" buyers ask for — make governance a headline feature, not a footnote.
- **Governance and accountability**: documented process (gated pipeline, agent registry, test-suite ownership, decision logs) is a differentiator; show real artifacts or faithful renderings of them.
- **Measurable outcomes and integration story**: quantified results from comparable work; for Conclave, honest equivalents are "N projects through the pipeline," gate/test evidence, template catalog — real numbers only.
- **Human validation**: ~71% of buyers want humans validating AI outputs — Conclave's design literally encodes this; say so plainly.
- **Analyst grounding**: real, verifiable citations (title, publisher, year, and ideally link). Never a stat without a source; never a source that doesn't say what's claimed.

## 4. Information architecture: small multi-page site (Home / Solutions / Contact)

- **Home**: thesis + compressed proof + persona value + route to Solutions and Contact. Keep nav minimal (3–4 items); minimal navigation is a proven conversion pattern.
- **Solutions**: the deep-dive for evaluators — how the pipeline works, agent roster/roles, governance model, templates/stack tab module with detail cells. Progressive disclosure: overview cards → expandable detail. This page carries the technical-buyer burden so Home can stay light.
- **Contact**: one action, zero friction. State response expectation. No fake form if nothing processes it — a mailto/real address is more honest than a dead form (and the placeholder `hello@conclave.example` must be replaced before external sharing — human-owned).
- **Cross-page consistency**: shared header/footer, identical nav order, THRED-style footer brand block on every page; consistent copper identity. Every page ends with the closing CTA pattern.
- **Real routes** (FastAPI-served) with correct titles, meta descriptions, canonical URLs per page — table stakes even for a local-first site.

## 5. Performance and accessibility table stakes

- **WCAG 2.2 AA** is the current build target (EAA mandates it in the EU; smarter than building to 2.1). ~96% of sites fail basic checks — passing is itself a differentiator, and for a platform selling *governed* software delivery, an inaccessible marketing site is a self-refuting artifact.
- Specifics for this design language: color contrast of copper-on-dark text (verify 4.5:1 body / 3:1 large); `prefers-reduced-motion` support for the always-moving animations and marquee (looping motion without a pause/reduce path is a WCAG 2.2.2 failure); keyboard-operable tab modules with proper ARIA (`tablist`/`tab`/`tabpanel`); focus-visible states on the grow-on-hover underline links; semantic landmarks and heading order per page.
- **Core Web Vitals**: LCP < 2.5s, CLS < 0.1, INP < 200ms. Self-contained assets and zero external requests (project constraint) make this easy — keep it that way: system font stack or subsetted self-hosted fonts, SVG/CSS animation over video/canvas where possible, no layout shift from late-loading hero art.
- Mobile-first: majority of landing-page visits are mobile; marquees, tab modules, and giant typography all need deliberate small-screen behavior, not just shrinkage.

## 6. Common failure modes (hard rules for this project)

1. **Fabricated or unverifiable claims**: invented customer quotes, logos of companies that aren't customers, made-up stats, misattributed analyst quotes. Project hard rule: only real, verifiable citations. Every stat must trace to a checkable source; if a Gartner claim can't be verified, cut it.
2. **Stat misuse**: real stat, wrong framing (out-of-context percentages, vendor-funded studies presented as independent, old data presented as current). Cite year and scope inline.
3. **Dark patterns**: fake urgency/scarcity, forced-consent contact forms, disguised ads, confirm-shaming CTAs. B2B enterprise buyers punish these; also increasingly regulated (FTC/EU dark-pattern enforcement).
4. **Overpromising the AI**: implying full autonomy, implying production customers or scale that doesn't exist. The trust-gap data says buyers detect and penalize this.
5. **Animation over substance**: THRED-style motion that harms readability, performance, or accessibility, or that decorates rather than explains.
6. **Marketing/product drift**: site describes capabilities the platform doesn't have (or has removed). Mitigation: source claims from `admin/MAS_REGISTRY.md` / `ROADMAP.md` at build time and re-verify at Test.

## 7. Devil's-advocate notes for Plan gate

- **Biggest risk: overclaiming.** Conclave is an internal platform with zero external customers and local-only projects. Any copy resembling "trusted by energy companies" or implying commercial traction is fabrication. Force the plan to define the honest proof set up front (real artifacts, real project count, real gate evidence) and forbid customer-shaped language.
- **Who is this actually for?** "Marketing site" implies external buyers, but the site is local-dev with a placeholder email and no deployment target. If the real audience is demo/stakeholder-showcase, say so in the plan — it changes CTA design (Contact page may be the weakest page in the IA; challenge whether it earns a full page vs. a strong footer block).
- **THRED replication vs. accessibility budget**: "always-moving animations" and "replicate remaining THRED components" is a scope magnet and a WCAG risk. Plan should rank components by messaging value and require reduced-motion parity for each, not port them wholesale.
- **Persona tabs need real content**: a CxO-style tab module with thin, near-duplicate copy is worse than no tabs. If we can't write three genuinely distinct persona value stories, cut to two or drop the module.
- **Gartner-citation rule needs an enforcement mechanism**, not a vibe: plan a citations manifest (claim → source → verified date) that the Test gate checks, so the hard rule survives future enhancements.
- **Self-referential proof cuts both ways**: "built by Conclave itself" is compelling only if the site is excellent. Any accessibility failure, broken route, or sloppy copy directly undermines the product claim. Quality bar here is a product claim, not a nice-to-have.

---

Sources: [Genesys Growth — B2B SaaS homepages 2026](https://genesysgrowth.com/blog/designing-b2b-saas-homepages), [Genesys Growth — landing pages 2026](https://genesysgrowth.com/blog/designing-b2b-saas-landing-pages), [SaaS Hero — value prop messaging](https://www.saashero.net/strategy/b2b-saas-value-prop-messaging/), [SaaS Hero — high-converting landing pages](https://www.saashero.net/design/high-converting-landing-page-examples/), [TrustRadius — bridging the trust gap](https://solutions.trustradius.com/vendor-blog/bridging-the-trust-gap-b2b-tech-buying-in-the-age-of-ai/), [INFUSE — Voice of the Buyer AI Reality Check](https://infuse.com/insight/voice-of-the-buyer-ai-research-reality-check-from-hype-to-proof/), [Insider Growth HQ — what enterprise buyers expect from AI](https://www.insidergrowthhq.com/p/what-enterprise-buyers-really-expect), [Kai Waehner — enterprise agentic AI trust](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/), [Siteimprove — Core Web Vitals and WCAG](https://www.siteimprove.com/blog/core-web-vitals-wcag/), [Juicebox — WCAG 2.2 accessibility guide](https://juiceboxinteractive.com/blog/accessibility-guide/), [Level Access — WCAG compliance 2026](https://www.levelaccess.com/compliance-overview/wcag-web-content-accessibility-guidelines/), [Kritano — web accessibility 2026](https://kritano.com/blog/web-accessibility-the-complete-guide-for-2026).

---

## 2026-07-23 — /what breadth: functional scope + honest boundary (functional-agent)

Pipeline IS genuinely general-purpose (16 agents, 9 gates; code-agent has
Read/Write/Edit/Bash — writes arbitrary code, not just template fills;
plan-agent already handles the "none-of-the-3-templates" branch). Templates
are accelerators, not the ceiling — human is right that "3 templates"
undersells it.

**Honest functional breadth (legitimate pipeline outputs):** web apps
(SPA/SSR), internal tools/dashboards/admin, HTTP APIs/microservices, agentic/
LLM automations, RAG/knowledge/document-processing, GenAI chatbots, data
pipelines/ETL/batch, integrations/connectors/webhooks, CLI/dev tooling,
customer portals. Proven stack: Python/FastAPI, Next.js/JS web, LangChain/
LangGraph, Chroma.

**HARD OUT (dishonest to claim — no toolchain):** native mobile (iOS/Android),
embedded/firmware/IoT, games/GPU/model-TRAINING at scale, desktop-native,
blockchain/smart contracts, formally-certified/regulated SW (medical/avionics
— governance = human-gates+test-evidence, NOT formal certification).

**MUST HEDGE (can design/build, not operate-as-implied):** cloud/production
hosting — deploy-agent target_env is LOCAL-ONLY (cloud is roadmapped, not
shipped); "deploy" today = local prod/ repo + uvicorn + smoke test. Also: no
"at scale"/multi-tenant-SaaS delivered claims, no hard-real-time/low-latency
(no perf harness), non-templated stacks carry more risk than "wide range"
implies.

**Honest center of gravity:** "a wide range of AI-centric and web/API/data
software" delivered to YOUR environment — NOT "any software." The FDE
"in your own environment" framing naturally covers the local/self-hosted
reality as a positive, not a limitation.

**Words to BAN on the page:** "any software", "anything", "production-ready in
the cloud", "at scale" (as delivered-today claims). **Claims-manifest rows
needed:** (a) delivery=local/self-hosted, cloud roadmapped; (b) web not
native-mobile; (c) no embedded/real-time/certified claims; (d) templates =
accelerators (backed by plan-agent ambiguous-branch handling).
