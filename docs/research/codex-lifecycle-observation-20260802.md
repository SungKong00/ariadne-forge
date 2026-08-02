---
id: RESEARCH-CODEX-LIFECYCLE-OBSERVATION-20260802
kind: research-report
status: completed
authority: advisory-evidence
scope: codex-lifecycle-observation
owner: workflow-owner
checked_at: 2026-08-02
evidence_status: externally-source-backed-unimplemented-untested-locally
supersedes: null
aliases:
  - Codex lifecycle observation
  - App Server lifecycle evidence
  - subagent lifecycle limits
---

# Codex lifecycle observation evidence

## Decision question

What lifecycle conditions can Ariadne distinguish from current Codex product and
App Server evidence without inventing a global timeout policy, and what is the
smallest justified handoff for the existing Skill-first plan?

## Scope and non-scope

### Scope

- Official Codex subagent orchestration and App Server lifecycle evidence checked
  on 2026-08-02.
- Source evidence relevant to keeping host observation, contract currency,
  phase semantic disposition, evidence disposition, inspection trigger, and
  close disposition separate; the normative values remain project policy.
- Version and documentation drift relevant to a future App Server client.
- Project fit against `PLAN-0002`'s Skill-first, no-runtime default.

### Non-scope

- Defining Ariadne policy, a state-machine enum, timeout values, or a runtime.
- Changing `agent-orchestration.md`, configuring a custom agent, or implementing
  an App Server client.
- Claiming local App Server behavior, transport replay behavior, or fixture
  success. Those were not exercised here.
- Claiming an actual Research Orchestrator pilot, B10 run, paired run, or
  lifecycle behavior validation. This report preserves advisory source evidence
  only; no raw repository execution artifact supports those claims.

Official documentation describes Codex surfaces; it does **not** define
Ariadne policy. This report is advisory evidence for the document owner and
does not compete with its normative lifecycle contract.

## Evidence labels

| Label | Meaning |
|---|---|
| **App Server evidence: externally source-backed** | The bounded claims below are supported by the checked official docs or official repository snapshot. |
| **App Server evidence: unimplemented** | This repository has not added an App Server client, lifecycle runtime, schema consumer, or configuration for these observations. |
| **App Server evidence: untested locally** | No local App Server session, emitted event stream, recovery path, or generated installed-version schema was tested for this report. |

## Source plan and observations

The source plan used current official product documentation for supported
surface behavior, current official App Server documentation for public protocol
semantics, and a commit-pinned official repository snapshot for versioned type
details. Local observations remain separate from upstream claims.

