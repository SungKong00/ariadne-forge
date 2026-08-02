---
id: POLICY-MODEL-0001
kind: model-selection-policy
status: active
authority: normative
scope: repository
owner: project-owner
last_verified: 2026-08-02
external_checked_at: 2026-08-02
model_family_snapshot: GPT-5.6
behavior_status: unvalidated-until-calibration
---

# 작업별 모델·추론 강도 선택 정책

## 1. 목적과 현재 상태

이 문서는 Ariadne가 작업과 역할마다 **재작업 위험을 충분히 낮추는 모델과 reasoning effort를 추천·기록·재평가**하는 방법을 정한다. 이 프로젝트는 모델 사용량을 조금 아끼다 잘못된 판단·반복 구현을 만드는 것보다, 불확실하거나 실패 비용이 큰 작업에 상위 configuration을 과감히 쓰는 쪽을 선호한다.

두 종류의 근거를 구분한다.

- **현재 확인된 외부 사실**: Codex가 지원하는 모델의 공식 용도, reasoning effort, custom agent 설정 표면
- **아직 검증할 프로젝트 선택**: `ROUTINE / GENERAL / FRONTIER` profile, 역할별 초기값, 승급·강등 규칙

따라서 현재 모델 매핑은 2026-08-02 snapshot이고, 이 정책의 실제 품질·비용 효과는 PLAN-0002의 비교 평가 전까지 `unvalidated`다. 모델 이름이나 가용성이 달라져도 workflow 전체를 고치지 않도록 안정적인 profile과 변하기 쉬운 concrete mapping을 분리한다.

## 2. 서로 다른 네 가지 결정

다음을 하나의 복잡도 점수로 합치지 않는다.

| 결정 | 답하는 질문 | 값 예시 |
|---|---|---|
| workflow route | 어떤 절차와 검증 깊이가 필요한가? | Quick / Standard / Deep |
| model profile | 이 역할에 필요한 최소 모델 역량은 무엇인가? | ROUTINE / GENERAL / FRONTIER |
| reasoning effort | 선택한 모델이 이번 역할에서 얼마나 깊게 점검해야 하는가? | low / medium / high / xhigh |
| execution shape | main이 직접 하는가, bounded subagent를 쓰는가? | direct / delegated / parallel read |

네 축은 관련이 있지만 같지 않다.

- Deep 연구에서도 명확한 문서 추출·정리는 ROUTINE leaf가 할 수 있다.
- Quick 질문이라도 보안·데이터 손실에 관한 material decision이면 FRONTIER profile이 필요할 수 있다.
- deterministic test runner는 Deep 구현의 일부여도 ROUTINE일 수 있다.
- 모델을 높이는 것과 subagent 수를 늘리는 것은 별도 결정이다.

## 3. 선택 원칙

1. **reliability before token savings**: 어느 후보가 충분한지 불명확하면 재작업 비용과 오류 영향을 먼저 보고 상위 configuration을 선택한다.
2. **minimum sufficient after evidence**: 낮은 후보는 acceptance quality가 유지된다는 비교 근거가 있을 때 최적화 수단으로 채택한다.
3. **risk floor first**: 역할 이름보다 잘못됐을 때의 결과와 검증 가능성이 profile의 하한을 정한다.
4. **oracle-aware**: 정확한 test·schema·기대 출력처럼 강한 oracle이 있으면 낮출 수 있고, 미학·아키텍처처럼 oracle이 약하면 높인다.
5. **profile before product name**: 계획과 Skill에는 profile을 우선 기록하고, 실제 모델명은 time-stamped mapping과 실행 기록에 둔다.
6. **observed escalation**: 실패 원인이 입력·도구·권한 문제면 모델을 높이지 않는다. 얕은 검토나 역량 부족이라는 증거가 있을 때 effort 또는 profile을 높인다.
7. **no blind retry**: 같은 입력과 configuration으로 설명 없이 반복하지 않는다.
8. **actual over claimed**: Skill 문구가 특정 모델을 강제했다고 가정하지 않고 실제 선택된 모델·effort를 확인 가능한 범위에서 기록한다.

## 4. 현재 profile mapping

