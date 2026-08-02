---
id: POLICY-OPERATING-0001
kind: operating-policy
status: active
authority: normative
scope: repository
owner: project-owner
last_verified: 2026-08-02
---

# Evidence-first 작업 운영 모델

## 1. 핵심 원리

1. 추론을 없애지 않고 **추론과 권한을 분리**한다.
2. 모든 미세 선택이 아니라 결과를 바꿀 수 있는 **material decision**에 근거 부담을 둔다.
3. 비판, 다수결, schema 통과, 그럴듯한 설명은 각각 진실의 충분조건이 아니다.
4. 진행 중 새 정보가 생기면 route, 연구, 계획을 다시 열 수 있다.
5. 절차적 규칙으로 충분한 동안 code runtime을 만들지 않는다.
6. 외부 사실, 프로젝트 규범, 실행 증거, 사용자 선호를 같은 종류의 근거로 섞지 않는다.

### Material decision

다음 중 하나에 해당하면 material이다.

- 사용자에게 보이는 동작이나 acceptance criterion을 바꾼다.
- 아키텍처, dependency, 데이터·보안 경계, public API를 바꾼다.
- 새 convention을 만들거나 기존 active convention을 벗어난다.
- 되돌리기 어렵거나 외부 시스템에 효과를 낸다.
- 실패했을 때 후속 작업이 잘못된 가정 위에서 계속될 수 있다.

가까운 코드의 active convention을 그대로 적용하는 변수명·문법·작은 refactor에는 별도 ADR을 만들지 않는다. 적용한 convention과 테스트가 묶음 근거다.

## 2. 근거 부담

| 종류 | 최소 근거 | 추가 조건 |
|---|---|---|
| 사용자 요구·선호 | 현재 사용자 지시 | 저장소 규범을 영구 변경하려면 문서 반영 또는 결정 기록 |
| 현재 저장소 사실 | 직접 읽은 파일·Git 상태·실행 결과 | worker 요약만 인용하지 않음 |
| 외부 기능·API 사실 | 현재 버전의 공식 문서·공식 저장소 | version-sensitive면 확인 날짜와 버전 기록 |
| 아키텍처·기술 선택 | 대안, 판단 기준, 프로젝트 적합성, 반례 | 고비용·고위험이면 prototype 또는 비교 실행 |
| 코드·UI 완료 | acceptance criterion별 직접 증거 | 독립 검토와 문서 영향 확인 |
| 고위험 외부 효과 | 위 근거 + 명시적 사용자 승인 | 권한·rollback/reconciliation 확인 |

근거가 없으면 다음 중 하나를 택한다.

- 조사한다.
- 가설 또는 candidate로 낮춘다.
- 더 작은 reversible 선택으로 바꾼다.
- 사용자에게 결정을 요청한다.
- `BLOCKED` 또는 `INSUFFICIENT_EVIDENCE`로 끝낸다.

## 3. Intake와 Document Binding

변경 전 다음을 순서대로 확인한다.

1. 사용자 목표, 제외 범위, 위험한 해석을 적는다.
2. 대상 파일·기능·문서 scope를 추정한다.
3. 적용되는 `AGENTS.md` chain을 확인한다.
4. `docs/README.md`에서 현재 project·architecture·policy를 찾는다.
5. convention registry에서 path, applicability, alias, 설명으로 후보를 찾고 본문을 읽는다.
6. 관련 accepted decision과 active plan을 확인한다.
7. 누락·충돌·stale 의심을 기록한다.

Standard/Deep plan에는 다음 표를 넣는다.

| 문서 | 적용 이유 | 상태·신선도 | 충돌·조치 |
|---|---|---|---|
| `path` | 이 작업에 적용되는 이유 | active / candidate / stale? | 없음 / 재검토 / owner 결정 |

검색은 ID나 exact label 하나에 의존하지 않는다.

- 대상 path와 scope를 먼저 사용한다.
- title, `aliases`, 한국어·영어 표현, 본문 설명을 full-text 검색한다.
- LLM은 좁혀진 후보 본문을 읽고 적용 가능성을 판정한다.
- canonical ID는 찾기 위한 유일한 키가 아니라 선택 후 관계를 안정적으로 기록하는 키다.

