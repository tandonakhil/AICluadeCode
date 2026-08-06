# SECURITY_KB — conclave-finance-studio

Owner: `security-architect`. Gate 6 · Architecture, joint owner with
`solution-architect`.
Created 2026-07-31 · **Status: proposed under standing authorization
(`batch_authorized`), awaiting human review.**

Scope of this file: authentication, authorization and segregation of duties;
credential and secrets handling; the posting boundary; retention and
tamper-evidence; the disposition of `industry-expert`'s obligations A–S; the
threat model; input-validation boundaries; and the security test suite.

**Not in this file, deliberately.** Component decomposition, data flow, the
semantic layer, storage-technology selection and the warehouse-lag resolution
belong to `solution-architect` this pass. Content and behaviour guardrails —
what the model is permitted to *say*, refusal behaviour, bias — belong to
`responsible-ai-architect`. Where those lanes touch mine I state a
**constraint** on their design rather than designing their component (§11), and
where a boundary is genuinely unclear I say so rather than resolving it
silently (§10.3).

---

## 0 · Completeness check — binding decisions this pass was checked against

Every binding decision in `PROJECT_CONTEXT.md`'s Decisions Log, in full, and how
this design satisfies or conflicts with it.

| Binding decision | How this design satisfies it |
|---|---|
| **2026-07-30 — Product shape: BOTH (pre-built agents *and* a builder)** | The builder (F16) is deferred, but the SoD design is built for it now, not later. §1.3's authorship-closure engine is defined over *authored artefacts*, not over "skills authored in the builder" — so when F16 ships, a user-authored skill version enters the closure with no new mechanism. This is the direct answer to `DOMAIN_KB` §7.1: the author role is enforced before the builder that creates it exists. |
| **2026-07-30 — Personas: all three** | Role model §1.2 names all three plus four non-persona roles the compliance surface requires (data owner, policy owner, assurance, auditor). FP&A's read path is the one role that touches no approval capability — stated explicitly rather than left implied. |
| **2026-07-30 — Write-back with per-action approval** | §1.3 makes `approver ∉ authorship_closure ∪ {invoker}` a broker-enforced precondition of approval, not a policy statement. §2 removes the posting credential from MVP1 entirely. §3 extends the same separation *outside* our boundary via CUEC C8, because in MVP1 the poster is a human loading a file. |
| **2026-07-30 — A7.2 and A8.3 delegated to SMEs** | A7.2's answer (`DOMAIN_KB` §6.2) is treated here as a **security** requirement, not only a product one: §6 T6 records that dwell, override-rate and probe metrics are the *only* instruments that distinguish a diligent approver from a rubber-stamping one, which makes them controls in my lane and drives the probe-visibility ACL. |
| **2026-07-31 — SCOPE CORRECTION: not the GL, do not imitate GL** | Nothing here designs a ledger control. Oracle's posting integrity, balancing, period control and reversal mechanics are Oracle's; §3 treats them as CUECs to be *verified*, never as controls to be rebuilt. Our retention clock (§4) attaches to the decision dossier, not to a copy of the ledger. |
| **2026-07-31 — PRODUCT DIRECTION part 1: research-driven backlog** | No feature invented, none dropped. Every requirement in this file lands on an existing feature (F36, F40, F1, F2, F5, F38, F39, F41) or on deployment process. Seven genuinely new requirements are marked **NEW** in §10.1 so they cannot enter the build unnoticed or be assumed already covered. |
| **2026-07-31 — PRODUCT DIRECTION part 2: NL, skill-based, datasets under guardrails** | §6 T2 treats the NL surface as the primary injection boundary and §7 specifies the model→broker interface as an untrusted input boundary. The `no free-form SQL` rule (`PLAN` §6.2, `AC-F39-02`) is re-stated here as a **security** control with a database-grant backstop (§2.4), so it survives an application-logic defect. |
| **2026-07-31 — STANDING AUTHORIZATION to build MVP1; trust SME judgement; make assumptions** | Calls made, not returned. §11 lists the five assumptions I made (SA1–SA5) and what would reverse each. One item is escalated at the end of §11 and it is not a blocker. |
| **2026-07-31 — MVP1 SCOPED TO ERP DATA ONLY** | Single-source narrows the trust boundary count but not the obligation set. §2.4's per-skill least-privilege grants are specified against certified dataset objects rather than against source systems, which is the same phase-2 seam `PLAN` §8 asks for — adding a non-Oracle source must not require re-granting per skill. |
| **2026-07-31 — Gate 4 ambiguity 1: refusal surface is F50** | The refusal surface is in my authz model: A19–A22 refusals are **not** permission-gated. No role, including administrator, can unlock them, and no capability allowlist may name them. A refusal that a sufficiently privileged user can turn on is a roadmap gap wearing a refusal's clothes — §1.4. |
| **2026-07-31 — Gate 4 ambiguity 2: F42 not cuttable while criterion 21 stands** | Untouched. No security requirement here depends on F42 or would make it cheaper to cut. |
| **2026-07-31 — Gate 4 closed: 186 criteria; no criterion may assert explanation quality** | Honoured. **No requirement in this file asserts explanation quality**, and my suite (§9) contains no scenario that could be passed by writing a clearer explanation. §6 T2's injection defences are deliberately specified as *structural* (the model cannot name a dataset, cannot author SQL, cannot select its own capability) rather than as "the model should ignore instructions in data", which would be a prompt-quality assertion and therefore not a control. |
| **2026-07-31 — Gate 5(a): `AC-F41-03` strengthened, riskiest element largest** | Not contradicted. §6 T6's probe-visibility ACL constrains *who can read probe assignment*, never how anything is rendered. |
| **2026-07-31 — Gate 5(b): routing budget with recorded controller override** | Adopted into the authz model: the routing-budget override is a controller-role capability, is subject to the same override rules as obligation O (dual-authorised, reason-coded, time-boxed, counted), and is **not** a path by which an SoD block can be cleared (§1.3.6). |
| **2026-07-31 — Gate 5(c): probe reveal timing routed to `responsible-ai-architect`** | Not decided here. I constrain only *access* to the forward probe schedule (§6 T6); the reveal-timing decision remains `responsible-ai-architect`'s and my ACL is compatible with either answer. |
| **2026-07-31 — Gate 5(d): MVP1 desktop web only; product remains multi-surface** | §2.3 and §6 T1 specify enforcement at the broker precisely so that a second surface inherits it by construction. No control in this file is implemented in, or depends on, the desktop web client. |
| **2026-07-31 — Gate 5 closed: narrative collapsed and last; no green anywhere** | Compatible. The two security-relevant UI states I require — CUEC verification status on the export screen (§3.5) and SoD eligibility before review (§1.3.6) — are specified as *stated facts with dates and names*, never as a green tick. A green "verified" badge would be exactly the "fine, move on" affect the gate-5 decision prohibits. |
| **Full roster, 14 agents. Test Policy: all suites blocking, no advisory exceptions** | §9 defines the security suite's scenarios so it can return `0` rather than `3`. Exit `3` is not a pass and I have written no scenario the build cannot pass. |
| **`security-architect` owns `industry-expert`'s compliance obligations** | §5 disposes of all nineteen obligations A–S individually: discharged by design (with the component named), discharged by process (with the owner named), or deferred (with the owner and the trigger named). No obligation is left as "handled by the architecture". |

**Conflicts with a binding decision: none.** One disagreement with
`solution-architect` is flagged in §10.2 and one with `plan-agent`'s tier
framing in §5.2 — both stated openly rather than resolved silently.

---

## 1 · Authentication & Authorization Design

This section is mandatory and is never collapsible to a waiver. The decision is
reasoned to from stated criteria, and the criteria are checkable against this
project's actual attributes rather than taken on trust.

### 1.1 The decision

**Authenticated, per-identity access is required for every interaction with
this system in MVP1, including read-only exploration. There is no anonymous
path, no shared login, no "pilot mode" that defers auth, and no unauthenticated
route of any kind.**

Concretely:

1. **Authentication is federated to the customer's identity provider** via OIDC
   authorization-code flow with PKCE. **No local password store is built in
   MVP1.** Rationale: the customer already runs an IdP for Oracle ERP Cloud;
   building a second credential store for a finance-critical system creates a
   joiner/mover/leaver control we would then have to design, document and have
   tested, and de-provisioning lag on a system that approves journals is an
   audit finding waiting to happen. Federating makes termination of employment
   an immediately effective revocation, which is the property an auditor
   actually tests.
2. **MFA is required and is asserted by the IdP**, not by us. We record the
   `amr`/`acr` claim in the approval record as the *authentication strength*
   field obligation A already requires (`INDUSTRY_KB` §4.3, dossier item 6). We
   do not merely record "a user was signed in"; we record how they proved it.
3. **Step-up re-authentication at the moment of approval.** An approval
   (`AC-F41-*`), an override second key (`AC-F36-07`), a guardrail bundle
   publication, and a dataset certification each require a fresh authentication
   assertion no older than 5 minutes. This is the non-repudiation leg: a
   long-lived session on an unlocked laptop at 11pm on day 3 is precisely the
   `INTAKE.md` A3.2 scenario, and "someone was logged in as them" is a defence
   that destroys the evidential value of every approval in the period, not just
   the disputed one.
4. **Sessions are short and are bound.** Idle timeout 30 minutes, absolute
   lifetime 8 hours, tokens bound to the authenticated session (sender-
   constrained, e.g. DPoP or mTLS-bound where the deployment supports it), and
   invalidated on IdP-signalled termination. Cookies `HttpOnly`, `Secure`,
   `SameSite=Lax` (Strict breaks the OIDC return leg), with CSRF protection on
   every state-changing route regardless.
5. **Authorization is deny-by-default and is evaluated at the broker.** The UI's
   only role is not to offer what the broker would refuse. The broker is the
   control (§2.3, obligation M). This is not a duplication of
   `solution-architect`'s enforcement topology — it is the security requirement
   that topology must satisfy.

**Why not "no auth needed for a local MVP".** That conclusion is available on
some projects on this platform and it is not available here; §1.2 states the
criteria that make it unavailable, and every one of them is checkable against
this project's own documents.

### 1.2 The criteria evaluated to reach that decision

Each criterion is stated with the project attribute that decides it and the
source that records that attribute, so a reader can falsify my conclusion.

| # | Criterion | This project's answer | Source |
|---|---|---|---|
| 1 | **Multi-user?** | Yes — three primary personas with *structurally different* authority. Approval is a named-person control; a system that cannot tell two users apart cannot implement it. | `INTAKE.md` A2.2; Decisions Log 2026-07-30 |
| 2 | **Does the product implement a segregation-of-duties control?** | Yes, and it is the defining one. SoD is authorization by definition. There is no way to have SoD and not have authn/authz. | `INTAKE.md` A-write; `DOMAIN_KB` §7.1; obligation F |
| 3 | **Is identity itself an evidential artefact?** | Yes. Obligation A requires approver identity *and authentication strength* inside an immutable record. Auth is not access control here — it is a data field in the audit evidence. | `INDUSTRY_KB` §4.3 item 6 |
| 4 | **Regulated data / regulated output?** | Yes on both. ICFR scope on day one; there is explicitly **no "pilot outside SOX" path**. Negative assurance ("no exceptions") is itself a regulated output, so even the read-only path is in scope. | `INDUSTRY_KB` §4.1, §12.2 |
| 5 | **PII?** | **Undetermined and treated as present.** Ledger data is generally not personal data, but payroll accruals, commission and expense data can be, and nobody has yet confirmed the pilot warehouse's contents. I do not escalate this — I design for the worse case and enforce it (§6 T7): datasets carry a `contains_personal_data` classification at certification, and personal-data-flagged datasets are denied to any model-bound or action-capable path in MVP1. | `INDUSTRY_KB` §4.5 (routed to me); this pass's call |
| 6 | **Network exposure beyond localhost?** | Yes. Desktop web over a warehouse, used by a distributed finance team during close, reaching a customer's Oracle tenant. Nothing about this runs on one machine. | `INTAKE.md` A5.1, A6.1 |
| 7 | **Deployment target?** | A hosted service against a customer's warehouse and ERP tenant. §11 SA1 records my assumption that MVP1 pilots single-tenant-per-customer with tenancy modelled from day one. | `PLAN` §10 (CUEC "per tenant"); this pass's call |
| 8 | **Does the system act on the outside world?** | Yes, at one remove. MVP1 exports a Journal Import artefact a human loads into the general ledger of a company that may be a public filer. The blast radius of an unauthenticated actor is a fraudulent journal in someone's audited financial statements. | `PLAN` §7.3 F40 |
| 9 | **Is there a plausible "single trusted user" reading?** | No. Even a one-person pilot fails criteria 2 and 3: with one identity there is no second key and every approval record is evidentially void. | — |
| 10 | **Would deferring auth be cheap to retrofit?** | No. Retrofitting identity into a dossier corpus already written is the same class of problem as retrofitting the version tuple (`PLAN` §7.3 F2) — the historical records simply do not have the field. Seven-year retention means the gap is permanent. | `INDUSTRY_KB` §4.3; obligation G |

Ten criteria, ten pointing the same way, four of them independently sufficient.
The decision is not close and I record it as not close.

### 1.3 The role model and the SoD constraint engine — `author ≠ approver ≠ invoker`

This is the hard part of the gate and it is where I have done the most design.
`DOMAIN_KB` §7.1 found a real defect: a third role, the **author**, has more
effective control over the ledger than either preparer or approver, because the
author sets what is prepared, what evidence surfaces, and what threshold
suppresses an exception. Formally preparer ≠ approver; substantively, self-
approval by proxy. MVP1 has no builder — but it has guardrail bundles,
threshold values, declared populations and dataset certifications, and **all of
those are authored by somebody**. The defect exists in MVP1. It just has fewer
authors.