공식 Codex 설명이 직접 지지하는 것은 Luna·Terra·Sol의 상대적 용도와 기본 Power 설정이다. `ROUTINE / GENERAL / FRONTIER`라는 이름, 각 모델과의 연결, 역할별 effort 시작점은 그 설명을 바탕으로 만든 **Ariadne의 calibration 전 가설**이지 공식 권장표나 영구 순위표가 아니다.

### 모델 역량 profile

| profile | 현재 모델 mapping | 공식 설명에서 가져온 특성 | Ariadne 적용 후보 |
|---|---|---|---|
| ROUTINE | `gpt-5.6-luna` | 명확하고 반복적인 고용량 작업 | 추출·분류·변환, 구조화 요약, deterministic 검사 보조 |
| GENERAL | `gpt-5.6-terra` | 강한 추론·도구 사용이 필요한 일상 workhorse | 일반 구현·디버깅·코드 탐색·문서 검토 |
| FRONTIER | `gpt-5.6-sol` | 복잡하고 열린 고가치 작업의 분석·판단·완성도 | 깊은 연구 종합, 아키텍처·고위험 비판, 충돌 해결 |

### Reasoning effort 시작점

| 상황 | 초기 effort |
|---|---|
| 한 단계 exact 변환처럼 극도로 단순하고 강한 oracle이 있는 task | low |
| 명확한 bounded 작업의 기본값 | medium |
| 규칙이 둘 이상 상호작용하거나 내용·edge case가 조금이라도 복잡해짐 | high |
| 상충 근거·고위험·최종 decision owner·복합 불확실성 또는 one-shot 신뢰성이 중요함 | xhigh |

profile 하한과 effort 하한은 각각 판정하고 둘 다 만족해야 한다. 높은 effort가 낮은 model profile을 자동 보상하거나, 높은 model profile이 낮은 effort를 자동 보상한다고 가정하지 않는다. 예를 들어 Sol medium은 `FRONTIER profile + medium effort`이고, Terra high는 `GENERAL profile + high effort`다. calibration이 반대 근거를 주기 전에는 전자가 `FRONTIER/high` 하한을, 후자가 `FRONTIER` 하한을 충족했다고 보지 않는다.

보완 규칙:

- 가용한 Codex surface에서 분류 전 main 작업의 안전한 출발점은 현재 공식 Power 기본인 Sol medium이다. 이는 `FRONTIER profile + medium effort`일 뿐 모든 material role의 effort 하한을 충족한다는 뜻은 아니다. 요구가 명확해지면 역할별로 낮추거나, 어려운 material decision이면 high로 올린다.
- `xhigh`는 다중 출처·상충 근거·보안·데이터 손실·최종 phase/cross-phase decision owner처럼 high 대비 추가 품질을 확인할 가치가 큰 경우의 후보이다.
- `max`는 지원하는 surface·모델에서 가장 어려운 단일 품질 우선 작업의 비교 후보로만 사용한다. 대부분의 작업에 기본 적용하거나 모든 custom-agent config에서 portable하다고 가정하지 않는다.
- Ultra는 개별 역할의 model profile이 아니라 subagent를 사용하는 surface-dependent 실행 방식이므로 이 표에 넣지 않는다.
- 권장 모델을 사용할 수 없으면 같은 profile에 가장 가까운 가용 모델을 선택하고 deviation을 기록한다. 가용성 차이를 조용히 무시하지 않는다.

### 신뢰성 우선 configuration ladder

| configuration | 기본 사용 |
|---|---|
| Luna low | exact input/output과 강한 oracle이 있는 극도로 단순한 한 단계 작업만 |
| Luna medium | 명확하고 bounded한 ROUTINE 작업의 기본값 |
| Luna high | bounded하지만 여러 규칙·조건·문서 의미를 함께 처리해야 하는 ROUTINE 작업 |
| Terra medium | 요구·변경 경계·test가 명확한 단순 일반 구현 |
| Terra high | 한 component 안에서 여러 파일·edge case·검토 깊이가 필요한 구현 |
| Sol medium | 요구 모호성, 넓은 context 종합, component 간 영향처럼 model capability 폭이 더 필요한 구현·계획 |
| Sol high | 아키텍처, 상충 근거 종합, 고위험 비판·판정 |
| Sol xhigh | 위 작업이 복합적이거나 최종 decision owner이고, 실수 후 재작업 비용이 사용량보다 크다고 판단되는 경우 |