초기에는 vector store나 embedding index를 만들지 않는다. paraphrase·오탈자·한영 fixture에서 실제 recall 누락이 측정되면 lexical+semantic retrieval spike를 연다.

## 4. 경로 선택

Route는 LLM의 임시 판단이며 Codex가 보장하는 분류기가 아니다.

| 경로 | 전형적 작업 | 최소 흐름 |
|---|---|---|
| Quick | 설명, 읽기, 명백한 한 파일 수정, 낮은 위험 | 관련 문서 확인 → 응답/수정 → 직접 검증 → 문서 영향 |
| Standard | 여러 파일, 설계 선택, 새 테스트, 중간 불확실성 | 완료 계약 → 문서 바인딩 → 계획 → 필요 시 연구/비판 → 한정 구현 → 독립 검증 → 문서 영향 |
| Deep | 새 아키텍처, 넓은 변경, 고위험, 외부 근거 충돌 | 완료 계약 → 연구 팀 → 종합·비판·해결 → 단계 계획 → 단계별 구현·검증 → 최종 독립 판정 |

파일 수만으로 정하지 않는다. 다음 신호를 함께 본다.

- 요구 모호성·새로움
- 영향 범위와 되돌리기 비용
- security·privacy·데이터 위험
- 외부 사실의 최신성
- 검증 난이도와 관측 가능성
- 관련 convention의 존재·신선도
- 병렬 독립 작업의 실제 유무

불확실하면 상위 경로를 임시 선택하되, 첫 조사 뒤 불필요한 절차가 확인되면 낮출 수 있다. 반대로 Quick 중 새 위험이 발견되면 즉시 올린다. under-routing 0은 보장이 아니라 holdout 평가 목표다.

### 모델 선택은 별도 축이다

Route는 절차의 깊이이고 모델 profile은 해당 역할에 필요한 역량이다. 둘을 `Quick=Luna`, `Deep=Sol`처럼 고정 결합하지 않는다. 역할의 material risk, oracle 강도, 모호성, 근거 충돌을 기준으로 [`model-selection.md`](model-selection.md)의 `ROUTINE / GENERAL / FRONTIER` profile과 reasoning effort를 정한다.

Standard/Deep의 main material role과 material decision을 내리는 delegated role은 추천 profile·effort, rationale, escalation condition을 role contract에 넣고 실행 후 actual model·effort를 확인 가능한 범위에서 기록한다. Bounded mechanical leaf는 축약 binding을 쓸 수 있다. Skill 문구만으로 특정 모델 적용을 보장하지 않는다.

### 판단 계층과 host control을 분리한다

위임을 열면 [`agent-orchestration.md`](agent-orchestration.md)를 따른다.

- Quick은 main이 직접 처리할 수 있다.
- Standard/Deep에서 research phase를 열면 물리적인 Research Orchestrator session이 질문 분해, leaf 계약, packet 판정, follow-up과 최종 보고를 소유한다.
- Standard/Deep에서 implementation phase를 열면 물리적인 Implementation Orchestrator session이 단계 분해, planner·writer·verifier 계약, 진척·재계획·검증 판정과 최종 보고를 소유한다.
- 현재 surface에서 main은 session 생성, safety·permission 검사와 spawn·send·wait·stop·close만 대행하는 control-plane proxy다. leaf packet을 재종합하지 않고 parent session에 전달한다.
- planning record에는 direct descendant spawn 실패와 same-session continuation 성공이 적혀 있지만 raw host transcript가 없어 behavior validation으로 credit하지 않는다. 따라서 direct nested control을 전제하지 않고 host-mediated hierarchy를 pilot 대상으로 유지한다.

## 5. Completion Contract

Standard/Deep 작업은 delegation이나 구현 전에 다음을 고정한다.

```markdown
## Outcome
사용자에게 생길 구체적 결과

## Verification
- acceptance criterion과 각각의 관측 방법

## Constraints
- 반드시 지킬 project·security·compatibility 조건

## Boundaries
- writable paths
- forbidden paths·외부 효과

## Stop when
- 완료, needs-decision, blocked, failed 조건
```

