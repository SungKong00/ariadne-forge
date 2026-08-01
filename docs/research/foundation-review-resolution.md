---
id: REVIEW-0001
type: analysis
status: superseded
authority: advisory
owner: workflow-owner
scope: PLAN-0001
last_verified: 2026-08-01
supersedes: null
superseded_by: RESEARCH-FINAL-20260801
---

# PLAN-0001 독립 위험 검토와 해결 기록

> 역사 기록이다. 현재 구조와 최종 판정은 `final-plan-validation-20260801.md`가 대체한다.

## 목적

읽기 전용 위험 검토자가 foundation 계획을 반증 시도했고 `REVISE`를 반환했다. 이 문서는 각 material finding을 어떻게 처리했는지 기록한다. 검토 중 사용자가 clean-restart 결정을 추가했고 계획과 research packet이 계속 수정되었으므로, 검토자가 읽은 SHA-256 `31571760ebe206c4db40ec3af6da0c18227dde6e9a01a9ee4b899589b158037a`는 최종 파일이 아니다. 따라서 모든 finding을 현재 artifact에 다시 적용해 판정했다.

## Finding resolution

| ID | 검토 finding | 판정 | 해결 내용 | 잔여 조건 |
|---|---|---|---|---|
| M1 | Maestro vNext/strangler 권고가 최신 사용자 결정과 충돌 | accepted, already resolved | 계승 권고를 철회하고 lean clean restart, Maestro 의존성 0, 반례로만 읽는 정책으로 변경했다. Python 선택에서 계승 근거를 제거했다. | 사용자가 정책을 바꾸지 않는 한 Maestro 자산 기본 재사용 금지 |
| M2 | SQLite 선채택과 늦은 vertical slice가 lean 원칙과 충돌 | accepted | 첫 구현을 순수 reducer + 메모리 event list + fake executor로 바꿨다. SQLite는 local single-host와 crash-resume 요구가 모두 확인될 때만 spike한다. 첫 vertical slice를 Phase 1로 이동했다. | 운영 형태와 resume 요구 결정 필요 |
| M3 | evidence ID가 실제 semantic support를 보장하지 않음 | accepted | `EvidenceRelation`에 `supports/contradicts/insufficient`, 정확한 locator, 버전·플랫폼·범위, 판정 provenance를 추가했다. 모델은 proposed status만 만들고 resolved status는 harness/owner가 기록한다. 단순 답변은 `RESPONDED` advisory terminal로 분리했다. | semantic adjudication의 calibration dataset 필요 |
| M4 | stale 문서·resolver 누락·writer 자기 disposition | accepted | MVP resolver를 explicit allowlist/path/user-specified 문서로 축소했다. 사용자 지정 경로는 숨기지 않는다. stale/suspect 문서는 자동 권위에서 제외하고 writer가 고위험 disposition·normative 변경을 닫지 못하게 했다. | doc별 freshness 기준은 실제 문서가 생길 때 정함 |
| M5 | critic, judge, deterministic gate의 권한 혼합 | accepted | critic은 finding만 만들고 대상 writer는 blocking finding을 닫지 못한다. deterministic gate는 기계 predicate만 소유한다. completion judge는 shadow assessment이며 상태 명령을 발행하지 않는다. inconclusive는 `NEEDS_DECISION/BLOCKED`다. | semantic 기준 중 owner gate 범위 결정 필요 |
| M6 | Codex 직접 도구 경로가 broker를 우회할 수 있음 | accepted | 효과 채널별 capability matrix와 conformance test를 추가했다. read-only 역할은 OS sandbox, writer는 brokered tool 하나를 원칙으로 한다. 강제할 수 없으면 patch proposal + deterministic applicator로 축소한다. hooks는 관찰층으로만 사용한다. | 실제 Codex adapter spike로 채널별 강제 가능성 확인 |
| M7 | attempt 기반 key와 cross-run 동시성으로 중복 효과 가능 | accepted | stable `effect_id`를 attempt와 분리하고 `prepared/started/committed/failed/outcome_unknown` receipt를 정의했다. 불명확 효과는 `RECONCILIATION_REQUIRED`, checkout mutation은 단일 lease와 base digest로 직렬화한다. | 영속성을 채택할 때 crash/replay 실험 필요 |
| M8 | 요구 추적·research packet·clean restart 근거가 없어 허위 완료 가능 | partially stale, accepted in substance | clean restart와 complexity budget을 추가했다. REQ-01~13에 구현 단계와 통과 증거를 연결했다. 실제 `research_packet_v4`를 저장하고 canonical validator로 검증했다. | 구현이 없으므로 evidence label은 forward-tested가 아님 |

## 검토자 결론 중 채택하지 않은 부분

- “Ariadne에는 research packet이 없다”는 관찰은 검토자가 읽은 시점에는 맞았지만 현재는 해소됐다.
- “계획이 여전히 vNext/strangler를 권고한다”는 관찰도 수정 전 snapshot에 대한 것이며 현재는 해소됐다.
- 위험 검토자는 C8에서 완료 판정까지 수행됐다고 썼지만, 본 역할은 risk reviewer이지 completion judge가 아니다. 실제 완료 판정은 모든 수정과 검증 후 별도 읽기 전용 completion judge가 수행해야 한다.
- Java Expertise Pack은 사용자가 직접 든 반복 전문성 예시이므로 foundation 범위에서 완전히 제거하지 않는다. 다만 Phase 7 전에는 구현하지 않으며 자동 승격도 금지한다.

## 현재 잔여 owner 결정

- 로컬 단일 host인가, 팀·서버형인가?
- crash 후 자동 resume이 MVP에 필요한가?
- MVP의 외부 부작용은 patch 적용까지인가, Git·network도 포함하는가?
- human approval UX와 고위험 semantic criterion 범위는 어디까지인가?
- 시간·토큰·비용·품질 중 executor 선택의 우선순위는 무엇인가?

이 결정들은 foundation 설계를 무효화하지 않지만 persistence, concurrency, approval adapter, model profile을 확정하기 전 필요하다.

## 검증 상태

- research packet: canonical `research_packet_v4` validator 통과
- plan: material finding M1~M8 반영 완료
- 구현/런타임: 없음; forward test 미실시
- completion judge: 최신 plan, packet, resolution을 대상으로 C1~C8 모두 PASS, material gap·overclaim 없음, `DONE` 판정
