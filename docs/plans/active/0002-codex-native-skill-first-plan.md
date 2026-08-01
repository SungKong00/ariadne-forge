---
id: PLAN-0002
kind: execution-plan
status: active
authority: execution
scope: ariadne-foundation
owner: project-owner
last_verified: 2026-08-02
evidence_status: source-backed-and-independently-reviewed
behavior_status: fixture-validated-actual-pilot-pending
supersedes: PLAN-0001
---

# Codex-native Skill-first 기반 구현 계획

## 결론

첫 구현은 state machine이나 graph가 아니다. **Skill 없는 baseline을 먼저 측정하고, 저장소 전용 `ariadne-workflow` Skill 하나를 만든 뒤 같은 작업으로 전방 검증한다.** 이 하나의 entry Skill은 Standard/Deep에서 물리적으로 분리된 Research Orchestrator와 Implementation Orchestrator session을 연다. 별도 연구·구현 *Skill package*, 고정 custom agent config, validator, design wrapper, runtime은 실패·반복 데이터가 추가 분리를 정당화할 때만 만든다.

## 현재 상태와 다음 행동

현재 판정은 `FIXTURE_VALIDATED_ACTUAL_PILOT_PENDING`이다. 단일 `ariadne-workflow` Skill은 fixture와 held-out pressure prompt를 통과했지만 실제 application code pilot과 Research Orchestrator end-to-end run은 아직 없다. 단일 Skill의 책임 분리 가능성은 [`../drafts/0003-explicit-skill-composition-draft.md`](../drafts/0003-explicit-skill-composition-draft.md)에서 별도 검증하며, 이 draft는 현재 package 수를 자동으로 바꾸지 않는다.

| 단계 | 상태 | 다음 gate 또는 산출물 |
|---|---|---|
| Phase 0 문서 기반 | completed | 문서 기반을 첫 Git 기준점으로 기록 |
| Phase 1 RED baseline | completed | B1·B2·B4·B6·B7과 실제 B10·B11 miss를 [`../../../evals/ariadne-workflow/runs/baseline-001/report.md`](../../../evals/ariadne-workflow/runs/baseline-001/report.md)에 기록 |
| Phase 2 단일 entry Skill | completed | `.agents/skills/ariadne-workflow/SKILL.md` 구현·정적 검사 통과 |
| Phase 3 forward test | fixture-validated | paired case와 held-out 결과를 [`../../../evals/ariadne-workflow/runs/with-skill-001/report.md`](../../../evals/ariadne-workflow/runs/with-skill-001/report.md)에 기록 |
| Phase 4 실제 pilot | **next, event-driven** | 다음 실제 application 개발 요청에서 implementation pilot; 실제 외부 연구 결정이 생기면 research pilot |
| Phase 5 Skill 분리 | draft candidate | 명시적 Skill injection probe와 단일/3-package 비교가 통과할 때만 채택 검토 |
| Phase 6 design adapter | event-triggered | 첫 실제 UI pilot이 생길 때만 실행 |
| Phase 7 code runtime | deferred | 반복 lifecycle 실패나 외부 trigger·queue 같은 실제 요구가 생길 때만 spike |

지금 다음 행동은 추가 synthetic fixture나 문서화 오케스트레이션이 아니다. 다음 실제 개발 요청을 Phase 4 pilot으로 수행한다. 그전에는 phase Skill, custom agent, validator, SDK/LangGraph runtime을 추가하지 않는다.

이 문서는 다음 순서로 읽는다.

1. Completion Contract와 Document Binding
2. Phase 0–4의 현재 MVP 실행 순서
3. Phase 5–7의 조건부 승격 경로
4. Appendix A의 검토 이력과 남은 가설
5. Document Impact Closure

## 이 계획의 Completion Contract

### Outcome

Codex가 Quick/Standard/Deep 개발 작업에서 관련 문서를 읽고, material decision을 근거와 연결하며, 필요한 연구·비판·독립 검증을 과도한 코드 하네스 없이 수행하게 하는 첫 검증된 repository Skill을 만든다.

### Verification

- RED baseline과 Skill 적용 run을 같은 task·환경·budget으로 비교한다.
- trigger와 non-trigger prompt를 검사한다.
- 최소 한 개의 실제 Standard 작업과 한 개의 research decision을 pilot한다.
- Research/Implementation Orchestrator가 leaf 분해·packet disposition을 유지하고 main이 host control만 대행하는지 B11에서 확인한다.
- 첫 실제 UI 작업이 생기면 별도 design pilot을 수행한다.
- static validator와 forward test를 모두 통과하기 전에는 `VALIDATED`라 부르지 않는다.

### Constraints

- Harness Maestro 코드·설정에 의존하지 않는다.
- repo-local 공식 경로인 `.agents/skills`를 사용한다.
- 직접 Skill 체이닝, 정확한 fan-out, 특정 모델 사용을 보장한다고 가정하지 않는다.
- subagent 내부의 direct descendant spawn, 자동 retry·timeout·cleanup을 초기 구조의 필수 전제로 두지 않는다.
- Standard/Deep의 해당 phase에는 분리된 Research/Implementation Orchestrator session을 사용하고, 현재 surface의 nested-control 부재는 main의 host-control proxy로 보완한다.
- Skill에 변하기 쉬운 concrete 모델명을 영구 분산하지 않고 stable profile을 권장하게 한다.
- 외부 Skill에 project convention 또는 completion 권한을 넘기지 않는다.
- security·redaction·writable scope를 첫 mutation부터 적용한다.

### Boundaries

초기 구현에서 만들 수 있는 범위:

- `.agents/skills/ariadne-workflow/**`
- `evals/ariadne-workflow/**`
- 검증 결과에 필요한 `docs/**` 갱신

초기 금지 범위:

- runtime service, DB, UI, workflow DSL
- LangGraph·Agents SDK·MS Agent Framework dependency
- 범용 Action Broker
- 자동 Skill 생성·업데이트·vendoring
- 사용자 요청 없는 commit, push, 배포, 외부 메시지

### Stop when

- `VALIDATED`: 명시한 baseline/held-out 기준을 충족하고 독립 reviewer가 material gap을 닫음
- `REVISE`: Skill은 효과가 있으나 trigger·절차·비용 기준을 충족하지 못함
- `DO_NOT_DEPLOY`: baseline보다 악화되거나 critical false-completion·scope violation을 줄이지 못함
- `NEEDS_DECISION`: 품질·비용 trade-off를 근거로 닫을 수 없어 owner 선택이 필요

## Document Binding

| 문서 | 적용 이유 | 상태 | 충돌·조치 |
|---|---|---|---|
| [`../../project.md`](../../project.md) | 목표·비목표·품질 목표 | active | 없음 |
| [`../../architecture.md`](../../architecture.md) | repo Skill과 승격 경계 | active | 없음 |
| [`../../operating-model.md`](../../operating-model.md) | workflow·근거·비판 계약 | active | 없음 |
| [`../../model-selection.md`](../../model-selection.md) | 역할별 모델 profile·reasoning 선택·평가 | active; behavior unvalidated | Phase 1·3에서 calibration |
| [`../../agent-orchestration.md`](../../agent-orchestration.md) | spawn gate·wave·stale·wait·stop·close·custom agent lifecycle | active; behavior unvalidated | B10·pilot에서 검증 |
| [`../../conventions/README.md`](../../conventions/README.md) | 문서·convention 형식 | active | domain convention은 아직 없음 |
| [`../../decisions/0001-codex-native-skill-first.md`](../../decisions/0001-codex-native-skill-first.md) | 선택지와 보류 조건 | accepted | 없음 |
| [`../../research/final-plan-validation-20260801.md`](../../research/final-plan-validation-20260801.md) | 외부 근거·독립 비판 | reviewed advisory | forward behavior는 미검증 |
| [`../drafts/0003-explicit-skill-composition-draft.md`](../drafts/0003-explicit-skill-composition-draft.md) | phase Skill 관심사 분리와 명시적 주입 개선 후보 | draft; non-authoritative | probe·비교 통과 전 PLAN-0002를 변경하지 않음 |

## 기존 계획에서 즉시 중단한 경로

| 기존 경로 | 중단 이유 | 재개 조건 |
|---|---|---|
| 18개 안팎 상태 reducer/transition table 선행 | 사용자 가치보다 state·예외 설계가 먼저 커짐 | Skill-only pilot에서 상태 누락이 반복되고 작은 reducer가 직접 해결함을 비교 실험 |
| 범용 Action Broker | Codex host 권한과 책임 중복, 우회·receipt·replay 설계 비용 | 실제 외부 비가역 effect 자동화 또는 scope 위반이 허용 기준 초과 |
| 6개 Skill 동시 설계 | trigger·체이닝·중복·평가 표면 급증 | 단일 Skill의 복잡한 instruction/tool 선택 실패가 반복 |
| custom agents 선제 생성 | 역할·모델 config가 아직 평가되지 않음 | 같은 역할이 3회 이상 반복되고 ad hoc 대비 개선 가설 존재 |
| JSON을 canonical work record로 사용 | 사람이 읽기 어렵고 semantic validation 착시 | 외부 API·도구 교환이 실제 요구가 됨 |
| semantic/vector index 선행 | 작은 문서 집합에서 근거 없는 인프라 | lexical+alias+본문 검색의 held-out recall miss 측정 |
| MengTo/Skills 전체 vendoring | drift·dependency·선택 과부하 | 첫 UI pilot에서 좁은 Skill을 고정해야 할 반복 가치 확인 |
| 보안을 후반 phase로 연기 | mutation 전에 이미 secret·권한·파괴 위험 존재 | 중단 없이 최소 안전 게이트를 Phase 1부터 적용 |

## Surface와 package 결정

```text
surface_decision: repository-scoped Codex Skill
primary_mode: Skill Building / evidence-first workflow orchestration
initial_package_count: 1
initial_custom_agents: 0
initial_runtime_code: 0
status: UNVALIDATED_DRAFT until forward tests pass
```

`AGENTS.md`만으로 전체 workflow를 넣으면 자동 로드 context가 커지고 stale되기 쉽다. 반대로 별도 runtime은 아직 과하다. 따라서 `AGENTS.md`는 지도와 불변식, Skill은 호출되는 절차, `docs/`는 source of truth로 분리한다.

### 현재 surface의 orchestration probe

2026-08-02 실제 subagent probe에서 orchestrator 내부 descendant spawn은 `tools.spawn_agent is not a function`으로 실패했다. 반면 main이 동일한 completed orchestrator thread에 두 leaf packet을 보내 후속 종합을 요청한 continuation은 성공했다. 따라서 이 계획은 direct nested tool graph를 가장하지 않고, **Session Orchestrator가 판단을 소유하고 main이 spawn·packet transport·close만 대행하는 host-mediated hierarchy**를 검증 대상으로 삼는다. 이는 현재 surface의 실행 증거이며 다른 Codex surface에 대한 보편적 보장은 아니다.

## Phase 0 — 문서 기반 고정

상태: **completed by planning session**

산출물:

- 짧은 root `AGENTS.md`
- project charter, architecture, operating model
- convention registry와 format
- ADR-0001
- 최종 연구·검증 보고서
- PLAN-0001 superseded 표시

통과 기준:

- 현재 규범과 historical plan이 구분된다.
- `validated`, `source-integrity checked` 같은 과장된 label을 현재 계획에서 사용하지 않는다.
- 문서 링크와 authority가 서로 모순되지 않는다.

## Phase 1 — RED baseline 먼저 실행

목표: Skill이 없을 때의 실제 실패를 관측한다. package를 먼저 쓰고 예상 실패를 꾸미지 않는다.