완료 조건은 “코드를 작성함”이 아니라 관측 가능한 결과다. 테스트를 못 돌리면 이유와 미검증 범위를 남기며 통과한 것처럼 표현하지 않는다. 적용되는 agent lifecycle가 있는 repository/phase의 `COMPLETE`는 [`agent-orchestration.md`](agent-orchestration.md)의 evidence gate를 통과해야 하며, host completion, completed turn/item 또는 phase semantic packet 하나만으로는 충분하지 않다.

### Stage gate receipt

체크리스트는 기억 보조가 아니라 **다음 단계로 넘어가기 위한 종료 증거**로 사용한다. 하나의 거대한 목록을 모든 작업에 적용하지 않고 다음 세 층으로 나눈다.

1. **Core gate**: 모든 작업에 적용되는 짧은 불변식
2. **Phase gate**: research, planning, implementation, verification처럼 실제로 열린 phase에만 적용
3. **Domain gate**: UI, security, data migration, external effect처럼 해당 위험이 있을 때만 적용

Standard/Deep의 phase 종료 시 다음 receipt를 남긴다. Quick은 같은 의미를 한두 줄로 축약할 수 있다.

Skill-only MVP에서 이 receipt는 hard enforcement가 아니라 behavioral forcing function이다. 예상 receipt가 없거나 잘못된 역할이 승인했으면 main은 다음 phase를 열지 않는 규칙으로 운용하고, 반복 누락이 측정될 때만 좁은 validator로 승격한다.

```yaml
gate:
status: PASS | REOPEN | NEEDS_DECISION | BLOCKED
basis_locators: []
unresolved: []
next_authorized_action:
decision_owner:
```

Core gate는 다음 여섯 항목이다.

| Gate | 통과 조건 |
|---|---|
| Outcome | 관측 가능한 outcome, verification, boundary, stop condition이 있다. |
| Document Binding | 적용 문서, 적용 이유, 신선도·충돌 조치와 실제 read receipt가 있다. |
| Material Decision | 각 material decision에 아래 Basis Card 또는 명시적 fallback disposition이 있다. |
| Research Trigger | 연구 여부 또는 생략 근거가 있고 새 불확실성에 따라 다시 열 수 있다. |
| Authority/Scope | decision owner, writable scope, effective permission, dependency와 stale 조건이 있다. |
| Closure | acceptance별 raw evidence, 독립 검토, 잔여 위험과 Document Impact가 있다. |

Material Decision Basis Card는 다음 최소 필드를 가진다.

```yaml
decision:
materiality_axis:
  # behavior | architecture | dependency | data-security | public-api
  # convention | irreversible-effect | cascading-assumption
citable_basis_present: YES | NO
basis:
  - kind: user-requirement | project-policy | repository-fact |
          direct-result | current-official-source
    locator:
    supports_exactly:
reasoning_bridge:
counterevidence_or_limitation:
reversibility_and_blast_radius:
disposition: ADOPT | RESEARCH | REVERSIBLE_CANDIDATE |
             NEEDS_DECISION | BLOCKED
owner:
verification_or_revisit_condition:
```

`citable_basis_present: YES`는 결론 전체가 비추론적이라는 뜻이 아니다. 검증 가능한 요구·정책·저장소 사실·실행 결과·현재 공식 source가 판단 기반을 실제로 지지하고, 남은 추론 연결과 한계를 공개했다는 뜻이다. `NO`이면 조용히 진행하지 않고 연구, reversible candidate, 사용자 결정 또는 중단으로 disposition한다.

체크리스트 누락과 gaming을 줄이기 위해 phase exit는 세 번 나눠 본다.

1. 요구·계획·diff에서 material decision 후보를 발견한다.
2. 기록된 decision의 locator와 `supports_exactly`, 반대 근거, 검증 조건을 확인한다.
3. fresh-context verifier가 기록되지 않은 material decision과 raw evidence mismatch를 다시 찾는다.

