---
id: DOCS-INDEX
kind: registry
status: active
authority: normative-map
scope: repository
owner: project-owner
last_verified: 2026-08-02
---

# Ariadne Forge 문서 지도

이 디렉터리는 프로젝트 지식의 원본이다. `AGENTS.md`는 이 지도로 들어오는 짧은 입구이며, 같은 규칙을 여러 문서에 복제하지 않는다.

## 현재 권위 문서

| 문서 | 역할 | 권위 |
|---|---|---|
| [`project.md`](project.md) | 목표, 비목표, 품질 기준 | normative |
| [`architecture.md`](architecture.md) | 현재 선택한 시스템 구조와 확장 조건 | normative |
| [`operating-model.md`](operating-model.md) | 라우팅, 연구, 비판, 구현, 검증, 문서 운영 | normative |
| [`model-selection.md`](model-selection.md) | 역할별 모델 profile·reasoning 선택과 calibration | normative; concrete mapping은 time-stamped snapshot |
| [`agent-orchestration.md`](agent-orchestration.md) | subagent topology·role contract·생명주기·custom agent 승격 | normative; canonical lifecycle statically aligned, behavior unvalidated; no Research/B10 behavior pilot claimed |
| [`conventions/README.md`](conventions/README.md) | convention 형식·우선순위·등록부 | normative |
| [`decisions/0001-codex-native-skill-first.md`](decisions/0001-codex-native-skill-first.md) | 현재 구조를 선택한 이유와 대안 | accepted decision |
| [`plans/active/0002-codex-native-skill-first-plan.md`](plans/active/0002-codex-native-skill-first-plan.md) | 다음 구현 단계와 검증 기준 | active execution plan |
| [`research/final-plan-validation-20260801.md`](research/final-plan-validation-20260801.md) | 최종 계획의 근거·충돌·한계 | advisory evidence |
| [`research/codex-lifecycle-observation-20260802.md`](research/codex-lifecycle-observation-20260802.md) | Codex lifecycle 관찰의 공식 source·schema 경계와 미해결 한계 | advisory source evidence; version-limited, not a Research pilot, local behavior validation, or universal proof |

## 현재 실행 산출물

| 산출물 | 역할 | 상태 |
|---|---|---|
| [`.agents/skills/ariadne-workflow/SKILL.md`](../.agents/skills/ariadne-workflow/SKILL.md) | Quick/Standard/Deep route, phase owner, host lifecycle와 evidence completion 진입 Skill | static oracle alignment only; B10 behavior unvalidated; no current paired run or actual pilot claim |
| [`../evals/ariadne-workflow/runs/baseline-001/report.md`](../evals/ariadne-workflow/runs/baseline-001/report.md) | no-Skill RED baseline 기록 | recorded revision / prior cases only; not current lifecycle behavior evidence |
| [`../evals/ariadne-workflow/runs/with-skill-001/report.md`](../evals/ariadne-workflow/runs/with-skill-001/report.md) | with-Skill prior-case 기록 | recorded revision / prior cases only; not a current paired or universal claim |
| [`../evals/ariadne-workflow/fixtures/b10-lifecycle-observation/scenarios.md`](../evals/ariadne-workflow/fixtures/b10-lifecycle-observation/scenarios.md) | 12-case lifecycle observation grader oracle | predeclared and static checked; not executed; behavior-unvalidated; no B10 run report |
| [`../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md`](../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md) | PLAN-0003 W0-R3 frozen oracle | identity-only `FROZEN_ON_V0_RECEIPT`; 23 canonical blocks exact/matching; its `NOT_RUN` cells are frozen oracle state, not current execution results |
| [`../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/run-record.md`](../evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/run-record.md) | W2 candidate execution record | B/F1 owner `PASS`, B/F2 second owner `PASS`, B/F3 owner `FAIL`; B/F4 and two mode smokes `NOT_RUN` after required termination; no independent grade, bridge, compatibility, adoption, effect, or model claim |

## 개선 초안

아래 문서는 다음 개선 후보를 검토하기 위한 초안이며 현재 규범이나 실행 순서를 바꾸지 않는다.

| 문서 | 검토 주제 | 상태·권위 |
|---|---|---|
| [`plans/drafts/0003-explicit-skill-composition-draft.md`](plans/drafts/0003-explicit-skill-composition-draft.md) | PLAN-0002 baseline A를 보존한 same-owner embedded-method B의 historical candidate execution disposition; 1-vs-3은 deferred Option E | completed; historical partial candidate execution; W0-R3 freeze receipt와 W2 partial execution을 구분해 기록하며, required termination 뒤 재개 지시·adoption 권위 없음 |

## 문서 종류와 쓰임

