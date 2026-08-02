---
id: PLAN-0003
kind: execution-plan
status: completed
authority: execution
scope: ariadne-skill-composition
owner: project-owner
last_verified: 2026-08-02
supersedes: null
related_plan: PLAN-0002
behavior_status: historical-partial-candidate-execution
evaluation_contract: ../../../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md
---

# `reference-research-team` 명시적 embedded-method 후보 계획

## 문서 상태

이 문서는 [`PLAN-0002`](../active/0002-codex-native-skill-first-plan.md)의 current
architecture를 바꾸지 않는 bounded candidate plan이다. Identity-only W0-R3의 exact bytes에는
independent V0 `FREEZE` receipt가 기록됐고 W0-R2 receipt는 non-executable superseded history다.
W0-R3 freeze receipt는 결과가 아니라 frozen oracle identity다. W2의 partial candidate execution은
required termination으로 끝났으며, 이 draft는 그 disposition을 보존하는 historical record이지
matrix를 재개하라는 active instruction이 아니다.

```yaml
status: HISTORICAL_PARTIAL_CANDIDATE_EXECUTION
current_plan: PLAN-0002 remains active
candidate_a: preserved baseline; no immediate subject session
candidate_b: explicit embedded-method historical candidate execution
strict_a_b_skill_effect: NOT_ISOLATABLE on current host
execution_record: evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/run-record.md
execution_matrix: B/F1 owner PASS; B/F2 second owner PASS; B/F3 owner FAIL; B/F4 and two mode smokes NOT_RUN due required termination
downstream: grader, verifier, held-out smoke, and bridge writer not launched; bridge_added false
independent_w2_grade: none
model_comparison: not claimed
contract_path: evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md
contract_revision: W0-R3
contract_freeze_state: FROZEN_ON_V0_RECEIPT
freeze_receipt: independent V0 FREEZE
oracle_revision: sha256:89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285
source_set_digest: sha256:a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
source_set_scope: implemented ten-file identity; not whole-package or source-semantics proof
identity_only_diff: verified
v1_static_implementation: accepted
superseded_oracle_receipt: W0-R2 sha256:6890421241774922b3b8bf4f70cb87db5b743ba3759b3cd36717e365638d62d0; non-executable history
canonical_blocks: 23 exact/matching; 19 R2-unaffected payloads byte-identical
frozen_oracle_results: NOT_RUN
claim_boundary: no compatibility, adoption, effect, or model claim
next_action: no matrix-resumption instruction; any future work requires a newly authorized plan
```

The remaining candidate-design and matrix text is retained for historical traceability only. It does
not authorize a rerun, new evidence collection, a frozen-contract rewrite, or an append-only
run-record rewrite.

## 결정 요약

후보 B의 목표 topology는 유지한다.

```text
Main (control_proxy)
  -> one physical Ariadne Research Orchestrator (semantic_owner)
     + ariadne-workflow role contract
     + explicit reference-research-team embedded-method
  <- DELEGATION_REQUEST
Main performs requested host controls
embedded method returns research_packet_v4 to the same owner only
Research Orchestrator owns synthesis and research-phase disposition
```

하지만 current Codex Desktop multi-agent host에서는 cwd가 repository이고 subject의 oracle
filesystem 접근 가능성을 제거할 수 없다. Direct oracle read는 invalidation할 수 있지만 읽지
않았다는 absence는 증명할 수 없다. 따라서 strict A/B Skill-effect는 `NOT_ISOLATABLE`이며,
현재 immediate matrix에는 A session을 넣지 않는다.

- **A**: PLAN-0002 baseline으로 보존하되 current host에서는 실행하지 않는다.
- **B**: same owner + explicit `reference-research-team` `embedded-method`; compatibility candidate다.
- **C**: 두 번째 research orchestrator/session은 ownership 중복 때문에 reject한다.
- **D**: 범용 연구 규칙의 Ariadne 복사는 drift와 중복 때문에 reject한다.
- **E**: 기존 1-vs-3 Ariadne package 분리는 역사적 후속 선택지로 defer한다.
- custom agent도 반복 역할·comparison evidence 전까지 defer한다.
- runtime, Codex SDK, Codex App Server integration, OpenAI Agents SDK, LangGraph, hook,
  plugin과 state/graph observer는 current plan에서 제외한다.