locator 존재, checklist 완료율, source 개수는 의미적 타당성의 대리 지표가 아니다. “material decision 없음”도 scope·plan·diff를 근거로 설명한다. 정적 validator는 필드·링크·status 같은 구조만 검사하고 semantic truth를 판정했다고 표현하지 않는다.

## 6. Research를 여는 원리

연구는 닫힌 keyword whitelist로 결정하지 않는다. 다음은 강한 신호이지 전부 충족해야 하는 규칙이 아니다.

- 사용자가 조사·비교·최신 확인을 요청했다.
- version-sensitive 외부 API, 법·보안·표준·제품 기능을 전제로 한다.
- 중요한 선택지 사이 trade-off가 있고 프로젝트 근거가 없다.
- active convention이 없거나 실제 코드·요구와 충돌한다.
- source가 서로 충돌하거나 한 source family에 편중됐다.
- 디자인 수치·패턴이 취향이 아니라 채택 근거를 요구한다.
- planner, worker, reviewer 중 누구든 낮은 confidence나 hidden assumption을 발견했다.

다음이면 연구를 생략할 수 있다.

- 현재 authoritative project doc와 직접 실행 증거가 답을 충분히 정한다.
- reversible한 작은 실험이 문헌 조사보다 더 직접적이다.
- Quick 질문이 안정된 사실이고 사용자가 출처를 요구하지 않았다.

Standard/Deep에서 생략하면 한 줄 rationale을 남긴다. 연구 필요성은 Intake에서 한 번만 판단하지 않고 plan exit, 구현 중 전제 변경, verification mismatch에서 다시 확인한다. 어떤 역할도 새 material uncertainty를 발견하면 연구를 다시 열 수 있다.

각 확인 시 고정 신호 목록뿐 아니라 다음 열린 질문을 함께 사용한다.

> 지금 틀리면 후속 작업을 무효화하거나 크게 재작업하게 만들지만 아직 기록되지 않은 전제가 있는가?

## 7. Research Session

### 질문과 source plan

먼저 결정 질문, scope/non-scope, 신선도 기준, 채택 기준을 적는다. 그다음 주제에 맞게 lane을 동적으로 고른다. 예시는 다음과 같다.

- 공식 문서·표준
- 공식 저장소와 실제 API·코드
- 논문·일차 연구
- 신뢰할 수 있는 실무 사례
- 커뮤니티의 failure report와 반례
- 로컬 프로젝트 사실

모든 연구에 모든 lane을 열지 않는다. Standard/Deep 연구가 열리면 main은 먼저 Research Orchestrator session에 결정 질문, completion contract, Document Binding과 source 제약을 준다. Research Orchestrator가 주제에 맞는 lane과 초기 leaf 수를 판단해 `DELEGATION_REQUEST`를 만들고, main은 안전 검사 뒤 host spawn을 대행한다. 초기 leaf는 최대 3개가 기본이지만 hard threshold는 아니다. 한 lane만으로도 material gap을 닫을 수 있으면 줄이고, 세 개를 넘겨야 하면 독립성·추가 가치·검증 가능성을 설명한다.

leaf packet은 main을 거쳐 Research Orchestrator에 전달된다. Research Orchestrator가 관련성·출처 품질·상충·누락을 판정하고, 결정에 영향을 주는 gap에만 좁은 follow-up을 요청하며, critic 결과의 수용·반박·미해결 disposition까지 마친 뒤 close authorization 없는 `RESEARCH_COMPLETE`를 main에 올린다. Main은 leaf 원문을 대신 종합하지 않고 raw evidence를 독립 검사한다. `EVIDENCE_COMPLETE`를 기록해 같은 Research Orchestrator에 receipt로 보낸 뒤에만 dependent Implementation을 열며, close confirmation은 이 dependency gate와 별개다.

### Source tier

| Tier | 예 | 주 용도 |
|---|---|---|
| 0 | 사용자 요구, 현재 파일·Git·raw 실행 결과 | 프로젝트 사실과 권위 |
| 1 | 공식 문서·표준·공식 저장소·일차 연구 | 외부 사실·기능·안전 요구 |
| 2 | 원저자 설명, maintainer 자료, 검증된 reference implementation | 해석·설계 의도 |
| 3 | 전문 실무 글·커뮤니티 사례 | failure mode·실무 trade-off 탐색 |
| 4 | 검색 snippet·집계·출처 불명 주장 | 후보 발견만; 최종 근거로 채택하지 않음 |

