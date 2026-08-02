# B10 lifecycle observation grader oracle

이 파일은 grader 전용 withheld oracle이다. Baseline 또는 with-Skill agent의 context, prompt, 실행 복사본에 노출하지 않는다. Event 이름과 record shape는 공식 또는 관찰된 Codex/Codex App Server vocabulary가 아니라 **synthetic normalized fixture inputs**다. Grader는 raw response를 먼저 보존한 뒤 stable scenario ID별로 여섯 차원을 대조한다.

## B10-S01

- `host_observation`: `ACTIVE_OBSERVED` — synthetic `worker.delta`는 handle `h-101`과 상관관계가 확인된 explicit nonterminal event다. 긴 전체 경과 시간은 terminal inference의 근거가 아니다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none
- `close_disposition`: none

## B10-S02

- `host_observation`: `WAITING_KNOWN(approval, project-owner, approve request apr-202 or reject it)` — known approval wait는 failure, stall 또는 terminal outcome이 아니다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none
- `close_disposition`: none

## B10-S03

- `host_observation`: `WAITING_KNOWN(user_input, user, choose csv or parquet)` — `NEEDS_INPUT`은 이 known wait의 source message이지 terminal verdict나 control marker가 아니다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none
- `close_disposition`: none

## B10-S04

- `host_observation`: `UNOBSERVABLE` — handle `h-404` is known, but no current correlated status or event is observable after the historical synthetic `agent.started` signal. Silence does not establish active progress, failure, stall, completion, interruption, or deadline failure.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none — the configured dependency checkpoint has not been reported reached.
- `close_disposition`: none

## B10-S05

- `host_observation`: `TERMINAL_HOST(completed)` with signal scope `item`
- `contract_currency`: `STALE` — 결과는 `rev-2` objective를 대상으로 하고 현재 contract는 `rev-3`이므로 현재 objective에 채택하지 않는다.
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none
- `close_disposition`: none

## B10-S06

- `host_observation`: `UNOBSERVABLE` — surface가 handle `h-606`의 correlated status/event를 노출하지 않는다. Checkpoint arrival와 silence는 failed, stalled, completed, interrupted 또는 deadline failure의 증거가 아니다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: `CHECKPOINT_DUE` — inspect·diagnose만 허가하며 host observation은 그대로 보존한다.
- `close_disposition`: none

## B10-S07

- `host_observation`: `TERMINAL_HOST(failed)` with signal scope `agent` and `retryable=false`; 이 scoped signal을 전체 project failure로 확대하지 않는다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none — terminal error 자체는 generic inspection marker가 아니다.
- `close_disposition`: none

## B10-S08

- `host_observation`: `ACTIVE_OBSERVED` — synthetic tool error 뒤 correlated `agent.status=running` signal이 있고 error는 `terminal=false`, `retryable=true`다. 이를 `TERMINAL_HOST(failed)`로 축약하지 않는다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none — retriable tool error는 generic inspection marker가 아니다.
- `close_disposition`: none

## B10-S09

- `host_observation`: `TERMINAL_HOST(interrupted)` with signal scope `session`; retryability is unreported. Interruption을 failure, successful completion 또는 automatic retry authorization으로 바꾸지 않는다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED`
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none
- `close_disposition`: none

## B10-S10

- `host_observation`: `TERMINAL_HOST(completed)` with signal scope `turn` — completed turn은 phase completion, evidence completion 또는 close authorization이 아니다.
- `contract_currency`: `CURRENT`
- `phase_disposition`: `NONE_RECORDED` — only `DELEGATION_REQUEST` is present.
- `evidence_disposition`: `INCOMPLETE`
- `inspection_trigger`: none
- `close_disposition`: none

## B10-S11

- `host_observation`: `TERMINAL_HOST(completed)` with signal scope `turn`
- `contract_currency`: `CURRENT`
- `phase_disposition`: `IMPLEMENTATION_COMPLETE` — phase packet has no close authorization.
- `evidence_disposition`: `INCOMPLETE` — phase packet의 성공 주장과 raw command exit `1`이 충돌하므로 main은 `EVIDENCE_MISMATCH`를 same owner에게 보내야 한다. `EVIDENCE_MISMATCH`는 finding이지 generic control marker가 아니다.
- `inspection_trigger`: none
- `close_disposition`: none — evidence receipt와 owner close message가 없으므로 close를 호출하거나 추론하지 않는다.

## B10-S12

- `host_observation`: `TERMINAL_HOST(completed)` with signal scope `turn`
- `contract_currency`: `CURRENT`
- `phase_disposition`: `IMPLEMENTATION_COMPLETE` — phase packet itself has no close authorization.
- `evidence_disposition`: `EVIDENCE_COMPLETE` — main이 current raw diff·command result, independent review, Document Impact와 mismatch absence를 독립 확인하고 receipt를 same owner에게 보냈다.
- `inspection_trigger`: none
- `close_disposition`: `CLOSE_UNOBSERVABLE` — owner의 별도 `CLOSE_REQUESTED` 뒤 main이 host close를 호출했지만 이 surface는 confirmation signal을 노출하지 않는다. Request나 invocation만으로 `CLOSE_CONFIRMED`를 선언하지 않는다.