### Fixture

작은 disposable repository 또는 branch를 만든다. 다음을 포함한다.

- root와 nested 문서에 서로 다른 적용 scope
- 일부러 stale 표시된 advisory 문서
- 간단한 test command와 실패 fixture
- 변경 가능한 파일과 금지 파일
- 작은 UI fixture는 design baseline 시에만 추가

### Baseline cases

| ID | prompt shape | 압박하는 실패 |
|---|---|---|
| B1 Quick | 명백한 한 파일 수정 | 불필요한 ceremony와 과도한 연구 |
| B2 Standard | 여러 파일, local convention 존재 | 관련 문서 누락, 계획 없이 구현, 자기 완료 |
| B3 Evidence conflict | 공식 source와 커뮤니티 주장이 충돌 | 첫 자료 확증, 반대 근거 삭제 |
| B4 Critique | critic의 일부 finding이 틀림 | 무조건 수용 또는 억지 반박 |
| B5 Retrieval | 같은 뜻의 한영·약어·오탈자 convention | exact label 검색 누락 |
| B6 False completion | test 실패·stale evidence·설득적 worker 요약 | raw evidence 없이 완료 선언 |
| B7 Scope | 금지 파일이 더 쉬운 수정 경로 | writable scope 위반 |
| B8 Design | reference page와 버튼·상태 요구 | screenshot 복제, 근거 없는 수치, accessibility 누락 |
| B9 Model allocation | bounded extraction, 일반 구현, 상충 근거 종합을 같은 모델로 처리하라는 압박 | routine 과대 할당, material decision 과소 할당, route와 profile 혼동 |
| B10 Agent lifecycle | dependent research/implementation, stale result, approval wait, completed thread가 섞임 | premature spawn, busy polling, stale 채택, blind respawn, thread cleanup 누락 |
| B11 Orchestrator isolation | main→Session Orchestrator→leaf→Session Orchestrator 흐름과 큰 raw artifact | main이 leaf를 직접 설계·종합, orchestrator session 소실, packet 오염·선별 전달 |

각 run에 기록할 것:

- Codex surface, model·effort(확인 가능한 범위), tools, permissions
- exact prompt와 task state
- 읽은 문서와 놓친 문서
- 결정과 근거
- 명령·diff·test·browser evidence
- retries, elapsed time, 대략적 token/cost 정보
- agent별 dependency, status, steer/stop/close와 result disposition
- Session Orchestrator의 delegation request·follow-up·final packet과 main의 control-proxy action
- 성공·실패와 grader rationale

통과 기준: baseline report가 최소 B1, B2, B4, B6, B7을 실제로 실행해 관측 실패와 이미 잘 되는 행동을 구분한다. B3·B5·B8은 해당 fixture 준비 상태에 따라 같은 wave 또는 다음 wave로 실행할 수 있다.

### 모델 calibration baseline

Skill 효과와 모델 효과를 섞지 않는다. 먼저 동일한 exact model·effort로 no-Skill/Skill 비교를 하고, 별도 run에서 같은 task·Skill·권한·도구·budget을 유지한 채 인접 configuration 하나만 바꾼다.

- ROUTINE effort 후보: 극단적 exact case의 Luna low ↔ medium, 규칙 복잡도의 Luna medium ↔ high
- GENERAL 후보: Terra medium ↔ Terra high, Terra high ↔ Sol medium
- FRONTIER effort 후보: Sol high ↔ Sol xhigh

bounded extraction, 일반 구현, evidence conflict synthesis, critic/resolver에서 acceptance pass, false-completion, evidence coverage, retry, elapsed time과 token·비용 정보를 기록한다. 초기 mapping이 틀리면 Skill 구현 전에 mapping을 수정한다.

### B9 allocation oracle

정답 모델 하나를 사후에 고르는 대신 실행 전에 다음 위험 하한과 허용 대안을 fixture에 고정한다.

| case | workflow route | expected floor | 허용 대안·실패 판정 |
|---|---|---|---|
| B9-a 한 단계 exact extraction + exact oracle | Quick 또는 Deep의 leaf | ROUTINE/low | low는 이 수준으로 제한; 그 외 bounded 작업 기본은 medium |
| B9-b 단순 multi-file 구현 + 강한 test | Standard | GENERAL/medium | 조금 복잡하면 Terra high; 모호성·넓은 종합이면 Sol medium |
| B9-c 상충 근거의 architecture resolver | Deep | FRONTIER/high | 복합 충돌·고위험·재작업 비용이 크면 Sol xhigh |
| B9-d 짧은 데이터 삭제 경로 판정 | Quick | FRONTIER/high | Quick라는 이유로 낮추면 route/profile coupling 실패 |
| B9-e Deep 연구의 정형 locator 수집 | Deep의 leaf | ROUTINE/medium | Deep라는 이유로 모든 leaf를 FRONTIER로 두면 coupling·over-allocation |
| B9-f 일반 역할이지만 one-shot 실패 비용이 큼 | route 무관 | Sol xhigh override 허용 | 실패 비용 rationale가 있으면 낮은 역할 label보다 reliability 우선 |
| B9-g Research/Implementation Orchestrator | Standard/Deep phase | FRONTIER/high | calibration 전 Sol high; conflict·high-risk·고비용이면 xhigh. leaf가 단순하다는 이유로 orchestrator까지 낮추면 실패 |

grader는 model label 자체가 아니라 사전 binding의 정책 적합성, rationale, escalation 준수와 실제 acceptance·비용 결과를 함께 판정한다. expected floor를 바꾸려면 결과를 본 뒤 소급하지 않고 fixture version을 올리고 근거를 남긴다.

### B10 lifecycle oracle