검색 결과 설명문만 인용하지 않고 실제 페이지·파일을 연다. 외부 URL이 존재한다는 것과 그 내용이 claim을 지지한다는 것을 분리한다.

### Research report 형식

Canonical human artifact는 Markdown이다. JSON은 tool/API 교환이 실제로 필요할 때의 export다.

```text
frontmatter: id, kind, status, scope, owner, checked_at, aliases
# Decision question
## Scope and non-scope
## Source plan and queries
## Tiered source table
## Claim matrix
## Options and trade-offs
## Conflicts and unresolved questions
## Adopted candidates
## Rejected or weak claims
## Recommendation, confidence, conditions
## Implementation handoff
```

Source table은 최소한 source ID, title, URL/path, tier, checked date/version, exact locator, 직접 지지하는 claim, limitation을 포함한다.

Claim matrix는 statement, `fact / project-choice / practice / inference / hypothesis`, supporting·contradicting source, applicability, confidence, `supported / disputed / insufficient`를 분리한다.

Schema validator가 검사할 수 있는 것은 필수 field·내부 reference·URL 형식 정도다. source 내용의 정확성이나 semantic support까지 자동 검증했다고 쓰지 않는다.

## 8. 비판·반박·해결

비판자는 판결자가 아니라 결함 탐지자다. material finding에는 다음이 필요하다.

- 정확한 대상과 주장
- 근거 또는 재현 절차
- 영향과 severity
- 어떤 자료가 나오면 finding이 반박되는지
- 확인하지 못한 부분

원 작성자는 먼저 finding을 정확히 재진술하고 반박 가능성을 성실히 조사한다.

- 더 강한 근거, 적용 범위 불일치, 재현 실패, 반례가 있으면 `rebutted`를 제안한다.
- 타당한 근거가 없으면 억지 반박을 만들지 않고 `accepted` 또는 `partially_accepted`와 수정안을 낸다.
- 양쪽 근거가 남으면 `unresolved`로 둔다.

작성자와 critic은 자신의 쟁점을 최종 폐쇄하지 않는다. 독립 resolver도 근거가 포함된 advisory packet을 반환한다. Standard/Deep phase 안의 `rebutted / accepted / partially_accepted / unresolved` 최종 disposition은 해당 Research/Implementation Orchestrator가 소유한다. 프로젝트 권위·사용자 선호 사이의 선택처럼 근거만으로 닫을 수 없는 경우에만 `NEEDS_DECISION`으로 project owner에게 올린다.

기본 critique round는 1회다. material conflict에 필요한 좁은 추가 근거 요청 1회를 넘으면 무한 토론 대신 `NEEDS_DECISION` 또는 `BLOCKED`로 보낸다. 반박 성공률이나 finding 수를 agent 성과 지표로 쓰지 않는다.

## 9. 구현과 검증

### 계획

구현 계획은 다음을 연결한다.

- requirement와 acceptance criterion
- Document Binding
- 선택한 architecture/pattern과 대안
- 단계별 writable scope와 owner
- material role별 model profile·reasoning effort와 escalation condition
- 단계별 검증 명령·관측
- 알려진 위험, rollback 또는 중단 조건
- 문서 영향 후보

“유지보수성·확장성을 고려한다”는 문장만으로는 부족하다. 해당 품질이 중요한 구체 scenario와 설계가 이를 만족하는 이유가 있어야 한다.

### 구현

