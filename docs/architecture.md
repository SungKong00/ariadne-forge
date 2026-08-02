---
id: ARCH-0001
kind: architecture
status: active
authority: normative
scope: repository
owner: project-owner
last_verified: 2026-08-02
---

# Ariadne Forge 아키텍처

## 한 문장 구조

Ariadne는 별도 workflow engine이 아니라 **얇은 저장소 지침 + 하나의 진입 Skill + Codex의 기본 작업·subagent 기능 + 직접 확인 가능한 검증 증거**로 시작한다.

```mermaid
flowchart TB
    U["사용자 요구"] --> A["짧은 AGENTS.md 지도"]
    A --> D["프로젝트 문서·컨벤션"]
    A --> S["ariadne-workflow Skill"]
    S --> M["메인 Codex 오케스트레이터"]
    M --> R["Research Orchestrator session"]
    R -. "leaf contract" .-> M
    M --> RL["research·critic leaves"]
    RL -. "bounded packet via main" .-> R
    R --> RP["RESEARCH_COMPLETE without close authorization"]
    RP --> M
    M --> RE["Main independent inspection: EVIDENCE_COMPLETE"]
    RE -->|"receipt"| R
    R -->|"CLOSE_REQUESTED"| M
    RE -->|"dependent implementation gate"| I["Implementation Orchestrator session"]
    I -. "leaf contract" .-> M
    M --> IL["planner·writer·verifier leaves"]
    IL -. "bounded packet via main" .-> I
    I --> IP["IMPLEMENTATION_COMPLETE without close authorization"]
    IP --> M
    M --> IE["Main independent inspection: EVIDENCE_COMPLETE"]
    IE -->|"receipt"| I
    I -->|"CLOSE_REQUESTED"| M
    M --> O["완료 / 재작업 / 연구 재개 / 사용자 결정"]
```

점선 경로에서 main은 Codex host control을 대행할 뿐, leaf 분해와 packet 의미 판정을 넘겨받지 않는다. 이 구조는 논리적으로 계층형이고 현재 surface에서는 host-mediated다.

## 구성 요소

### 1. Repository knowledge

- `AGENTS.md`: 자동으로 로드되는 짧은 지도와 최소 안전 규칙
- `docs/project.md`: 변하지 않는 목표와 비목표
- `docs/architecture.md`: 현재 구현 구조와 승격 조건
- `docs/operating-model.md`: 작업 흐름과 역할·근거 계약
- `docs/model-selection.md`: 안정적인 역량 profile과 현재 모델·reasoning mapping
- `docs/agent-orchestration.md`: subagent topology, role contract, wait·steer·stop·close 생명주기
- `docs/conventions/`: 범위별 active convention과 등록부
- `docs/decisions/`: 되돌리기 어렵거나 넓은 영향을 가진 선택의 이유
- `docs/plans/`: 장기·복합 작업의 실행 기록
- `docs/research/`: 출처, 주장, 충돌과 한계를 보존하는 advisory 자료

### 2. Repository-scoped entry Skill

첫 구현 대상은 다음 하나뿐이다.

```text
.agents/skills/ariadne-workflow/
└── SKILL.md
```

`SKILL.md`의 한 가지 일은 evidence-first 개발 workflow를 지휘하고 현재 repository 권위 문서를 필요한 시점에 읽게 하는 것이다. `docs/operating-model.md`의 내용을 Skill 전용 reference에 복제하지 않는다. 반복 누락이 forward test에서 관측될 때만 좁은 reference를 추가하고, UI metadata나 암시 호출 제어가 실제로 필요할 때만 `agents/openai.yaml`을 추가한다. 초기 package에는 자체 runtime, DB, workflow DSL, network service를 넣지 않는다.

Skill의 상태는 package 생성 직후에도 `UNVALIDATED_DRAFT`다. 정적 검사와 실제 Codex forward test를 모두 통과하기 전에는 ready라고 부르지 않는다.

