# DOMAIN_KB — Child Development & Parenting Guidance

Project: little-milestones (kid profile + age-aware milestone chat + age-based
activity suggestions in the first slice; photos/timeline/products deferred).
Compiled at Intake gate by functional-agent, 2026-07-10. Web-researched;
sources at bottom.

## 1. Domain overview

The domain is infant-to-toddler (roughly 0–36 months) developmental
milestones, age-appropriate activities, and general parenting guidance.

- **Milestones are surveillance tools, not tests.** The authoritative U.S.
  reference is the CDC "Learn the Signs. Act Early." program, co-developed
  with the American Academy of Pediatrics (AAP). Checklists exist for each
  well-child-visit age (2, 4, 6, 9, 12, 15, 18, 24, 30, 36 months...). Their
  purpose is to catch the minority of children who may benefit from early
  intervention — not to rank children within the normal range.
- **The 2022 revision matters.** In February 2022 the CDC/AAP moved milestone
  checklists from ~50th-percentile framing ("half of kids do X by this age")
  to **75th-percentile** framing ("most — at least 75% of — children do X by
  this age"), added 15- and 30-month checklists, added social-emotional
  milestones, and removed hedging language like "may" or "begins to." The
  intent: eliminate the "wait-and-see" response when a child misses a
  milestone — under the new lists, a missed milestone is a clearer signal to
  discuss with a pediatrician. This drew public controversy (misleading
  claims that CDC "lowered the bar," e.g. crawling removed as a milestone,
  walking moved from 12 to 18 months); professional reactions were mixed
  (Autism Society supportive; ASHA cautious). **Practical consequence for
  this app: any milestone content must state which framing it uses and must
  not mix pre-2022 and post-2022 age numbers — they mean different things.**
- **Normal variation is wide.** Ranges like "walking: 9–18 months" reflect
  the boundaries of typical neurodevelopment; timing *within* the normal
  range is clinically meaningless. Milestone anxiety among parents is nearly
  universal even when development is fine.
- **Corrected age for preemies.** AAP advises tracking preterm children
  (esp. born <36 weeks) by corrected/adjusted age (chronological age minus
  weeks early) for at least the first 24 months. An app keyed only to
  birthdate will systematically mis-age preterm infants.
- **Standardized screening cadence.** Developmental screening is recommended
  at 9, 18, and 30 months, autism-specific screening at 18 and 24 months;
  surveillance at every well visit. An app is an adjunct to this, never a
  substitute.
- **Activity guidance has hard safety anchors**: AAP safe-sleep rules
  (back-to-sleep, bare firm sleep surface, no soft bedding, never sofas/
  armchairs for sleep), supervised-awake-only tummy time (short sessions from
  birth, building to 15–30 min/day by ~7 weeks), choking/suffocation rules
  (no small parts under 3, no pacifiers tethered to objects, food-texture
  rules), water supervision. Age-appropriate activity content that ignores
  these is not merely low-quality — it is dangerous.

## 2. Key risks & edge cases (devil's-advocate material for Plan/Architecture)

### R1. "Your kid should be doing X by now" framing is the core product risk
A naive milestone chat that compares the child's age to a milestone list and
reports deficits will (a) generate false alarm and anxiety for the large
majority of kids inside the normal range, and (b) worse, generate false
reassurance ("plenty of kids walk late, don't worry") for the minority who
actually need evaluation — the exact wait-and-see behavior the 2022 CDC
revision was designed to kill. The chat's persona must be: *most children do
X by age Y; if not, it's worth mentioning to your pediatrician* — never
diagnosis, never "your child is behind," and never "don't worry" in response
to a missed post-2022 milestone.

### R2. Information vs. medical advice — the line the LLM will drift across
Users will ask medical questions ("is this rash normal," "fever after
vaccines," "he's not talking, is it autism"). Research on consumer AI health
advice found problematic answers roughly half the time, and parents often
cannot distinguish AI-generated from clinician-written content — sometimes
trusting the AI *more*. The system prompt must hard-scope to developmental
information and activities, refuse diagnosis/medication/symptom triage, and
route to pediatrician/emergency services. **Escalation red flags the chat
must never talk a parent out of**: loss of previously acquired skills
(regression), marked asymmetry (one side moves much less), unusual stiffness
or floppiness, persistent feeding/swallowing difficulty, no response to loud
sounds, no social smile by ~3 months, poor head control by ~4 months. Also:
corrected age must never be used to explain away regression, asymmetry, or a
parent's stated concern.

### R3. Ungrounded LLM generation of milestone ages will be wrong or stale
The plan chose genai-chatbot (no RAG corpus): milestone ages and activity
suggestions come from model weights. Model training data mixes pre- and
post-2022 milestone numbers and non-authoritative parenting-blog content.
Devil's-advocate position for Architecture: the first slice should at minimum
embed a small, vetted, hand-curated milestone/activity table (CDC 2022
checklist ages, AAP activity-safety rules) in the prompt or as app data,
rather than trusting free generation — this is cheap and removes the largest
correctness risk. Full RAG can stay deferred; a static vetted table cannot.

### R4. Age computation edge cases
- Prematurity/corrected age (see above) — at minimum ask gestational status
  at profile creation, or clearly state the app assumes full-term.
- Month arithmetic: "9 months old" boundaries, leap years, and checklists
  keyed to specific visit ages (15 vs 18 months behave differently).
- Multiple children / twins (twins are disproportionately preterm).
- Children already in early-intervention or with diagnosed conditions —
  generic milestone framing is wrong for them; the app should acknowledge
  this population rather than pretend it doesn't exist.
- Out-of-range ages (newborn <2 months, or child ages past 36 months) —
  define behavior instead of extrapolating.

### R5. Activity suggestions carry physical-safety liability
Suggestions must be filtered by hard safety rules, not just "fun at this
age": no unsupervised tummy time, nothing contradicting safe-sleep (no
"cozy blanket play in the crib"), no small-part toys under 3, no whole
grapes/nuts/popcorn-type food activities for infants/toddlers, water play
only with active supervision. Each suggestion should carry supervision
context. This belongs in the functional test suite as explicit adversarial
scenarios ("suggest a sleep-time comfort activity for my 3-month-old").

### R6. Children's data privacy — relevant even before photos
The first slice already stores a child profile (name, birthdate, possibly
gestational age = health data). COPPA technically governs data collected
*from* children under 13 by child-directed services — this app collects data
*about* children *from* parents, so COPPA may not strictly apply, but
children's-privacy expectations, state privacy laws, and (if ever
international) GDPR treatment of children's/health data do. Data-minimization
is the domain norm: collect only what the feature needs (birthdate + optional
prematurity info beats full name + demographics). The deferred photo-upload
feature is where this escalates sharply — flag it now so Architecture doesn't
paint the storage design into a corner.

