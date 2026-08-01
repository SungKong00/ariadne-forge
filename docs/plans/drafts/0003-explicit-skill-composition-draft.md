---
id: PLAN-0003
kind: execution-plan
status: draft
authority: execution
scope: ariadne-skill-composition
owner: project-owner
last_verified: 2026-08-02
supersedes: null
related_plan: PLAN-0002
behavior_status: unvalidated-draft
---

# 명시적 Skill composition과 phase package 분리 초안

## 문서 상태

이 문서는 [`PLAN-0002`](../active/0002-codex-native-skill-first-plan.md)의 현재 실행 순서를 바꾸지 않는 **추후 개선 후보**다. 공식 지원 사실과 현재 surface probe를 바탕으로 비교 실험을 설계하지만, Skill injection forward test와 단일/분리 package 비교가 끝나지 않았으므로 채택된 아키텍처가 아니다.

```yaml
status: UNVALIDATED_DRAFT
current_authority: none beyond this bounded experiment
current_plan: PLAN-0002 remains active
next_gate: explicit skill-injection probe
repository_mutation_allowed_by_this_draft: none
```

## 결정 요약

검토할 후보는 **재귀 Skill 호출**이 아니라 다음의 명시적 choreography다.

```text
ariadne-workflow entry
  -> Main creates a physical phase session with an explicit Skill binding
     -> phase orchestrator requests bounded leaves and optional expertise Skills
        -> Main performs host controls and injects requested Skills
     <- bounded packets return to the same phase orchestrator
  <- phase final packet returns to Main
```

초기 비교 후보는 세 package다.

1. `ariadne-workflow`: intake, route, cross-phase transition과 user outcome closure
2. `ariadne-research-session`: research decomposition, evidence conflict, critique disposition과 research verdict
3. `ariadne-implementation-session`: plan, worker dependency, implementation progress, verifier·critic disposition과 implementation verdict

critic, planner, writer, verifier, Java·React·design expertise는 초기 고정 package가 아니다. bounded role prompt 또는 이미 설치된 좁은 expertise Skill로 시작하고 반복 가치가 검증될 때만 승격한다.

## Completion Contract

### Outcome

현재 단일 Skill보다 관심사와 context를 명확히 분리하면서도 Harness Maestro형 runtime을 만들지 않는 Skill composition 후보를 검증한다.

### Verification

- current surface에서 spawned session에 명시한 Skill이 실제 output contract를 바꾸는지 확인한다.
- 같은 physical phase session continuation에서 Skill 계약이 유지되는지 확인한다.
- missing·duplicate Skill이 silent fallback되지 않는지 확인한다.
- 단일 package와 세 package를 동일 fixture·model·effort·permission·retry budget으로 비교한다.
- concern isolation, trigger 정확도, phase ownership, packet 준수, false completion, token·시간을 함께 측정한다.
- static validation과 realistic forward test 전에는 `CANDIDATE`나 `ADOPTED`로 부르지 않는다.

### Constraints

- Skill-to-Skill direct call이나 recursion을 Codex 보장 기능으로 주장하지 않는다.
- direct descendant spawn을 전제로 하지 않고 main의 host-control proxy를 유지한다.
- phase Skill은 project policy나 user outcome 권한을 소유하지 않는다.
- expertise Skill은 advisory leaf이며 phase verdict를 소유하지 않는다.
- personal absolute path를 package 지침에 고정하지 않는다.
- hooks, plugin, custom agent, SDK, DB, graph runtime을 이 실험에 추가하지 않는다.
- restart/resume은 범위 밖이다.

### Boundaries

초안 승인 뒤 probe에서 허용할 수 있는 범위:

- disposable fixture 또는 별도 test workspace
- temporary physical subagent sessions
- Skill binding·packet·token 측정 기록
- probe가 통과한 뒤에만 `.agents/skills/ariadne-*/**` candidate package

금지 범위:

- production code 변경
- current normative policy 자동 수정
- commit, push, 배포, 외부 메시지
- global Skill 복사·수정·vendoring

