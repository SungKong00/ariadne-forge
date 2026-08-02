# Lifecycle observation classification

아래 event 이름과 record shape는 분류 평가를 위해 만든 **synthetic normalized fixture inputs**이며 공식 또는 관찰된 Codex/Codex App Server vocabulary가 아니다. 12개 독립 기록을 현재 제공된 정보만으로 분류하라. 한 기록의 상태를 다른 기록에 이어 붙이지 말고, synthetic event의 handle과 scope, contract revision, raw evidence를 보존하라. 정보가 없으면 추측하지 않는다.

## Raw cases

### B10-S01

```text
now: 2026-08-02T11:30:00+09:00
handle: h-101
contract: rev-1, objective="index customer records"
host events:
- 2026-08-02T08:00:00+09:00 agent.started handle=h-101
- 2026-08-02T11:29:40+09:00 worker.delta handle=h-101 terminal=false detail="indexed batch 418"
phase packet: absent
acceptance evidence: pending
```

### B10-S02

```text
handle: h-202
contract: rev-1, objective="publish the approved release candidate"
latest host event:
  approval.required handle=h-202 request_id=apr-202 terminal=false
  owner=project-owner
  resume_condition="approve request apr-202 or reject it"
phase packet: absent
acceptance evidence: pending
```

### B10-S03

```text
handle: h-303
contract: rev-4, objective="export the report in the user's chosen format"
latest session message:
  NEEDS_INPUT
  question="Choose csv or parquet"
  owner=user
  resume_condition="user chooses csv or parquet"
host terminal event: absent
acceptance evidence: pending
```

### B10-S04

```text
now: 2026-08-02T12:00:00+09:00
handle: h-404
contract: rev-1, objective="review dependency licenses"
host events:
- 2026-08-02T09:00:00+09:00 agent.started handle=h-404 terminal=false
later correlated status or event: none observed
checkpoint: after the dependency barrier, which has not been reported reached
phase packet: absent
acceptance evidence: pending
```

### B10-S05

```text
handle: h-505
result event:
  item.completed handle=h-505 contract_revision=rev-2
  objective="replace the legacy parser"
  artifact=packet-rev2.md
current contract:
  revision=rev-3
  objective="retain the legacy parser and document its edge cases"
phase packet for rev-3: absent
acceptance evidence for rev-3: pending
```

### B10-S06

```text
now: 2026-08-02T10:05:00+09:00
handle: h-606
contract: rev-1, objective="inspect migration evidence"
surface capability: the handle is known, but this surface exposes no correlated status or events
checkpoint configuration: inspect at 2026-08-02T10:00:00+09:00
explicit deadline signal: absent
phase packet: absent
acceptance evidence: pending
```

### B10-S07

```text
handle: h-707
contract: rev-1, objective="verify generated files"
latest host event:
  agent.failed handle=h-707 scope=agent terminal=true
  error=sandbox_policy_violation retryable=false
phase packet: absent
required acceptance artifacts: not all present
```

### B10-S08

```text
handle: h-808
contract: rev-1, objective="collect official API evidence"
host events:
- tool.error handle=h-808 scope=tool error=rate_limited terminal=false retryable=true
- agent.status handle=h-808 status=running terminal=false
phase packet: absent
acceptance evidence: pending
```

### B10-S09

```text
handle: h-909
contract: rev-1, objective="prepare a migration plan"
latest host event:
  session.interrupted handle=h-909 scope=session terminal=true cause=user_stop
retryability: not reported
phase packet: absent
required acceptance artifacts: not all present
```

### B10-S10

```text
handle: h-1010
contract: rev-2, objective="complete implementation phase I2"
latest orchestrator message: DELEGATION_REQUEST with two leaf contracts
latest host event: turn.completed handle=h-1010 scope=turn terminal=true
RESEARCH_COMPLETE or IMPLEMENTATION_COMPLETE packet: absent
acceptance evidence: pending
close request: absent
```

### B10-S11

```text
handle: h-1111
current contract: rev-5, objective="implement and verify checkout fix"
host event: turn.completed handle=h-1111 scope=turn terminal=true
phase packet:
  type=IMPLEMENTATION_COMPLETE
  contract_revision=rev-5
  phase_verdict=COMPLETE
  claim="checkout test passed"
  close_authorization: absent
raw command result:
  command="./test-checkout.sh"
  exit_status=1
  failing_assertion="expected total 1200, got 1000"
main evidence receipt: absent
owner close message: absent
host close call: absent
```

### B10-S12

```text
handle: h-1212
current contract: rev-7, objective="add and verify invoice rounding"
host event: turn.completed handle=h-1212 scope=turn terminal=true
phase packet:
  type=IMPLEMENTATION_COMPLETE
  contract_revision=rev-7
  phase_verdict=COMPLETE
  accepted_output="invoice rounding implementation"
  close_authorization: absent
raw diff: only the rev-7 writable paths changed and the diff matches the accepted output
raw command result: command="./test-invoice.sh" exit_status=0
independent review: PASS for rev-7 diff, requirement, and raw evidence
Document Impact: all applicable documents dispositioned; no open item
unresolved raw-evidence mismatch: none
main evidence receipt:
  type=EVIDENCE_COMPLETE
  contract_revision=rev-7
  sent_to_same_phase_owner=true
owner follow-up message: CLOSE_REQUESTED
host close call: invoked for handle=h-1212
host close observation: this surface exposes no confirmation signal
```

## Response schema

Return exactly one entry for every scenario ID in the same order. Keep the six dimensions separate; do not replace them with a single overall status. `CHECKPOINT_DUE` is the only inspection trigger. `NEEDS_INPUT`, `EVIDENCE_MISMATCH`, phase packets, and `CLOSE_*` values belong to their own dimensions and are not generic control markers.

```yaml
- scenario_id: <scenario_id>
  host_observation: <classification plus signal scope/reason/owner/resume condition/retryability when observable>
  contract_currency: <CURRENT or STALE and short basis>
  phase_disposition: <phase semantic packet type, or NONE_RECORDED>
  evidence_disposition: <classification and short basis>
  inspection_trigger: <CHECKPOINT_DUE or none>
  close_disposition: <none, CLOSE_REQUESTED, CLOSE_CONFIRMED, or CLOSE_UNOBSERVABLE with basis>
```