- Quick은 main agent가 직접 구현할 수 있다.
- Standard/Deep은 main이 먼저 Implementation Orchestrator session을 연다.
- Implementation Orchestrator가 research final packet, completion contract, Document Binding, active convention과 프로젝트 문서를 읽고 단계·dependency·writable scope·검증 gate를 설계한다.
- planner·writer·verifier leaf의 계약과 순서는 Implementation Orchestrator가 결정한다. main은 host control과 안전 검사만 대행한다.
- 읽기·조사·테스트 분석은 독립이면 병렬화한다.
- 쓰기는 겹치지 않는 소유 범위만 병렬화한다.
- dependent worker는 선행 packet을 Implementation Orchestrator가 disposition한 다음 wave에서 시작한다.
- 각 단계 후 worker는 changed files, 실행 명령, 결과, 계획 이탈, 남은 위험을 보고한다.
- main은 packet을 Implementation Orchestrator에 전달하고 material diff·raw result·권한 범위를 직접 확인한다. Phase semantic packet과 raw evidence가 충돌하면 main이 결론을 바꾸지 않고 `EVIDENCE_MISMATCH` packet을 같은 Implementation Orchestrator에 돌려보낸다. 진행·재작업·추가 연구·완료의 의미 판정은 Implementation Orchestrator가 한다.
- Implementation Orchestrator는 모든 stage와 독립 검증을 닫은 뒤 close authorization 없는 `IMPLEMENTATION_COMPLETE`와 계획 이탈·남은 위험을 main에 보고한다. Main이 raw evidence와 Document Impact를 독립 검사해 `EVIDENCE_COMPLETE` receipt를 같은 owner에게 보내면 owner가 별도 `CLOSE_REQUESTED`를 내고, main은 실제 host evidence로 close disposition을 기록한다.

계획과 다른 선택이 더 타당하면 숨기지 않는다. 이유·근거·영향을 제시하고 재계획 또는 owner 결정을 거친다.

### 검증

1. **Mechanical**: syntax, schema, lint, type, test exit status
2. **Behavioral**: acceptance scenario, regression, 실제 실행·브라우저 상태
3. **Independent review**: fresh context에서 requirement, diff, raw evidence, 위험 검토
4. **Document impact**: 규범·설명·계획·연구의 갱신 여부

writer의 설득적 요약, critic의 다수 의견, schema 통과만으로 완료하지 않는다. 현재 Skill-only 단계의 completion은 절차적 assurance이며 hard guarantee가 아님을 명시한다.

## 10. Document Impact Closure

변경 후 관련 문서마다 다음 중 하나를 기록한다.

| disposition | 의미 |
|---|---|
| `update` | 동작·계약·현재 구조가 바뀌어 같은 변경에서 갱신 |
| `create` | 새 권위 문서가 실제로 필요 |
| `unchanged` | 확인했지만 현재 내용이 계속 정확함; 이유 기록 |
| `supersede` | 기존 문서를 보존하고 새 문서가 대체 |
| `defer` | 별도 작업이 필요하며 owner·조건·위험 기록; 완료를 막는지 명시 |

문서 갱신은 코드 동작과 같은 변경에서 하는 것이 기본이다. 연구 기록이나 ADR만 고치고 현재 normative 문서를 낡게 두지 않는다.

## 11. Convention Research

active convention이 없거나 의심스러우면 다음 순서를 사용한다.

1. hard constraint: 언어·framework·접근성·보안·플랫폼 규칙
2. project context: 기존 코드, architecture, 사용자, product direction
3. reference research: 공식 가이드, 실제 사례, 반례
4. options: 최소 두 후보와 trade-off
5. prototype 또는 작은 적용
6. independent critique와 검증
7. `candidate` 등록
8. 실제 작업과 held-out task에서 유효하면 `active` 승격

외부 style guide는 기본값 후보이지 프로젝트의 자동 권위가 아니다. 프로젝트별 명료성과 일관성이 더 중요하면 근거를 남기고 다르게 선택할 수 있다.

상세 형식과 우선순위는 [`conventions/README.md`](conventions/README.md)를 따른다.

## 12. Design Assurance Loop

Design Assurance는 UI·design 작업에만 여는 domain gate다. Completion Contract와 적용 가능한 active convention이 상위 계약이고, 아래 Reference Evidence System·Design Execution Contract·Multi-axis Visual QA는 그 계약을 구체화한다.