### 3. Main orchestrator

메인 Codex 세션은 다음만 소유한다.

- 요구사항과 완료 계약 확인
- 임시 작업 경로 선택과 재평가
- 필요한 문서 바인딩 확인
- 해당 phase의 Research/Implementation Orchestrator session 생성, close authorization 없는 phase packet 수신, raw evidence의 독립 검사와 `EVIDENCE_COMPLETE` receipt 회신
- session orchestrator가 요청한 역할·모델·병렬화 manifest의 안전·권한·write overlap·host feasibility 검사
- spawn·send·wait·stop·close handle, 여섯 lifecycle 차원과 실제 host close evidence 관리
- leaf packet을 의미 재종합 없이 parent session에 전달하고, material locator·diff·실행 결과를 직접 확인
- Session Orchestrator의 `phase_verdict`와 `recommended_next_action`을 입력으로 전체 사용자 목표의 다음 phase 또는 중단 상태 결정
- 사용자에게 근거와 남은 위험을 포함한 최종 보고

Quick 작업은 직접 답하거나 구현할 수 있다. Standard/Deep에서 해당 연구·구현 phase가 열리면 main은 leaf 분해·연구 종합·구현 진행 판정을 직접 흡수하지 않는다. Session Orchestrator가 실패하면 새 물리적 Session Orchestrator에 stable packet을 넘기거나 `NEEDS_DECISION / BLOCKED`로 끝낸다. main-owned leaf 분해나 PLAN-0002 runtime fallback을 사용하지 않는다.

### 4. Research/Implementation Orchestrator

두 역할은 이름만 붙인 논리적 단계가 아니라 main과 분리된 물리적 Codex session이다.

- **Research Orchestrator**: 결정 질문과 source plan 수립, research·critic leaf 계약, packet 품질·충돌·반례 판정, 좁은 follow-up, 비판 disposition, close authorization 없는 `RESEARCH_COMPLETE` 보고와 evidence receipt 이후의 별도 `CLOSE_REQUESTED`를 소유한다.
- **Implementation Orchestrator**: acceptance criterion을 단계·dependency·write ownership으로 분해하고 planner·writer·verifier leaf 계약, 단계 진척·stale·재계획, 계획 비판과 구현 검증 disposition, Standard/Deep UI Design Assurance domain phase, close authorization 없는 `IMPLEMENTATION_COMPLETE` 보고와 evidence receipt 이후의 별도 `CLOSE_REQUESTED`를 소유한다.
- 둘 다 main에 `DELEGATION_REQUEST`를 보내며, 현재 surface에서는 main이 host tool을 대행하고 결과 packet을 같은 session에 돌려준다.
- main은 안전·권한·scope·host 가능성 외의 이유로 manifest를 다시 설계하거나 leaf 결과 중 편한 것만 골라 전달하지 않는다.

### 5. Ephemeral leaf roles first

초기 research scout·비판자·planner·구현자·검증자는 parent Session Orchestrator가 만든 명확한 role contract를 받은 ad hoc subagent다. custom agent를 선제적으로 많이 만들지 않는다.

Role contract에는 반드시 다음을 넣는다.

- objective와 입력
- writable paths와 forbidden paths
- 반환 형식과 근거 요구
- 검증 방법
- model profile·reasoning effort 추천, 근거와 escalation condition
- parent session, dependency, stale condition, timebox/checkpoint, decision owner와 main control proxy
- stop condition
- 다른 writer가 있는지와 소유 범위

같은 역할이 반복되고 일반 prompt보다 더 나은 결과를 낸다는 forward test가 쌓이면 `.codex/agents/<role>.toml`로 승격한다. 모델과 `model_reasoning_effort`를 재현 가능하게 고정할 때도 [`model-selection.md`](model-selection.md)의 인접 configuration 비교와 [`agent-orchestration.md`](agent-orchestration.md)의 custom agent 생명주기를 먼저 충족한다.