Terra high와 Sol medium 사이에서는 “같은 bounded 문제를 더 깊게 점검”하면 Terra high, “더 넓은 context·모호성·종합 판단 능력”이 필요하면 Sol medium을 우선한다. 경계가 불명확하고 오류 비용이 작지 않으면 Sol medium 이상으로 올린다.

어떤 역할이 원래 ROUTINE/GENERAL이더라도 hidden failure 비용, 시간 제약, 사용자 영향, 약한 oracle, 반복 실패 때문에 one-shot 신뢰성이 더 중요하면 **special reliability override**로 Sol xhigh를 선택할 수 있다. 이 override는 역할 label이 아니라 구체적 실패 비용과 `왜 낮은 후보의 재시도보다 낫다고 보는지`를 한 줄로 기록한다.

두 축의 신호가 동시에 있으면 model profile과 effort 각각의 더 높은 하한을 결합한다.

| model profile floor / effort floor | low | medium | high | xhigh |
|---|---|---|---|---|
| ROUTINE | Luna low | Luna medium | Luna high | Sol xhigh reliability override |
| GENERAL | Terra medium | Terra medium | Terra high | Sol xhigh reliability override |
| FRONTIER | Sol medium | Sol medium | Sol high | Sol xhigh |

예를 들어 넓은 context 종합 때문에 FRONTIER가 필요하고 edge-case 검토 때문에 high가 필요하면 Sol high다. Terra high와 Sol medium 중 하나를 임의로 고르는 문제가 아니다. 표의 configuration은 calibration 전 신뢰성 우선 기본값이며 더 낮은 조합으로 대체하려면 비교 근거가 필요하다.

## 5. 위험 하한과 조정 신호

### 초기 하한

| 관찰된 작업 조건 | 초기 하한 |
|---|---|
| 명확하고 bounded하며 reversible하고 강한 deterministic oracle이 있음 | ROUTINE 후보 |
| 여러 파일 또는 의미 판단이 필요하지만 일반적인 구현·검토이고 검증 가능 | GENERAL |
| 보안·privacy·데이터 migration·비가역 변경·public API·architecture 경계·material conflict의 최종 판정 | FRONTIER |

이는 keyword classifier가 아니다. 예를 들어 `security`라는 단어가 있어도 단순 로그 형식 변환이면 ROUTINE이 가능하고, 단어가 없어도 사용자 데이터 삭제 경로를 고르면 FRONTIER다. 결과의 중대성과 검증 가능성을 본다.

### 한 단계 높이는 신호

- 요구나 성공 조건에 해결되지 않은 모호성이 있다.
- Tier 0/1 근거가 충돌하거나 중요한 반례가 남았다.
- 실패를 빠르게 잡을 oracle이 약하거나 주관적이다.
- component·team·data boundary를 가로지른다.
- 이전 run이 사실 누락, 잘못된 완료 판정, edge case 누락으로 실패했다.
- critic 또는 advisory resolver가 blocking material finding을 제기한다.
- 한 번의 정확한 결과가 중요하고 재실행·rollback·사용자 검토 비용이 모델 사용량보다 크다.

### 낮출 수 있는 신호

- 입력·출력·scope가 작고 명시적이다.
- test, compiler, schema, exact comparison 같은 강한 oracle이 있다.
- 실패가 쉽게 되돌릴 수 있고 외부 효과가 없다.
- 같은 역할의 비교 평가에서 낮은 후보가 품질 floor를 반복 충족했다.

낮출 수 있다는 신호가 위험 하한을 자동으로 무효화하지 않는다. 고위험 결정의 mechanical subtask만 낮추고 최종 판단자는 하한을 유지한다.

## 6. 역할별 초기 추천