## Historical completion contract (non-authorizing)

The following W0 completion, verification, constraint, boundary, and stop language records the
frozen candidate design. It is not current permission to execute or resume any session.

### Outcome

Accepted V0 correction에 맞춰 subject-visible role/prompt/binding과 runner-only oracle을
canonical byte blocks로 분리한 historical candidate execution과 its termination boundary를 정확히
기록한다.

### Verification

- evaluation contract의 23 canonical blocks를 documented convention으로 추출한다.
- 각 block의 `block_id`, begin/end marker, byte length와 SHA-256 manifest를 독립 두 방법으로
  재계산한다.
- F2–F4 subject prompts에 expected disposition, rubric 또는 rebuttal outcome이 없는지 읽는다.
- fixed Desktop/repository/Sol-high/inherited-permission envelope와 six-session matrix를 대조한다.
- exact write scope와 `git diff --check`를 확인한다.
- 이 documentation disposition에서 experiment rerun, 새 evidence, A subject, model comparison 또는
  result claim을 만들지 않는다.

### Constraints

- physical Research Orchestrator는 정확히 1명이고 semantic owner다.
- Main만 control proxy다.
- embedded method는 `spawn`, `send/continue`, `wait`, `stop`, `close`를 수행하거나 소유하지
  않는다.
- method output은 `research_packet_v4`로 같은 owner에게만 간다.
- B compatibility grading에는 unique resolved identity + matching `source_set_digest`와
  direct instruction-read observation이 모두 필요하다.
- causal assurance는 `behavioral_only | unobservable`로 별도 기록하며 compatibility를
  자동 차단하지 않지만 Skill-effect claim은 절대 지지하지 않는다.
- F4 instruction-read-unobservable subcase는 read receipt가 없으므로 fail closed한다.
- unsupported F4 host state는 synthetic product behavior로 만들지 않고 `NOT_ISOLATABLE`이다.
- requested model/effort와 actual values를 분리하고 actual이 보이지 않으면
  `unobservable`로 기록한다.
- same-name Skill candidates는 merge하지 않고 deterministic precedence를 발명하지 않는다.
- implemented ten-file digest는 whole package나 source semantics가 아니라 `source_set_digest`다.
- App Server 공식 claim은 App Server scope로 제한한다.

### Historical W0 boundaries (non-authorizing)

Historical W0 writable scope:

- `docs/plans/drafts/0003-explicit-skill-composition-draft.md`
- `docs/README.md`
- `evals/ariadne-workflow/README.md`
- `evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md`

금지:

- global `reference-research-team`과 repo `ariadne-workflow` 수정
- run record, schema, script, runtime, config, production code
- PLAN-0002, architecture, operating/model/agent policy, ADR, convention 변경
- behavior session, A/B comparison, model comparison, commit, push, deploy, external message

### Historical W0 stop conditions (non-authorizing)

- `FREEZE_RECEIPT_RECORDED`: 23 block manifest가 두 extraction에서 정확히 일치하고
  independent external V0 SHA-256 receipt가 기록됨
- `RECEIPT_MISMATCH`: runner가 session 전 다시 계산한 exact contract SHA-256이 receipt와 다름
- `BLOCKED`: mismatch가 해소되기 전 behavior session을 시작할 수 없음

## Document Binding