## Codex 지원 경계

| 항목 | 현재 확인 | 설계상 의미 |
|---|---|---|
| repo Skill discovery | `$REPO_ROOT/.agents/skills` 공식 지원 | Skill 원본을 저장소에 둔다. 별도 설치 script 불필요 |
| Skill activation | 명시적 `$skill`과 description 기반 암시 호출 | 중요 pilot은 명시 호출로 테스트한다 |
| subagent 요청 | 사용자·AGENTS·Skill 지침으로 요청 가능 | 읽기 중심 병렬 조사와 독립 검토에 사용 |
| host orchestration | spawn, follow-up routing, wait, 결과 수집, thread close 지원 | 별도 manager runtime 없이 main이 control-plane proxy 역할 수행 |
| inspect·steer·stop·close | app/CLI/IDE surface별 control 지원 | surface 차이를 숨기지 않고 지원되는 control만 사용 |
| project custom agents | `.codex/agents/*.toml` 지원; format은 발전 가능 | 반복 역할을 나중에 승격하고 migration 조건 기록 |
| 모델·effort·sandbox | custom agent 또는 spawn/config에서 설정 가능; parent live permission 상속 | Skill 텍스트만으로 강제됐다고 주장하지 않음 |
| 동시 thread 상한 | `agents.max_concurrent_threads_per_session` 지원 | baseline 전 project 값 고정하지 않음 |
| Skill 간 직접 호출 API | 확인되지 않음 | Skill 체인을 결정적 함수 호출처럼 설계하지 않음 |
| 정확한 fan-out·순서 | 명시 요청은 지원되지만 deterministic 실행 보장은 문서화되지 않음 | Session Orchestrator의 manifest와 barrier를 main이 실행하고 실제 spawn·완료를 확인 |
| descendant spawn | planning record에는 subagent 내부 `spawn_agent` 미노출 실패가 있으나 raw host transcript 없음 | behavior validation으로 credit하지 않고 direct nested control을 전제하지 않음 |
| orchestrator continuation | planning record에는 same-session continuation 성공이 있으나 raw host transcript 없음 | 물리적 session 가설은 유지하되 pilot에서 직접 검증 |
| 완전한 context 격리 | main이 host tool result를 수신하므로 현재 surface에서는 불가능 | bounded packet·raw artifact locator로 오염 제한; 완전 격리가 실제 요구가 되면 PLAN-0002 밖의 새 evidence-backed decision 검토 |
| 의미 기반 근거 검증 | 기본 제공 아님 | schema/link 검사와 semantic review를 분리 |
| 문서만으로 path write 강제 | 보장되지 않음 | 권한 모드, 소유 범위, diff 검증을 함께 사용 |

동일한 이름의 Skill은 자동 병합되거나 예측 가능한 하나로 shadow된다고 가정하지 않는다. 프로젝트 Skill 이름은 충돌 가능성이 낮은 `ariadne-*` prefix를 쓴다.

## 상태와 영속성

초기에는 상태 reducer를 만들지 않는다.

- 한 대화 안의 작업: Codex plan과 대화 기록
- 복합·장기 작업: `docs/plans/active/`의 Markdown execution plan
- 실제 사실: 현재 파일, Git diff, 명령 종료값, 테스트·브라우저 산출물
- 둘 이상의 agent wave: plan 안의 작은 Lifecycle Ledger; 별도 orchestration DB 없음

다음 순서는 phase 사이의 의사소통·workflow state를 위한 표기이지 host observation state가 아니며, 코드 state machine enum이나 reducer도 아니다. lifecycle observation, contract currency, evidence completion, close semantics의 규범적 분류·판정은 [`agent-orchestration.md`](agent-orchestration.md)가 유일하게 소유한다. 이 문서는 그 값을 다시 정의하지 않는다.

```text
INTAKE -> PLANNED -> RESEARCHING? -> IMPLEMENTING? -> VERIFYING
       -> COMPLETE | NEEDS_DECISION | BLOCKED | FAILED | CANCELLED
```