| 역할 | profile·effort 시작점 | 조정 조건 |
|---|---|---|
| 요구 정리·route 선택 | GENERAL medium | 모호한 대규모·고위험 요구는 FRONTIER medium/high |
| file map·검색·정형 추출 | ROUTINE medium | 극단적으로 단순할 때만 low; 규칙·내용 복잡도가 생기면 Luna high 또는 GENERAL |
| 공식 문서·저장소 evidence leaf | GENERAL medium | exact locator 수집은 ROUTINE medium; 상충 해석이면 Terra high 또는 FRONTIER |
| Research Orchestrator | FRONTIER high | source conflict·high stakes·복합 조율·최종 연구 phase disposition이면 Sol xhigh |
| Implementation Orchestrator | FRONTIER high | calibration 전 Standard/Deep 기본은 Sol high; Standard/Deep UI Design Assurance domain phase도 이 owner가 소유. conflict·architecture·고위험·재작업 고비용이면 Sol xhigh. 좁고 reversible하며 strong-oracle인 Standard 역할에서만 별도 비교 후 강등 후보 |
| 일반 구현·디버깅 | GENERAL medium | 조금 복잡하면 Terra high; 모호성·넓은 종합은 Sol medium; 고위험 경계 변경은 Sol high/xhigh |
| deterministic test·lint·schema 보조 | ROUTINE medium | 극도로 단순한 실행·전사만 low; 실패 의미와 acceptance 판정은 위험 하한 적용 |
| 독립 코드·계획 critic·resolver leaf | GENERAL high | material security·architecture finding이면 Sol high, 복합 비판이면 xhigh; 최종 phase disposition이 아니라 advisory packet 반환 |
| cross-phase route·최종 사용자 outcome 판정 | FRONTIER high | 복합·고비용이면 Sol xhigh; Session Orchestrator의 phase disposition을 대체하지 않고 mismatch는 해당 session에 반환 |
| UI reference 수집·수치 측정 | ROUTINE/GENERAL medium | 저작권·출처·상태 해석이 복잡하면 GENERAL high |
| bounded Design Execution Contract·시각 종합 leaf | GENERAL high | Completion Contract·active convention에 종속된 advisory/implementation packet을 반환; 새 visual system, 높은 독창성·완성도 요구는 FRONTIER high |

critic과 advisory resolver leaf는 finding을 만들지만 phase를 폐쇄하지 않는다. Phase를 폐쇄하는 Research/Implementation Orchestrator와 cross-phase 사용자 outcome을 판정하는 main은 각각 자신이 소유한 결정의 위험 하한보다 낮은 profile을 쓰지 않는다. 서로 다른 모델을 썼다는 사실도 독립성이나 정답의 증거가 아니다. fresh context, 원문 근거와 raw artifact 접근이 더 중요하다.

## 7. 선택·승급·강등 절차

1. 역할의 objective, 성공 oracle, 잘못됐을 때의 material consequence를 적는다.
2. 위험 하한을 정한다.
3. 모호성·근거 충돌·boundary·oracle 강도로 profile과 effort를 조정한다.
4. 재작업 비용이 큰 특수 상황이면 profile 하한과 별도로 Sol xhigh reliability override를 검토한다.
5. 추천 profile·effort와 한 줄 rationale, escalation condition을 role contract에 넣는다.
6. 실행 후 actual model·effort와 deviation, 실패 유형을 기록한다.
7. 실패 원인을 먼저 나눈다.
   - context·instruction 누락 → 입력과 contract 수정
   - tool·permission·환경 실패 → 실행 조건 수정
   - 검토 깊이 부족 → 같은 profile에서 effort 상향
   - 판단 역량·모호성 처리 부족 → profile 상향
   - 성공 oracle 부재 → 검증 설계 또는 사용자 결정
8. 같은 configuration의 첫 실패 후 원인에 맞는 변경 없이 한 번 더 실패하면 blind retry를 중단한다. 새 근거와 rationale가 있을 때만 재시도하고, 아니면 재계획·상향·`NEEDS_DECISION` 중 하나를 택한다.
9. 강등은 직감이 아니라 같은 역할의 대표 task 비교에서 품질 floor가 유지될 때만 한다.

## 8. 적용 표면과 Model Binding

profile 추천이 실제 모델 선택으로 이어지는 방법은 Codex surface마다 다르다.

| 실행 위치 | 적용 방법 | 한계·대응 |
|---|---|---|
| 현재 main task | composer·CLI·session 설정의 현재 모델을 사용하고 profile을 추천 | Skill이 실행 중 main 모델 변경을 보장하지 않음; 위험 하한 미달이면 지원되는 model switch, 적합한 delegated Session Orchestrator·명시된 decision owner 또는 사용자 결정을 사용 |
| ad hoc subagent | 지원되는 spawn 요청에 model·reasoning override를 명시 | parent permission·가용 모델을 따르며 actual 값을 기록 |
| 반복 custom agent | `.codex/agents/<role>.toml`의 `model`, `model_reasoning_effort` | calibration·승격 조건 전에는 만들거나 pin하지 않음 |