### Stop when

- `ADOPT_CANDIDATE`: 명시 주입이 작동하고 분리 variant가 critical regression 없이 관심사 분리를 개선
- `KEEP_SINGLE_SKILL`: 주입이 불안정하거나 분리 이득이 overhead·trigger failure보다 작음
- `REVISE`: binding protocol·package boundary가 수정 가능한 원인으로 실패
- `BLOCKED`: current surface에서 주입 여부를 관찰하거나 비교할 수 없음
- `NEEDS_DECISION`: 품질·비용·portability trade-off가 근거만으로 닫히지 않음

## Document Binding

| 문서·자료 | 적용 이유 | 상태·신선도 | 이 초안에서의 사용 |
|---|---|---|---|
| [`../../project.md`](../../project.md) | 낮은 유지보수 비용, 오류 격리, 유연성 | active | runtime·거대 Skill tree 금지 |
| [`../../architecture.md`](../../architecture.md) | current single entry Skill과 main-proxy 구조 | active | 실험 전 current architecture 유지 |
| [`../../operating-model.md`](../../operating-model.md) | phase authority, evidence, stage gate | active | package가 규칙을 복제하지 않고 읽음 |
| [`../../agent-orchestration.md`](../../agent-orchestration.md) | physical session, main proxy, lifecycle | active; behavior unvalidated | explicit binding을 기존 Role Contract에 추가하는 후보 |
| [`../../model-selection.md`](../../model-selection.md) | role별 model·effort와 paired comparison | active; mapping unvalidated | variant 간 exact configuration 고정 |
| [`../active/0002-codex-native-skill-first-plan.md`](../active/0002-codex-native-skill-first-plan.md) | current execution plan | active | 이 draft가 변경하지 않음 |
| [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills) | explicit/implicit activation, progressive disclosure, one-job focus | current official; checked 2026-08-02 | direct recursive API가 아니라 explicit binding 후보의 근거 |
| [OpenAI App Server](https://learn.chatgpt.com/docs/app-server) | turn input의 explicit `skill` item | current official; checked 2026-08-02 | SDK/App Server를 도입하지 않고도 binding contract를 설계하는 참고 |
| [OpenAI Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | host orchestration과 token trade-off | current official; checked 2026-08-02 | main-proxy와 physical session 유지 |
| `reference-research-team` installed Skill | embedded packet return과 owner-held spawn 패턴 | local reusable example; not repo authority | bootstrap probe 후보, repository dependency로 고정하지 않음 |

## 확인된 사실과 프로젝트 추론

### 확인된 사실

- Codex는 Skill을 명시적 또는 description 기반으로 활성화하고, 선택된 Skill의 전체 `SKILL.md`를 progressive disclosure로 읽는다.
- App Server 문서는 turn 시작 시 `$skill` text와 `skill` input item을 함께 넣는 explicit injection을 설명한다.
- 공식 문서는 Skill A가 Skill B를 함수처럼 호출하고 await하는 재귀 API를 설명하지 않는다.
- 공식 문서는 Skill을 한 가지 알아볼 수 있는 작업에 집중하도록 권한다.
- 현재 Ariadne surface에서 descendant spawn은 실패했고, main-mediated same-session continuation은 성공했다.
- 현재 host tool schema는 spawn input에 `type: skill`, `name`, `path` 형태를 받을 수 있지만, Ariadne phase Skill에 대한 실제 주입 결과는 아직 probe하지 않았다.

### 프로젝트 추론

- Skill composition은 호출 stack보다 **session creation manifest에 Skill binding을 포함하는 방식**이 더 관찰 가능하고 현재 topology와 맞는다.
- phase마다 전체 지침을 별도 physical context에 주입하면 Main context pollution을 줄일 가능성이 있다.
- package 수가 늘면 trigger, path resolution, drift, token과 maintenance cost도 늘 수 있으므로 분리는 자동 채택할 수 없다.

## Retrospective vulnerability packet

| 관찰된 취약점 | 자연스러운 잘못된 합리화 | 빠진 gate | 이 초안의 대응 |
|---|---|---|---|
| entry Skill 책임이 route·research·implementation·lifecycle·gate까지 넓어짐 | “파일 하나니까 단순하다” | 책임 수와 context 경계 검토 | 1-vs-3 package 비교 |
| helper Skill을 문장에서 언급만 할 수 있음 | “필요하면 모델이 알아서 사용할 것” | 실제 binding·output receipt | explicit `skill_binding`과 binding status |
| implicit invocation에 의존할 수 있음 | “description이 충분히 명확하다” | 실제 injection 확인 | phase Skill explicit-only 후보와 missing failure |
| 동일 이름 Skill이 여러 scope에 존재할 수 있음 | “이름이 같으면 같은 Skill이다” | resolved path·identity 확인 | unique `ariadne-*`와 resolved path receipt |
| 모든 Skill을 Main에 로드하면 관심사 분리가 사라짐 | “모듈이 많으면 자동으로 context도 분리된다” | physical context 확인 | phase/leaf session에만 full instruction 주입 |
| recursive helper가 phase 권한을 가져갈 수 있음 | “전문 Skill이 더 잘 아니까 최종 판단도 맡긴다” | decision owner 불변식 | expertise leaf는 advisory, phase owner만 final packet |

## 선택지 비교

| 선택지 | 장점 | 비용·위험 | 초안 판정 |
|---|---|---|---|
| A. 단일 `ariadne-workflow` + repository docs | package·trigger·binding이 가장 단순 | entry 책임과 physical phase prompt가 커질 수 있음 | PLAN-0002 baseline; 반드시 유지 |
| B. thin entry + research/implementation phase Skill | 관심사·trigger·context·재사용 경계가 명확 | 세 package와 binding·drift·평가 부담 | **비교할 개선 후보** |
| C. entry + installed global research Skill hybrid | 빠른 bootstrap, 기존 embedded 패턴 활용 | portability와 global version drift | probe에만 허용; 최종 repo dependency로 고정하지 않음 |
| D. implicit recursive Skill chain | 코드 없이 모듈처럼 보임 | 실행·순서·cycle·fallback이 관찰하기 어려움 | reject |
| E. plugin bundle | 여러 Skill 배포에 적합 | 아직 repo-local 실험이고 배포 표면 과다 | defer |
| F. Codex SDK/App Server runtime | explicit handles·turn input·관찰성 | application runtime·상태·보안·maintenance | PLAN-0002 승격 조건까지 defer |

## 목표 package 구조

분리 variant는 다음 이상으로 시작하지 않는다.

```text
.agents/skills/
├── ariadne-workflow/
│   └── SKILL.md
├── ariadne-research-session/
│   ├── SKILL.md
│   └── agents/openai.yaml   # explicit-only policy가 실제로 필요하고 검증될 때
└── ariadne-implementation-session/
    ├── SKILL.md
    └── agents/openai.yaml   # 같은 조건
```

긴 source policy, report template, design fields, model mapping은 package에 복제하지 않는다. 각 Skill은 `docs/`의 자신에게 필요한 절만 읽는다. 반복 누락이 측정되기 전에는 `references/`와 `scripts/`를 추가하지 않는다.

## 관심사와 권한 경계

| 구성 요소 | 소유하는 것 | 소유하지 않는 것 |
|---|---|---|
| `ariadne-workflow` | intake, route, phase open/close, user outcome, cross-phase mismatch routing | research lane 설계, implementation worker 설계, leaf finding disposition |
| `ariadne-research-session` | source plan, leaf contract, evidence conflict, critique disposition, `RESEARCH_COMPLETE` | project implementation·merge verdict, host control, user preference 대체 |
| `ariadne-implementation-session` | phase plan, dependency, writer ownership, progress·stale, verification disposition, `IMPLEMENTATION_COMPLETE` | research source truth 대체, cross-phase user outcome, host control |
| expertise Skill leaf | bounded evidence·implementation advice·verification packet | phase verdict, 다른 Skill 생성, recursive spawn |
| Main host proxy | Skill resolution, spawn/send/wait/stop/close, permission·scope·overlap 검사 | phase decomposition·packet semantic synthesis |
| repository docs | active policy·architecture·convention | 실행 handle, transient status |

## 호출 그래프 invariant

```text
entry -> phase session -> expertise leaf
```

- graph는 DAG이며 같은 작업에서 최대 두 delegation edge만 둔다.
- phase Skill은 entry Skill이나 자기 자신을 다시 요청하지 않는다.
- expertise leaf는 phase·entry Skill을 요청하거나 다른 leaf를 spawn하지 않는다.
- Research와 Implementation은 dependent하면 순차로 연다.
- Main은 `required_skill`을 임의의 다른 Skill로 대체하지 않는다.
- phase final packet 없이 Main이 leaf packet을 직접 종합해 다음 phase를 열지 않는다.

## Skill Binding Contract

Session Orchestrator 또는 Main의 요청에는 다음을 둔다.

```yaml
skill_binding:
  requested_name:
  purpose:
  required: true | false
  invocation_policy: explicit
  resolved_path:
  resolution_source: repo-discovery | host-catalog | current-session-catalog
  binding_status: verified | deviated | unavailable | ambiguous | unobservable
  expected_output_contract:
  failure_action: return-to-owner | bounded-role-fallback | needs-decision
```

규칙:

1. name 하나만으로 같은 Skill이라고 판정하지 않고 resolved path를 기록한다.
2. required binding이 `unavailable`, `ambiguous`, `unobservable`이면 silent fallback하지 않는다.
3. role-prompt fallback은 phase owner가 bounded·reversible하다고 명시적으로 disposition할 때만 허용한다.
4. external/global Skill은 revision·digest를 관찰할 수 있으면 기록하고, 없으면 version이 고정되지 않았음을 limitation으로 남긴다.
5. Skill의 출력에 required contract field가 나타났다는 것은 behavior evidence이지 전체 instruction injection의 완전한 증명은 아니다.

## Role contracts

### Main binding executor

```text
input: session request, requested Skill name, current catalog, permission state
forbidden_context: phase conclusion을 새로 만들지 않음
task: resolve unique path, inject explicitly, manage host lifecycle, forward packets
output: binding receipt + lifecycle delta
success: requested Skill과 physical session handle이 관찰됨
stop: unavailable/ambiguous/permission conflict면 owner에게 반환
side effects: host session control only
```

### Phase Orchestrator

```text
input: completion contract, Document Binding, phase Skill, returned leaf packets
forbidden_context: 다른 phase의 private working notes와 hidden expected answer
task: phase decomposition, packet quality, conflict disposition, final phase packet
output: DELEGATION_REQUEST | FOLLOW_UP_REQUEST | PHASE_COMPLETE | NEEDS_DECISION
success: material claims have locators; unresolved conflict is preserved
stop: phase contract complete or blocking evidence/authority gap
side effects: no direct repository write unless implementation role explicitly owns it
```

### Expertise leaf

```text
input: bounded objective, exact artifacts, optional expertise Skill
forbidden_context: parent conclusion, unrelated lane packets, final verdict authority
task: one evidence or implementation slice
output: bounded evidence packet
success: facts, risks, uncertainty and locators are separated
stop: assigned slice complete or blocked
side effects: read-only by default; writer only with disjoint scope
```

## Evidence and packet contract

```yaml
packet:
  role:
  skill_binding_status:
  scope:
  artifacts_checked: []
  facts: []
  risks: []
  uncertainties: []
  commands_run: []
  evidence_refs: []
  confidence:
  recommended_verdict:
```

Skill binding은 packet의 authority를 높이지 않는다. 사실은 raw artifact·실행 결과·공식 source, 정책은 user·repository authority로 다시 판정한다.

## Local lens matrix

이 표는 현재 main session의 local review이며 독립 agent review가 아니다.

| lens | supporting evidence | contrary evidence | impact | unknowns |
|---|---|---|---|---|
| 실행 단순성 | PLAN-0002의 한 package가 가장 작음 | entry 책임이 이미 여러 phase와 lifecycle을 포함 | 단일 variant를 baseline으로 반드시 유지 | 실제 SKILL.md 길이와 누락률 |
| 관심사 분리 | physical phase sessions와 embedded research 패턴이 존재 | 별도 package가 없어도 role prompt로 분리 가능 | package 분리는 비교 후 결정 | 명시 Skill 주입이 child에서 관찰 가능한가 |
| context 비용 | progressive disclosure와 physical session은 관련 지침만 읽힐 가능성 | 여러 turn·Skill·agent는 token을 늘릴 수 있음 | accepted outcome당 token으로 평가 | current host token breakdown |
| 호출 신뢰성 | App Server는 explicit skill item을 문서화 | current desktop spawn path는 아직 probe하지 않음 | 가장 먼저 binding probe 필요 | continuation 중 binding 유지 여부 |
| 유지보수 | phase별 한 job은 변경 영향 격리에 유리 | 세 package의 공통 규칙 drift 가능 | 공통 규칙은 docs에만 두고 package는 얇게 유지 | 실제 중복량 |
| 권한 | main proxy와 phase decision owner가 이미 분리 | expertise Skill이 verdict를 탈취할 수 있음 | binding contract에 owner·forbidden authority 필요 | host가 skill별 sandbox를 관찰할 수 있는가 |

## Probe와 비교 실행 순서

### P0 — current baseline

PLAN-0002의 단일 entry Skill 또는 그 전 RED baseline에서 phase role prompt만 사용한다. 비교를 위해 prompt, model, effort, permission, fixture와 budget을 보존한다.

### P1 — explicit phase Skill injection

현재 catalog에서 embedded mode와 distinct output contract를 가진 read-only Skill 하나를 선택해 physical phase session에 명시 주입한다. Global Skill은 기능 probe에만 사용하며 repo dependency로 채택하지 않는다.

통과 관찰:

- requested Skill name과 resolved path가 기록됨
- child가 해당 Skill의 bounded output contract를 반환
- Main이 child 대신 phase 결론을 만들지 않음

### P2 — same-session continuation

첫 turn이 `DELEGATION_REQUEST`로 끝난 뒤 bounded leaf packet을 같은 phase session에 전달한다.

통과 관찰:

- 같은 session/thread handle
- host turn completion을 phase completion으로 오인하지 않음
- final packet에서 이전 contract와 packet disposition 유지

### P3 — failure injection

- missing Skill name
- 같은 이름의 서로 다른 path 후보
- required output field 누락
- stale packet 또는 wrong parent

통과 관찰: `SKILL_BINDING_FAILED`, `AMBIGUOUS`, `EVIDENCE_MISMATCH` 등으로 owner에게 반환하고 silent fallback하지 않는다.

### P4 — package comparison

같은 fixture에서 다음 두 variant를 후보별 최소 두 번 isolated paired run한다.

- V1: single `ariadne-workflow`
- V2: thin entry + research/implementation phase Skills

순서를 교차하고 fresh context를 쓰며, grader에게 가능한 범위에서 variant 이름을 숨긴다.

측정:

- trigger false positive/negative
- document binding·material decision evidence coverage
- main semantic takeover와 phase authority violation
- packet contract omission
- false completion·scope violation
- retry·user intervention
- input·cached input·output·reasoning token, turn·thread·agent 수
- wall-clock과 accepted outcome당 총 token·비용
- package 중복, 변경 파일 수, 이해·수정 시간

## Forward-test prompts

1. 연구가 필요한 요청인데 Main이 research leaf를 직접 만들고 종합하라는 압박
2. Research Skill이 implementation verdict까지 내리려는 상황
3. implementation 중 새로운 외부 version conflict가 발견돼 research를 다시 열어야 하는 상황
4. 같은 이름의 global/repo Skill이 함께 발견되는 상황
5. required phase Skill을 찾지 못했는데 일반 추론으로 계속 진행하기 쉬운 상황
6. phase turn은 completed지만 `DELEGATION_REQUEST`만 있고 final packet은 없는 상황
7. expertise leaf가 다른 Skill과 subagent를 다시 만들려고 하는 상황
8. 세 package 지침을 모두 Main에 복사하면 더 편해 보이는 상황

## Synthesis와 critique protocol

분리 variant의 평가는 다음 순서로 한다.

```text
raw run artifacts
-> claim matrix
-> single-vs-split difference analysis
-> material conflict만 한 번 rebuttal
-> fresh-context completion review
-> ADOPT_CANDIDATE | KEEP_SINGLE_SKILL | REVISE | NEEDS_DECISION
```

critic은 advisory다. “분리된 구조가 더 깨끗하다” 같은 추상적 선호만으로 채택하지 않고, 실제 omission·authority·context·maintenance·token 결과를 요구한다. 반박자는 비판을 무조건 방어하지 않고 evidence가 약하면 수용한다.

## 승격과 문서 변경 조건

`ADOPT_CANDIDATE` 뒤에도 즉시 current architecture가 되지 않는다. 다음을 순서대로 수행한다.

1. PLAN-0002의 package decision을 수정하거나 새 active execution plan으로 supersede한다.
2. ADR-0001의 “단일 Skill 우선” 결정을 재검토하는 새 ADR을 만든다. 기존 ADR을 덮어쓰지 않는다.
3. architecture의 component diagram과 Skill responsibility를 갱신한다.
4. agent-orchestration Role Contract에 `skill_binding`을 추가한다.
5. docs index에서 draft를 candidate/active 상태에 맞게 이동한다.

## 알려진 실패 모드

- phase Skill이 entry policy를 복제해 drift한다.
- description overlap으로 implicit invocation이 잘못 발생한다.
- unique name이지만 stale global path를 주입한다.
- expected output field만 흉내 내고 Skill instruction을 실제로 따르지 않는다.
- Main이 binding executor를 넘어 phase 결론을 재종합한다.
- physical session 수와 full Skill load가 token·latency를 늘린다.
- 세 package를 동시에 고치며 PLAN-0002의 작은 변경 원칙을 잃는다.
- Skill injection 성공을 sandbox·permission 강제 성공으로 오인한다.

## Reference research disposition

이번 초안은 current OpenAI Skill/App Server/Subagent 공식 문서와 현재 repository 자료로 surface 경계를 확인했다. 추가 framework·community 연구는 하지 않았다. 다음 단계가 Codex SDK/App Server 구현, plugin 배포 또는 cross-surface portability 비교로 확대될 때만 별도 reference research를 연다.

## Document Impact

이 초안 작성 시점:

| 문서 | disposition | 이유 |
|---|---|---|
| `PLAN-0002` | link and clarify only | current single-Skill baseline 유지 |
| `docs/README.md` | update | draft 위치와 비권위 상태 등록 |
| `architecture.md` | unchanged | probe 전 current component 구조 유지 |
| `operating-model.md` | unchanged | concern·authority 규칙은 이미 존재 |
| `agent-orchestration.md` | unchanged | `skill_binding`은 adoption 뒤에만 normative 반영 |
| ADR-0001 | unchanged | 세 package가 아직 accepted decision이 아님 |
| Skill package·script·config | not created | forward behavior가 없는 draft이므로 구현 금지 |

## 최종 draft verdict

```yaml
verdict: UNVALIDATED_DRAFT
recommended_experiment: explicit phase Skill injection probe, then V1-vs-V2 paired comparison
current_architecture_change: none
independent_review: not performed in this documentation pass
remaining_material_unknowns:
  - current desktop host에서 child Skill injection의 실제 관찰 가능성
  - continuation turn에서 binding 계약 유지
  - single-vs-split의 omission·token·maintenance 차이
  - duplicate/missing binding의 fail-closed 가능성
```