| 종류 | 답하는 질문 | 상태 예시 | 규범 여부 |
|---|---|---|---|
| project / policy / convention | 지금 무엇을 지켜야 하는가? | active, superseded | active만 규범 |
| decision | 왜 이 선택을 했는가? | proposed, accepted, superseded | accepted 결정 자체는 유효하나 현재 규칙은 policy·convention에도 반영 |
| plan | 앞으로 어떤 순서로 바꿀 것인가? | draft, active, completed, superseded | 해당 작업 범위에서만 실행 기준 |
| research | 어떤 근거와 반례가 있는가? | draft, reviewed, stale | advisory; 단독으로 프로젝트 규칙을 바꾸지 않음 |
| guide / reference | 어떻게 사용하며 무엇이 존재하는가? | active, stale | 명시된 범위에서 설명 자료 |

Diátaxis의 tutorial/how-to/reference/explanation 구분은 사용자·개발자 안내 문서가 실제로 생길 때 적용한다. 정책·계획·연구·결정의 권위 구분을 대신하지 않는다.

## 공통 metadata

현재 지식으로 취급되는 Markdown 문서는 YAML frontmatter에 다음을 둔다.

```yaml
---
id: TYPE-UNIQUE-ID
kind: registry | project-charter | architecture | operating-policy | model-selection-policy | agent-orchestration-policy | convention-registry | convention | decision | execution-plan | research-report | validation-report
status: draft | candidate | active | accepted | completed | deprecated | superseded | rejected | stale
authority: normative | normative-map | decision | execution | advisory-evidence
scope: repository-or-bounded-scope
owner: accountable-owner
last_verified: 2026-08-01
supersedes: null
aliases: []
---
```

모든 status를 모든 kind에 사용하지 않는다. project·policy·convention은 `active`일 때만 현재 규범이고, decision은 `accepted`, plan은 `active`, research는 `completed`여도 advisory다. 외부 자료 확인이 핵심인 research는 `last_verified` 대신 또는 함께 `checked_at`을 쓸 수 있다. `supersedes`, `aliases`, `applies_to`는 관계·검색·적용 범위가 실제로 있을 때만 채운다.

## 문서 유형별 최소 계약

| kind | 최소 본문 | 만들지 않는 경우 |
|---|---|---|
| project-charter | 목적, 품질 목표, 비목표, 성공 기준, 중단·재검토 원칙 | 작업 하나의 요구만 기록할 때 |
| architecture | 맥락·경계, 구성 요소, invariant, 지원 사실/가설, 대안·승격 조건 | 구현 구조가 아직 전혀 없을 때 상세 component 예측 |
| operating-policy | trigger, 입력, 역할·권한, 산출물, 검증·중단·reopen 규칙 | 일회성 실행 순서만 필요할 때 |
| model-selection-policy | 안정적 profile, 현재 모델 mapping, 위험 하한, 기록·승급·재검토 규칙 | 모델명을 여러 workflow 문서에 직접 반복할 때 |
| agent-orchestration-policy | spawn gate, role contract, dependency·wait·steer·stop·close, custom agent lifecycle | agent 하나의 일회성 prompt만 필요할 때 |
| convention | [`conventions/README.md`](conventions/README.md)의 template과 lifecycle | 일회성 선택, formatter 소유 형식, stack 미정 분야 |
| decision | context, drivers, options/trade-off, decision, consequences, revisit, evidence | 쉽게 되돌릴 작은 local choice |
| execution-plan | completion contract, Document Binding, 단계·owner·검증, stop/replan, Document Impact | 짧고 명백한 Quick 변경 |
| research-report | 질문·범위, source plan/locator, claim matrix, 대안, 충돌·한계, handoff | 현재 저장소 사실이나 작은 실험으로 바로 판정 가능할 때 |
| validation-report | research-report 계약 + 판정, 검증 범위·비범위, KEEP/MODIFY/STOP, 잔여 위험 | 실제 검증 없이 기존 결론을 재서술할 때 |

문서 유형이 다르다는 이유로 같은 규칙을 복사하지 않는다. 현재 규칙은 project/policy/convention 한 곳이 소유하고, decision은 이유, plan은 실행 순서, research는 근거와 한계를 링크한다.

## 충돌과 신선도

- 한 규칙의 권위 단위는 단순한 “주제”가 아니라 `(kind, scope, applicability, version)`이다.
- 같은 단위에 active 문서가 둘이면 자동 선택하지 않는다. 하나를 supersede하거나 owner 결정을 받는다.
- `last_verified`는 내용 검증 시점이지 자동 만료일이 아니다. 의존성 major 변경, 지원 환경 변경, 세 번 이상의 예외, 실제 실패가 생기면 즉시 재검토한다.
- 결정 기록은 과거를 보존한다. 새 결정이 기존 결정을 대체할 때 기존 파일을 덮어쓰지 않고 `supersedes`로 연결한다.

## 현재 보존 자료

`plans/active/0001-ariadne-forge-foundation-plan.md`와 기존 research packet은 초기 대안과 검토 이력이다. 일부 packet의 schema 검사는 구조와 내부 참조만 확인했으며 외부 출처의 의미·정확성을 자동 검증한 것이 아니다. 현재 선택과 충돌하면 이 인덱스가 가리키는 active 문서를 따른다.