main의 현재 모델이 위험 하한보다 낮고 변경·위임도 불가능하면, 그 역할의 material decision을 완료한 것처럼 폐쇄하지 않고 `NEEDS_DECISION` 또는 `INSUFFICIENT_EVIDENCE`로 둔다.

Quick direct 작업은 추천과 실제 값이 다를 때만 한 줄로 남겨도 된다. Standard/Deep의 main material role과 material decision을 내리는 delegated role은 별도 중복 block을 만들지 않고 [`agent-orchestration.md`](agent-orchestration.md)의 Role Contract 안에 다음 Model Binding을 넣는다. 실행 전에 recommendation과 binding status를 쓰고, 실행 후 actual 값을 채운다.

```markdown
model_binding:
- model_profile_floor: ROUTINE | GENERAL | FRONTIER
- effort_floor: low | medium | high | xhigh
- recommended: model / effort
- rationale_and_escalate_if:
- binding_status: verified | deviated | unobservable
- actual: model / effort / deviation
```

`verified`는 actual model·effort가 관측되고 두 하한을 만족할 때만 쓴다. `deviated`는 actual 값이 관측되지만 하한과 다르거나 availability fallback을 쓴 경우, `unobservable`은 actual 값을 확인할 수 없는 경우다.

- ROUTINE/GENERAL 하한이고 reversible하며 강한 oracle이 있으면 `unobservable`이어도 진행할 수 있다. 다만 profile 준수를 주장하지 않고 직접 검증·독립 review 결과와 함께 limitation을 보고한다.
- FRONTIER 하한, weak oracle 또는 고위험 material decision은 `unobservable` 상태의 결과만으로 폐쇄하지 않는다. 관측 가능한 적합 Session Orchestrator·명시된 decision owner, 사용자의 model 확인·전환, 또는 `INSUFFICIENT_EVIDENCE`가 필요하다.
- `deviated`가 하한 미달이면 같은 규칙을 적용한다. 더 높은 가용 configuration이라는 사실이 확인되면 deviation 이유와 calibration 상태를 남긴다.

정형 추출처럼 bounded한 delegated leaf는 `role → profile/effort; rationale; escalate-if` 한 줄만 넣고, 같은 wave의 actual 값은 실행 기록에서 묶어 남길 수 있다. material·deviated·unobservable 역할만 확장 Model Binding을 사용한다.

## 9. 비교 평가와 고정 조건

모델 선택 정책과 Skill 효과를 같은 실험에서 동시에 바꾸지 않는다.

- **Skill 비교**: task, workspace, permission, tools, exact model·effort, retry/time budget을 고정한다.
- **모델 calibration**: 같은 task와 Skill에서 인접 후보 하나만 바꾼다. 예: Luna low ↔ medium, Luna medium ↔ high, Terra medium ↔ high, Terra high ↔ Sol medium, Sol high ↔ xhigh.

pinning을 위한 calibration은 단일 run 승부로 끝내지 않는다.

- 같은 case·초기 상태에서 후보별 최소 2회의 isolated paired run을 수행한다.
- 순서 효과를 줄이도록 후보 실행 순서를 교차하거나 무작위화하고 fresh context를 쓴다.
- grading rubric과 acceptance artifact는 후보를 보기 전에 고정한다.
- 가능한 경우 grader에게 model label을 숨기고, 동일 grader protocol을 사용한다.
- 평균 headline 하나가 아니라 case별 결과, 실패 유형과 run 간 분산을 보고한다.

대표 task set은 최소한 bounded extraction, 일반 구현, evidence conflict synthesis, critic/advisory resolver, false-completion, design contract를 포함한다. 다음을 함께 비교한다.

- acceptance·contract pass와 결정 정확성
- false-completion, scope violation, 근거 누락
- critic finding disposition의 타당성
- retries와 사용자 개입
- wall-clock, token·비용 정보
- grader의 독립성과 known invalidity risk