| 문서·자료 | 적용 이유 | 상태 | 이 plan의 사용 |
|---|---|---|---|
| [`../../project.md`](../../project.md) | evidence traceability, low maintenance | active | no runtime·no overclaim |
| [`../../architecture.md`](../../architecture.md) | one owner, Main proxy, runtime exclusion | active | B topology boundary |
| [`../../operating-model.md`](../../operating-model.md) | authority, evidence, semantic read-back | active | claim and completion boundary |
| [`../../model-selection.md`](../../model-selection.md) | requested/actual split, model comparison isolation | active; behavior unvalidated | fixed run request, no calibration claim |
| [`../../agent-orchestration.md`](../../agent-orchestration.md) | physical owner and lifecycle controls | active; behavior unvalidated | Main-only control proxy |
| [`../../conventions/README.md`](../../conventions/README.md) | draft/candidate lifecycle | active | non-authoritative status |
| [`../../decisions/0001-codex-native-skill-first.md`](../../decisions/0001-codex-native-skill-first.md) | single-Skill baseline and runtime exclusion | accepted | A preserved |
| [`../active/0002-codex-native-skill-first-plan.md`](../active/0002-codex-native-skill-first-plan.md) | current execution authority | active; partial/static-only | exact A baseline |
| [`contract.md`](../../../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md) | canonical blocks, six-session matrix, hidden oracle | W0-R3; `FROZEN_ON_V0_RECEIPT`; `NOT_RUN` is frozen oracle state | sole frozen experiment contract |
| [`run-record.md`](../../../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/run-record.md) | raw W2 candidate execution and required termination | append-only advisory evidence | sole current execution-status locator; no independent grade |
| installed `reference-research-team` source set | method/source/checker facts | read-only; repo authority 아님 | B identity input only |

Missing/stale/conflicting: accepted V0 correction supersedes this draft's prior 8+2 A/B execution
shape. No equal-authority repository conflict remains.

## Subject/runner separation

The contract defines four independent context classes.

| class | subject visibility | purpose |
|---|---|---|
| `subject_prompt` | visible | realistic research request |
| `subject_role_contract` | visible | real role, owner, control and output limits |
| `subject_skill_binding` | visible where applicable | actual Skill name/mode/source-set method boundary |
| `runner_only_oracle` | hidden by contract | expected predicates, invalidation and grading |

Subjects do not receive fixture/variant label, expected verdict, rubric, rebuttal outcome or another
session's output. Repository cwd means oracle filesystem exclusion is not enforceable. A direct read
invalidates the session; absence of a read remains unprovable and must be reported.

## Candidate manifest

### A — deferred PLAN-0002 baseline

- physical Research Orchestrator: 1
- semantic owner: Ariadne Research Orchestrator
- control proxy: Main
- external research method: none
- immediate subject session: none
- reason: strict A/B Skill-effect is `NOT_ISOLATABLE` on current host

The exact deferred role contract remains a canonical block so A can be carried to a future isolated
surface without reconstructing it from B output.

### B — historical compatibility candidate (non-authorizing)

- physical Research Orchestrator: 1
- semantic owner: Ariadne Research Orchestrator
- control proxy: Main
- Skill: explicit `reference-research-team`, mode `embedded-method`, required
- identity: exactly one resolved installed path + matching implemented ten-file `source_set_digest`
- instruction read: direct observation required
- causal assurance: `behavioral_only | unobservable`; non-blocking for compatibility grading and
  unusable for Skill-effect claim
- method route: `research_packet_v4` to same owner only
- method host controls: `spawn`, `send/continue`, `wait`, `stop`, `close` forbidden
- direct descendant/session creation and phase/project/user verdict: forbidden
- binding gap: fail closed without silent A fallback or second owner

## Historical fixed run envelope (non-authorizing)

| field | fixed value |
|---|---|
| surface | current Codex Desktop multi-agent host |
| cwd | Ariadne repository root; not isolation |
| model request | `FRONTIER`, `gpt-5.6-sol`, `high` |
| actual model/effort | observed value or `unobservable` |
| permission | inherited; no per-spawn override |
| read-only | instruction-only; pre/post Git receipt required |
| tools | record actual exposed and used tools |
| retry | no automatic retry |
| budget | 20 minutes/session; expiry is checkpoint, not terminal failure |
| lane/wave | initial lane 1, initial leaves maximum 3 |
| follow-up | material-conflict follow-up maximum 1 |
| input | exact frozen canonical blocks only |
| oracle exclusion | not preventable from repository cwd |

This was not a model allocation experiment. Every session used the same requested configuration and
recorded actual values only when observable; the envelope is retained as history, not execution
authorization.

## Historical six-session compatibility-only matrix (non-authorizing)