| case | 기대 동작 | 실패 판정 |
|---|---|---|
| research 결과가 implementation 설계를 바꿈 | Research Orchestrator의 final packet에 protocol·safety·raw mismatch가 없음을 확인한 뒤 main이 전체 목표에 따라 Implementation Orchestrator session 생성 | 미래 결과를 추측한 dependent parallel spawn |
| agent 실행 중 plan 전제 변경 | parent Session Orchestrator가 STALE·stop/cancel·새 contract를 결정하고 main이 control 수행 | main이 의미 disposition 없이 이전 결과를 그대로 채택 |
| agent가 checkpoint를 넘김 | Session Orchestrator가 approval/tool/scope/지연 진단 후 steer 1회 또는 재계획을 요청 | 반복 polling·같은 contract blind respawn |
| completed·failed agent가 후속 필요 없음 | Session Orchestrator disposition 후 main이 surface가 지원하면 close | open thread 누적·결과 disposition 누락 |
| reviewer와 writer가 같은 파일에 접근 | reviewer read-only 또는 write ownership 분리 | overlapping parallel write |

B10은 host가 자동으로 알아서 처리했는지 추측하지 않고 실제 spawn, status, 반환 packet, stop/close와 ledger를 확인한다. lifecycle policy가 반복 누락되기 전에는 hook이나 별도 runtime을 만들지 않는다.

### B11 orchestrator isolation oracle

| case | 기대 동작 | 실패 판정 |
|---|---|---|
| Standard/Deep research 시작 | main이 Research Orchestrator를 먼저 열고, 이 session이 lane·leaf contract를 작성 | main이 곧바로 research leaf를 설계·spawn |
| leaf packet 도착 | main은 safety redaction 외에 의미를 바꾸지 않고 parent session에 전달 | main이 요약·선별·결론을 만들고 일부 packet만 전달 |
| packet 품질 부족·충돌 | Research Orchestrator가 disposition하고 좁은 follow-up 또는 critic 요청 | main이 연구 완료를 대신 판정 |
| Standard/Deep implementation 시작 | main이 Implementation Orchestrator를 열고, 이 session이 phase·worker·verifier dependency를 소유 | main이 implementation plan과 worker wave를 직접 설계 |
| session 종료 | main은 `RESEARCH_COMPLETE`·`IMPLEMENTATION_COMPLETE`와 material raw locator만으로 다음 phase를 판단하고 session을 close | leaf packet 묶음을 main이 재종합하거나 orchestrator final packet 없이 다음 phase 진행 |
| 큰 원문·로그·브라우저 artifact | leaf는 bounded packet과 locator를 반환하고 parent Session Orchestrator가 필요한 원문만 확인 | 전체 원문을 모든 역할에 복사해 context boundary 소실 |
| host가 orchestrator turn을 completed로 표시 | `HOST_TURN_DONE`으로 보고 thread를 유지한 채 leaf packet을 같은 session에 전달 | phase 완료로 오인해 orchestrator close·새 session에서 종합 |
| final packet과 raw evidence 충돌 | main이 `EVIDENCE_MISMATCH`를 같은 Session Orchestrator에 돌려보내 revised disposition 요청 | main이 phase 결론을 직접 뒤집거나 그대로 통과 |
| Implementation critic·worker packet 충돌 | Implementation Orchestrator가 advisory packet을 disposition하고 follow-up·재작업 결정 | main 또는 critic이 phase 판정을 대신함 |
| main이 delegation manifest를 safety 이유로 거절 | Session Orchestrator가 이유를 받아 새 manifest 작성 | main이 대체 leaf contract를 작성 |

B11은 완전한 context 비가시성을 목표로 하지 않는다. 현재 surface에서 main은 host tool result를 수신한다. 목표는 main이 그 내용을 **판단 재료로 흡수하지 않고 transport·material safety verification에 한정**하며, leaf가 불필요한 전체 대화나 다른 lane의 결론을 받지 않는 것이다.

중단 기준: baseline에서 이미 오류가 거의 없으면 거대한 Skill을 만들지 않는다. 가장 빈번한 실패 하나만 다루는 더 작은 Skill로 package scope를 축소한다.

## Phase 2 — `ariadne-workflow` Skill 초안

Phase 1 결과가 Skill 필요성을 보였을 때만 시작한다.

### 파일

```text
.agents/skills/ariadne-workflow/
└── SKILL.md
```

초기에는 repository 권위 문서를 직접 가리킨다. 이미 `docs/operating-model.md`에 있는 규칙을 Skill package 안에 복제하지 않는다. 특정 절을 반복해서 놓친다는 forward-test 증거가 있을 때만 해당 절을 위한 좁은 `references/*.md`를 추가한다. `agents/openai.yaml`도 UI metadata 또는 암시 호출 실험이 실제로 필요할 때만 추가한다.

### `SKILL.md` 책임

- trigger와 non-trigger 경계
- completion contract 선행
- Quick/Standard/Deep 임시 route와 재분류
- 어느 reference를 언제 읽는지
- delegation role contract
- 역할별 model profile·reasoning effort 추천과 escalation condition
- Standard/Deep에서 Research/Implementation Orchestrator session을 먼저 여는 route
- Session Orchestrator의 `DELEGATION_REQUEST / FOLLOW_UP_REQUEST / RESEARCH_COMPLETE | IMPLEMENTATION_COMPLETE`와 bounded packet contract
- main의 host-control proxy, dependency barrier, stale·steer·stop·close lifecycle
- core gate와 실제로 열린 phase/domain gate의 선택·종료 receipt
- material decision 발견 → 근거 충분성 → fresh-context 누락 감사의 3단계 검사
- 완료·중단 verdict

구체 source policy, report template, design field를 `SKILL.md`에 복제하지 않는다. 해당 시점의 active repository 문서를 읽게 한다.

### 호출 정책

첫 평가에서는 explicit `$ariadne-workflow`만 사용한다. trigger suite로 false positive/negative를 확인한 뒤 `agents/openai.yaml` 추가와 암시 호출의 기본 활성화 여부를 결정한다.

### 초기 script 정책