| ID | Source | Tier | Checked version/date and locator | Direct support | Limitation |
|---|---|---:|---|---|---|
| O1 | [Codex Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 1 | Mutable page checked 2026-08-02; “Orchestration and thread controls”, “Managing subagents” | Product-level spawning, follow-up routing, waiting, result collection, and surface-dependent inspection/control | Product/UI documentation, not a direct public subagent RPC contract |
| O2 | [Codex App Server](https://learn.chatgpt.com/docs/app-server) | 1 | Mutable page checked 2026-08-02; message schema, thread status, turn events, approvals, unsubscribe | Installed-version schema generation, explicit wait/status and terminal-turn events, subscription close semantics | Exact payload prose can drift from generated main-branch types |
| O3 | [Generated App Server TypeScript schema at `1e85ca0`](https://github.com/openai/codex/tree/1e85ca099e4265bf89f4016772d299816e231bb3/codex-rs/app-server-protocol/schema/typescript) | 1 | `ClientRequest.ts`, `ServerRequest.ts`, `ServerNotification.ts`, and v2 item/status unions; inspected commit `1e85ca099e4265bf89f4016772d299816e231bb3` | Commit-scoped request and lifecycle vocabulary, including the inspected public client-request surface | Main-branch snapshot; not the installed CLI's wire schema by implication |
| O4 | [App Server v2 Rust protocol types at `1e85ca0`](https://github.com/openai/codex/tree/1e85ca099e4265bf89f4016772d299816e231bb3/codex-rs/app-server-protocol/src/protocol/v2) | 1 | `thread.rs`, `turn.rs`, `item.rs`, and [`notification.rs`](https://github.com/openai/codex/blob/1e85ca099e4265bf89f4016772d299816e231bb3/codex-rs/app-server-protocol/src/protocol/v2/notification.rs#L38-L48) | Commit-scoped terminal states, collab observations, and retriable-error meaning | Types do not provide a progress SLA, replay guarantee, or semantic workflow completion |
| L1 | Local command observation | 0 | `codex --version` on 2026-08-02: `codex-cli 0.144.1` | Installed local CLI version only | No generated schema was produced or compared; this version is **not equivalent** to the O3/O4 main schema |
| P1 | [`PLAN-0002`](../plans/active/0002-codex-native-skill-first-plan.md) | 0 | Current plan read 2026-08-02; current status and constraints | Skill-first architecture and explicit current runtime exclusion; future evidence-triggered reconsideration requires a separate decision and plan | It is an execution plan, not evidence of App Server behavior |

The source plan deliberately excludes community reports, third-party SDKs, and
unrun local protocol experiments. It preserves the repository rule that an
external source's existence or schema shape does not itself prove semantic
completion or local behavior.

## Claim matrix

| ID | Statement | Kind | Supporting sources | Status and applicability | Confidence / boundary |
|---|---|---|---|---|---|
| C1 | Codex product documentation describes orchestration that spawns subagents, routes follow-ups, waits for requested results, collects results, and closes agent threads. | fact | O1 | supported; product-level Codex/ChatGPT behavior | High; controls and directness vary by surface |
| C2 | App Server exposes explicit terminal turn outcomes through `turn/completed`: `completed`, `interrupted`, or `failed`. | fact | O2, O3, O4 | supported; App Server turn lifecycle | High; this is host-turn termination, not Ariadne phase completion |
| C3 | Known approval or user-input waits can be observed through loaded-thread status/active flags and corresponding server requests. | fact | O2, O3, O4 | supported; loaded App Server threads | High; an opted-out or disconnected client may need a fresh state read |
| C4 | No inspected official source gives elapsed event silence a failure, stall, interruption, or completion meaning. | fact about inspected sources | O2, O3, O4 | supported within the inspected source set | High; absence from the inspected contract is not a universal negative guarantee |
| C5 | In the inspected commit, an error notification can be retriable (`willRetry`); terminal turn failure requires the terminal failed status, not any error event. | fact | O3, O4 | supported for commit `1e85ca0` | High for that snapshot; O2's Errors prose does not document `willRetry` |
| C6 | The inspected `ClientRequest` union has no client-callable `spawnAgent`, `sendInput`, `wait`, `resumeAgent`, or `closeAgent` request. | fact | O3 | supported for the inspected public main-branch request union | High but deliberately narrow: not a permanent claim about every Codex version, surface, or private control |
| C7 | Item, turn, agent/collaboration operation, phase, and evidence completion are separate boundaries. | inference | O1–O4 | supported inference | High; native lifecycle types do not certify a higher-level evidence contract |
| C8 | `thread/closed` can be part of subscription/in-memory unloading after unsubscribe inactivity and does not itself establish task success or failure. | fact | O2 | supported; App Server resource lifecycle | High; not a semantic close-confirmation signal for an Ariadne phase |

## Documentation and schema drift

The live App Server page says that TypeScript and JSON Schema artifacts
generated by `codex app-server` are specific to the installed Codex version.
Accordingly, the locally observed `codex-cli 0.144.1` is recorded only as a
local version observation; it is not treated as the same schema as upstream
main commit `1e85ca099e4265bf89f4016772d299816e231bb3`.

The supplied official-source inspection also found a material documentation/type
drift: live item prose uses an older `collabToolCall` description while the
commit-pinned generated types use `collabAgentToolCall` and different field
shapes. Exact field names and parsers therefore require schemas generated by
the installed binary at the time an integration is actually built.

`willRetry` is another version-sensitive limit. The checked Rust protocol type
documents a retryable error as transient and non-interrupting, while the live
Errors documentation does not describe that field. This supports the bounded
warning not to equate every error event with terminal failure; it does not
authorize embedding `willRetry` as a stable Ariadne rule or assuming the field
exists identically in `0.144.1`.

## Limits that remain explicit

- **Silence meaning:** event absence cannot distinguish active reasoning, an
  internal hang, notification suppression, lost transport, or unreported work.
  No safe universal event-gap or stall threshold is established here.
- **Close confirmation:** a product request to close and App Server
  `thread/closed` are not a universal confirmation that a semantic phase closed;
  some surfaces may not expose a confirmation at all.
- **Replay and delivery:** no inspected source establishes end-to-end event
  replay or delivery guarantees after disconnection, restart, or unsubscribe.
- **Semantic completion:** `item/completed`, `turn/completed`, a Done label, or
  a final message cannot alone establish that the phase contract, raw evidence,
  and independent review are complete.
- **Installed-version schema:** no generated App Server schema from local
  `0.144.1` was inspected, so payload compatibility is unknown.
- **Direct-RPC claim scope:** C6 concerns only the public `ClientRequest` union
  at commit `1e85ca0`; it does not assert that no other release, host, or private
  integration can expose a direct subagent control.

## Adopted advisory claims

The following are suitable as evidence inputs for the normative owner, subject
to its own review; they are not policy adopted by this report.

- Explicit host signals can distinguish known waits and terminal turn outcomes
  from unexplained non-observation.
- A positive activity/status signal is evidence of observed host activity, but
  elapsed duration or high reasoning effort is not evidence of health,
  correctness, or progress.
- A checkpoint may justify inspection or diagnosis, but silence alone does not
  justify a native `STALLED`, `FAILED`, or `TIMED_OUT` conclusion.
- Host-turn completion is necessary evidence where a host turn is involved but
  remains insufficient for semantic phase or evidence completion.
- Retriable error and explicit terminal failure must remain distinct when the
  versioned host evidence exposes that distinction.

## Rejected overclaims

- “No event for *N* seconds/minutes means the agent failed, stalled, or timed
  out.”
- “Any error event means terminal failure.”
- “A completed turn, item, collab operation, or Done label proves Ariadne
  completion.”
- “`thread/closed` proves a phase was closed successfully or unsuccessfully.”
- “App Server provides public client RPCs named `spawnAgent`, `sendInput`,
  `wait`, `resumeAgent`, and `closeAgent`.”
- “The checked main schema is the schema of local `codex-cli 0.144.1`.”
- “Official documentation determines Ariadne's lifecycle policy.”

## Unknowns

- Event notification replay and delivery behavior after disconnect or restart.
- A universally safe cadence for progress, suspicion, or timeout.
- The installed App Server schema and any mapping from local CLI `0.144.1` to
  the inspected main-branch payload shape.
- Host-specific or private controls outside the inspected public contracts.
- Semantic misalignment and evidence sufficiency from lifecycle status alone.
- Close confirmation on surfaces that do not expose a dedicated confirmation.

## Project-fit handoff

`PLAN-0002` retains the applicable architecture decision: Codex SDK, Codex App
Server, OpenAI Agents SDK, LangGraph, and runtime observer·graph·state runtime
code, dependency, or configuration are explicitly excluded from the current
implementation. They are not active or deferred PLAN-0002 phases. Future
reconsideration requires newly observed material evidence and a separate
decision/plan. App Server source material may describe observable host events,
but it does not answer silence, semantic misalignment, phase completion, or
evidence sufficiency by itself.

For the owner of the bounded implementation phase, this report supports the
following review questions rather than prescribing a duplicate policy:

1. Keep one normative lifecycle owner and separate host observation, contract
   currency, phase semantic disposition, evidence disposition, inspection
   trigger, and close disposition.
2. Treat silence, elapsed time, wait timeout, or checkpoint arrival only as a
   possible inspection trigger, never as proof of failure, stall, interruption,
   completion, or deadline failure.
3. Preserve scope, handle, contract revision, source, and observed limitation
   whenever lifecycle evidence is recorded.
4. Add a narrowly discriminating fixture only if it tests a newly adopted
   distinction that existing B10/B11 artifacts cannot distinguish; do not claim
   that it validates universal host behavior.
5. Generate and inspect the installed-version schema before any future App
   Server parsing or direct-control assertion.

This leaf created only this advisory report. Registration in the docs index,
any normative lifecycle edit, and any fixture or plan change are outside this
leaf's writable scope and require their assigned owner.

## Confidence and revisit conditions

Confidence is high for the explicit, version-scoped product and protocol facts
in the claim matrix; confidence is deliberately limited for behavior not
observed locally. Recheck the mutable documentation and regenerate schemas when
an App Server integration is proposed, a host surface changes, an event-delivery
requirement appears, or a lifecycle claim would become normative.