I am specifying it as an **enforced constraint evaluated at the broker**, not a
policy statement in a runbook.

#### 1.3.1 Principal types — the type partition is the first control

Every principal in the system has an immutable `type`, assigned at creation and
not editable by any role:

- **`human`** — a natural person, federated from the customer IdP.
- **`agent`** — a named non-human principal, one per agent, per obligation D
  (`AC-F5-01`). Holds workload identity, never a user token.
- **`service`** — infrastructure principals (the broker, the evidence writer,
  the CUEC prober, the export builder). Not user-facing.

**Hard rules, non-overridable at every permission level including
administrator:**

- The `approved_by`, `override_second_key` and `certified_by` fields accept a
  principal of type `human` only. The broker rejects any other, and the dossier
  schema has **no field a non-human principal can fill that carries approval
  semantics**. An agent's review of another agent's output may be attached as
  *evidence*; it can never be recorded as *approval*.
- No capability allowlist may grant `approve`, `override.second_key`,
  `dataset.certify` or `bundle.publish` to a principal of type `agent`. This is
  checked at bundle publication, not only at evaluation time — a bundle that
  attempts it fails to publish and names the offending grant.
- **A human's session token is never usable by an agent runtime.** Agent runs
  carry short-lived, audience-scoped workload credentials issued per run and
  bound to the run ID. There is no impersonation path and no "run as user".

This is the enforcement of `industry-expert`'s finding that **an AI cannot
occupy the human leg of an SoD control whose purpose is fraud deterrence rather
than accuracy** (`INDUSTRY_KB` §4.2 problem 2). That finding is not satisfied by
declining to build an AI reviewer; it is satisfied by making the approval field
structurally incapable of holding a non-human, so that a future feature cannot
quietly fill it.

#### 1.3.2 Roles (capability bundles, assigned via IdP group claims)

| Role | May | May not |
|---|---|---|
| **Staff accountant** | Invoke Tier 1 skills; explore uncertified datasets; disposition items (R1–R6); approve within the quantitative guardrail band assigned to the role | Certify datasets; author or publish guardrail bundles; approve above band; be a second key on their own override |
| **Controller / close manager** | Everything above; approve escalations; second key on overrides; approve risk-increasing bundle changes; exercise the gate-5 routing-budget override | Publish a bundle *and* approve output decided under it (§1.3.4); read the forward probe schedule (§6 T6) |
| **FP&A analyst** | NL inquiry and exploration over certified and uncertified datasets; read dossiers | Any approval capability whatsoever; invoke an action-capable skill; request an export |
| **Data owner** | Certify datasets, set certification metadata and the personal-data classification | Approve any proposal that read a dataset they certified for the period (§1.3.4) |
| **Policy owner** | Author guardrail rules and threshold values; propose a bundle | Publish it alone (dual authorisation, §6 T1); approve output decided under it |
| **Assurance** | Configure probe rate; read the forward probe schedule; read override/dwell metrics | Approve, invoke, certify, or author policy — a measurer who can also act is not a measurement |
| **Auditor (external/internal)** | Read dossiers; request an F1 export | Everything else. Read-only by construction, not by convention |
| **Platform admin** | Operate the service, manage principals and role assignment | Approve, certify, author policy, publish a bundle, read dossier contents, or alter retention (§4.4). Admin is an *operations* role, not a *finance* role |

**The platform-admin exclusion is deliberate and I expect it to be argued
with.** A conventional SaaS admin can do everything; here, an admin who can
grant themselves an approval capability *and* approve is a one-person path to
the ledger. Role assignment therefore emits a control event, and a self-grant —
any change to one's own role set — is rejected outright rather than logged.

#### 1.3.3 Authored artefacts — the closure's input set

An **authored artefact** is any versioned object that shapes what an agent
proposes or what surfaces to a reviewer. In MVP1 that set is exactly:

| Artefact | Feature | Author recorded as |
|---|---|---|
| Skill / agent definition version | F5 | Vendor-authored in MVP1 (F16 deferred); the field exists and is populated now |
| Prompt version | F2 | Prompt owner |
| Guardrail **rule** version (incl. every quantitative threshold value) | F36 | Policy owner named on the rule (obligation L requires a named owner — this is what it is *for*) |
| Guardrail **bundle** version | F36 | Proposer + publisher (dual, §6 T1) |
| Declared expected population for a skill | F38 | Population owner |
| Dataset certification version | F38 | Certifying owner (obligation Q) |
| Model version pin and parameter set | F2 | Registry owner |
| An override applied to a specific action | F36 | Requester + second key |

Every one of these is already required to be versioned and attributable by
obligations I, J, L, N and Q. **The SoD engine adds no new artefact and no new
metadata** — it consumes what F2, F36 and F38 already have to produce. That is
deliberate: an SoD control that needs its own parallel bookkeeping is one that
drifts out of sync with reality and then fails silently.

#### 1.3.4 The authorship closure — the computation, stated precisely

For a proposal `P`, the broker computes at decision time and stamps into `P`'s
record:

```
closure(P) = authors(skill_version(P))
           ∪ authors(prompt_version(P))
           ∪ authors(model_pin(P))
           ∪ authors(declared_population(skill(P)))
           ∪ ⋃ { certifying_owner(d) : d ∈ datasets_actually_read(P) }
           ∪ ⋃ { author(r)           : r ∈ rules_evaluated(P) }
           ∪ authors(any_override_applied(P))
```

Two design calls inside that expression, both of which matter:

- **`rules_evaluated(P)`, not "every rule in the bundle."** Taking the whole
  bundle would disqualify every policy owner from approving anything, which is
  an unworkable control that would be waived within one close — and a waived
  control is worse than a narrow one. The policy-decision log already records
  which rules participated in a decision (obligation N's decision ID, the
  OPA-style decision-log shape `INDUSTRY_KB` §13.1(2) points at), so this set is
  a read, not a new computation. It is also exactly the auditor's question:
  *who set the thing that let this through?*
- **`datasets_actually_read(P)`, not "datasets offered."** Under-selection is
  the failure that bites (`INDUSTRY_KB` §14.3); the population actually read is
  already recorded for coverage. Reusing it here means the SoD closure and the
  coverage statement cannot disagree.

**The constraint, evaluated by the broker as the Identity/SoD guardrail class
(`INDUSTRY_KB` §13.3):**

```
APPROVE(P) by principal a  requires:
    type(a) == human
    a ∉ closure(P)                          -- author ≠ approver
    a ≠ invoker(P)                          -- invoker ≠ approver
    a has the approve capability for P's risk band
    a's authentication assertion is < 5 minutes old
    a ∉ period_authors(P)                   -- see 1.3.5
```

and for an override (`AC-F36-07`):

```
OVERRIDE(P) requires two distinct principals k1, k2:
    type(k1) == type(k2) == human
    k1 ≠ k2
    k2 ∉ closure(P) ∪ {invoker(P), k1}
    reason code ∈ closed list
    scope == exactly one action, with an expiry
```

A denial under any of these produces an ordinary broker denial record with a
decision ID and a bundle hash, identical in kind to any other denial
(`AC-F36-01`, `AC-F36-03`), naming **which clause failed and which artefact put
the principal in the closure**. "You may not approve this" without saying why is
an instruction to find a workaround.

#### 1.3.5 The period leg, and why version-participation alone is not enough

Version-participation catches the direct case: you authored the exact threshold
that decided this proposal, so you cannot approve it. It does not catch the
sequenced case: *A* authors threshold v1, a run produces proposals under v1,
*A* then edits it to v2, and approves the v1 proposals — or *B* authors v1, *A*
authors v2 mid-period, and *A* approves the v1 output, having demonstrably
established control over that skill's behaviour within the same close.

So the constraint has a second, period-scoped leg, following `DOMAIN_KB` §7.1's
own formulation (*"anyone who has edited an agent's definition in the current
period"*):

```
period_authors(P) = { principals who authored any version of any artefact in
                      closure(P)'s artefact set, with an effective date
                      overlapping P's accounting period }
```

Both legs apply. Version-participation is permanent for that proposal; the
period leg expires with the period. I record the trade-off: the period leg is
the one that will generate the complaints, and it is the one that catches the
attack.

#### 1.3.6 The deadlock problem — the part most SoD designs get wrong

A hard constraint in a small finance team can lock the close: on day 3, nobody
is eligible. This is the failure mode `INDUSTRY_KB` §13.2(5) warns about — a
control with no sanctioned relief acquires an unsanctioned one, and the
unsanctioned one here is a manual journal keyed straight into Oracle outside
this system, which is worse in every respect including evidentially.

My call, in three parts:

1. **The Identity/SoD guardrail class is NOT override-eligible.** Obligation O's
   override path exists for quantitative, temporal, scope and capability
   classes. It does not extend to SoD, at any permission level. An override that
   can clear an SoD block is not a control; it is a second door. The gate-5
   routing-budget override is likewise not such a door.
2. **Eligibility is computed and shown *before* review, not at submit.** Every
   item in a review queue carries the set of currently-eligible approvers,
   computed when the proposal is created. A reviewer must never invest attention
   in an item they are structurally barred from approving and discover it at
   11pm on submit — that is how a control becomes a thing people route around.
   This is a **constraint on `solution-architect`'s queue design** (§10.1) and
   on F41's surface, not a new feature.
3. **The only relief is adding an eligible human, never removing the
   constraint.** If no eligible approver exists, the item is marked
   **SoD-blocked** and the sanctioned disposition is R5 — handoff, with a named
   owner and a due date (`PLAN` §7.2 F35), out to the customer's own manual
   process under Oracle's own controls. That outcome is honest, it is recorded,
   and it is *countable*: **SoD-blocked count per agent, per skill and per period
   is a monitored metric.** A rising count is read as authorship concentration
   — one person owns too many artefacts — which is a genuine control finding
   about the customer's organisation, surfaced by us rather than discovered by
   their auditor.

#### 1.3.7 What the SoD engine does not and cannot cover — stated, not hidden

- **It cannot see the human who loads the Journal Import file into Oracle.** In
  MVP1 that person is outside our boundary entirely. Requiring that they are not
  the in-product approver is CUEC **C8** (§3.2) — published as a named customer
  obligation, not assumed.
- **It cannot detect collusion.** Two people can defeat any two-key control.
  This is the residual every SoD design carries and I state it rather than imply
  otherwise. The compensating instruments are cross-period surveillance (F9) and
  the blast-radius caps (obligation P), which constrain the *aggregate* effect
  regardless of who authorised it — which is why §5 records obligation P as a
  security control and not only a domain one.
- **It cannot make a diligent approval out of an eligible one.** Eligibility is
  necessary, not sufficient. The instruments for the sufficiency question are
  dwell, override rate and probes (§6 T6).

### 1.4 What is deliberately not built in MVP1 — right-sizing, stated with the trade-off

Each of these is a decision, with what I traded away:

- **No local password store, no self-service registration, no password reset
  flow.** Traded: the product cannot be demoed to a customer who has no IdP, and
  a standalone sales demo needs a separate seeded environment. Accepted — the
  buyer runs Oracle ERP Cloud and therefore runs an IdP.
- **No fine-grained per-record ACLs on dossiers.** Any role with dossier read
  can read all dossiers in its tenant. Traded: a large customer wanting entity-
  level read segregation is not served. Accepted for MVP1 (single legal entity
  per `PLAN` §9.2 A3), and named as a revisit trigger.
- **No customer-managed encryption keys (BYOK/HYOK).** Traded: a customer with a
  key-custody policy will ask. Accepted for a pilot; §4.5 records that the key
  hierarchy is designed so BYOK is a substitution, not a re-architecture.
- **No SCIM provisioning.** Role assignment is by IdP group claim at login.
  Traded: role changes take effect at next login rather than immediately.
  Accepted — but *revocation* does not have this property, because session
  invalidation follows the IdP.
- **No dedicated SIEM integration.** Control events are emitted in a structured
  form ready to ship; the shipping is deployment configuration.
- **A19–A22 refusals are not permission-gated at all.** This is a *removal* of
  flexibility, deliberately: no role, no flag, no admin setting unlocks a
  refusal. Traded: a customer who wants one cannot have it without a code
  change and a new gate. That is the intended cost — per the Decisions Log,
  "not built yet" and "will never be built" are opposite answers to an auditor,
  and a refusal behind an admin toggle is the former pretending to be the
  latter.

### 1.5 Explicit revisit triggers

Any one of these re-opens §1 before the change ships. They are stated as
observable events, not as intentions.

| # | Trigger | What must be re-designed |
|---|---|---|
| 1 | **Before F16 (skill authoring) ships** | The closure's artefact set gains user-authored skill versions. Mechanism exists; the *policy* question — can a staff accountant author a Tier 1 skill at all, and who publishes it — is not answered here |
| 2 | **Before F17 / any direct posting into Oracle** | Per-agent Oracle identities, credential custody at the broker, and CUEC C1–C7 move from export-time to post-time. §2.5 |
| 3 | **Before F23/F24 (any mobile surface)** | `PLAN` §7.5 recommends rejecting mobile approval on control grounds; if overruled, step-up auth, device binding and session lifetime on a low-scrutiny surface all need re-deciding |
| 4 | **Before any second tenant shares infrastructure** | Tenant isolation moves from deployment-level to enforced-in-code; §11 SA1's assumption is retired |
| 5 | **On confirmation that the warehouse contains personal data** | The §6 T7 default-deny becomes insufficient on its own; GDPR lawful basis, cross-border transfer to the model provider, DPIA and the erasure-vs-retention conflict (§4.6) all open |
| 6 | **Before any external API or integration is exposed** | Machine-to-machine authn, per-client authz and rate limiting are not designed here because no such surface exists in MVP1 |
| 7 | **On the first customer with multiple legal entities or ledgers** | Entity-level authz segregation (§1.4) becomes required, and the closure gains an entity dimension |
| 8 | **If the filer status resolves to public accelerated** (`PLAN` §9.1) | Nothing in §1 changes — I designed to the harder floor — but §404(b) attestation means an external auditor will test these controls directly, which raises the evidence bar on §9's suite, not the design bar |
| 9 | **Before the first production close** | CUEC verification (§3) must have run and passed for the tenant. Not a design trigger; a go-live gate |

---

## 2 · Credential architecture and the posting boundary

Obligations D, E, M, S. The governing sentence, from `INDUSTRY_KB` §13.1(2):
**if the model can call Oracle directly, every guardrail is advisory regardless
of how it is written.**

### 2.1 MVP1 holds no Oracle write credential at all

`AC-F40-02` requires that no posting credential is resolvable anywhere in the
build. I am strengthening how that is achieved, because "the code does not call
the posting endpoint" is a weaker claim than it sounds:

- **The Oracle write credential does not exist in any MVP1 environment** — not
  in the secret store, not in a disabled state, not with an empty value, not in
  a commented-out configuration key. The name of the secret is not present. A
  credential that exists but is unused is one refactor away from being used, and
  it is indistinguishable from one that is used, to anyone reading the config.
- **No client library capable of submitting a journal is a build dependency.**
  The export path (`export/journal_import.py`) writes a file; it constructs no
  HTTP request to a posting endpoint.
- **The absence is asserted twice** — statically (secret name and dependency
  scan) and at runtime (an attempt to resolve a posting credential from any
  module returns nothing and emits a control event, `AC-F36-04`). §9 owns both.

This is the cleanest form of obligation E that will ever exist on this project,
and it is temporary. §2.5 states what changes when F17 arrives, so the promotion
is a designed step rather than a discovery.

### 2.2 Per-agent principals — no shared integration account, ever

`INDUSTRY_KB` §15.2 trap 3: a shared integration account makes every entry from
this system look like one service user, destroying obligation D's per-agent
attribution and leaving Oracle's own approver unable to tell which agent, which
run, or which human authorised anything. `INDUSTRY_KB` §4.2 problem 3 states the
deeper version: a human SoD violation leaves two names in the log; an agent SoD
collapse leaves one.

Design:

- **One principal per agent** (`AC-F5-01`), with its own entitlement set and its
  own log stream, auto-inventoried (`AC-F5-02`).
- **Agents authenticate to the broker with workload identity**, issued per run,
  audience-scoped to the broker, bound to the run ID, and short-lived. An agent
  never holds a long-lived secret and never holds a downstream credential.
- **The broker maps `(agent principal, skill version, action)` to a downstream
  credential.** The mapping is data in the guardrail bundle, so it is versioned,
  hash-addressed and diffable like any other policy. An agent cannot request a
  credential; it requests an *action*, and the broker decides whether that
  action exists for that principal and then uses the credential itself.
- **The broker rejects any action from a principal that is not a registered
  agent version.** This closes the "run it under a generic account to break
  attribution" insider path (§6 T5), and it composes with `AC-F2-04` (a run
  whose artefact versions are unregistered does not start).