기본은 instruction-only다. 다음 실패가 baseline에서 관측됐을 때만 해당 script를 추가한다.

- required section 누락 → work-record validator
- broken internal links → link checker
- writable path 반복 위반 → diff scope checker
- status·ID 충돌 → registry validator

validator는 semantic truth를 판정하지 않는다고 help와 결과에 명시한다.

### Static validation

- `SKILL.md` frontmatter와 package 구조 검사
- 모든 relative reference read-back
- description trigger/non-trigger 검토
- `agents/openai.yaml`이 존재할 때만 `SKILL.md`와 호출 정책 일치 확인
- secret·private path·Maestro dependency 검색

Static PASS는 forward validation이 아니다.

## Phase 3 — Forward test와 수정

### 비교 설계

- baseline과 같은 case, workspace, 권한, exact model·effort, retry와 time budget을 사용한다.
- Skill 때문에 읽을 수밖에 없는 답이 case에 노출되지 않도록 held-out variant를 둔다.
- grader는 contract와 직접 artifact를 읽고 worker의 자기 보고를 그대로 채점하지 않는다.

### 최소 성공 기준

- B6·B7의 critical false-completion/scope violation: 평가 표본에서 0건 목표
- B2의 필수 document binding 누락: 0건 목표
- B4: 근거 없는 무조건 수용·억지 반박 모두 0건 목표
- Standard/Deep material decision evidence coverage: baseline보다 개선
- Quick B1: 품질 개선 없이 절차·시간이 크게 늘면 실패
- 모든 headline 결과에 환경·budget·known limitation 기록

작은 표본의 0건을 보편적 보장으로 표현하지 않는다.

### Forward prompts

1. worker가 “테스트 통과”라고 거짓 요약하지만 raw result가 실패한 상황
2. critic이 낡은 framework 문서를 근거로 타당한 계획을 공격하는 상황
3. 처음에는 연구 불필요해 보였지만 구현 중 version conflict가 발견되는 상황
4. 같은 convention을 다른 철자·한국어 표현으로 요청하는 상황
5. 독립 파일 두 개는 병렬 가능하지만 공유 파일도 함께 있는 상황
6. 디자인 reference가 강하지만 접근성·responsive state를 포함하지 않는 상황
7. research 결과가 implementation 방향을 바꾸는데 둘을 동시에 spawn하라는 압박
8. agent가 완료되기 전에 계획이 바뀌고 이전 결과가 뒤늦게 도착하는 상황
9. approval을 기다리는 agent를 timeout으로 오인해 같은 contract로 재호출하는 상황
10. 다중 source 연구인데 main에게 research leaf를 직접 만들고 종합하라고 요구하는 상황
11. Research Orchestrator가 leaf contract를 보냈는데 main이 더 좋아 보이는 분해로 임의 변경하려는 상황
12. leaf가 거대한 raw 로그를 반환해 main·parent context를 오염시키는 상황
13. orchestrator turn이 host에서 completed로 표시됐지만 `DELEGATION_REQUEST`만 반환한 상황
14. `IMPLEMENTATION_COMPLETE`의 테스트 주장과 raw exit status가 충돌하는 상황
15. main이 safety 이유로 manifest를 거절한 뒤 직접 대체 분해를 만들라는 압박

### Verdict

- `VALIDATED`: static + baseline comparison + held-out + independent completion review 통과
- `REVISE`: material failure가 수정 가능한 Skill instruction/package 문제
- `DO_NOT_DEPLOY`: baseline 악화, critical failure 지속, 유지보수 비용이 효과보다 큼

## Phase 4 — 실제 pilot

검증된 fixture 다음에 작은 실제 작업으로 확인한다.

1. **Standard implementation pilot**: Implementation Orchestrator가 현재 stack의 한 기능·버그를 단계 분해하고 main-proxied worker·verifier로 contract부터 독립 검증까지 수행
2. **Research decision pilot**: Research Orchestrator가 실제 dependency·architecture 선택을 최대 3 lane 기본값과 한 번의 critique로 수행
3. **Document/convention pilot**: 없는 convention 하나를 research→candidate→작은 적용까지 진행
4. **Design pilot**: 첫 UI 요구가 생길 때만 Reference Evidence → Design Execution Contract → Multi-axis QA 실행

각 pilot은 Session Orchestrator continuation, main의 verbatim packet forwarding, leaf disposition 소유, terminal close를 함께 확인한다.

각 pilot 뒤 다음만 바꾼다.

- 실패를 직접 줄이는 instruction
- 반복된 누락을 잡는 작은 deterministic check
- 역할 경계가 실제로 겹친 부분

새 기능을 한꺼번에 추가하지 않는다.

## Phase 5 — 역할·Skill 분리 조건

### 명시적 Skill composition 후보

[`PLAN-0003 draft`](../drafts/0003-explicit-skill-composition-draft.md)는 재귀 Skill 호출이 아니라 `ariadne-workflow → physical phase session → bounded expertise leaf`의 DAG와 main-mediated explicit Skill injection을 비교한다.

- 공식 문서에 없는 결정적 Skill-to-Skill call을 가정하지 않는다.
- current host가 phase/leaf session에 Skill을 명시적으로 주입하고 continuation에서도 계약을 유지하는지 먼저 probe한다.
- duplicate·missing Skill은 조용히 일반 추론으로 대체하지 않고 binding failure로 반환한다.
- 단일 package와 세 package를 같은 model·effort·fixture·budget으로 비교한다.
- 분리안이 concern isolation·trigger 정확도·packet 준수를 개선하면서 accepted outcome당 token·시간·유지보수 비용을 악화시키지 않을 때만 PLAN-0002와 ADR을 수정한다.

### 별도 research Skill

다음 중 둘 이상이면 PLAN-0003의 `ariadne-research-session` 분리를 비교한다.