### R7. Anxiety-aware tone is a functional requirement, not polish
The user is frequently a sleep-deprived, worried parent at 2 a.m. Comparative
framing ("most babies her age already..."), percentile talk, and absolutist
language increase anxiety and are contraindicated by how CDC itself now
frames milestones ("most children," "talk to your doctor if"). Tone
requirements should be testable (functional suite: check responses to "my
14-month-old isn't walking" for both false alarm and false reassurance).

### R8. Later-slice landmines to record now
- **Product recommendations** (deferred): recalled baby products and
  sleep-positioner/inclined-sleeper category bans are real; any future
  product feature needs a safety/recall filter (CPSC), not raw LLM output.
- **Life-journey visualization** (deferred): if it plots the child against
  milestone timelines, R1 applies in visual form — a chart showing a child
  "behind the line" is the anxiety machine in picture form.
- **RAG mode** (deferred): if introduced, corpus must be vetted pediatric
  sources (CDC, AAP/HealthyChildren.org), not scraped parenting blogs.

## 3. What does NOT warrant pushback

The approved first-slice split itself is sound: profile + age-aware chat +
activity suggestions is a coherent, testable slice, and deferring photos
(privacy-heavy) and products (recall-safety-heavy) is the right call. The
template choice (genai-chatbot over rag-knowledge-base) is defensible for the
slice *provided* R3's vetted-static-table mitigation is adopted — free-form
generation of milestone ages without any grounding is the one assumption in
the current plan I would actively contest at Architecture.

## 4. Sources

- CDC/AAP 2022 milestone revision (rationale, 75th percentile, new 15/30-mo
  checklists): [AAP News](https://publications.aap.org/aapnews/news/19554/CDC-AAP-update-developmental-milestones-for),
  [AAFP editorial](https://www.aafp.org/pubs/afp/issues/2022/1000/editorial-cdc-developmental-milestone-checklist.html),
  [PMC review of revised checklists](https://pmc.ncbi.nlm.nih.gov/articles/PMC11025040/)
- Controversy / "lowered the bar" claims debunked:
  [Science Feedback](https://science.feedback.org/review/cdcs-updated-developmental-milestone-checklists-dont-mean-standards-childrens-development-lowered-change-surveillance-strategy/),
  [Child Neurology Foundation interview w/ Dr. Paul Lipkin](https://www.childneurologyfoundation.org/category-news-breaking-down-the-new-cdc-milestones/),
  [Sensory Health (STAR Institute)](https://sensoryhealth.org/node/1856)
- Normal range, parental anxiety, milestone-tracking practice:
  [Evidence-Based Parenting (pediatric neurology NP guide)](https://evidence-basedparenting.org/blog/developmental-milestones-guide),
  [CDC Milestone Tracker app](https://www.cdc.gov/act-early/milestones-app/index.html),
  [Harvard Health on milestone apps](https://www.health.harvard.edu/blog/app-helps-track-developmental-milestones-2017111412718)
- AI chatbots and pediatric/medical advice risk:
  [Eugene Pediatric Associates](https://www.eugenepeds.com/healthy-kids/the-risks-of-using-ai-for-medical-information/),
  [HealthyChildren.org (AAP) on AI chatbots & kids](https://www.healthychildren.org/English/family-life/Media/Pages/are-ai-chatbots-safe-for-kids.aspx),
  [CNBC — when/how to use AI for parenting advice](https://www.cnbc.com/2026/01/22/when-how-to-use-ai-chatbots-for-parenting-advice-researcher.html)
- Infant activity/sleep safety:
  [HealthyChildren.org — Back to Sleep, Tummy to Play](https://www.healthychildren.org/English/ages-stages/baby/sleep/Pages/back-to-sleep-tummy-to-play.aspx),
  [AAFP — AAP safe-sleep recommendations](https://www.aafp.org/pubs/afp/issues/2017/0615/p806.html),
  [Johns Hopkins — infant safe sleep](https://www.hopkinsmedicine.org/health/wellness-and-prevention/infant-safe-sleep)
- Red flags and corrected age for preterm infants:
  [Texas Health — developmental red flags](https://www.texashealth.org/baby-care/Infancy/developmental-red-flags),
  [Red-flag milestones in premature babies (PubMed)](https://pubmed.ncbi.nlm.nih.gov/33775086/)
- Children's data privacy:
  [FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions),
  [COPPA Rule, 16 CFR 312](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312)
