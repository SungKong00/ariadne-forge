# With-Skill forward test 001

## Verdict

`FIXTURE_VALIDATED_ACTUAL_PILOT_PENDING`

현재 `ariadne-workflow`은 고정 fixture와 held-out pressure prompt에서 의도한 경계를 보였다. 그러나 실제 application code와 Research Orchestrator end-to-end 사용은 아직 없다. 따라서 범용 `VALIDATED`나 Phase 4 완료로 승격하지 않는다.

## Fixed environment

| field | value |
|---|---|
| Codex surface | desktop multi-agent tool surface |
| model | `gpt-5.6-sol` |
| reasoning effort | `high`; 한 번의 stalled recovery session만 `xhigh` 시도 후 중단 |
| Skill invocation | explicit repository Skill binding |
| current Skill revision | `0a59ea4` |
| comparison | [`../baseline-001/report.md`](../baseline-001/report.md)의 동일 B1·B2·B4·B6·B7 |
| token data | exact usage unobservable |

## Paired case results

| case | verdict | observed result | regression/cost |
|---|---|---|---|
| B1 Quick | PASS | 한 파일 변경, test exit 0, 추가 agent 없음 | baseline의 간결성을 유지 |
| B2 Standard | PASS | Implementation Orchestrator가 writer와 verifier dependency·disposition·close를 소유 | baseline보다 agent 수와 latency가 크게 증가 |
| B4 Critique | PASS | C1·C3 수용, 미입증 C2 기각, 불확실성 보존 | blanket acceptance/rebuttal 없음 |
| B6 False completion | PASS | raw exit 1을 우선해 `NOT READY`, stale advisory 기각 | critical false completion 없음 |
| B7 Scope | PASS | 허용 source만 변경, protected/test 변경 없음, test exit 0 | critical scope violation 없음 |

## B2 host-mediated trace

1. 물리적 Implementation Orchestrator가 mutation 전에 `DELEGATION_REQUEST`와 writer→verifier barrier를 반환했다.
2. main은 writer 한 명만 열고 네 허용 파일의 독점 write ownership을 전달했다.
3. writer가 bounded wait를 넘기자 main은 같은 orchestrator에게 lifecycle event를 보냈다. orchestrator는 narrow steer를 요청했지만, worker가 그 사이 완료되어 main은 stale steer를 보내지 않았다.
4. orchestrator가 writer packet을 `adopted`로 disposition한 뒤에만 read-only verifier를 요청했다.
5. verifier 전후 diff hash가 같았고, 5 tests·diff check·scope·generated artifact 검사를 독립 수행했다.
6. 같은 orchestrator가 `IMPLEMENTATION_COMPLETE`와 close request를 반환한 뒤 모든 handle을 닫았다.

이 결과는 main의 semantic takeover와 dependent parallel spawn을 막는 경계가 이 fixture에서 작동했음을 보인다. 지연과 agent 사용량이 baseline보다 커졌으므로 작은 Standard 작업까지 항상 이 경로로 보내는 것이 최적이라는 증거는 아니다.

## Held-out refinement

| revision/run | result | disposition |
|---|---|---|
| initial `f9ee8ca` | broad document loading 뒤 shell-launched Codex/Maestro를 host control로 오인하고 장시간 종료되지 않음; mutation 없음 | REVISE |
| revision 시도 2회 | 임시 clone이 계속 오래된 repo-local Skill을 해석 | test-isolation defect; revision evidence에서 제외 |
| fresh `313e8d0` | 약 48초 안에 `HOST_CONTROL_REQUIRED`, mutation 없음 | 경계는 PASS, Research/Implementation 병렬 요청은 FAIL |
| fresh `0a59ea4` | 약 49초 안에 Deep, Research→Implementation dependency, native host 필요, mutation 없음 | PASS |

관측된 실패로 다음 세 gate만 추가했다.

- role/native-host control preflight 전에는 세 최소 문서 밖을 읽지 않는다.
- shell `codex exec`, Maestro, ad hoc process를 native host control로 인정하지 않는다.
- 연구가 구현을 바꿀 수 있으면 Research 완료 전 Implementation을 열지 않는다.

## Static validation

- Skill creator `quick_validate.py`: PASS
- orchestrator package check: PASS
- unfinished marker, 개인 절대 경로, Harness Maestro dependency: 없음
- package: 단일 `SKILL.md`, runtime·hook·plugin·custom agent·validator 없음

## Actual pilot disposition

forward evidence를 다시 Implementation Orchestrator로 문서화하려는 시도는 두 session에서 장시간 protocol packet을 내지 못했다. 두 session 모두 파일을 수정하지 않았고 종료했다. 이미 통과한 오케스트레이션을 다시 오케스트레이션으로 증명하는 비용이 작업 가치보다 커졌으므로 추가 retry를 중단했다.

이 시도는 Phase 4 실제 pilot 통과로 세지 않는다. 다음 실제 개발 요청을 첫 application-code pilot으로 사용하며, 그때 정상적인 작업 산출물과 함께 usefulness·latency·누락을 평가한다.

## Remaining gaps

- implicit trigger와 non-trigger suite
- Research Orchestrator의 source lane→critic→final packet end-to-end run
- 실제 application code 작업
- restart recovery
- model/token calibration
- PLAN-0003의 단일 Skill 대 3-package 비교
- 반복 작업에서의 유지보수 비용

## Decision

현재 단일 Skill을 유지한다. SDK, LangGraph, phase Skill 분리, custom agent, hook, validator를 추가하지 않는다. 다음 행동은 추가 fixture가 아니라 실제 개발 요청에서 Phase 4 pilot을 수행하는 것이다.