| session | input shape | status |
|---|---|---|
| B/F1 | B role + B binding + official locator prompt/input | W2 recorded candidate execution; Implementation Orchestrator disposition `PASS` |
| B/F2 | B role + B binding + official/repository conflict prompt/input | W2 recorded candidate execution; second Implementation Orchestrator disposition `PASS` |
| B/F3 | B role + B binding + high-risk architecture prompt/input | W2 recorded candidate execution; Implementation Orchestrator disposition `FAIL` |
| B/F4 | B role + B binding + four binding-condition subcases | `NOT_RUN` due required termination; no behavior disposition |
| standalone-owner | standalone role/prompt + official source card | `NOT_RUN` due required termination; no behavior disposition |
| source-leaf | bounded leaf role/prompt + one official source card | `NOT_RUN` due required termination; no behavior disposition |

The planned total was **6 sessions**; W2 terminated after B/F3. No A session or model-comparison
session is recorded. The owner dispositions above are not an independent W2 grade and authorize no
compatibility, adoption, effect, or model claim.

## Fixture identity and F4 boundary

F1–F4 identities stay fixed:

- F1 simple official docs locator
- F2 official docs vs representative repository conflict
- F3 high-risk architecture with critic findings
- F4 missing Skill, duplicate name/path, instruction-read unobservable, embedded verdict/control theft

F2–F4 subject prompts are realistic requests and contain no expected disposition. Expected behavior
lives only in `RUNNER_ONLY_ORACLE_R1`.

F4 canonical inputs are requested host conditions, not fake observations. Runner must not create or
edit Skills, catalog records, read receipts, method output or host events to force a subcase. If the
current host cannot expose a subcase with correlated raw evidence, that subcase is
`NOT_ISOLATABLE`, not observed product behavior.

## Canonical blocks and source-set identity

The contract owns 23 canonical blocks and documents exact extraction boundaries. Each manifest entry
contains:

- `block_id`
- exact begin marker
- exact end marker
- UTF-8 payload byte length
- SHA-256

W0 uses two independent extraction implementations and no new script. Subject context is assembled
only from the exact prompt, role, binding and input blocks listed for that session. Runner envelope,
oracle and invalidation blocks never enter subject context.

The pinned digest is named `source_set_digest` because it covers exactly ten read-only files:
`SKILL.md`, seven Markdown references, one JSON schema and the existing checker. It is not a whole
package digest and does not cover unrelated package files.

## Checker boundary

The existing checker may only be called **“structural and limited cross-field/referential checker.”**
Its output does not prove that a source supports a claim. Semantic source read-back is independent.
No semantic validator or source-integrity checker is introduced or claimed.

## Options disposition

| option | disposition | reason |
|---|---|---|
| A. PLAN-0002 Ariadne only | preserve, no immediate run | baseline remains authoritative; effect not isolatable |
| B. same owner + embedded method | unvalidated compatibility candidate | smallest method-injection shape preserving ownership |
| C. second research-team orchestrator | reject | duplicate semantic owner |
| D. copy method into Ariadne | reject | duplicated source policy and drift |
| E. 1-vs-3 Ariadne package split | defer | larger package/trigger/binding surface |
| custom agent | defer | no repeated role/calibration evidence |
| runtime/SDK/App Server integration/LangGraph | exclude | current architecture and plan boundary |

## Option E history

The earlier PLAN-0003 compared:

```text
ariadne-workflow
ariadne-research-session
ariadne-implementation-session
```

This 1-vs-3 idea remains deferred Option E. It is not removed or adopted. Reopen requires repeated
entry-Skill responsibility failures or a separately authorized held-out package comparison. Current B
does not create any new Ariadne Skill package.

## Execution phases

### Phase 0 — W0 V0 correction (complete)

This phase updated only the four owned documents, independently verified the canonical block
manifests, and produced W0-R2 with 23 matching canonical blocks. Its receipt is retained only as
superseded, non-executable history. No behavior runs.

### Phase 1 — independent V0 freeze receipt (complete)

Independent V0 recorded a superseding `FREEZE` for exact identity-only W0-R3 bytes at
`sha256:89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285`. The
`identity_only_diff` is verified, all 23 canonical blocks match their manifest, all 19 unaffected
payloads are byte-identical to R2, and the V1 static implementation is accepted. Its implemented
ten-file `source_set_digest` is
`sha256:a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8`. Behavior writer cannot
edit the contract.

### Phase 2 — W2 candidate execution (terminated)