- **owner**: Standard/Deep UI의 domain phase와 semantic disposition은 Implementation Orchestrator가 소유한다. Reference 수집·작성·검증을 leaf에 위임할 수 있지만 main이나 외부 Skill이 owner를 대체하지 않는다. Quick UI는 main이 직접 가볍게 처리한다.
- **entry gate**: UI scope·사용자 목적·Completion Contract·Document Binding·writable scope를 확인하고, 적용할 active convention, 접근성 위험, reference 필요성, viewport/state와 검증 강도를 정한다. Standard/Deep은 Implementation Orchestrator가 이 receipt를 승인해야 구현을 시작한다.
- **exit gate**: applicable active convention 준수, task-scoped Design Execution Contract acceptance, 실제 결과의 multi-axis QA, accessibility, proportionate behavioral/performance evidence, originality·provenance risk, raw artifact read-back과 Document Impact가 닫혀야 한다.
- **reopen triggers**: 목적·content·reference·active convention 변경, 새로운 viewport/state/localization/accessibility/performance/originality 위험, browser 결과와 contract 불일치, raw evidence mismatch 또는 수정 회귀가 생기면 contract나 필요한 QA lane을 다시 연다.

Quick UI는 별도 무거운 domain-phase ceremony 없이 직접 처리할 수 있지만, 적용 가능한 convention과 accessibility를 지키고 scope·risk에 비례한 browser/behavioral verification과 Document Impact를 남긴다.

디자인 작업은 다음 세 시스템을 기본 뼈대로 쓰되, 여섯 축 QA로 완성한다.

### A. Reference Evidence System

단일 screenshot이 아니라 필요에 따라 전체 page, section crop, video interval, HTML/CSS/code, asset, interaction state를 수집한다. 각 item에 source, capture time, viewport/device, version/revision, 사용 목적, 채택·비채택 요소, 저작권·독창성 위험을 기록한다.

레퍼런스는 “복제 대상”이 아니라 목적·패턴·제약을 이해하기 위한 증거다.

재현이 필요한 browser evidence는 가벼운 manifest로 묶는다. 해당 artifact에 실제로 영향을 주는 field만 기록하되 기본 후보는 다음과 같다.

- capture ID, source URL/route, source revision과 artifact digest
- captured-at, browser/version/OS, viewport/DPR
- locale, timezone, theme/color scheme
- test fixture·data-state·role ID; raw cookie·token·auth storage는 제외
- interaction path, readiness assertion, 관찰 대상 state
- screenshot/video/trace/DOM·network artifact locator와 redaction·license 상태

기본은 full-page context 1개와 결정에 중요한 section/state 증거다. trace·video는 상호작용 원인 조사, 실패, 고위험 상태에 선택적으로 사용하고 모든 성공 run에 상시 수집하지 않는다. coverage matrix에는 확인한 viewport/state/interaction과 확인하지 않은 영역을 함께 적는다.

### B. Design Execution Contract

Design Execution Contract는 한 task의 UI/domain 실행 계약이며 Completion Contract와 active convention에 종속된다. 그 자체는 active convention이 아니고 project-wide 기본값을 만들지 않는다. 반복 가치가 있는 candidate 값·패턴은 [`conventions/README.md`](conventions/README.md)의 lifecycle을 거쳐야만 convention으로 들어간다.

화면 또는 section마다 다음을 적는다.

- 사용자·제품 목적과 content
- layout, hierarchy, spacing rhythm
- typography, color, token과 asset
- default/hover/focus/active/disabled/loading/error/empty state
- responsive·localization behavior
- motion의 trigger, duration/easing 후보, reduced-motion 처리
- keyboard·semantics·contrast·target size 같은 accessibility 기준
- performance budget과 구현 제약
- reference에서 채택·거절한 이유
- acceptance criterion과 필요한 evidence

근거 없는 수치는 `candidate`다. contract에 적었다는 이유만으로 active convention이 되지 않는다.

### C. Multi-axis Visual QA Loop

실제 브라우저 결과를 기준으로 다음 축을 검사한다.

1. visual hierarchy·alignment·spacing·typography
2. interaction과 모든 중요 state
3. responsive와 localization
4. accessibility와 reduced motion
5. performance
6. reference originality·brand 적합성

