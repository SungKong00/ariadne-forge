---
name: ariadne-workflow
description: Use when executing or reviewing Ariadne Forge repository work that changes files, makes a material technical decision, opens research, or coordinates Standard/Deep implementation or verification; routes Quick/Standard/Deep work, binds project documents, preserves physical phase ownership, and requires evidence-backed completion.
---

# Ariadne Workflow

Apply the smallest workflow that preserves evidence, ownership, and verification. Do not add ceremony to a settled Quick task. Do not let time pressure erase a Standard/Deep phase owner.

## 1. Bind the repository before acting

Read the nearest `AGENTS.md` and `docs/README.md`. For every mutation also read `docs/project.md` and `docs/operating-model.md`. Then load only what the repository map says applies:

- `docs/conventions/README.md` and the active convention for implementation or design
- `docs/architecture.md` and accepted decisions for boundaries or dependencies
- `docs/model-selection.md` and `docs/agent-orchestration.md` for Standard/Deep delegation
- the active execution plan when the task implements planned work

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

### Main control-proxy loop

1. Give the phase orchestrator the user outcome, completion contract, document binding, authority, budget, model binding, and forbidden scope.
2. Receive `DELEGATION_REQUEST` rather than inventing leaf contracts in main.
3. Check only safety, permission, overlapping writes, host capacity, dependencies, and secret exposure.
4. Spawn an initial wave of at most three independent leaves unless the phase orchestrator justifies another bounded wave and the host confirms capacity.
5. Enter every handle in a lifecycle ledger immediately. If a batch spawn partly fails, preserve known handles and reconcile before retrying.
6. Forward leaf packets to the same phase session without semantic selection or rewrite, except explicit safety redaction.
7. Let the phase orchestrator disposition packets and request one narrow follow-up where evidence requires it.
8. Treat a host-completed turn after `DELEGATION_REQUEST` as `HOST_TURN_DONE`, not phase completion.
9. Close leaves only after disposition. Close the phase session only after its final packet requests closure and raw evidence has no unresolved mismatch.

Use this minimum ledger:

```text
agent_ledger:
- handle:
- parent_phase:
- objective:
- dependencies:
- write_scope:
- status:
- stale_if:
- packet_disposition:
- close_status:
```

## 6. Follow the assigned session role

Determine the role from the explicit session contract. Do not self-promote between roles.

### Research Orchestrator

- Design independent source or risk lanes and their exact output contracts.
- Return `DELEGATION_REQUEST`; do not perform all leaf research yourself.
- Check packet relevance, authority, conflicts, contrary evidence, and unresolved assumptions.
- Use one conflict-only rebuttal round when a material claim would change the verdict.
- Require evidence for rebuttal; do not reward automatic resistance. Accept a criticism when a sound rebuttal cannot be supported.
- End with `RESEARCH_COMPLETE`, `INSUFFICIENT_EVIDENCE`, or `NEEDS_DECISION`.

### Implementation Orchestrator

- Divide the phase by dependency and disjoint write ownership.
- Request planner, worker, critic, or verifier leaves only when they provide independent value.
- Ensure plans cite requirements, project documents, conventions, research packets, and repository facts.
- Disposition criticism as `accepted`, `partially_accepted`, `rejected`, or `needs_evidence` with reasons.
- Require raw diff and command evidence before completion.
- End with `IMPLEMENTATION_COMPLETE`, `PARTIAL`, `BLOCKED`, or `NEEDS_DECISION`.

### Leaf

- Perform only the assigned bounded contract.
- Do not spawn descendants, make the parent phase decision, or widen write scope.
- Return a bounded evidence packet:

```text
role:
scope:
artifacts_checked:
facts:
risks:
uncertainties:
commands_run:
evidence_refs:
confidence:
recommended_verdict:
```

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
- mark stale evidence and unresolved mismatches
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

- Do not add a runtime, graph framework, hook, plugin, custom agent, or deterministic validator without an observed repeated failure that it directly solves.
- Do not assume Skill-to-Skill recursion, descendant spawn, automatic retry, cleanup, model binding, or context invisibility.
- Do not duplicate active project policy inside this package when a direct repository read is sufficient.
- Do not push, deploy, send external messages, or perform irreversible work without user authority.
- Do not expose secrets or private paths in prompts, packets, logs, or committed artifacts.