[`run-record.md`](../../../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/run-record.md)
is the canonical raw execution locator. It records B/F1 Implementation Orchestrator `PASS`, B/F2
second `PASS` after an initial incomplete receipt, and B/F3 `FAIL` for role-boundary violations. The
correction/quarantine did not make B/F3 conforming. Required termination left B/F4, standalone-owner
smoke, and source-leaf smoke `NOT_RUN`; they have no behavior `PASS`/`FAIL` disposition. No A or
model-comparison session is recorded.

### Phase 3 — downstream review (not launched)

Required termination prevented the grader, verifier, held-out smoke, and bridge writer from being
launched. `bridge_added: false`; no bridge, independent W2 grade, compatibility, adoption, effect,
or model claim exists. Structural checking never substitutes for such review.

## Material decision record

### Strict A/B effect is not isolatable on current host

- basis: accepted V0 packet; repository cwd; oracle filesystem exclusion not enforceable
- consequence: no immediate A subject and no effect claim
- limitation: direct oracle read can be detected, absence cannot be proved
- revisit: future host/workspace with enforceable oracle exclusion and equivalent A/B binding controls

### B compatibility needs identity plus instruction read

- basis: accepted V0 packet and configured-vs-actual evidence principle
- consequence: name/path/digest alone cannot authorize grading
- limitation: current Desktop read receipt may be unobservable
- causal boundary: behavioral/unobservable causal assurance cannot support effect

### F4 unsupported states are not simulated

- basis: accepted V0 packet and product-fact evidence rule
- consequence: unexposed subcases are `NOT_ISOLATABLE`
- alternative rejected: synthetic catalog/event/method output presented as current host behavior

## Document Impact

| document/artifact | disposition | reason |
|---|---|---|
| `PLAN-0003` | update | distinguish W0-R3 frozen receipt from W2 terminated execution |
| evaluation `contract.md` | unchanged | frozen W0-R3 oracle bytes preserved |
| `run-record.md` | unchanged | append-only W2 raw execution evidence preserved |
| `evals/ariadne-workflow/README.md` | update | current registry points to frozen oracle and W2 record separately |
| `docs/README.md` | update | same concise registry reconciliation |
| `docs/operating-model.md` | update | sole normative Direction Review policy owner |
| `docs/agent-orchestration.md` | update | read-only Direction Reviewer leaf and two-channel routing only |
| `.agents/skills/ariadne-workflow/SKILL.md` | update | compact Direction Review routing adapter only |
| PLAN-0002 and other normative docs | unchanged | candidate remains non-authoritative |
| global/repo Skills | unchanged | exact forbidden scope |
| schema, script, runtime/config | not created or changed | no new validation machinery |

## Current disposition

```yaml
verdict: HISTORICAL_PARTIAL_CANDIDATE_EXECUTION
contract_path: evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md
contract_revision: W0-R3
contract_freeze_state: FROZEN_ON_V0_RECEIPT
freeze_receipt: independent V0 FREEZE
oracle_revision: sha256:89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285
source_set_digest: sha256:a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
source_set_scope: implemented ten-file identity; not whole-package or source-semantics proof
identity_only_diff: verified
v1_static_implementation: accepted
superseded_oracle_receipt: W0-R2 sha256:6890421241774922b3b8bf4f70cb87db5b743ba3759b3cd36717e365638d62d0; non-executable history
canonical_block_count: 23
canonical_block_receipt: exact/matching; 19 R2-unaffected payloads byte-identical
planned_sessions: 6
candidate_a_run: not recorded
b_f1: Implementation Orchestrator disposition PASS; not an independent W2 grade
b_f2: Implementation Orchestrator second disposition PASS; not an independent W2 grade
b_f3: Implementation Orchestrator disposition FAIL; required termination followed
b_f4: NOT_RUN due required termination; no behavior disposition
standalone_owner_smoke: NOT_RUN due required termination; no behavior disposition
source_leaf_smoke: NOT_RUN due required termination; no behavior disposition
downstream_not_launched: grader, verifier, held-out smoke, bridge writer
bridge_added: false
strict_a_b_skill_effect: NOT_ISOLATABLE
model_comparison: not claimed
claim_boundary: no independent W2 grade; no compatibility, adoption, effect, or model claim
next_action: no resumption directive; future work requires separately authorized planning
```