한 번의 수정에서는 **하나의 검증 가능한 가설**을 우선한다. “CSS 속성 하나만”이라는 경직된 규칙은 아니다. 관련 변수가 상호작용하면 묶음 가설로 바꾸고 회귀 범위를 넓힌다. before/after와 바뀐 축, 유지돼야 할 축을 기록한다.

Screenshot baseline 비교에서는 browser·OS·font·viewport와 animation 상태를 고정하거나 차이를 기록한다. pixel diff는 변화 탐지 증거이지 목적·사용성·접근성의 자동 판정자가 아니다. 성능 기준은 프로젝트가 정한 budget과 lab evidence를 사용하고, 배포 후 field data가 생기면 lab 결과와 구분해 해석한다.

### MengTo/Skills 사용

첫 UI pilot에서 이미 가용한 좁은 Skill만 명시적으로 선택한다. upstream 전체를 자동 설치·갱신하거나 vendor하지 않는다.

- capture/interpretation Skill → Reference Evidence 보조
- design-first·layout·motion Skill → contract 후보 보조
- originality·performance·animation Skill → QA 보조

각 사용에는 Skill 이름, source revision/digest(가능한 경우), 입력 project context, 산출물과 limitation을 기록한다. MengTo 결과는 bounded adapter output일 뿐 접근성·프로젝트 token·convention 승격·phase disposition·완료 판정의 권위가 아니다.

## 13. 재사용 자산 승격

Java, React, 디자인 등 반복 전문성은 “한 에이전트가 계획·구현·검증을 모두 맡는 역할”이 아니라 기존 역할에 주입하는 좁은 Skill/reference가 된다.

승격 조건:

- 같은 gap이 최소 3개의 실제 작업에서 반복되거나 심각한 단일 실패가 있다.
- 일반 prompt 대비 개선할 behavior가 명확하다.
- trigger와 non-trigger prompt가 있다.
- 독립 reviewer가 역할 중복과 권한 확대를 검사한다.
- static validation과 forward test를 통과한다.
- owner, version, 갱신·폐기 조건이 있다.

조건 전에는 작업별 prompt와 결과를 보존할 뿐 상시 custom agent를 만들지 않는다.

## 14. 최소 안전 게이트

모든 mutation 전에 확인한다.

- writable·forbidden scope
- 현재 worktree의 사용자 변경
- secret, credential, PII 노출 가능성
- network·external system 접근 필요성
- destructive·irreversible action 여부
- rollback 또는 복구 방법

보안은 후반 phase가 아니다. 다만 초기부터 범용 보안 플랫폼을 만드는 것도 아니다. 현재 작업의 실제 위험에 맞는 host permission, read-only agent, 사용자 승인과 검증을 쓴다.

## 15. Verdict와 평가

허용 verdict 예시:

- `COMPLETE`: 모든 acceptance criterion의 증거가 있고 blocking finding·문서 영향이 닫힘
- `PARTIAL`: 유용한 결과는 있으나 명시된 항목이 미완료
- `NEEDS_DECISION`: 근거만으로 닫을 수 없는 사용자·owner 선택
- `INSUFFICIENT_EVIDENCE`: 조사 또는 실행 증거가 부족
- `BLOCKED`: 외부 조건이나 권한 없이는 진행 불가
- `FAILED`: 시도했지만 완료 조건을 충족하지 못함
- `CANCELLED`: 사용자가 중단하거나 요청이 대체됨

Skill forward test는 같은 task·환경·budget에서 baseline과 비교한다. 최소 측정 항목은 다음과 같다.

- 관련 문서 recall과 잘못된 문서 적용
- material decision의 근거 coverage
- 연구 under-trigger와 over-trigger
- false-completion
- scope violation
- critic finding 중 실제 결정 변경률
- Quick 작업의 시간·token overhead
- 사용자 개입 횟수와 최종 품질

headline 통과율만 보고하지 않는다. 추천 profile, 실제 모델, reasoning setting, tools, permissions, task set, retries, 시간·token budget, grader와 known invalidity risk를 함께 기록한다. Skill 효과 비교와 모델 calibration은 서로 다른 실험으로 분리한다.
