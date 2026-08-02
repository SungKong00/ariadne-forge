---
name: ariadne-workflow
description: Use when executing or reviewing Ariadne Forge repository work that changes files, makes a material technical decision, opens research, or coordinates Standard/Deep implementation or verification; routes Quick/Standard/Deep work, binds project documents, preserves physical phase ownership, and requires evidence-backed completion.
---

# Ariadne Workflow

Apply the smallest workflow that preserves evidence, ownership, and verification. Do not add ceremony to a settled Quick task. Do not let time pressure erase a Standard/Deep phase owner.

## 0. Identify role and control surface

Use the explicit session contract to identify exactly one role:

- **main/control proxy**: receives the user outcome and can use host multi-agent controls
- **Research Orchestrator** or **Implementation Orchestrator**: owns one physical phase session
- **leaf**: performs one bounded contract and returns evidence

Default to main only when handling the user request directly. Do not let a child session self-promote to main because its parent is not visible.

The first gate is mandatory. Before repo-wide search, broad document loading, planning, mutation, or delegation, inspect the current role and whether the current Codex host surface natively exposes tracked controls equivalent to spawn, send/continue, wait, and close. Record:

```text
role_control_preflight:
- assigned_role: main | research-orchestrator | implementation-orchestrator | leaf | ambiguous
- host_controls: available | unavailable | partial | unobservable
- provisional_route: Quick | Standard | Deep | unresolved
- allowed_next_read:
```

Until this receipt exists, the only repository reads allowed are the nearest `AGENTS.md`, `docs/README.md`, and `docs/operating-model.md`. Do not recursively inventory the repository or read the full plan/research set during preflight.

Shell-launching `codex exec`, another CLI session, Harness Maestro, or an ad hoc process does not count as native host control. Do not inspect or start those as a fallback unless the user explicitly authorizes that different execution surface.

If the request is plausibly Standard/Deep and needs a phase owner but this session has no full host controls and is not explicitly assigned as a phase orchestrator or leaf, return immediately:

```text
HOST_CONTROL_REQUIRED:
- provisional_route:
- required_phase: research | implementation
- phase_order_and_dependency:
- reason:
- minimum_documents_checked:
- no_mutation_performed: true
```

Do not exhaustively research, design, or mutate while waiting for a physical phase owner.

## 1. Bind the repository before acting

Main and phase orchestrators read the nearest `AGENTS.md` and `docs/README.md`. For every mutation phase also bind `docs/project.md` and `docs/operating-model.md`. Then load only what the repository map says applies:

- `docs/conventions/README.md` and the active convention for implementation or design
- `docs/architecture.md` and accepted decisions for boundaries or dependencies
- `docs/model-selection.md` and `docs/agent-orchestration.md` for Standard/Deep delegation
- the active execution plan when the task implements planned work

A leaf reads the nearest applicable `AGENTS.md`, the exact documents named in its parent contract, and the target artifacts. It does not reload the whole global document set unless the contract is missing, stale, or conflicting. Report that gap instead of silently filling it.

Before mutation, record this compact receipt in working notes or commentary:

```text
document_binding:
- documents_read:
- applicable_scope:
- missing_stale_or_conflicting:
- resolution_action:
```

Do not infer that a document was understood merely because an output happens to comply. Stop with `NEEDS_DECISION` when equal-authority applicable documents conflict.

## 2. Declare completion and scope

Write the minimum contract before implementation or delegation:

```text
completion_contract:
- outcome:
- verification:
- writable_scope:
- forbidden_scope:
- constraints:
- stop_when:
```

For a one-step read-only answer, this may be one sentence. For Standard/Deep work, every field is required. Existing unrelated changes remain outside writable scope.

## 3. Route adaptively

Use repository definitions from `docs/operating-model.md`; do not classify by keywords alone.

- **Quick**: bounded, reversible, strong oracle, no material unresolved decision. Work directly, follow applicable conventions, verify, and report.
- **Standard**: multiple interacting files or rules, a meaningful design choice, or independent verification value.
- **Deep**: architecture conflict, broad research synthesis, high-risk effect, weak oracle, or expensive rework.

Record:

```text
route_receipt:
- route: Quick | Standard | Deep
- evidence_for_route:
- research_now: yes | no
- research_rationale:
- escalate_if:
```

Re-evaluate at plan exit, when an implementation assumption changes, and when verification disagrees. The open research question is:

> Is there an unrecorded premise that would invalidate or substantially rework downstream work if it is wrong?

## 4. Execute Quick work directly

For Quick work:

1. Apply the nearest active convention.
2. Make the smallest scoped change.
3. Run the strongest proportionate oracle.
4. Check material decisions and document impact.
5. Return `IMPLEMENTED`, `PARTIAL`, `BLOCKED`, or `NEEDS_DECISION` with direct evidence.

Do not spawn agents or open external research merely to make the work appear rigorous.

## 5. Open physical phase owners for Standard/Deep

The invoking main is the cross-phase decision owner and host-control proxy. It must not absorb research or implementation phase ownership.

Before research leaf work, open a physical **Research Orchestrator session**. Before implementation planning, worker allocation, or phase verification, open a physical **Implementation Orchestrator session**. Bind this Skill explicitly to the session when the surface supports Skill injection.

Open only the next dependency-ready phase. If research evidence can change implementation requirements, architecture, convention, or technology choice, run Research first. Do not open dependent Implementation until main has independently inspected the Research artifacts, recorded `EVIDENCE_COMPLETE`, and sent that receipt to the same Research Orchestrator. `RESEARCH_COMPLETE` alone is not the dependency gate, and close confirmation is a separate control outcome. A request to parallelize dependent phases does not remove this barrier.

Record before any leaf spawn or Standard/Deep mutation:

```text
phase_owner_receipt:
- phase: research | implementation
- session_handle:
- decision_owner:
- control_proxy:
- skill_binding: verified | unavailable | ambiguous | unobservable
- initial_leaf_limit: 3
- host_feasibility:
```

If the current surface cannot open or continue the required physical phase session, return `NEEDS_DECISION` or `BLOCKED`; do not silently let main perform the phase.

### Direction Review adapter