어느 단계에서도 새 근거가 필요하면 `RESEARCHING`, 요구가 틀렸거나 계획이 깨지면 `PLANNED`, 사용자 판단이 필요하면 `NEEDS_DECISION`으로 돌아갈 수 있다.

## 쓰기와 부작용

초기 정책은 “전역 single writer”가 아니다.

- 같은 파일 또는 겹치는 책임 범위에는 동시에 한 writer만 둔다.
- 서로 독립된 파일은 소유 범위를 명시하면 병렬 작성할 수 있다.
- 병합 전에 메인 세션이 전체 diff와 검증 결과를 본다.
- commit, push, 배포, 외부 메시지, 결제, 삭제처럼 외부적·비가역적인 효과는 사용자 권한과 호스트 approval을 요구한다.

범용 Action Broker는 만들지 않는다. Skill 개선 후에도 scope 위반이 반복되면 해당 경로에만 patch proposal + 작은 deterministic applicator를 실험한다.

## 결정론적으로 검사할 것과 의미 판단할 것

| 결정론적 검사 후보 | 의미 검토가 필요한 것 |
|---|---|
| 파일·링크 존재, 필수 절, 허용 status | 요구 해석이 맞는가 |
| Git diff와 writable path 교집합 | 설계가 프로젝트에 적합한가 |
| 명령 종료값, 테스트·lint 결과 | 출처가 주장을 실제로 지지하는가 |
| screenshot·trace artifact 존재 | UI가 목적·위계·사용성을 충족하는가 |
| 명시된 version·digest 형식 | 비판이 타당한가, 반박이 충분한가 |

정적 validator는 왼쪽만 판정한다. 오른쪽까지 검증했다고 표현하지 않는다.

## 현재 구현의 runtime 제외

PLAN-0002 구현은 Codex SDK, Codex App Server, OpenAI Agents SDK, LangGraph와 runtime observer·graph·state runtime 코드, dependency, configuration을 명시적으로 채택하지 않는다. 이 항목들은 PLAN-0002 안의 active·deferred phase, ladder 또는 spike가 아니다.

향후 재검토는 process restart 자동 resume, multi-day human wait, 외부 event·queue, cross-process worker, 반복된 false-completion·권한 우회처럼 **직접 관찰된 material 요구나 실패**가 생긴 경우에만 시작한다. 그때도 PLAN-0002를 암묵적으로 확장하지 않고 새 decision과 plan에서 동일 vertical slice, 실패 주입, 보안·상태 소유, migration·maintenance cost를 비교한다. 기능표나 advisory research만으로 재검토를 열지 않는다.

## 외부 디자인 Skill 경계

MengTo/Skills는 디자인 전용 bounded adapter 후보다. 첫 UI pilot 전에는 설치·복사·vendor하거나 wrapper Skill을 만들지 않는다. Standard/Deep UI domain phase는 Implementation Orchestrator가 소유하고, Quick UI는 active convention·accessibility·proportionate verification 아래 main이 직접 처리할 수 있다.

- reference capture·해석: `stitched-full-page-capture`, `video-to-superprompt`, `html-to-interaction-prompts`
- proposal: `design-first-ui-prompting`과 좁은 layout/motion Skill
- 보조 QA: originality·animation·performance 관련 Skill

외부 Skill의 산출물은 후보와 관찰이다. Task-scoped Design Execution Contract는 Completion Contract와 active convention에 종속되며 active convention 자체가 아니다. Candidate 값은 convention lifecycle을 거쳐야만 승격된다. 프로젝트 목적, active convention, 접근성, 반응형·상태 동작, 성능, 독창성, 실제 브라우저 결과가 최종 판단 근거다. 설치·vendoring이 필요해지면 현재 구현 범위를 넓히지 말고 license, upstream revision, digest와 수정 내역을 별도 결정으로 검토한다.