**Composed teams.** `INDUSTRY_KB` §4.2 requires the SoD analysis to be performed
on the *composed team*, not on each agent in isolation. MVP1 ships no team
composition, but the closure in §1.3.4 is defined over the artefacts a proposal
actually used, which composes correctly by construction: a proposal produced by
two agents carries both skill versions and therefore both author sets. Recorded
so it is not re-derived when teams arrive.

### 2.3 The broker is the only enforcement point, and the only credential holder

Obligation M. Three properties, all of which are security properties and not
architectural preferences:

1. **The UI is never an enforcement point.** `AC-F36-03` already asserts that a
   direct API call bypassing the front end is denied identically. The security
   restatement: the front end must contain no authorization logic whose removal
   would change what is permitted. Any rule that exists *only* in the client is
   a defect, and §9 tests for it by calling the API directly with each role.
2. **There is exactly one broker.** Not one per surface, not one per skill. Two
   enforcement points drift; the second one is always the weaker one, and with
   three surfaces on the roadmap (`INTAKE.md` A5.1) a per-surface broker
   guarantees a future MVP-quality mobile path around a hardened web path.
3. **The broker fails closed** (`AC-F36-17`). If the bundle is unresolvable or
   its hash does not verify, every action is denied. I extend this to credential
   resolution: if the broker cannot verify *which* principal is asking, it does
   not act, and does not fall back to a default identity.

### 2.4 Warehouse read access — least privilege enforced below the application

Obligation Q says action-capable and assurance-emitting skills read only
certified datasets on the skill's allowlist. `PLAN` §6.2 enforces this in
`semantic/` and `catalogue/`. **My requirement adds a second, independent layer,
and this is a constraint on `solution-architect` (§10.1):**

- Each skill executes warehouse queries under a **database role granted only the
  certified dataset objects on that skill's allowlist**. A Scope-guardrail
  defect, or a resolver bug, then still cannot read an uncertified or
  out-of-scope dataset, because the grant does not exist.
- Grants are expressed against **certified dataset objects**, never against raw
  source tables or source-system names. That keeps the phase-2 seam open
  (`PLAN` §8): adding a non-Oracle source must not mean re-granting every skill.
- **Read-only.** No skill's warehouse role holds INSERT, UPDATE, DELETE or DDL
  on any object. The system is a reader of the warehouse and a writer of its own
  evidence store, and those are different credentials with no overlap.
- **No free-form SQL path exists** (`AC-F39-02`, `PLAN` §11 criterion 19). The
  resolver returns a certified-query identifier plus bound parameters. Restated
  as a security control: model output never reaches a SQL parser, so SQL
  injection via prompt injection is not mitigated — it is *absent*. §7 carries
  the boundary detail.

### 2.5 The posting boundary when F17 arrives — designed now, built later

Recorded so the promotion gate (`PLAN` §7.3: ≥95% precision over one closed
period, per-batch line cap, batch-level approval) is a step and not a rewrite:

- **Per-agent Oracle identities**, not one integration user (obligation S).
- **The credential lives only in the broker**, retrieved per action from the
  secret store, never cached in an agent context, never passed as a tool
  argument, never present in a model context.
- **The dedicated journal source and category** (obligation S) is already in
  MVP1's export header (`AC-F40-04`); at posting it becomes the enforced target
  and the broker refuses any submission naming another source or category.
- **The poster's only trigger is a verified in-product approval record**
  (`INDUSTRY_KB` §4.2 obligation E): the broker validates the approval record's
  signature and its SoD clauses *again* at post time, rather than trusting that
  the approval endpoint checked them. Re-validation at the credentialled step is
  the difference between a control and a sequence of hopeful calls.
- **Batch-level approval with a per-batch line cap** — because the domain
  failure is wholesale (`DOMAIN_KB` §6.4: an agent with a wrong mapping errs 400
  times in ninety seconds), and 400 individual approvals is not a control.

### 2.6 Secrets handling — concrete, and checkable against repo state

**Verified this pass**: the root repository's `.gitignore` excludes
`projects/*/dev/` and `projects/*/prod/`, so nothing inside the project's build
tree is tracked by the platform repo. **The project's `dev/` repository does not
exist yet** — `code-agent` has not run — so there is no project `.gitignore` to
inspect. That is a statement of fact, not a pass.

**Binding on `code-agent`, before the dev repo's first commit:**

- `dev/.gitignore` contains at minimum: `.env`, `.env.*`, `!.env.example`,
  `*.pem`, `*.key`, `*.p12`, `*.pfx`, `credentials.json`, `service-account*.json`,
  `.venv/`, `__pycache__/`, `node_modules/`, `.next/`.
- `.env.example` **is** committed, with every key present and every value a
  visible placeholder. A missing key in the example file is how a real key ends
  up pasted into a tracked config.
- **No secret is ever read from a `NEXT_PUBLIC_*` variable, and no such variable
  ever holds one.** Next.js inlines those into the client bundle; a key placed
  there is published, not configured. This is the single most common way a
  credential leaves a project of this shape and it is worth naming explicitly.
- The model-provider API key is held by the model gateway (a `service`
  principal), not by agent code and not by the frontend.
- Secrets are resolved at process start or per action from the environment or a
  secret manager; they are never written to disk by the application, never
  logged, and never included in a dossier, a rendered view or an export. Log and
  dossier writers apply a redaction pass keyed on the known secret names.
- **Rotation** is possible without a code change and without invalidating
  historical evidence — see §4.5 for why that is non-trivial for signing keys.

§9 owns the secrets-leak check, including a git-history scan of the dev repo
once it exists. Per my contract I will report a discovered leak; I will not
rewrite history to scrub it.

---

## 3 · Obligation S — complementary user entity controls, and the AutoPost trap

This is the sharpest single finding carried into this gate, and it is worth
restating in one sentence before designing against it:

> Oracle's AutoPost proceeds through approval **"if journal approval is being
> used"** — conditional. In a tenant where journal approval is not enabled for
> our source and category, our exports post with no human leg in Oracle at all,
> **and we would not know.**
> (`INDUSTRY_KB` §15.2 trap 2, citing Oracle's own posting documentation.)

A control narrative that says "the human approves in Oracle" is, in some
tenants, describing a control that is switched off. CUECs relied on but never
checked are findings waiting for the first audit. So they are checked.

### 3.1 The CUEC register — a governed object, not a document

A **CUEC register** exists per tenant, as data, in the evidence store. Each
entry carries: `id`, `statement` (the customer obligation in the customer's
language), `why_it_matters` (which of our control claims collapses without it),
`verification_method`, `evidence_artefact`, `verifier` (a named human on the
customer side for attestations; a `service` principal for probes),
`verified_at`, `result`, `expires_at`, and `last_drift_check`.

It is published to the customer as a named list of *their* obligations — the
`INDUSTRY_KB` §12.1(4) requirement — and it is simultaneously the machine-
readable object `AC-F40-05` gates the export on.

### 3.2 The MVP1 CUEC set

MVP1 exports rather than posts, which changes *when* each obligation bites but
removes none of them — and it adds one (C8) that would not exist if we posted
directly.

| ID | Customer obligation | Without it | Method |
|---|---|---|---|
| **C1** | A journal **source** is created and reserved exclusively for this system | Our entries are not enumerable in Oracle; the blast-radius answer exists only in our own store, which is the answer an auditor trusts least | Probe |
| **C2** | A journal **category** is likewise reserved | As C1, at finer grain | Probe |
| **C3** | **Journal approval is enabled and required** for that source/category combination | The system-of-record leg of the two-key model does not exist. This is the trap | Probe |
| **C4** | **No AutoPost criteria set can select our source without approval** — checked against *every* criteria set that could match, not only the obvious one | Our exports post unapproved and silently. Note that Oracle *recommends* scheduling AutoPost immediately after Journal Import, so the dangerous configuration is the one a diligent Oracle admin is advised to build | Probe, per criteria set |
| **C5** | No other scheduled or automated process posts our source | C4's answer is defeated by a second path | Probe + attestation |
| **C6** | Warehouse **ETL completeness** control exists, with a named owner and a schedule | Obligation C's IPE support has no upstream. Every "no exceptions" we emit rests on a population we cannot vouch for | Attestation + F26 tie-out |
| **C7** | **Source extract integrity** — extracts are complete and unaltered between ERP and warehouse | As C6, at the transport | Attestation + F26 tie-out |
| **C8** | **The human who loads the Journal Import file into Oracle is not the in-product approver of the proposals in it** | The two-key model collapses to one key by a route entirely outside our software. **This CUEC exists only because MVP1 exports rather than posts** — it is the SoD leg §1.3.7 states we cannot enforce | Attestation, per named loader |
| **C9** | De-provisioning: IdP access removal is timely, and the roles in §1.3.2 are mapped to groups the customer actually governs | Our entire authz model rests on claims the customer controls | Attestation |

C8 is the one I most want on the record. It is a direct consequence of the
MVP1-exports decision, it did not exist in the posting design, and it is
exactly the kind of obligation that gets discovered by an auditor rather than
declared by a vendor.

### 3.3 Verification method — probes, not questionnaires

"Verified" must mean *we read the tenant's actual configuration*, not *the
customer said yes*. C1–C5 are all readable configuration.

- **Probe.** A `service` principal with a **read-only** Oracle role reads the
  journal source and category definitions, the approval configuration for that
  source/category, and every AutoPost criteria set that could match it. The
  probe credential is read-only and is a different credential from anything in
  §2.5 — a prober that could change configuration would be a control that can
  falsify its own evidence.
- **The raw probe response is retained as the evidence artefact** in the
  evidence store, under the same retention clock as everything else (§4). A
  verification result without the underlying response is an assertion, not
  evidence, and it is the auditor's second question.
- **Attestation, where no read exists** (C6–C9): a signed statement by a named
  customer control owner, dated, with a supporting artefact (a screenshot, a
  control description, a job schedule), and an expiry. Where an item is
  attested rather than probed, that fact is carried into the dossier and the
  export (§3.5) — because the strength of our claim differs, and pretending
  otherwise is the failure this whole section exists to prevent.

### 3.4 When verification runs — the part that makes it a control

Verification "at deployment" is not enough: a tenant's configuration changes
after deployment, we do not see the change, and a stale pass is
indistinguishable from a current one.

1. **At deployment**, before the first export. Blocking.
2. **At export time**, every time. C1–C5 are cheap probes; running them at the
   moment of export makes "verified" mean "verified now" rather than "verified
   in March". This is the change that turns the register from documentation into
   enforcement, and it is a **constraint on `solution-architect`'s deployment
   and export design** (§10.1), not a new feature.
3. **On a schedule, each close**, including for attested items, so C6–C9 do not
   silently age.
4. **Attested items expire.** 90 days or one close, whichever is sooner. An
   expired attestation is a *fail*, not a warning.

**Drift detection.** Each probe result is compared with the last recorded
result. Any difference is a **drift event**: a first-class control event in the
evidence store, which blocks export until re-verified and re-attested where
relevant. Drift is the only mechanism by which we can learn that a customer
turned journal approval off, and it must be loud. Drift on C3 or C4
specifically is the highest-severity control event this system can emit,
because it means our control narrative became false without anyone acting.

### 3.5 Fail-closed, and what the user and the auditor see

- `AC-F40-05` already refuses the export when a tenant's CUEC checklist is
  unverified or failed. **I extend it: stale counts as failed**, and the refusal
  names which items and why (unverified / failed / expired / drifted).
- The export screen states the CUEC position in words with dates and names —
  *"C3 journal approval required: verified by probe 2026-07-31 09:12; C8 loader
  separation: attested by [name] 2026-06-30, expires 2026-09-28"* — and
  **never as a green tick.** Per the gate-5 decision there is no green in this
  product, and "verified" is precisely the affect that would invite a depleted
  reviewer to move on. Consistent with `UX_KB` §5.5, which already renders the
  CUEC verification date on that screen.
- `AC-F40-06` requires the dossier and the export to state that the Oracle-side
  configuration is a customer-controlled prerequisite verified per tenant on a
  stated date. I add one field: **the verification *method*** — probed or
  attested. An auditor who cannot tell which is which cannot weigh the evidence,
  and they will ask.
- **The honest residual, recorded rather than buried:** for attested items our
  assurance is exactly as good as the attestation. That is a residual risk owned
  by the named customer control owner, stated in the register and carried into
  the export. It is not a gap in our design; it is the correct allocation of a
  control we do not own — but it is only correct if it is *stated*.

---

## 4 · Retention, immutability and tamper-evidence

Obligations G, H, I. 17 CFR 210.2-06 / SOX §802: seven years, attaching to the
**decision dossier**, not to a copy of the ledger (`INDUSTRY_KB` §12.1(1)).
Oracle keeps the book of record. We keep the only artefact that explains *why*
Oracle contains what it contains — which makes our store both smaller and more
attractive to an attacker than the ledger itself (§6 T4).

### 4.1 The retention clock

- **Seven years, anchored to the end of the accounting period the dossier
  relates to**, not to the date the row was written and not to the date the
  project ships. A journal exported in this system's first month must still be
  reconstructible in 2033.
- **Configurable upward per tenant, never downward.** A configuration change
  that would shorten retention below the floor is rejected outright, at every
  permission level, and the attempt is a control event. Tax and statutory
  regimes push this longer in some jurisdictions; nothing legitimate pushes it
  shorter, so the control is asymmetric by design.
- **Retention is set per object at write time**, so it survives any later
  change to bucket-level or policy-level configuration. A retention policy
  applied at the container level is a policy an administrator can edit; a
  retention period stamped on the object is not.
- **Legal hold** suspends expiry indefinitely and independently of the retention
  period, settable and clearable only by a principal distinct from the
  application (§4.4).
- **Expiry is the only deletion path that exists.** There is no API, no admin
  screen and no support procedure that deletes a dossier.

### 4.2 WORM — the specific property that matters

`INDUSTRY_KB` §4.3 asks for non-rewritable, non-erasable storage. The
implementation detail that decides whether that is real:

**Object-lock in compliance mode, not governance mode.** Governance mode is
bypassable by a sufficiently privileged principal, and a sufficiently
privileged principal is exactly the threat we are defending against here (§6
T4, T6). Compliance mode cannot be shortened or removed by *anyone*, including
the account root, for the duration of the retention period. This is the whole
point: the control must hold against the person who administers it.

**The cost, accepted and stated:** garbage written under a compliance lock
cannot be deleted for seven years, which is both a storage-cost exposure and an
availability attack (§6 T4). Mitigations are write-rate limits on the evidence
writer and a per-period expected-volume alarm — cheap, and they belong in the
design now because the failure is unrecoverable by construction.

`AC-F1-02` requires that an attempted update or delete fails, leaves the dossier
unchanged, *and is itself recorded*. Recording the attempt is an application-
layer control and is necessary but not sufficient: an attacker operating at the
storage layer never touches the application. §4.4 closes that.

### 4.3 Tamper-evidence — hashing alone is not enough

`AC-F1-03` requires that a dossier altered outside the application is detected.
A per-dossier content hash stored beside the dossier detects accidental
corruption and a careless attacker. It does not detect an attacker who alters
the dossier *and* recomputes the hash, which is the attacker we care about,
because the motive for touching the evidence store at all is to make a decision
look different than it was.

Three layers, each of which the layer above it does not subsume:

1. **Per-dossier content hash**, computed at write, covering the full dossier
   including the rendered view and the version tuple.
2. **A hash chain per tenant per period**, so a dossier cannot be removed or
   reordered without breaking the chain — a single dossier's hash says nothing
   about whether a *different* dossier was deleted, and deletion of an
   inconvenient record is the more likely attack than alteration of one.
3. **A periodic anchor in a separate trust domain.** The period's chain head is
   signed by a key held in a KMS/HSM with sign-only, non-exportable material,
   under a principal **the application cannot assume**, and the signed root is
   written to an append-only log in a different account and credential domain.
   An attacker who owns the application and the evidence store still cannot
   produce a consistent history, because they cannot re-sign the anchors.

That third layer is what makes the property *tamper-evident* rather than
*tamper-inconvenient*, and it is the one that is normally omitted. I am
specifying it as a requirement; the mechanism selection (which KMS, which log)
is `solution-architect`'s (§10.1).

**Obligation H** — a reversal is a new record, never a mutation — falls out of
this for free: an append-only store with no update path cannot express a
mutation. `AC-F40-10`'s bidirectional linkage is a new record pointing at an
old one, both immutable.

### 4.4 Separation of duties on the store itself

The evidence store needs its own SoD, because §1's SoD is enforced by the
application and the application is a principal here too.

| Principal | May | May not |
|---|---|---|
| Application evidence writer | Put objects, with retention stamped at write | Delete; shorten retention; alter lifecycle or lock configuration; read the signing key |
| Retention administrator | Set legal holds, manage lifecycle configuration | Write dossiers; read dossier contents |
| Anchor signer | Sign a chain head | Read or write dossiers |
| Auditor export builder | Read dossiers, produce bundles | Write or delete anything |

**No principal holds two of these.** In particular the application cannot delete
and cannot re-sign, which is what makes §4.3 layer 3 meaningful.

**Storage-layer audit trail.** Every API call against the store — including
denied ones, including `DeleteObject`, `PutObjectRetention` and lifecycle
changes — is logged to the same separate trust domain as the anchors, not to
the application's own logs. An attacker who compromises the application must
not be able to edit the record of what they did to the evidence. Alerts fire on
any deletion attempt, any retention-shortening attempt, and any lock-
configuration change, because in a correctly-operating system the expected rate
of all three is zero.

### 4.5 Keys, and why rotation is a design problem here

Keys rotate; dossiers live seven years. If rotation invalidates verification,
the tamper-evidence claim silently expires and nobody notices until an auditor
asks in year four.

- **Hash chaining is key-independent.** Deliberate: the integrity backbone
  survives any key event.
- **Anchor signatures carry a key ID.** Old public keys are retained
  indefinitely — well beyond the retention period — and are included in the
  auditor export bundle (§4.7) so verification is possible offline and forever.
- **Encryption at rest** uses a per-tenant key. Rotation re-wraps data keys;
  it does not re-encrypt or rewrite objects, which it could not do anyway under
  a compliance lock. This is why the key hierarchy must be envelope-based from
  day one, and it is why **BYOK later is a substitution rather than a
  re-architecture** (§1.4).
- Rotation schedule and compromise-response are deployment runbook items owned
  by `deploy-agent`, and the runbook must state what is re-verified after a
  compromise-driven rotation.

### 4.6 The retention-vs-erasure conflict, flagged not resolved

If the warehouse contains personal data (§1.2 criterion 5), a GDPR erasure
request collides head-on with a seven-year compliance lock on a store designed
to make deletion impossible. The usual resolution is that a legal-obligation
basis for retention overrides erasure for the retained record, but that is a
*legal* determination and I am not making it.

**My MVP1 design avoids the collision rather than resolving it**: personal-data-
flagged datasets are denied to model-bound and action-capable paths (§6 T7), so
person-level attributes do not enter dossiers in the first place. That is a
containment, not an answer, and it is revisit trigger #5.

### 4.7 The auditor export — evidence without a login

`AC-F1-04`: parseable by a party with no application login and no access to the
running system. *"Auditors will want an extract, not a login"*
(`INDUSTRY_KB` §4.3, obligation G). The bundle contains:

- one structured record per dossier, with every field `AC-F1-01` requires,
  fully denormalised — **no field renders only as an in-application reference**,
  which means no internal IDs standing in for content and no URLs back to us;
- the **rendered views** as self-contained static files (§7.5 — scriptless and
  sanitised, because we are handing an auditor a file containing text an
  attacker may have controlled);
- a manifest of per-dossier hashes, the period's chain, the signed anchors, and
  the public keys needed to verify them;
- a small, dependency-free **verification script** and a plain-language
  statement of what verification does and does not prove;
- an explicit statement where a period contains zero dossiers (`AC-F1-06`) —
  silence is never a pass (`FUNCTIONAL_SPEC` §2 C2);
- the CUEC register position for the period, with method and dates (§3.5).

Export is itself a security-relevant action; §6 T3 covers it as an exfiltration
channel and §9 tests its authorization.

---

## 5 · Obligations A–S — which bind MVP1, and how each is discharged

`industry-expert` found A, C, D, G, I, J binding at **Tier 1**, because an
agent-prepared, human-certified output is an **IT-dependent manual control**,
which drags IPE completeness/accuracy testing along with it. `PLAN` §3.1 extends
the Tier 1 set to A, C, D, G, I, J, L, M, N, O, P, Q, R. I agree with both and
have checked each obligation individually rather than accepting the table.

**Disposition key**: **DESIGN** — discharged by a designed mechanism, component
named. **PROCESS** — discharged by a process, owner named. **DEFER** — not
discharged in MVP1, owner and trigger named.

| Obl. | Binds MVP1? | Disposition | How, concretely |
|---|---|---|---|
| **A** — approval record incl. the rendered view | **Yes, Tier 1** | **DESIGN** | F1 + F41. Security additions: approver identity is a `human`-typed federated principal, the record carries the IdP authentication-strength claim, and step-up re-auth <5 min old is a precondition (§1.1). The rendered view is stored scriptless (§7.5) so the evidence artefact is itself safe to replay |
| **B** — thresholds explicit, versioned, shown at approval | **Yes, Tier 1** | **DESIGN** | F36 Quantitative class. Security addition: threshold values exist **only** inside the hash-addressed bundle — never as a mutable database row an admin can UPDATE — because threshold widening is the highest-leverage single-field attack in the system (§6 T1) |
| **C** — completeness/accuracy of inputs evidenced (IPE) | **Yes, Tier 1** | **DESIGN + PROCESS** | F26 + F38 discharge the mechanism. The upstream half is not ours: ETL completeness and extract integrity are CUEC **C6/C7**, owned by a named customer control owner and verified per §3.4. IPE with an unverified upstream is IPE in name |
| **D** — per-agent identity, least privilege, own log stream | **Yes, Tier 1** | **DESIGN** | F5 + §2.2. No shared account exists; the broker rejects unregistered principals; workload identity is per run and audience-scoped |
| **E** — preparer/poster split; the model never holds the Oracle credential | **Yes** | **DESIGN** | Discharged in MVP1 in its strongest possible form: **the posting credential does not exist** (§2.1), and the poster is a human outside our boundary. §2.5 states what must be built before F17 so this is a step, not a cliff |
| **F** — approver ≠ requester ≠ agent author ≠ invoker | **Yes, and it is the hard one** | **DESIGN, with one leg as PROCESS** | §1.3's authorship closure, broker-enforced, non-overridable, with a period leg and a stated deadlock path. The leg we cannot enforce — the human who loads the file into Oracle — is CUEC **C8** (§3.2), published as a named customer obligation |
| **G** — append-only, tamper-evident, ≥7 yr, auditor-consumable export | **Yes, Tier 1** | **DESIGN** | §4 in full: compliance-mode object lock, three-layer tamper-evidence with an anchor in a separate trust domain, store-level SoD, offline-verifiable export bundle |
| **H** — a reversal is a new record | **Partly; mostly Oracle's** | **DESIGN** | Falls out of §4's no-update store; we retain bidirectional linkage (`AC-F40-10`). Ledger-side reversal mechanics are Oracle's and we do not rebuild them |
| **I** — immutable version tuple per proposal | **Yes, Tier 1** | **DESIGN** | F2. Security relevance: the tuple is the closure's input set (§1.3.4), so an incomplete stamp is an **SoD failure**, not only a reproducibility failure. That link is not obvious and is why F2 is a security dependency of F36 |
| **J** — model/prompt/**policy** change is ICFR change control | **Yes, Tier 1** | **DESIGN + PROCESS** | F2's changelog + the bundle diff. Security addition: bundle publication is **dual-authorised**, and a *risk-increasing* diff (threshold widened, cap raised, rule removed, allowlist extended) is classified as such and requires controller approval (§6 T1). The classification is mechanical, not a judgement call |
| **K** — model deprecation tracked with a migration control | **Yes, Tier 1 start** | **PROCESS** | Owner: `solution-architect` (`PLAN` §10). Security-relevant leg, and mine: **models are pinned to dated versions, never to a moving alias.** A provider silently changing the model behind a stable alias is an unauthorised change to an ICFR-relevant control, and an alias makes it undetectable |
| **L** — guardrail as declarative policy object, deny-by-default allowlist | **Yes, Tier 1** | **DESIGN** | F36. Security reading: deny-by-default is what makes the authz surface *enumerable*. "Here are the seven actions this agent may take" is testable; a prohibition list can never be evidenced as complete |
| **M** — enforcement at a single broker holding the credentials; UI never enforces | **Yes, Tier 1** | **DESIGN** | §2.3. One broker, fails closed, no client-side authorization logic, asserted by direct-API tests per role (§9) |
| **N** — bundle hash + decision ID per action; negative-control suite; shadow mode | **Yes, Tier 1** | **DESIGN** | F36. Security addition (§6 T1): a fixture that **used to fire and no longer does** is reported as a *regression*, not a pass. Without that, the negative-control suite is the natural detector for threshold widening and does not detect it |
| **O** — overrides dual-authorised, reason-coded, time-boxed, counted | **Yes, Tier 1** | **DESIGN** | F36 + §1.3.4's override clause. Security addition: **the Identity/SoD class is not override-eligible** (§1.3.6). An override that clears an SoD block is a second door |
| **P** — blast-radius caps, stateful, non-disableable | **Yes, Tier 1** | **DESIGN** | F36. I record this as a **security** control, not only a domain one: it is the only mechanism that constrains aggregate effect regardless of who authorised it, which makes it the sole residual defence against collusion (§1.3.7) and against a compromised agent (§6). Extended in §6 T1: caps cannot be *widened* past a deployment-time ceiling set by a principal distinct from the tenant admin |
| **Q** — certified datasets, skill allowlists | **Yes, Tier 1** | **DESIGN** | F38/F39, plus §2.4's database-grant backstop so a resolver defect cannot reach an uncertified dataset. Extended in §6 T7: certification carries a **personal-data classification**, and flagged datasets are denied to model-bound and action-capable paths in MVP1 |
| **R** — declared population, computed coverage, no negative assurance below full coverage | **Yes, Tier 1** | **DESIGN** | F38/F42. Security relevance and the reason I did not treat it as someone else's: an injected instruction that *suppresses* a finding produces a false clean result, so **the "no exceptions" conclusion must be emitted by the coverage machinery and never by the model** (§6 T2, §10.1) |
| **S** — dedicated Oracle source/category, approval required, per-agent Oracle identity, CUECs verified per tenant | **Partly — Tier 2** | **DESIGN (now) + DEFER (posting legs)** | Binding **now**: the dedicated source/category in the export header (`AC-F40-04`) and the per-tenant CUEC verification (§3), which is fail-closed at export. Deferred to F17 with owner `security-architect` + `solution-architect`: per-agent Oracle identities and broker credential custody (§2.5). Trigger: the `PLAN` §7.3 promotion gate |

**Two things I want visible rather than buried in the table:**

1. **Nothing is discharged by "we do not own the GL."** `INDUSTRY_KB` §12.1 is
   right that the net effect is neutral at best and slightly worse on the
   evidence side. Not owning the ledger removed execution, balancing and ledger
   retention from our build; it *added* a cross-system reliance (the CUECs) and
   a warehouse-to-ERP reconciliation obligation. My design carries both.
2. **Obligation I is a security dependency, not just an audit one.** The version
   tuple is the input to the SoD closure. If F2's stamp is incomplete for any
   artefact class, §1.3's constraint silently under-computes and approvals that
   should be blocked are permitted. **F2 must therefore ship before, or with,
   F36's Identity/SoD class — not after it.** That sequencing constraint is
   mine and it is not currently recorded anywhere else.

---

## 6 · The threat model

Nobody has written one for this system. This is it. It is written from the
attacker's side — *what would I do with this system* — rather than as a control
checklist, because a checklist derived from the controls we already planned
cannot find the gaps in them.

**Adversaries considered**: an external attacker with a foothold (stolen
session, compromised dependency); a **malicious insider** at each of the three
privilege levels (staff accountant, controller, platform admin); a compromised
or manipulated agent; a compromised model provider or supply chain; and — the
one that is easy to forget — an insider whose goal is not to *cause* a bad entry
but to *destroy the evidence* of one.

**Assets, ranked by what an attacker gains:** the guardrail bundle (control over
what is permitted, for everyone, silently) > the evidence store (control over
what is *knowable*) > the export path (bulk data egress) > individual proposals
> warehouse read access.

Note the ranking. The bundle outranks the ledger data, and the evidence store
outranks the export. That ordering is not the intuitive one and it drives what
follows.

### T1 — Threshold widening: the highest-leverage single-field change

**The attack.** Change one number. A quantitative guardrail's threshold moves
from $25k to $250k; a blast-radius cap moves from 20 proposals per run to
2,000; a rule is removed from the bundle. Nothing breaks, nothing alerts, no
entry is wrong on its face — the population of things that *become exceptions*
simply shrinks, and everything that would have escalated now passes silently.
`DOMAIN_KB` §7.1 names it exactly: *"the most damaging possible builder action
is not a bad prompt; it is widening an auto-pass threshold — a one-field change
that silently converts exceptions into non-events."*

It is the best attack in this system because it is **retrospectively deniable**
(a threshold is a legitimate business parameter and there is always a reason to
raise one) and because its effects look like normal operation.

**Controls.**

1. **Thresholds live only in the hash-addressed bundle** (§5, obligation B).
   There is no mutable configuration row, no admin screen field, no environment
   variable. Changing a threshold means issuing a new bundle, which means a new
   hash, a diff, and a change record (`AC-F36-15`).
2. **Bundle publication is dual-authorised** — the proposing author and a
   distinct publisher, and the publisher may not be the rule's author. *This is
   a new requirement not currently in F36's criteria*; flagged in §10.1.
3. **Risk-increasing diffs are classified mechanically** — threshold raised, cap
   raised, rule removed, allowlist extended, effective-date backdated — and
   require controller-level approval regardless of who else may edit policy
   (`DOMAIN_KB` §7.1). Mechanical classification matters: a judgement-based
   "significant change" test is one an attacker argues their way through.
4. **Blast-radius caps are non-disableable** (`AC-F36-13`) and I extend it:
   **they are also non-*widenable* beyond a ceiling set at deployment by a
   principal distinct from the tenant administrator.** Non-disableable but
   freely settable to 10^9 is disableable with extra steps.
5. **The author of a rule cannot approve output decided under it** (§1.3.4) —
   so widening a threshold to let your own proposal through does not let you
   approve it.
6. **Regression detection in the negative-control suite.** `AC-F36-05` runs
   firing and non-firing fixtures against the live bundle each close and on
   every bundle change. **A fixture that previously fired and no longer fires is
   reported as a regression and fails the suite** — not silently re-baselined.
   Without that clause the suite is the natural detector for this attack and
   does not detect it, because a widened threshold produces a bundle whose
   fixtures were updated alongside it. *Also a new requirement; §10.1.*
7. **Bundle-version continuity is visible at approval** (`AC-F36-18` already
   shows the bundle version in force), and the Monitors screen shows bundle
   changes for the period alongside override rate — so a reviewer approving
   under a bundle that changed mid-period can see that it did.

**Residual.** A controller who authors a wide threshold, waits a period, and
then approves under it in the next period passes both the version leg and the
period leg of §1.3. Detection falls to cross-period surveillance (F9) and to
override/escalation-rate monitoring. Stated, not solved.

### T2 — Prompt injection arriving through ledger data

**The attack.** Journal descriptions, line memos, vendor names and reference
fields are free text, and in many estates that text originates outside the
finance team — supplier-provided invoice descriptions, self-service expense
narratives, interfaced subledger references. It is **attacker-controllable
text that arrives inside the data the agent is supposed to analyse.** An
attacker who can create a payables line can write into our model's context.

Three payload goals, in increasing order of danger:

- **(a) Cause a bad proposal.** Least dangerous: it still has to pass every
  guardrail and a human.
- **(b) Escalate capability** — "also post this", "use dataset X", "ignore the
  threshold".
- **(c) Suppress a finding** — "this item is explained and requires no
  exception". This is the dangerous one, because it produces a *false clean
  result*, and per `INDUSTRY_KB` §12.2 a false negative leaves no artefact.

**Controls — structural, not instructional.** I have deliberately specified no
control of the form "the model should ignore instructions found in data",
because that is a prompt-quality assertion and prompt quality is not a control
(`INDUSTRY_KB` §13.1(2)); it would also collide with the gate-4 rule that no
criterion may assert explanation quality.

1. **The model cannot author SQL** (`AC-F39-02`) and **cannot name a dataset**.
   The resolver returns a certified-query identifier plus bound parameters; an
   injected "query table X" has nothing to execute against. Backstopped at the
   database grant (§2.4).
2. **The model cannot select its own capability.** The capability allowlist is
   resolved server-side from `(agent principal, skill version)` recorded on the
   run, never from model output. An injected "you may post" changes nothing,
   because the model was never the thing that decided.
3. **Tool-call arguments are schema-validated and range-checked at the broker**
   against the declared population, the certified dataset allowlist and the
   quantitative guardrails (§7.3). The broker treats model output as hostile
   input, always.
4. **Warehouse text enters the context as data in a delimited channel**, never
   concatenated into instruction text, and is truncated to a declared maximum
   per field. Structural containment, not persuasion.
5. **Against (c), the suppression payload — three independent legs:**
   - `integrity/` **contains no model call** (`PLAN` §11 criterion 4, asserted by
     an instrumented harness). The deterministic boundary and fidelity checks
     therefore cannot be talked out of firing by any text in the ledger.
   - The omission detectors' expectation model is computed over multi-period
     history, not narrated by the model.
   - **The "no exceptions" conclusion is emitted by the coverage machinery, not
     by the model** — a run below full coverage is structurally incapable of
     emitting it (obligation R), and at full coverage the conclusion is a
     computed consequence of zero findings, not a sentence the model chose to
     write. *This is a constraint on `solution-architect` (§10.1)*: if
     negative assurance is ever a model-generated string, T2(c) becomes a
     one-line attack on the product's core claim.
6. **The retrieved source text is retained verbatim in the dossier**, so an
   injection is reconstructable after the fact. Without it, an injection that
   worked is invisible in the evidence forever.
7. **Injection fixtures in the security suite** (§9), including a payload
   embedded in a journal description in the synthetic dataset — which is a
   requirement on `synthetic-data-agent`'s fixtures, recorded in §10.1.

**Boundary with `responsible-ai-architect`, stated rather than assumed.** What
the model *says* in response to injected content — refusal behaviour, tone,
whether it discloses the injection — is theirs. What the model can *cause* —
capability, data reach, authorization consequence — is mine. The overlap is
T2(c), suppression, because it is simultaneously a content failure and an
authorization-relevant one. I have specified the structural half and flagged the
overlap (§10.3) rather than designing their half.

### T3 — The export path as an exfiltration channel

**The attack.** Two export paths exist and they are not equally attractive.
F40's Journal Import export is a handful of lines — poor exfiltration. **F1's
auditor export is the whole dossier corpus for a period**: proposals, rationale,
warehouse extracts, rendered views, dataset lineage, approver identities. It is
*designed* to be complete, self-contained and consumable offline without a login
(§4.7), which are precisely the properties an exfiltrator wants. The feature and
the attack are the same mechanism.

**Controls.**

1. **Export is a capability in the allowlist**, granted to the auditor role and
   to controllers, never to staff accountants or FP&A (§1.3.2), and enforced at
   the broker like any other action.
2. **Every export is itself an event in the append-only store**, recording the
   requester, the authenticated identity and strength, the scope (tenant,
   period), the dossier count, and the destination. Export is the one read
   operation that is logged as though it were a write, because in exfiltration
   terms it is one.
3. **Exports are watermarked** with the requesting identity and timestamp, in
   the manifest and on each rendered view, so a leaked bundle is attributable.
4. **The blast-radius class applies to export**: a cap on exports per period per
   principal, with an escalation beyond it. An auditor legitimately exports once
   or twice per period; twenty exports in a night is the signature.
5. **Export scope is bounded to dossiers for a period.** There is no
   export-by-query, no arbitrary filter, no "export all history" control. The
   shape of the export is not attacker-selectable.
6. **The bundle is delivered to an access-controlled location with an
   expiry** — never an unauthenticated link, never an email attachment, never a
   permanently-valid URL.
7. **The NL inquiry surface has a result-row cap and no raw-dataset download.**
   Otherwise the exploration tier becomes an unmetered export channel that
   bypasses every control above — which is the more likely route, because it
   does not look like an export at all.

### T4 — The dossier store as a target, precisely because it is the evidence

**The attack.** Two variants, and the second is under-considered.

- **Alteration**: change what a dossier says, so a decision looks different than
  it was. Converts a detectable error into an undetectable one.
- **Destruction**: delete the dossiers for a period. This is the more effective
  attack, because it does not require producing a *consistent* false history —
  and because a missing record defeats reconstruction just as thoroughly as a
  falsified one. It is also a felony under SOX §802's anti-destruction
  provisions, which is worth stating: the attacker's incentive is high precisely
  because the exposure is high.

**Controls** — §4 in full, and the four that matter most here:

1. **Compliance-mode object lock** (§4.2) — not governance mode. The control
   must hold against the account's own administrator, because that is the
   threat.
2. **Store-level SoD** (§4.4) — the application can write and cannot delete; the
   retention administrator can hold and cannot read; no principal has both.
3. **Anchors in a separate trust domain** (§4.3 layer 3) — an attacker holding
   the application and the store still cannot produce a consistent history
   because they cannot re-sign.
4. **The storage-layer audit trail ships to that same separate domain**, and
   alerts on any delete attempt, retention-shortening attempt or lock-
   configuration change. `AC-F1-02`'s application-recorded attempt is necessary
   and insufficient; an attacker at the storage layer never touches the app.

**Availability variant, stated because compliance-mode locks make it
unrecoverable:** an attacker who can write can fill the store with garbage under
a seven-year lock that nobody — including us — can delete. Mitigations are
write-rate limits on the evidence writer and a per-period expected-volume alarm
(§4.2).

### T5 — Identity collapse

**The attack.** Run agents under a shared or generic account so that attribution
is destroyed. An agent SoD collapse leaves one name in the log where a human
violation leaves two (`INDUSTRY_KB` §4.2 problem 3), and once attribution is
gone, both §1.3's closure and F5's lineage answer become wrong rather than
merely missing — which is worse, because they still look like answers.

**Controls.** No shared account exists (§2.2); the broker rejects any action
whose principal is not a registered agent version; workload identity is issued
per run and bound to the run ID; a human session token is never usable by an
agent runtime (§1.3.1). At F17, per-agent Oracle identities and the dedicated
journal source make attribution survive into the customer's own ledger, which is
the only place an auditor can independently check it.

### T6 — The malicious (or merely exhausted) controller

**The attack.** The highest-privilege human insider does not need to break
anything. They certify a permissive dataset, or approve at 11pm without reading,
or — the specific one — **defeat the measurement instrument**: if the person
being measured for review precision can see which queue items are injected
probes, the probes measure nothing.

**Controls.**

1. **The controller cannot be their own second key** (§1.3.4), cannot approve
   output decided under a rule they authored or a dataset they certified
   (§1.3.4/§1.3.5), and cannot clear an SoD block by override (§1.3.6).
2. **Probe-visibility ACL — a specific new requirement.** The **forward** probe
   schedule and probe labels are readable only by the **assurance** role, which
   holds no approval, invocation, certification or policy-authoring capability
   (§1.3.2). No reviewer — including a controller — can read which pending items
   are probes. Consistent with `UX_KB` §5.6's design (probes indistinguishable
   before disposition) and with whatever `responsible-ai-architect` decides about
   reveal timing *after* disposition; my constraint is on the forward schedule
   only. *New requirement; §10.1.*
3. **Dwell, override rate and probe response are security controls, not
   telemetry.** They are the only instruments that distinguish a diligent
   approver from a rubber-stamping one, and a rubber-stamping approver is
   functionally identical to a compromised one. That is why F12 and F41's
   monitoring legs appear in a security KB at all.
4. **Self-grant is rejected**, not logged (§1.3.2) — no principal can change
   their own role set, at any level.

**Residual, stated plainly.** Collusion between an eligible approver and an
author defeats §1.3 entirely, as it defeats every two-key control. The only
remaining defence is aggregate: blast-radius caps (obligation P) and cross-
period surveillance (F9), which constrain effect regardless of authorisation.

### T7 — Supply chain: the model provider and the data that reaches it

**The attack surface.** Warehouse content enters a third party's infrastructure
in every model call. Three distinct risks: personal data leaving the customer's
jurisdiction; a provider silently changing the model behind an alias (an
unauthorised change to an ICFR-relevant control, `INDUSTRY_KB` §4.4); and a
compromised dependency in our own build reaching the broker or the evidence
writer.

**Controls.**

1. **Personal-data default-deny.** Dataset certification carries a
   `contains_personal_data` classification (extending obligation Q's metadata),
   and a Scope guardrail denies any flagged dataset to a model-bound or
   action-capable path in MVP1. This resolves the question `PLAN` §10 handed me
   — *does the warehouse hold personal data?* — **by design rather than by
   escalation**: I do not need the answer to build safely, and the classification
   makes the answer visible per dataset when it arrives.
2. **The model gateway is the only egress to a provider**, network-allowlisted.
   Agent code has no outbound internet path.
3. **Contractual**: zero-retention and no-training terms, and a named
   sub-processor list. Owner: whoever holds the commercial relationship;
   recorded here because it is a *control*, not a procurement detail.
4. **Model versions are pinned to dated versions, never to a moving alias**
   (§5, obligation K), and an unregistered version refuses to run
   (`AC-F2-04`).
5. **Dependency integrity**: lockfiles committed, pinned versions, and a
   dependency-vulnerability check in the pipeline. A missing dependency or a
   failing scan is a gap I report to `code-agent`, never one I work around.

### T8 — Time

Small, and auditors ask. Timestamps in the dossier are evidence: an approval
whose time is client-supplied is an approval whose time can be chosen.
**All evidential timestamps are server-side**, from a trusted, monitored time
source; the client's clock is never recorded as fact, only ever as a
client-reported field distinguishable from the authoritative one.

---

## 7 · Input validation boundaries

Stated as trust boundaries rather than as a list of validation rules, because
the useful question is *where does data change trust level* — and on this system
two of those boundaries are not the obvious ones.

### 7.1 The boundaries, enumerated

| # | Boundary | Trust change | Validation |
|---|---|---|---|
| B1 | Browser → API | Untrusted → authenticated | Schema validation on every field; authn before authz before business logic; CSRF on all state-changing routes; rate limits per principal |
| B2 | IdP → session | External assertion → identity | Full OIDC validation: signature, issuer, audience, `nonce`, expiry, and `amr`/`acr` recorded not merely checked |
| B3 | Agent runtime → broker | **Untrusted** → decided | §7.3. This is a trust boundary even though both sides are ours |
| B4 | Warehouse → semantic layer → model context | **Untrusted content** → model input | §7.2. The one most likely to be misread as internal |
| B5 | Model output → broker tool call | **Untrusted** → action | §7.3 |
| B6 | Oracle config probe → CUEC register | External → evidence | Response schema-validated; raw response retained; a malformed or unexpected response is a *fail*, never a pass (`FUNCTIONAL_SPEC` §2 C2) |
| B7 | Warehouse text → rendered view → stored evidence → auditor's browser | Untrusted → **persisted and later replayed** | §7.5. The under-considered one |
| B8 | File upload | — | **No upload path exists in MVP1.** Stated so its later addition is a change, not a gap |

### 7.2 B4 — warehouse content is untrusted input

The instinct is that the warehouse is an internal system and its contents are
trusted. They are not: its contents originate in subledgers fed by suppliers,
employees and interfaces. Free-text fields — descriptions, memos, references,
vendor names — are attacker-controllable in many estates. Controls are §6 T2's:
delimited data channel, per-field length caps, no path from that text to a SQL
parser, no path from that text to a capability decision, and verbatim retention
so an injection is reconstructable.

### 7.3 B3 and B5 — the broker treats everything as hostile

The broker is the enforcement point (§2.3), so it must not trust its callers,
including our own agent runtime.

- Every tool call is validated against a **strict schema**: unknown fields
  rejected, not ignored; types and ranges enforced; enumerations closed.
- **No free-text field is ever interpreted as an identifier.** Dataset,
  skill, account and period references are IDs resolved server-side against the
  run record, never strings the caller supplies.
- **No path, URL or command ever appears in a tool argument.** There is no
  file-read, file-write, network-fetch or shell capability in any allowlist.
- Amounts, dates and account combinations are validated against the declared
  population and the quantitative guardrails **before** any downstream effect.
- Denials are uniform: same shape, same decision-ID mechanism, whether the
  caller is the UI, the agent runtime or a direct API call (`AC-F36-03`).

### 7.4 Authorization is checked at the broker, per action, on every call

Not at the session's start, not at the queue's render, not once per run. The
classic failure — object-level authorization checked on the list endpoint and
not on the detail endpoint — is exactly what §9's per-role direct-API scenarios
exist to find.

### 7.5 B7 — the stored rendered view, which we later hand to an auditor

Obligation A requires storing *what the human saw*, and `AC-F41-04` requires it
to be reproducible. So the evidence artefact contains ledger text an attacker
may have authored, and §4.7 hands that artefact to an auditor as a file they
open outside our application, with no CSP and no sandbox of ours.

That is a stored-XSS sink whose blast radius is an external auditor's browser,
and it is not a hypothetical chain — every link in it is a requirement.

**Controls.** Contextual escaping at render; a strict CSP in the application;
the stored rendered view **sanitised at write** and stored scriptless; replay
inside the application served from a sandboxed context; and, in the export
bundle, rendered views that contain **no script, no external references and no
active content of any kind**, verified by a test rather than by review. This
last one is a requirement on F1's export that is not currently in its criteria;
§10.1.

---

## 8 · Suite execution status for this gate — stated plainly

**No suite was executed this pass, and none could have been.**
`dev/tests/suites/security/run.sh` does not exist; the project has no `dev/`
repository at all, because `code-agent` has not yet run. This is the
**Architecture** gate, not the Test gate, so nothing was expected to run — but
per my contract I state it explicitly rather than let a design document read as
though it carried test results.

Everything in this file is **DESIGN — NOT EXECUTED**. For a security document in
particular, "not run" and "no vulnerabilities found" are opposite claims, and
nothing here should be read as the second.

The one factual check I did perform, using read-only inspection: the root
repository's `.gitignore` excludes `projects/*/dev/` and `projects/*/prod/`
(§2.6). The project's own dev-repo `.gitignore` cannot be checked because it
does not exist yet.

At the Test gate I will execute `dev/tests/suites/security/run.sh` for real.
Per the platform's standing lesson, a suite once reported as unexecuted is
re-run, never waved through on the strength of a thorough-looking static pass.

---

## 9 · Test-suite ownership — the security suite at the Test gate

Entry point: `dev/tests/suites/security/run.sh`. All suites blocking; exit `3`
(no scenarios defined) is not a pass. Per-scenario evidence to
`projects/conclave-finance-studio/test-evidence/security-<YYYY-MM-DD>.md` under
`test-agent`'s convention, each scenario marked `EXECUTED` /
`STATIC ONLY — NOT EXECUTED` / `PARTIAL`.

The scenarios below are the suite's design. Each names what it proves and,
where one exists, the acceptance criterion it exercises.

**S1 — Authorization boundary matrix.** For every role in §1.3.2 × every
capability, call the API **directly**, bypassing the front end. Assert every
cell matches the intended matrix and every denial carries a decision ID and a
bundle hash. Covers `AC-F36-03`, obligation M. Specifically includes: FP&A
attempting any approval; staff accountant attempting dataset certification and
bundle publication; platform admin attempting to approve, to certify, to read a
dossier's contents, and to alter retention; auditor attempting anything other
than read and export.

**S2 — SoD closure enforcement.** Seed an artefact authored by principal *X*;
have *X* attempt to approve a proposal whose closure contains them, via every
route. Assert denial, with the denial naming the clause and the artefact.
Repeated per artefact class: skill version, prompt version, rule/threshold,
declared population, dataset certification, model pin, override. Then the
period leg: *X* authors v2 mid-period, attempts to approve v1 output, denied.

**S3 — SoD negative control.** An eligible approver *Y* approves successfully.
A suite in which every approval is denied proves nothing except that the system
is broken; without S3, S2 passes trivially on a system that denies everything.

**S4 — Invoker ≠ approver.** The principal who invoked the run cannot approve
its output, including when they are otherwise eligible.

**S5 — The human leg cannot be occupied by an agent.** Attempt to record an
`agent`-typed principal as `approved_by`, as an override second key, and as a
dataset certifier, at every permission level and via direct API. Assert
rejection. Attempt to publish a bundle granting `approve` to an agent principal;
assert publication fails naming the grant.

**S6 — SoD is not override-eligible.** Attempt to clear an SoD block with an
override, with a dual-authorised override, with an administrator, and with the
routing-budget override. Assert all four fail. Assert an SoD-blocked item is
counted in the monitored metric.

**S7 — No Oracle posting credential exists.** Static: no posting-credential
secret name, no journal-submission client library in the dependency tree.
Runtime: attempt to resolve a posting credential from every module; assert
nothing is returned and a control event is recorded. Covers `AC-F40-02`,
`AC-F36-04`, obligation E.

**S8 — Credential containment.** Attempt to resolve any downstream credential
from an agent context, from the semantic layer, from a detector and from the
frontend. Assert all fail with a recorded control event. Assert no credential
appears in a dossier, a rendered view, an export or a log line.

**S9 — Secrets-leak check.** Scan the working tree and the dev repository's
**git history** for credential patterns, private keys and provider API keys.
Assert `.gitignore` covers `.env` and key material, that `.env.example` contains
every key with placeholder values, and that **no `NEXT_PUBLIC_*` variable holds
a secret**. A finding here is reported to the human and to `code-agent`; I do
not rewrite history to remove it.

**S10 — Prompt injection via ledger data.** Fixtures with payloads embedded in
journal descriptions, vendor names and line memos, targeting each of §6 T2's
three goals. Assert: no SQL is executed from model output; no dataset outside
the skill's allowlist is read; no capability outside the allowlist is invoked;
and — the important one — **a seeded exception is still detected and a "no
exceptions" conclusion is not emitted** when the payload attempts suppression.

**S11 — Injection into the stored evidence.** A payload in ledger text that
reaches a rendered view. Assert the stored view is scriptless, and that the
**export bundle's** rendered views contain no script, no external references
and no active content. Covers §7.5.

**S12 — Input validation at the broker.** Unknown fields, wrong types,
out-of-range amounts, path- and URL-shaped strings, oversized fields, and
identifier-shaped free text in every tool-call argument. Assert rejection with
a uniform denial shape.

**S13 — Evidence-store immutability.** Attempt update and delete via every
surface, API and administrative path; assert failure, that the dossier is
unchanged, and that the attempt is itself recorded (`AC-F1-02`). Alter a stored
dossier's bytes out-of-band; assert detection identifies it (`AC-F1-03`).
Remove a dossier out-of-band; assert the **chain** detects the removal — a
per-object hash alone would not.

**S14 — Retention floor.** Attempt to shorten retention below seven years, to
remove an object lock, and to delete an unexpired object, at every permission
level including the store's administrative principal. Assert all fail.

**S15 — Store-level SoD.** Assert the application's principal holds no delete,
no retention-shortening and no lifecycle permission, and that no single
principal holds two of §4.4's four roles.

**S16 — Export authorization and exfiltration limits.** Assert export is denied
to unentitled roles; that each export is recorded with requester, scope and
count; that the bundle is watermarked; that the per-period export cap trips;
that no export-by-arbitrary-query path exists; and that the NL inquiry surface
enforces a result-row cap with no raw-dataset download.

**S17 — Export verifiability offline.** Verify a bundle with no application
access, using only the bundle's own manifest, anchors, public keys and
verification script. Then tamper with one dossier inside the bundle and assert
verification fails and names it.

**S18 — CUEC fail-closed.** For each state — unverified, failed, expired,
drifted — assert the export is refused and the refusal names the item and the
state (`AC-F40-05`). Assert a probe run at export time, a drift event recorded
as a control event, and the method (probed vs. attested) carried into the
dossier and the export (`AC-F40-06`).

**S19 — Threshold-widening detection.** Widen a threshold, raise a cap, and
remove a rule. Assert each produces a new bundle hash, a change record naming
the rule, owner and effective dates, a **risk-increasing** classification, a
dual-authorisation requirement, and — the one that matters — a
**negative-control regression**: a fixture that previously fired and no longer
does is reported as a regression and fails the suite.

**S20 — Blast-radius caps cannot be widened past the deployment ceiling**, at
any permission level, through any surface or API (extends `AC-F36-13`).

**S21 — Session and authentication controls.** Idle and absolute timeout;
session invalidation on IdP termination; step-up re-auth enforced at approval,
override second key, bundle publication and dataset certification; the
authentication-strength claim present in the approval record; approval refused
when the assertion is stale.

**S22 — Probe-schedule confidentiality.** Assert no reviewer role, including
controller and administrator, can read the forward probe schedule or probe
labels via any API, and that nothing rendered before disposition distinguishes
a probe (composes with the UX suite's assertion of the same property).

**S23 — Self-grant rejection.** Every role attempts to modify its own role set;
assert rejection rather than logging.

**S24 — Fail-closed behaviours.** Unresolvable or hash-mismatched bundle: every
action denied (`AC-F36-17`). Unverifiable principal: no action, no default
identity. Unavailable evidence store: **no action proceeds unrecorded** — a
system that keeps working when it cannot write evidence is a system producing
unevidenced ledger effects.

**Where a scenario cannot run** — a missing dependency, an absent entry point —
I will report it as a gap to `code-agent` and mark the scenario
`STATIC ONLY — NOT EXECUTED`. I will not install anything, start a server, or
edit the code under test to make my own suite pass.

---

## 10 · Constraints on `solution-architect`'s design, and disagreements

### 10.1 Constraints — stated as requirements on its design, not as designs

Fourteen items. Where one is a **new requirement** not currently carried by any
acceptance criterion, it is marked **NEW** so it cannot enter the build
unnoticed or be assumed to be already covered.

1. **One broker, not one per surface.** Enforcement and credential custody are
   singular (§2.3).
2. **Per-skill database grants scoped to certified dataset objects**, read-only,
   as a backstop below the application (§2.4).
3. **The evidence store and the operational store are separate at the storage
   layer, not by convention** — `PLAN` §9.3 hands this question to gate 6 and
   my answer is: separate, with the application holding write-only rights and no
   delete anywhere in its policy (§4.4).
4. **Compliance-mode object lock, not governance mode** (§4.2).
5. **A tamper-evidence anchor signed by a key the application cannot use, in a
   separate trust domain** (§4.3 layer 3). **NEW** — `AC-F1-03` requires
   detection of alteration but nothing currently requires resistance to an
   attacker who recomputes the hash.
6. **The storage-layer audit trail ships to that separate domain**, with alerts
   on delete, retention-shortening and lock-configuration events. **NEW**.
7. **Retention stamped per object at write, floor non-lowerable** (§4.1).
8. **Envelope key hierarchy** so BYOK is a substitution, and old public keys
   retained beyond the retention period so old evidence stays verifiable
   (§4.5).
9. **CUEC probes run at export time, not only at deployment**, with drift
   detection blocking export (§3.4). **NEW** — `AC-F40-05` gates on verification
   state but nothing currently makes that state *current*.
10. **Bundle publication is dual-authorised**, publisher ≠ rule author, with
    mechanical risk-increasing-diff classification (§6 T1). **NEW**.
11. **Negative-control regression semantics**: a fixture that previously fired
    and no longer does fails the suite (§6 T1). **NEW**.
12. **Approver eligibility is computed and surfaced when the item enters the
    queue**, not at submit (§1.3.6). **NEW**, and it is a queue-design
    constraint, which is why it is stated here rather than designed here.
13. **Negative assurance is emitted by the coverage machinery, never as a
    model-generated string** (§6 T2). This may already be the intent; it is not
    currently written down anywhere, and the attack it prevents is a one-liner.
14. **Export rendered views are scriptless and free of active content**, tested
    (§7.5). **NEW** on F1's criteria.

Two sequencing constraints, both mine:

- **F2 (version registry) ships before or with F36's Identity/SoD class**,
  because the version tuple is the closure's input set (§5). An incomplete stamp
  silently under-computes the SoD constraint and permits approvals that should
  be blocked — a control that fails open and quietly.
- **F38's dataset certification metadata gains a `contains_personal_data`
  classification** before any model-bound path ships (§6 T7).

One constraint on `synthetic-data-agent`, for gate 7: fixtures must include
**injection payloads embedded in journal descriptions, vendor names and line
memos**, alongside the sequences already requested in `PLAN` §10.

### 10.2 Disagreement with `solution-architect`, flagged rather than resolved

`PLAN` §10 assigns "WORM/immutable store selection and ≥7-year retention (G)"
to `solution-architect`. I have taken the **security properties** of that store
— compliance vs. governance mode, store-level SoD, the external anchor, the
audit-trail destination — as mine, and left **technology selection, cost and
operational shape** as theirs. I think that split is right, but it is a split I
have asserted rather than negotiated, and it overlaps at exactly one point:
whether the evidence store and the operational store share infrastructure
(`PLAN` §9.3). My answer is no. If `solution-architect` proposes shared
infrastructure with logical separation, that is a genuine disagreement and it
should go to the human rather than be reconciled quietly, because the
difference is whether a single compromised credential reaches both the state and
the evidence of what changed it.

### 10.3 Boundary with `responsible-ai-architect` that is genuinely unclear

Stated rather than resolved, per instruction. **Suppression-by-injection**
(§6 T2 goal (c)) sits on the line: the model declining to report a finding
because ledger text told it to is simultaneously a content-guardrail failure
(theirs) and an integrity failure in a regulated output (mine). I have specified
the structural half — deterministic detectors with no model call, coverage
computed outside the model, negative assurance not model-authored — and have not
touched the behavioural half. If `responsible-ai-architect` reads the whole of
T2(c) as theirs, my structural controls are still required and are not
duplicated by anything they would write; if they read none of it as theirs, the
behavioural half is unowned. **It should be settled explicitly at this gate
rather than each of us assuming the other has it.**

---

## 11 · Calls made under the standing authorization

The human authorized MVP1 and asked that SME judgement be trusted. These are
made, not returned, each with what would reverse it.

| # | Call | Basis | What would reverse it |
|---|---|---|---|
| **SA1** | **MVP1 deploys single-tenant per customer, with tenant modelled as a first-class dimension from day one** | Obligation S is per-tenant; the CUEC register, retention and key hierarchy are all per-tenant. Modelling tenancy now and deploying isolated is the cheap combination; retrofitting tenancy into a dossier corpus is not possible | A decision to run shared infrastructure for two customers — revisit trigger #4, and it changes isolation from deployment-enforced to code-enforced |
| **SA2** | **Federated OIDC only; no local password store in MVP1** | The buyer runs Oracle ERP Cloud and therefore runs an IdP; a second credential store creates a JML control we would have to design and have tested | A pilot customer without a usable IdP. Cost is a real one: no standalone demo without a seeded environment |
| **SA3** | **Personal data is assumed present and denied by design** rather than escalated | I do not need the answer to build safely, and default-deny makes the answer visible per dataset when it arrives. Escalating would have blocked the gate on a fact about the customer | Confirmation that the warehouse holds personal data *and* a business need to analyse it — revisit trigger #5, which opens GDPR basis, transfer and DPIA |
| **SA4** | **Platform admin holds no finance capability** — cannot approve, certify, author policy, or read dossier contents | An admin who can grant themselves approval and then approve is a one-person path to the ledger | A customer operational need I have not anticipated. I expect this one to be argued with and I would want it argued in front of the human |
| **SA5** | **The Identity/SoD guardrail class is not override-eligible**, and the only relief for a deadlock is adding an eligible human | An override that clears an SoD block is a second door. The honest fallback — R5 handoff to the customer's manual process under Oracle's own controls — is recorded and counted | Evidence from a pilot that SoD-blocked rates make the close unworkable. That is a real risk and the metric exists precisely so the question can be answered with data rather than argued |

**One escalation, and it does not block anything.** `PLAN` §9.1's open item —
public vs. private filer — reaches me too. It changes nothing in this design: I
built to the public-filer floor because there is no "pilot outside SOX" path
once postings are in play, and because a private filer's *risk* floor is not
lower (restatements concentrate in smaller, non-accelerated filers). It changes
only how directly an external auditor will test these controls under §404(b),
which raises the evidence bar on §9's suite rather than the design bar on §1–§7.
No decision waits on it.

---

## 12 · Sign-off note for the joint Architecture gate

Presented jointly with `solution-architect`'s pass. My position:

- **The gate's hardest item — `author ≠ approver ≠ invoker` — is designed as an
  enforced constraint** (§1.3), computed from artefacts F2, F36 and F38 already
  produce, evaluated at the broker, non-overridable, with a stated deadlock
  path and a counted failure mode. It closes the `DOMAIN_KB` §7.1 defect in
  MVP1, where the authors are policy owners and data owners, and it extends to
  the builder unchanged when F16 ships.
- **The AI cannot occupy the human leg** — enforced by principal type, at the
  schema level, so a future feature cannot quietly fill the field (§1.3.1).
- **Obligation S's conditional AutoPost trap is designed against**, with probes
  rather than questionnaires, at export time rather than at deployment only,
  fail-closed on stale as well as failed, and with drift as a first-class
  control event (§3).
- **Seven new requirements are flagged** rather than assumed covered (§10.1,
  marked NEW): the external tamper-evidence anchor; the storage-layer audit
  trail in a separate trust domain; export-time CUEC probing with drift
  detection; dual-authorised bundle publication with mechanical
  risk-increasing-diff classification; negative-control **regression**
  semantics; approver eligibility surfaced when an item enters the queue rather
  than at submit; and scriptless rendered views in the auditor export.
- **Two disagreements are on the record rather than reconciled**: shared vs.
  separate evidence infrastructure (§10.2) and the ownership of
  suppression-by-injection (§10.3).
- **Nothing was executed.** §8. This is a design gate and the security suite is
  designed, not run.

---

## 13 · Gate 10 ruling (2026-08-05) — the sixth claim prohibition, and the T-gates

Ruling pass, at the orchestrator's request, on `solution-architect`'s
`ARCHITECTURE_KB` §25.3.3. The analysis/execution boundary is jointly owned
(§10.1 constraint 1, §2.3), so this is mine to co-sign or refuse.

### 13.0 Completeness check — binding decisions since v1.0.0

Re-read `PROJECT_CONTEXT.md`'s Decisions Log in full. Binding decisions
recorded since my last pass, and how this ruling stands against each:

| Binding decision | This ruling |
|---|---|
| **2026-08-05 `[override]`, nine `NOT VERIFIED` criteria, ship as pilot** | Not reopened. None of the nine is claimed met here. This ruling adds to the override's claim-prohibition list, which the override itself declares "unchanged by this override" — an addition is therefore in scope for the human, not for me to enact. I do not write it into the Decisions Log. |
| **The five claim prohibitions** | All five survive verbatim. §13.2's sixth is additive; it overlaps none of them. Prohibition 2 (no tamper-evidence against a party with application-level write access) is the nearest neighbour and is about the *evidence store*, not the *broker*; a reader cannot derive the boundary statement from it. |
| **2026-08-05 gate 10 — register 19 NARROWED NOT CLOSED, closes on T1/T2/T3** | Endorsed in §13.3, with one added conjunct (T4). |
| **2026-08-05 gate 10 — register 1 (mTLS) unchanged, re-linked as T1–T3's peer** | Agreed, §13.4, and I strengthen the reason. |
| **2026-08-05 gate 10 — export must be style-inlined** | Compatible. §13.5's export disclosure is a payload/integrity-section requirement, not a stylesheet one, and `AC-F1-10`'s no-active-content rule is untouched. |
| **2026-08-05 gate 10 — register 30 re-scoped upward (uncalibrated threshold binds every future primitive)** | Untouched by this ruling. |
| **2026-08-05 orchestrator correction — IA approval inferred, not asked** | No security control in this file depends on the pass-17 IA. §13.5's finding is about a *disclosure* that must appear on screens and in the export; it is IA-independent and survives whichever IA the human confirms. |
| **2026-08-05 orchestrator correction — Part A2 partially built; J3/J4 unwalkable** | No security scenario in §9 traverses J3 or J4. No conflict. |
| **2026-08-05 pass 24 — orphan check, scoped to `app/ui/` only** | Directly relevant, and §13.5 D1 is an instance the scope excludes. Recorded there rather than as a separate complaint. |
| **Test Policy: all suites blocking, no advisory exceptions** | Honoured. §13.5's three findings are labelled **static review, not suite-executed** — see §13.6. I have not presented an unexecuted check as a passing one. |

**Conflict with a binding decision: none.** One disagreement with
`solution-architect` is flagged in §13.5 and it is a disagreement about
*classification*, not about direction.

### 13.1 Decision — CO-SIGNED, with the wording amended

The five prohibitions are **not** sufficient, and the gap `solution-architect`
identifies is real. I co-sign a sixth prohibition. My reason is not the one
given in §25.3.3, and the difference matters.

§25.3.3 argues the gap is that the prohibition list travels where screens do
not. That is true. But it rests on a premise I checked and could not confirm:
that the pilot strip discloses the collapsed boundary per screen. **It does
not** — see §13.5 D1. The pilot strip discloses *data provenance* (synthetic
fixture, cannot support a posting or an assurance conclusion) and says nothing
about topology, and `ges_gateway.is_pilot_transport()` — the accessor that
exists so a screen can say so — has **no call site in the application**.

So the sixth prohibition is needed for a stronger reason than §25.3.3 gives:
it is not that the disclosure exists on screens and fails to travel. It is that
**the disclosure of this particular weakening does not currently exist on any
surface at all** — not on a screen, not in the export payload, not in the
prohibition list. The three places a reader could meet it are three misses.

### 13.2 The wording I would put in front of the human

Longer than `solution-architect`'s draft by two sentences, and both additions
are load-bearing: the first states what remains true so the prohibition cannot
be read as retracting more than it does, the second closes the credential
inference a reader will otherwise make from §2 of this file.

> **Prohibition 6 — the trust boundary.** No claim that the analysis/execution
> trust boundary is enforced as a **process** boundary. In the pilot's
> single-command configuration (`backend/pilot.py`) it is a **module** boundary:
> the guardrail broker runs inside the api process, and a prompt-injected tool
> in that process could reach `ges.executor` by `import` alone. Relatedly, no
> claim that the pilot demonstrates the credential boundary: the rule that a
> credential resolves only inside the `ges` process is enforced by that process
> reading its own `CONCLAVE_PROCESS_ROLE`, so in a single process it is
> self-asserted rather than enforced.
>
> **What remains true and is not withdrawn by this prohibition.** The guardrails
> themselves are enforced at the broker, not in the interface, and every
> terminal control on the surface goes through it. No Oracle posting credential
> exists in any MVP1 environment and no journal-submission library is a
> dependency (`AC-F40-02`). The pilot process holds no declared credential at
> all — its warehouse is the synthetic fixture, opened without a credential — so
> nothing was exposed; what is absent is the *enforcement*, not the secret. The
> two-process topology is built and has an executing test witness that starts
> the broker as a separate OS process, asserts a different pid holds the
> credential while the api role is refused it, and drives a real broker decision
> over a TCP socket. It is not what the pilot runs.

Three notes on why it is worded that way.

1. **"could reach `ges.executor` by `import` alone" is kept from the original
   draft and is exactly right.** I checked: `backend/pilot_transport.py` is the
   sole composition root, it lives outside the `app` package, and the static
   "the api package never imports `ges`" check still holds — which is precisely
   why the residual is invisible to every suite that runs in one interpreter.
2. **The credential sentence is mine and I insist on it.** `ges/credentials.py`
   decides `in_ges_process()` by reading an environment variable *inside the
   process being constrained*. That is the same objection `solution-architect`
   raises against `CONCLAVE_ENV` in T2 — "a check the attacker's process
   performs on itself" — applied to the credential rule, and it is the sentence
   a reader of `SECURITY_KB` §2.3 ("the broker is the only enforcement point,
   and the only credential holder") will otherwise assume the pilot demonstrates.
   `AC-F36-04` is not falsified by this: nothing resolves in the pilot, because
   the pilot process declares no role at all. The claim I am prohibiting is the
   *demonstration*, not the criterion.
3. **"nothing was exposed" is stated deliberately.** A prohibition that reads
   like an incident report will be over-corrected for by whoever receives it.
   The honest shape is: no secret was at risk, the mechanism that would protect
   one is not in force.

### 13.3 Ruling on T1 / T2 / T3 — all three endorsed as security gates, plus a T4

**T1 — the `ges` package is not on the api host's disk.** Endorsed, and it is
the operative one for me too. It is the only one of the three that changes the
property from *asserted* to *true by construction*, and it is checkable by a
party with no source access — which matters because §4.7's auditor is defined
as someone with no application login. A control an auditor can verify from the
artefact is worth more than one they must take on trust.

**T2 — `pilot_transport.py` absent from the api image, not merely refused at
runtime.** Endorsed, and the reasoning is correct and generalisable: a runtime
refusal executed by the process it constrains is a control that fails to the
attacker's advantage the moment the attacker has code execution in that
process. Note that T2 is *strictly weaker than T1 and still necessary*: T1
removes the callee, T2 removes the composition root. Neither subsumes the
other, because a future file could collapse the boundary without being
`pilot_transport.py`, and T1 is what stops that class. Keep both.

**T3 — one complete approval end-to-end over `LoopbackHttp`.** Endorsed, and I
would raise its priority above where §25.3.2 places it. I read the current
`ARCH_04`: it drives a broker `decide` over the socket and asserts the outcome
is one of `allow`/`deny`/`abstain` — it does not require `allow`, and it does
not carry the approval through the workflow write path to a recorded decision.
Meanwhile every approval the suites actually exercise runs in-process. So the
two configurations diverge unobserved at exactly the step that produces a
binding record. T3 is not tidiness; it is the last unwitnessed seam on the
write path.

**T4 — added, and it is mine: the pilot process must be unable to hold a
credential.** `backend/pilot.py` never sets `CONCLAVE_PROCESS_ROLE` and never
calls `assert_api_process_holds_no_credentials()`. That guard exists
(`ges/credentials.py`), it is called by `app/run.py` before uvicorn binds, and
it is **not** called by the one entry point that puts both halves of the
boundary in a single process — the entry point that most needs it. Today this
is inert (the pilot uses the synthetic warehouse and holds no declared
credential), which is why it is a hardening item and not a defect. It stops
being inert the first time someone runs the pilot from a shell that has
exported a warehouse credential for another purpose. **T4: `backend/pilot.py`
calls `assert_api_process_holds_no_credentials()` at startup and refuses to
serve if any declared or forbidden credential name is present in its
environment.** Owner `code-agent`; it is roughly one call, and unlike T1–T3 it
is buildable in a single-host pilot today.

Register entry 19 should close on **T1 ∧ T2 ∧ T3**, unchanged. T4 is a pilot
hardening item and is not a condition on entry 19 — it is a condition on
§25.3.1's "sufficient for the pilot" ruling, which is where I would attach it.

### 13.4 Ruling on the mTLS pairing — agree, and the reason is stronger than stated

`solution-architect` says register 1 (mTLS on loopback, currently a shared
token plus a 127.0.0.1 bind) is T1–T3's **peer, not its subset**, and that both
should reach the human once, together. **Agreed.**

The reason given — entry 1 secures the channel, T1–T3 establish there are two
processes — is correct but understates it. The security-side reason is that
**each is worthless in the failure mode the other prevents, and the combination
has a specific perverse ordering.** Satisfy T1–T3 without entry 1 and you have
built a real network hop protected by a bearer token, which is a *worse*
posture than the module boundary against a host-local attacker who can read the
token from the environment: the collapsed pilot at least never put the
credential on a wire. Satisfy entry 1 without T1–T3 and you have mutually
authenticated a channel between a process and itself.

So they are not merely presented together — they are **conjunctive**, and
staging them creates a window in which the deployment is arguably less safe
than the pilot. That is the sentence I would want in front of the human, and it
is the reason I would refuse a plan that lands T1–T3 in one release and entry 1
in the next.

One presentation constraint, since a joint item can still be presented badly:
it must reach the human as **one gate with five conjuncts (T1, T2, T3, T4,
entry 1)**, each individually falsifiable, and not as a paragraph of narrative
that a reader can approve as a whole. Four of the five are `deploy-agent`'s and
`code-agent`'s to build; none is mine.

### 13.5 Findings this pass produced that neither architect raised

**D1 — DEFECT, and it invalidates the premise of "gap, not defect".**
`ARCHITECTURE_KB` §25.3.1 lists as condition 5 that "every screen rendering a
broker fact obtained through it says so, in words, in the pilot strip", and
records all five conditions as currently holding. Condition 5 does not hold.
`app/ui/chrome.py:pilot_strip()` takes `state` and ignores it; its text is
fixed and is entirely about synthetic fixture data. `ges_gateway.py`'s own
docstring makes the same claim ("every screen ... says so in words"), and
`ges_gateway.is_pilot_transport()` is referenced by nothing in `app/` — the
only other occurrences in the tree are two stub classes in UI tests that set
`is_pilot_transport = False`. **The disclosure `solution-architect`'s "gap, not
defect" classification depends on has no call site.** I therefore disagree with
the classification: this is a gap *and* a defect, and the defect is the reason
the gap is worse than described. Owner `code-agent`. I am not fixing it —
fixing it would destroy the evidence that the five conditions were recorded as
holding when one did not.

Worth naming without blame: this is exactly the orphan class pass 24 built a
checker for, and pass 24's judgement call (c) scoped that checker to `app/ui/`.
`ges_gateway` is `app/`, not `app/ui/`. Pass 24 even recorded that widening the
scan to all of `app/` reports exactly one definition to look at —
`ges_gateway.PilotInProcessHttp` — and stopped one line short of the accessor
beside it. The consequence pass 24 anticipated in the abstract
(`LabelSetUnavailable` would not have been caught) has a second, live instance,
and this one is a security disclosure.

**D2 — the export does not carry the disclosure either, and there is an exact
mechanism for it that is already built and already tested.**
`app/evidence/export.py`'s `REQUIRED_INTEGRITY_SECTIONS` is a declared contract
requiring that where a weaker state is declared, the disclosure **names its
unmet criterion** — with the stated rationale that "the auditor reading this
file has no application login to go and look with (`AC-F1-04`)". Two sections
exist: `anchor` (`AC-F1-11`) and `retention` (`AC-F1-08`). There is **no
section for the transport or the topology.** So the artefact purpose-built for
the reader who never sees a screen states two of the pilot's three structural
weakenings and omits the third — and the omitted one is the boundary §3.2 says
the entire product claim reduces to.

This is the more durable answer to `solution-architect`'s own concern. A
prohibition list is a document that travels only as long as someone remembers
to carry it; a `transport` integrity section travels *inside every export*, is
enforced by an existing contract test, and cannot be forgotten by a person.
**Recommendation: add a third required integrity section** — keys
`process_boundary_enforced` (false in the pilot), `statement`, and the
residual reference. Note the residual reference cannot be an AC ID: unlike the
anchor and retention residuals, the process boundary has **no acceptance
criterion of its own** — it is carried only by register entry 19 and by
`ARCHITECTURE_KB` §3.2. That absence is itself a finding, and it is the reason
this weakening was the one that slipped through three disclosure surfaces while
the other two did not. Owners: `functional-design-agent` for whether a
criterion should exist; `code-agent` for the section.

**D3 — see T4 in §13.3.** `backend/pilot.py` bypasses the startup credential
guard.

None of D1–D3 changes my co-signature. D1 strengthens the case for the
prohibition; D2 says the prohibition alone is the weaker of two available
remedies and both should be taken.

### 13.6 Execution status of this pass — stated plainly

**Static review. No suite was executed by me this pass, and D1–D3 are
static-source findings, not test results.** They are checkable by reading four
named files and do not require execution to be true, but they have not been
witnessed by an executing scenario and I do not present them as having been.

The security suite entry point `dev/tests/suites/security/run.sh` **exists**
(it did not at gate 6, where §8 recorded that nothing was executed), and
`test-evidence/security-2026-08-04.md` records it executing. That evidence
predates `code-agent`'s pass 24 (`dev` @ `c8470d9`); re-running it against the
current tree is `test-agent`'s aggregation at the Test gate, and I did not run
it here because this is a ruling pass and the human is operating the pilot on
8030. **`dev/` was not modified by this pass and no process was started or
stopped.**

One suite-coverage gap for whoever owns the follow-up: no security scenario
asserts that the transport in force is disclosed. D1 survived because the
disclosure was never something a check could fail on. If D1 is fixed, the fix
needs a scenario that fails when the accessor loses its call site again.

---

## 14 · Change history

| Date | Version | Change | Approving decision |
|---|---|---|---|
| 2026-08-05 | 1.1.0 | MINOR — §13 added, gate 10 ruling pass. **Co-signs a sixth claim prohibition** on the analysis/execution trust boundary, with amended wording adding the credential-boundary clause and an explicit "what remains true" paragraph. Endorses T1/T2/T3 as security gates, **adds T4** (`backend/pilot.py` must call `assert_api_process_holds_no_credentials()`), and agrees register 1 (mTLS) is T1–T3's conjunctive peer with a strengthened reason for refusing to stage them. Three findings recorded: **D1** — no screen discloses the collapsed transport (`ges_gateway.is_pilot_transport()` has no call site), which contradicts `ARCHITECTURE_KB` §25.3.1 condition 5 and is a **classification disagreement** with `solution-architect`; **D2** — the export's `REQUIRED_INTEGRITY_SECTIONS` has no transport section, and the process boundary has no acceptance criterion to name; **D3** — the pilot entry point bypasses the startup credential guard. Static review; no suite executed, `dev/` unmodified. | Gate 10 ruling pass at the orchestrator's request, against `ARCHITECTURE_KB` §25.3.3; the sixth prohibition itself awaits the human |
| 2026-07-31 | 1.0.0 | Initial security architecture. Authentication & authorization design incl. the authorship-closure SoD engine (`author ≠ approver ≠ invoker`); credential architecture and the MVP1 posting boundary; obligation S CUEC register, probes and drift detection; retention, WORM and three-layer tamper-evidence; disposition of all nineteen obligations A–S; an eight-vector threat model; input-validation boundaries; and a 24-scenario security suite design. Five calls recorded under the standing authorization, four new requirements flagged, two disagreements left open for the human. | Standing authorization to build MVP1, `PROJECT_CONTEXT.md` Decisions Log 2026-07-31; gate 6 human review pending |