When an applicable phase needs to ask whether a plan would solve the user outcome, use the sole
Direction Review policy in [`docs/operating-model.md`](../../../docs/operating-model.md#direction-review)
and the ad hoc leaf/context/transport contract in
[`docs/agent-orchestration.md`](../../../docs/agent-orchestration.md#direction-reviewer-ad-hoc-read-only-leaf).
Route the returned packet to the owning phase Orchestrator before dependent implementation work; do
not duplicate or reinterpret the policy here.

### Lifecycle adapter

[`docs/agent-orchestration.md` §6](../../../docs/agent-orchestration.md#6-실행-생명주기) is the sole normative owner of lifecycle classification and closure. This section is only its compact operational adapter; do not recreate the normative table here.

- Derive host observation only from current evidence correlated to the handle. Use `ACTIVE_OBSERVED` only for an explicit nonterminal host status or event. Use `WAITING_KNOWN(reason, owner, resume_condition)` only when all three values are known; represent `NEEDS_INPUT` as this temporary wait, never as a terminal verdict. With no current correlated signal or no exposed status/control, use `UNOBSERVABLE`.
- Treat `CHECKPOINT_DUE` only as a request to inspect and diagnose. When the contract permits inspection, silence, checkpoint arrival, elapsed time, or a wait timeout can produce only `CHECKPOINT_DUE`; they never prove failed, stalled, interrupted, completed, or deadline failure. An unscoped error or interruption also does not justify a stronger host observation.
- Record `TERMINAL_HOST(completed | failed | interrupted)` only from an explicit correlated terminal signal, preserving its `spawn / item / turn / agent / session` scope and any observable retryability. Do not collapse retriable or nonterminal errors into terminal failure.
- Keep six dimensions separate: host observation; contract currency (`CURRENT | STALE`); phase semantic disposition; evidence disposition (`INCOMPLETE | EVIDENCE_COMPLETE`); inspection trigger (`none | CHECKPOINT_DUE`); and close disposition (`none | CLOSE_REQUESTED | CLOSE_CONFIRMED | CLOSE_UNOBSERVABLE`). A value in one dimension never decides another.
- `CHECKPOINT_DUE` is the only inspection/control marker. `NEEDS_INPUT` is normalized to a known wait, `EVIDENCE_MISMATCH` is an evidence finding returned to the owner while evidence stays `INCOMPLETE`, phase packets occupy phase semantic disposition, and `CLOSE_*` values occupy close disposition.
- Keep host completion, an explicit `RESEARCH_COMPLETE` or `IMPLEMENTATION_COMPLETE` phase packet, and `EVIDENCE_COMPLETE` distinct. After the phase packet, main independently inspects material raw artifacts in their current state and command evidence, mismatch resolution, fresh independent review, and Document Impact before recording `EVIDENCE_COMPLETE`.
- Follow the canonical close sequence: the phase owner emits the phase-complete packet without close authorization; main records and sends the `EVIDENCE_COMPLETE` receipt to that same owner; the owner then emits a separate `CLOSE_REQUESTED`; main invokes host close and records `CLOSE_CONFIRMED` or `CLOSE_UNOBSERVABLE` from actual host evidence. Close disposition does not gate dependent Implementation once Research evidence is complete.

### Two-channel leaf handoff adapter

[`docs/agent-orchestration.md` §5 “Two-channel owner-leaf handoff”](../../../docs/agent-orchestration.md#two-channel-owner-leaf-handoff) is the sole normative owner. Apply it as a behavioral contract, not hard output enforcement or direct agent-to-agent transport.

- A leaf returns only the short `LEAF_TRANSPORT_PACKET`; long evidence stays in an `EVIDENCE_ARTIFACT` identified by locator. Read-only leaves may create one only through an explicit narrow artifact sink.
- Main correlates and forwards the packet verbatim to its named parent, except marked safety redaction. Do not routinely open, select, repair, rewrite, or normalize the artifact during transport.
- The owning phase Orchestrator opens and dispositions the artifact. At final `EVIDENCE_COMPLETE`, main opens only material locators required for independent verification.
- Missing or mismatched identity, inaccessible or stale artifact evidence, inline long evidence, or out-of-scope writes remain `INCOMPLETE`; report `CONTRACT_VIOLATION` to the same owner instead of repairing the packet.

### Main control-proxy loop

1. Give the phase orchestrator the user outcome, completion contract, document binding, authority, budget, model binding, and forbidden scope.
2. Receive `DELEGATION_REQUEST` rather than inventing leaf contracts in main.
3. Check only safety, permission, overlapping writes, host capacity, dependencies, and secret exposure.
4. Spawn an initial wave of at most three independent leaves unless the phase orchestrator justifies another bounded wave and the host confirms capacity.
5. Enter every handle in a lifecycle ledger immediately. If a batch spawn partly fails, preserve known handles and reconcile before retrying.
6. Correlate and forward each `LEAF_TRANSPORT_PACKET` to its named phase session without semantic selection or rewrite, except explicit safety redaction; do not routinely open its artifact.
7. Let the phase orchestrator disposition packets and request one narrow follow-up where evidence requires it.
8. Record a host-completed turn after `DELEGATION_REQUEST` only as turn-scoped `TERMINAL_HOST(completed)`; it is not a phase semantic packet or `EVIDENCE_COMPLETE`.
9. After a phase-complete packet without close authorization, independently inspect only the material locators needed to verify raw evidence. Return `EVIDENCE_MISMATCH` to the same owner while evidence stays `INCOMPLETE`, or record and send an `EVIDENCE_COMPLETE` receipt.
10. After that receipt, accept a separate `CLOSE_REQUESTED` from the same owner, invoke host close, and record `CLOSE_CONFIRMED` or `CLOSE_UNOBSERVABLE` from the actual response or observation limit.
11. Open dependent Implementation on Research `EVIDENCE_COMPLETE`; do not substitute `RESEARCH_COMPLETE` or wait for close confirmation.

Use this minimum ledger:

```text
agent_ledger:
- handle:
- parent_phase:
- objective:
- dependencies:
- write_scope:
- contract_revision:
- stale_if:
- host_observation:
- observation_source_and_evidence:
- last_observed:
- limitation:
- terminal_scope_outcome_and_retryability:
- contract_currency: CURRENT | STALE
- phase_disposition: NONE_RECORDED | RESEARCH_COMPLETE | IMPLEMENTATION_COMPLETE | INSUFFICIENT_EVIDENCE | PARTIAL | BLOCKED | NEEDS_DECISION | SESSION_FAILED
- evidence_disposition: INCOMPLETE | EVIDENCE_COMPLETE
- packet_disposition:
- inspection_trigger: none | CHECKPOINT_DUE
- close_disposition: none | CLOSE_REQUESTED | CLOSE_CONFIRMED | CLOSE_UNOBSERVABLE
```

## 6. Follow the assigned session role

Determine the role from the explicit session contract. Do not self-promote between roles.

### Research Orchestrator

- Design independent source or risk lanes and their exact output contracts.
- Return `DELEGATION_REQUEST`; do not perform all leaf research yourself.
- Check packet relevance, authority, conflicts, contrary evidence, and unresolved assumptions.
- Use one conflict-only rebuttal round when a material claim would change the verdict.
- Require evidence for rebuttal; do not reward automatic resistance. Accept a criticism when a sound rebuttal cannot be supported.
- End the semantic phase with `RESEARCH_COMPLETE`, `INSUFFICIENT_EVIDENCE`, or `NEEDS_DECISION`. A `RESEARCH_COMPLETE` packet does not include close authorization; remain available for the main's evidence receipt or mismatch notice.

### Implementation Orchestrator

- Divide the phase by dependency and disjoint write ownership.
- Request planner, worker, critic, or verifier leaves only when they provide independent value.
- Ensure plans cite requirements, project documents, conventions, research packets, and repository facts.
- Disposition criticism as `accepted`, `partially_accepted`, `rejected`, or `needs_evidence` with reasons.
- Require raw diff and command evidence before completion.
- End the semantic phase with `IMPLEMENTATION_COMPLETE`, `PARTIAL`, `BLOCKED`, or `NEEDS_DECISION`. An `IMPLEMENTATION_COMPLETE` packet does not include close authorization; remain available for the main's evidence receipt or mismatch notice.

### Leaf

- Perform only the assigned bounded contract.
- Do not spawn descendants, make the parent phase decision, or widen write scope.
- Return only the short `LEAF_TRANSPORT_PACKET` defined by the canonical [two-channel handoff](../../../docs/agent-orchestration.md#two-channel-owner-leaf-handoff). Put long evidence in its authorized artifact sink or reference existing evidence; return `BLOCKED` if neither is available.

## 7. Audit material decisions

A material decision changes architecture, dependencies, public behavior, security, data, conventions, workflow ownership, or costly downstream work. Before adopting one, write:

```text
material_decision:
- decision:
- consequence_if_wrong:
- supporting_evidence:
- authority_and_freshness:
- viable_alternative:
- contrary_evidence_or_unknown:
- verification_or_revisit_trigger:
```

Inference may connect evidence to a decision, but inference alone is not external or repository evidence. Unsupported claims remain questions. Critic consensus is not correctness.

Before phase completion, ask a fresh-context reviewer or verifier to check whether any material decision lacks this record. If independent review is unavailable, mark the audit `unvalidated` rather than simulating independence.

## 8. Verify and close

Prefer raw artifacts over worker summaries:

- inspect the actual diff and writable scope
- run targeted tests, lint, build, browser, or source read-back that proves the claim
- compare reported exit status with raw output
- mark stale evidence and return every raw-evidence mismatch to the owning phase orchestrator for revised disposition
- require fresh independent review before `EVIDENCE_COMPLETE`; if unavailable, keep evidence `INCOMPLETE`
- decide document impact as `update`, `create`, `unchanged`, or `supersede`

Return a final packet:

```text
verdict: IMPLEMENTED | PARTIAL | BLOCKED | NEEDS_DECISION
artifacts_changed:
verification:
material_decisions_and_evidence:
phase_packets:
document_impact:
remaining_risks:
```

Static package checks do not prove behavior. Do not call this Skill `VALIDATED` until paired no-Skill/with-Skill forward tests and an independent completion review pass.

## Hard guardrails

- This implementation explicitly excludes Codex SDK, Codex App Server, OpenAI Agents SDK, LangGraph, and any runtime observer, graph, state runtime, runtime code, dependency, or configuration. Future reconsideration requires new direct evidence and a new decision/plan; it is not an active or deferred PLAN-0002 phase.
- Do not add a runtime, graph framework, hook, plugin, custom agent, or deterministic validator without an observed repeated failure that it directly solves.
- Do not assume Skill-to-Skill recursion, descendant spawn, automatic retry, cleanup, model binding, or context invisibility.
- Do not duplicate active project policy inside this package when a direct repository read is sufficient.
- Do not push, deploy, send external messages, or perform irreversible work without user authority.
- Do not expose secrets or private paths in prompts, packets, logs, or committed artifacts.