품질·false-completion·재작업을 1차 기준으로 보고 비용·지연은 2차 기준으로 본다. 낮은 후보는 단순히 평균 점수가 비슷해서가 아니라 material failure와 재작업률이 악화되지 않는다는 근거가 있을 때만 채택한다. 초기 표본이 작거나 차이가 불명확하면 상위 후보를 유지한다. 낮은 후보를 채택한 뒤에도 상위 profile의 sample audit로 놓친 오류를 확인하되 audit 비율은 baseline data 후 정한다.

`.codex/agents/<role>.toml`에 concrete model·`model_reasoning_effort`를 고정하려면 다음이 모두 필요하다.

- 같은 역할이 서로 다른 실제 작업에서 3회 이상 반복됨
- 적어도 두 개의 인접 configuration 비교
- 위 paired-run·순서·grader 통제를 충족한 calibration report
- 낮은 후보가 품질 floor를 충족하거나 높은 후보의 material 개선이 확인됨
- model 교체·deprecation 시 fallback과 재평가 조건 기록

그 전에는 `ariadne-workflow` Skill이 profile을 추천하고 main Codex가 현재 가용 모델을 선택한다.

## 10. 선택지와 trade-off

| 방식 | 장점 | 단점 | 판정 |
|---|---|---|---|
| 항상 Sol high 이상 | 단순하고 높은 capability headroom | 비용·지연, routine 작업 과잉, 작업별 개선 근거 없음 | 채택하지 않음 |
| 역할마다 모델명을 영구 고정 | 재현성과 예측 가능성 | 모델 교체·역할 변형·위험도 차이에 취약 | calibration 뒤 반복 역할에만 사용 |
| Codex의 자유 선택만 사용 | 가볍고 가용 모델 변화에 적응 | 선택 근거·재현·비용 통제가 약함 | Quick 또는 actual 기록이 가능한 경우에 한정 |
| 점수식 classifier | 자동화하기 쉬움 | 가짜 정밀도, 경계값 gaming, 새로운 위험 누락 | 초기에는 사용하지 않음 |
| reliability-biased profile + risk floor + 비교 평가 | 재작업 방지, 유연성, concrete model 교체 용이 | 사용량 증가, 기록·calibration 비용, 완전 결정론 아님 | **현재 선택** |

이 선택은 Codex가 이 분류를 정확히 보장한다는 뜻이 아니다. 하드코딩한 graph 대신 LLM 판단을 허용하되, 위험 하한·기록·raw evidence·독립 검토·forward evaluation으로 판단 권한을 제한하는 방식이다.

## 11. 외부 근거와 재검토

2026-08-02 확인한 OpenAI 공식 문서는 다음을 명시한다.

- [Codex Models](https://learn.chatgpt.com/docs/models): Sol은 복잡하고 열린 고가치 작업, Terra는 일상적인 workhorse, Luna는 명확하고 반복적인 작업에 적합하며, 기본 Power는 Sol medium이다.
- [Codex Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): agent별 모델·reasoning 선택, 미고정 시 Codex 선택, custom agent의 `model`·`model_reasoning_effort` 설정과 상속 규칙을 설명한다.
- [Codex Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference): 모델과 reasoning effort의 실제 구성 표면을 정의한다.
- [OpenAI latest model guide](https://developers.openai.com/api/docs/guides/latest-model): 높은 reasoning이 항상 최선이라고 가정하지 말고 대표 작업에서 현재 설정과 낮은 설정을 비교하라는 최적화 원칙을 제공한다.

공식 문서가 지지하는 것은 모델 특성, 설정 가능성과 일반적인 effort 조절 원칙이다. Ariadne의 profile 이름·concrete mapping, exact effort 시작점, 위험 하한, 3회 승격 기준이 실제로 최적이라는 주장은 공식 사실이 아니라 프로젝트 가설이다.

다음이면 즉시 재검토한다.

- 모델 family, 이름, 가용 reasoning effort 또는 Codex config precedence 변경
- deprecation·가격·usage limit 변화가 현재 mapping에 영향
- 같은 role에서 profile exception이 3회 이상 발생
- 하위 모델의 false-completion·근거 누락 또는 상위 모델의 과잉 비용이 반복
- Codex surface에서 profile recommendation을 실제 model binding으로 연결하는 방식이 변경