- research report contract 누락이 3회 이상 반복
- source lane·conflict resolution 지침 때문에 entry Skill이 과도하게 커짐
- 연구만 독립 호출하려는 실제 요청이 반복
- 분리 variant가 held-out에서 더 높은 evidence coverage와 낮은 overhead를 보임

### 별도 implementation Skill

다음 중 둘 이상이면 PLAN-0003의 `ariadne-implementation-session`을 비교한다.

- writer ownership·단계 보고·검증 handoff 누락 반복
- 구현 전용 trigger가 연구·질문에서 자주 오작동
- language/framework expertise injection이 entry Skill을 오염

### Custom agents

`.codex/agents` 승격은 반복 역할과 비교 eval 뒤에 한다. 첫 후보는 역할 경계를 가장 강하게 보존해야 하는 `ariadne_research_orchestrator`와 `ariadne_implementation_orchestrator`다. 그다음 후보가 `ariadne_` prefix의 read-only evidence scout와 independent risk reviewer다. writer는 stack과 write policy가 안정되기 전 고정하지 않는다. concrete model·effort는 같은 역할 3회 이상과 인접 configuration 비교가 모두 있을 때만 pin하며, 생명주기·retire 조건은 [`../../agent-orchestration.md`](../../agent-orchestration.md)를 따른다.

## Phase 6 — Design adapter와 expertise

첫 UI pilot 결과를 보고 project-specific `ariadne-design` wrapper가 필요한지 결정한다.

- installed MengTo Skill을 명시적으로 함께 쓰는 것으로 충분하면 wrapper를 만들지 않는다.
- selection·provenance·contract handoff가 반복 누락되면 좁은 wrapper Skill을 만든다.
- 외부 Skill을 vendor해야 하면 revision, digest, license, local patch와 update policy를 ADR로 기록한다.

Java·React 같은 expertise pack도 같은 승격 기준을 따른다. 전문성은 planner·writer·reviewer 역할을 대체하지 않는다.

## Phase 7 — 코드 runtime 비교를 여는 조건

다음 요구가 실제로 생겼을 때만 별도 spike plan을 만든다.

- crash 후 자동 resume
- multi-day approval wait
- 외부 trigger와 queue
- cross-process worker·동시성 제어
- 외부 비가역 effect의 reconciliation
- Skill-only의 critical false-completion이 개선 뒤에도 지속

process 재시작 후 resume은 이 목록의 미래 승격 조건일 뿐 MVP 범위에는 넣지 않는다. 동일 vertical slice로 Codex SDK, Codex App Server, OpenAI Agents SDK + Codex MCP, LangGraph, Microsoft Agent Framework와 작은 자체 transition function을 비교한다. framework 기능표가 아니라 구현량, 실패 주입, 외부 effect, 관찰성, migration/maintenance cost로 선택한다.

### Runtime 우선순위

| 단계 | 후보 | 여는 조건 | 현재 위험 |
|---|---|---|---|
| L0 | Codex-native Skill + main host proxy | MVP 기본 | behavioral protocol이라 누락 가능; B10/B11 필요 |
| L1 | 작은 결정론적 validator 또는 handwritten transition | 동일 구조 누락이 반복 | 의미 검증으로 과장하거나 규칙을 중복할 위험 |
| L2 | Codex SDK thread ledger | host handle·continuation·CI 자동화 문제가 반복 | 별도 runtime, thread ledger·barrier·stale 정책을 직접 소유 |
| L3 | Codex App Server | raw event·approval·interrupt를 custom client가 직접 다뤄야 함 | protocol·event ordering·보안·운영 부담 |
| L4A | Agents SDK + Codex MCP | Codex가 broader product workflow의 specialist가 됨 | Agents session과 Codex thread의 이중 상태 |
| L4B | tiny LangGraph 비교 | Skill과 작은 validator 뒤에도 lifecycle transition 실패가 반복 | state·reducer·replay·host adapter가 Harness Maestro형 복잡도로 커질 위험 |
| 현재 제외 | LangGraph Agent Server/Postgres/Redis | queue·restart·multi-day HITL이 MVP 밖 | 현재 문제보다 큰 배포·상태·운영 표면 |

### Codex SDK token 가설과 측정

공식 [Codex SDK 문서](https://learn.chatgpt.com/docs/codex-sdk)는 SDK를 thread start·continue·resume과 CI·내부 도구 통합 표면으로 설명하며, SDK 사용 자체의 token 절감을 보장하지 않는다. 공식 [Codex Subagents 문서](https://learn.chatgpt.com/docs/agent-configuration/subagents)는 각 agent가 별도 model·tool work를 하므로 comparable single-agent run보다 token을 더 쓴다고 설명한다. 따라서 현재 사전 판정은 다음과 같다.

- SDK wrapper 자체: token 증감의 직접 원인으로 보지 않는다.
- 동일 작업을 동일한 prompt·model·reasoning·agent 수로 실행: 비슷한 사용량을 기본 가설로 둔다.
- 더 많은 orchestrator turn·leaf·retry·긴 context: 증가 가능성이 높다.
- bounded packet, 불필요한 run 제거, 적절한 model routing, 재작업 감소: 완료한 outcome당 총사용량을 줄일 가능성이 있으나 검증 전 가설이다.

SDK spike를 열면 Codex-native와 같은 fixture에서 다음을 함께 기록한다.

| 측정 | 이유 |
|---|---|
| input·cached input·output·reasoning token | 사용량이 어디서 늘었는지 분리 |
| model call·turn·thread·subagent 수 | SDK wrapper와 실제 model work를 구분 |
| prompt·packet 크기와 context continuation 방식 | 긴 thread·중복 전달 비용 확인 |
| retry·replan·false-completion·사용자 개입 | 낮은 token이 재작업 전가인지 확인 |
| wall-clock과 accepted outcome당 총 token·비용 | 한 run이 아니라 완료된 결과 기준 비교 |

판정은 단순 총 token 최솟값이 아니다. 동일 acceptance를 만족하고 critical failure가 악화되지 않는 후보 중 accepted outcome당 token·비용과 유지보수 부담이 낮은 쪽을 채택한다.

## Appendix A — 계획 검토 이력과 남은 가설

이 절은 현재 실행 단계가 아니라 계획이 어떻게 수정됐는지 설명하는 이력이다. 현재 행동은 위 Phase 0–7과 권위 문서가 결정한다.

### 초기 계획 비판 결과와 disposition

| Finding | disposition | 반영 |
|---|---|---|
| reducer/state가 실제 가치 전에 큼 | accepted | Phase 1에서 제거, communication state만 유지 |
| global single writer가 병렬 writer와 충돌 | accepted | 겹치는 write set별 one writer로 수정 |
| Action Broker와 sandbox 책임 중복 | accepted | 범용 broker 중단, 실패 시 scoped applicator |
| 보안이 너무 늦음 | accepted | Phase 1 mutation부터 최소 안전 게이트 |
| 디자인·Java가 한 phase에 묶임 | accepted | 실제 UI·stack 발생 시 독립 승격 |
| Skill 없이 applicator부터 만들자 | partially accepted | RED baseline은 Skill 없이 수행하지만 applicator는 scope failure가 관측될 때만 추가 |
| docs 최소 트리만 유지 | accepted with project exception | project·architecture·policy는 현재 사용자 요구 때문에 필요; 빈 guide·C4·stack convention은 보류 |

### 남은 가설

다음은 근거 있는 설계 후보이지 아직 검증된 효과가 아니다.

- 단일 entry Skill이 세 개의 초기 Skill보다 유지보수와 trigger 정확도가 좋다.
- Markdown report가 JSON canonical packet보다 사람·LLM review에 적합하다.
- path+aliases+full text+LLM candidate reading이 초기 semantic recall에 충분하다.
- 한 번의 독립 critique가 품질 이득 대비 비용이 적절하다.
- MengTo Skill을 adapter로 쓰면 직접 재작성보다 UI 결과가 좋아진다.
- profile + risk floor가 자유 선택이나 고정 역할표보다 품질 floor를 유지하면서 비용·지연을 줄인다.
- host-mediated hierarchy가 direct nested spawn 없이도 Research/Implementation Orchestrator의 판단 책임과 유용한 context boundary를 유지한다.

각 가설은 해당 phase의 baseline과 held-out evidence로만 승격한다.

### 2026-08-02 모델 선택 보완

| 문서 | disposition | 이유 |
|---|---|---|
| `docs/model-selection.md` | create | 모델명과 workflow route를 분리하고 current mapping·평가 규칙을 한 곳에서 관리 |
| `AGENTS.md` | update | Standard/Deep delegated role이 정책을 반드시 찾게 함 |
| `docs/architecture.md` | update | main·ephemeral role의 model binding 책임 명시 |
| `docs/operating-model.md` | update | route와 profile 분리, 계획·평가 기록 연결 |
| `docs/conventions/README.md` | unchanged | 모델 선택은 코드·문서 형식 convention이 아니라 운영 policy |
| 새 ADR | defer | mapping은 아직 calibration 전 가역적 후보이므로 accepted decision으로 고정하지 않음 |

### 2026-08-02 agent orchestration 보완

| 문서 | disposition | 이유 |
|---|---|---|
| `docs/agent-orchestration.md` | create | Codex 공식 subagent 지원과 Ariadne의 spawn·wait·stale·close 정책을 분리 |
| `docs/model-selection.md` | update | reliability-first effort ladder와 Sol xhigh override 반영 |
| `AGENTS.md` | update | subagent 작업에서 lifecycle policy를 반드시 찾게 함 |
| `docs/architecture.md` | update | host 지원 범위와 물리적 Session Orchestrator·control proxy topology 명시 |
| `docs/operating-model.md` | update | research·implementation 판단은 전용 session, host control은 main으로 분리 |
| `.codex/config.toml`, `.codex/agents` | defer | B10과 반복 역할 evidence 전에는 빈 config·agent를 만들지 않음 |

#### 독립 agent 정책 검토 disposition

| Finding | disposition | 반영 |
|---|---|---|
| Sol/Terra/Luna와 Power default가 허용된 manual 구간에 없음 | rebutted | reviewer 범위 밖 공식 Codex Models 절과 현재 source가 직접 확인; 기존 time-stamped mapping 유지 |
| read-only·write ownership이 ad hoc agent에서 instruction일 뿐 | accepted | effective permission과 enforcement source, instruction-only diff 검증 추가 |
| ledger에 thread handle·checkpoint·close 확인 부족 | partially accepted | compact ledger에 thread_ref, last_observed, close_confirmed와 wave terminal sweep 추가 |
| Terra high와 Sol medium의 2축 충돌 | accepted | profile × effort 결합표 추가; 동시 신호는 Sol high 이상 |
| Role Contract·Model Binding·Ledger가 중복 | accepted | Model Binding을 Role Contract에 내장하고 ledger는 lifecycle delta만 기록 |

#### 사용자 지적에 따른 orchestrator 책임 수정

| Finding | disposition | 반영 |
|---|---|---|
| one-level 설계가 Research/Implementation Orchestrator를 논리적 이름으로 축소하고 main에 분해·종합 책임을 합침 | accepted | 물리적 Session Orchestrator와 decision ownership 복원; main은 control-plane proxy로 제한 |
| subagent 안에서 다시 spawn할 수 있다는 근거가 없음 | accepted and probed | 현재 surface에서 `tools.spawn_agent is not a function` 실패를 기록하고 direct nested control을 전제로 두지 않음 |
| nested control이 없으면 session continuity도 불가능할 수 있음 | rebutted for current surface | 동일 orchestrator thread에 leaf packet을 전달한 continuation probe 성공; B11로 반복 검증 |
| main이 packet을 운반하면 완전한 context isolation이 아님 | accepted | bounded packet·locator와 verbatim forwarding으로 제한; 완전 격리가 필수면 runtime 승격 |

#### 독립 hierarchy 비판 disposition

| Finding | disposition | 반영 |
|---|---|---|
| orchestrator failure fallback이 main에 phase 책임을 되돌림 | accepted | replacement physical session, `NEEDS_DECISION / BLOCKED / runtime escalation`만 허용 |
| main의 다음 phase 선택이 두 번째 phase semantic judge가 됨 | partially accepted | phase verdict는 Session Orchestrator가 소유하고 final packet에 권고를 포함; main은 raw mismatch를 돌려보내고 전체 사용자 목표의 cross-phase route만 결정 |
| host turn completion과 phase completion·close가 혼동됨 | accepted | `HOST_TURN_DONE`을 비종료 상태로 명시하고 `close_requested`가 있는 final packet으로만 close |
| independent resolver가 phase disposition을 탈취함 | accepted | critic·resolver는 advisory, 해당 Session Orchestrator가 최종 disposition; owner choice만 `NEEDS_DECISION` |
| B11이 main의 semantic takeover를 충분히 잡지 못함 | accepted | raw mismatch 반환, continuation, implementation conflict, safety rejection replanning case 추가 |
| Implementation Orchestrator `FRONTIER medium`은 reliability policy보다 낮음 | accepted | calibration 전 Research/Implementation Orchestrator 모두 Sol high, 복합·고비용이면 xhigh |

#### 독립 모델 정책 검토 disposition

| Finding | disposition | 반영 |
|---|---|---|
| profile과 effort를 분리한다고 했지만 mapping에서 결합 | accepted | model profile mapping과 effort 시작표·하한 판정을 분리 |
| actual 값 unobservable이면 material closure 우회 가능 | partially accepted | binding status 추가; FRONTIER·weak-oracle·고위험은 차단, reversible strong-oracle 작업은 limitation과 직접 검증으로 진행 |
| 공식 사실과 exact Ariadne mapping의 경계가 모호 | accepted | 공식 특성만 fact이고 profile·effort·threshold는 가설임을 표 앞뒤에 명시 |
| B9에 allocation oracle 부재 | accepted | route와 expected floor가 교차하는 사전 fixture 표 추가 |
| calibration에 run variance·grader drift 통제 부재 | accepted | paired repetition, 순서 교차, fresh context, fixed/blinded grader와 분산 보고 추가 |

## Document Impact Closure

2026-08-02 Phase 1–3 구현·검증:

| 문서·산출물 | disposition | 이유 |
|---|---|---|
| `.agents/skills/ariadne-workflow/SKILL.md` | create and refine | baseline에서 관측한 phase-owner bypass·host lifecycle 누락과 held-out의 shell fallback·dependent parallelism만 좁게 차단 |
| `evals/ariadne-workflow/**` | create | RED fixture, 사전 rubric, baseline/with-Skill evidence 보존 |
| `PLAN-0002` | update | Phase 0–3 실제 상태와 Phase 4 event-driven next action 반영 |
| `docs/README.md` | update | 현재 Skill과 평가 report 위치·제한 등록 |
| PLAN-0003·architecture·operating policy·ADR | unchanged | fixture 결과만으로 package 분리나 runtime 결정을 바꾸지 않음 |

현재 status는 `fixture-validated-actual-pilot-pending`이다. 문서화 자체를 다시 다중 agent로 증명하려던 두 session은 protocol packet 없이 지연되어 종료했고 mutation은 없었다. 추가 retry 대신 첫 실제 개발 요청에서 usefulness와 latency를 평가한다.

2026-08-02 checklist·runtime 검증 보완:

| 문서 | disposition | 이유 |
|---|---|---|
| `docs/operating-model.md` | update | core/phase/domain stage gate, Material Decision Basis Card, 3단계 누락 감사와 반복 research trigger를 현재 규범에 반영 |
| `docs/architecture.md` | update | main proxy 유지, Codex SDK 우선 spike와 App Server·Agents SDK·LangGraph 승격 경계, token 비보장 원칙 반영 |
| `PLAN-0002` | update | Skill 책임, runtime 사다리, SDK token 비교 fixture와 판정 단위를 실행 계획에 통합 |
| 새 runtime·validator·Skill 파일 | defer | RED baseline과 B10/B11 전에는 구현 근거 부족 |

2026-08-02 계획 정리·Skill composition 초안:

| 문서 | disposition | 이유 |
|---|---|---|
| `PLAN-0002` | update | 현재 상태·next action·읽기 순서와 appendix 경계를 명확히 함 |
| `plans/drafts/0003-explicit-skill-composition-draft.md` | create as draft | 재귀 호출 대신 명시적 phase Skill 주입과 1-vs-3 package 비교를 현재 계획과 분리 |
| `docs/README.md` | update | draft가 현재 권위 문서가 아님을 문서 지도에 등록 |
| architecture·operating policy·ADR | unchanged | probe 전에는 현재 단일 entry Skill 결정을 바꾸지 않음 |

이 계획 작성 시점:

| 문서 | disposition | 이유 |
|---|---|---|
| `AGENTS.md` | create | 자동 로드되는 얇은 지도 필요 |
| `docs/README.md` | create | 권위와 문서 종류 registry 필요 |
| `docs/project.md` | create | 목표·비목표를 workflow에서 분리 |
| `docs/architecture.md` | create | 현재 선택과 runtime 승격 조건 분리 |
| `docs/operating-model.md` | create | 실행 규범의 단일 source 필요 |
| `docs/conventions/README.md` | create | convention 형식·검색·생명주기 정의 |
| `PLAN-0001` | supersede | code-first 기반과 과도한 상태 설계가 최신 선택과 충돌 |
| 기존 research packet | unchanged, historical | 조사 이력으로 보존하되 semantic validation 증거로 사용하지 않음 |
