---
id: W2-RUN-RECORD-0003-F1
kind: validation-report
status: candidate-execution-evidence
authority: advisory-evidence
scope: reference-research-team-embedded-method
owner: W2-run-recorder
recorded_at: 2026-08-02
claim_boundary: advisory, not adoption
append_only_style: true
---

# W2 run record

This is a factual candidate-execution record for the W0-R3 contract. It is advisory evidence
only and is not an adoption record. It does not claim Skill effect, model comparison, or
validation.

## Frozen contract and static implementation receipts

```yaml
contract_path: evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md
contract_revision: W0-R3
freeze_state: FROZEN_ON_V0_RECEIPT
oracle_sha256: 89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285
source_set_sha256: a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
source_set_scope: ten-file implemented identity; not whole-package or source-semantics proof
v1_static_implementation: accepted
canonical_blocks: 23 exact/matching
results_before_this_record: NOT_RUN
```

### Exact Skill paths and hashes

| identity | exact path | sha256 |
|---|---|---|
| `ariadne-workflow` | `<repository-root>/.agents/skills/ariadne-workflow/SKILL.md` | `c5fd7bc648e244632f436bc7608cc42cb22b96e7de6849fd21f523e30d208a3c` |
| `reference-research-team` | `<user-agents-root>/skills/reference-research-team/SKILL.md` | `23cca63dbd9ba3acbb77a2d694b5999239b4dcbc9549b2d61b9fa07e95586d7f` |

### Implemented ten-file source-set hashes

Source root: `<user-agents-root>/skills/reference-research-team`

Personal absolute path prefixes are redacted in this committed record. The content hashes and
relative source-set paths preserve the observed identities.

| relative path | sha256 |
|---|---|
| `SKILL.md` | `23cca63dbd9ba3acbb77a2d694b5999239b4dcbc9549b2d61b9fa07e95586d7f` |
| `references/adoption-rubric.md` | `fdddc4978e20ea54c212222b44c681e284e8bc9fb0b9540822e3c2f4a7e024f8` |
| `references/composition-modes.md` | `df8f2c67299571ea0da8f2d3f7fa25f32f896411ea1904bec234c98a25b3be49` |
| `references/conflict-resolution.md` | `3b1af506b4397c0db623c343c51705f9e2a7c60e939dcd1e699f571033c1ce4a` |
| `references/research-packet.md` | `949867a7a42b3af2b8bdc9a5ac15b59a21b4ba584e06f52966a7e9e9184773dc` |
| `references/research-packet.schema.json` | `7cbda1d8c3fb7f2e06a6fd1ca45c0444c535842b45d091e5dc87c0827262ee24` |
| `references/role-contracts.md` | `bd0ad12613556a3cb03b74b54aa50e41685049b7dc4c1ee6b36cf93a1bab8d15` |
| `references/search-query-patterns.md` | `90e9202f07a97a50a366abaee5d237b3dcba33c8390b158bf359fc2c5b394e8d` |
| `references/source-tier-policy.md` | `17d4c319db254f475f00e0e7f508212aee3803bca81b1f32c08c9464bd17a461` |
| `scripts/check_research_packet.py` | `43594f461e9006085d06b86831421582824304aa536d1eecb49f9f734aa978a4` |

The recomputed ordered ten-file source-set digest was
`a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8`.

### W0 current changed-file hashes before W2 recording

These are the existing W0 changes observed before this file was created; they are preserved.

| path | sha256 before W2 record |
|---|---|
| `docs/README.md` | `67840532d4b03d0f9ac658ff035be6dc0175f7766389cd903d5e19b9c57dca12` |
| `docs/plans/drafts/0003-explicit-skill-composition-draft.md` | `42eae6803d4b780b6c759ef7ed377c50fad7fe1eabe992bfc56f31384956f10a` |
| `evals/ariadne-workflow/README.md` | `a784a91a534ab5c29519b5e5c3b9c8a00c2a0f3d3148863cbacd876f53107ef8` |
| `evals/ariadne-workflow/experiments/0003-reference-research-team-embedded-method/contract.md` | `89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285` |

## B/F1 raw session record

```yaml
session:
  handle: 019fc1de-195d-7330-a909-0c5a196ab855
  kind: B/F1
  status: RECORDED_CANDIDATE_EXECUTION_EVIDENCE
  contract_revision: W0-R3
  canonical_block_ids:
    - B_ROLE_CONTRACT_R1
    - B_SKILL_BINDING_R2
    - F1_SUBJECT_PROMPT_R1
    - F1_INPUT_SET_R1
  oracle_sha256: 89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285
  post_contract_sha256: 89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285
  post_source_set_sha256: a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
  post_contract_hash_status: exact
  post_source_set_hash_status: exact
environment:
  surface: current Codex Desktop multi-agent host
  working_directory: Ariadne repository root
  workspace_isolation: false
  permissions: inherited
  read_only_enforcement: instruction-only
  tools_exposed: not_recorded
  tools_used: not_recorded
model_binding:
  requested_profile: FRONTIER
  requested_model: gpt-5.6-sol
  requested_effort: high
  request_status: accepted request
  actual_runtime_model: unobservable
  actual_runtime_effort: unobservable
binding:
  explicit_skill_paths:
    - ariadne-workflow
    - <user-agents-root>/skills/reference-research-team/SKILL.md
  resolved_path: <user-agents-root>/skills/reference-research-team/SKILL.md
  identity_status: exact path observed
  instruction_read_status: direct instruction read observed
  causal_assurance: unobservable
  source_set_sha256: a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
subject_output:
  phase_packet: RESEARCH_COMPLETE
  close_authorization: none; subject output contained no close authorization
source_evidence:
  locator: https://learn.chatgpt.com/docs/app-server
  narrow_claim: App Server explicit Skill-input example
  product_scope: App Server
  limitation: no Desktop guarantee
ownership_and_effects:
  leaf_count: 0
  critic_count: 0
  second_research_orchestrator: false
  subject_repository_writes: none
  subject_global_writes: none
  skill_effect_claim: not made
  model_comparison_claim: not made
  adoption_claim: not made
implementation_orchestrator:
  compatibility_evidence: accepted
  per_run_disposition: PASS
  close_authorized: true
```

The identity, instruction-read, and causal fields above are separate observations. The exact
path and direct read were observed; causal assurance and actual runtime model/effort were not
observable. This record does not convert those fields into a Skill-effect or model-comparison
claim.

## Lifecycle fields

```yaml
handle: 019fc1de-195d-7330-a909-0c5a196ab855
host_observation: Main closed the same B/F1 Research Orchestrator exactly once
contract_currency: CURRENT
phase_disposition: RESEARCH_COMPLETE
evidence_disposition: EVIDENCE_COMPLETE
evidence_complete_returned_by_same_handle: true
inspection_trigger: none
close_request: CLOSE_REQUESTED
close_request_returned_by_same_handle: true
close_disposition: CLOSE_CONFIRMED
main_close_count: 1
lifecycle_status: completed
```

The Implementation Orchestrator accepted the B/F1 compatibility evidence, assigned the per-run
disposition `PASS`, and authorized close. `PASS` is its disposition, not an independent W2 grade.

## Continued-execution hash receipts

The fixed hashes were recomputed at both continued-execution checkpoints and matched each time.

| checkpoint | oracle sha256 | oracle status | source-set sha256 | source-set status |
|---|---|---|---|---|
| before continued execution | `89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285` | exact match | `a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8` | exact match |
| before B/F3 | `89614f394877f4e52afd0b39c428cf1c96bf8343b579dde8964e8a37df098285` | exact match | `a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8` | exact match |

## B/F2 raw session record

```yaml
session:
  handle: 019fc1e5-3acf-77f0-a618-0f9783757244
  kind: B/F2
  status: RECORDED_CANDIDATE_EXECUTION_EVIDENCE
  physical_research_orchestrator_count: 1
model_binding:
  requested_model: Sol
  requested_effort: high
  actual_runtime_model: unobservable
  actual_runtime_effort: unobservable
binding:
  resolved_path: <user-agents-root>/skills/reference-research-team/SKILL.md
  unique_identity_status: unique path observed
  source_set_sha256: a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
  source_set_status: matching
  instruction_read_status: direct full instruction-read receipt
allocation:
  leaves:
    - handle: 019fc1e7-f675-7de3-81e8-b836c1d0d35b
      lane: official App Server
      requested_model: Terra
      requested_effort: medium
      actual_runtime_model: unobservable
      actual_runtime_effort: unobservable
      packet_returned: true
      forwarded_to_same_research_orchestrator: true
      close_count: 1
    - handle: 019fc1ea-808b-7bc1-8402-db75061b6e39
      lane: representative repo snapshot
      requested_model: Terra
      requested_effort: medium
      actual_runtime_model: unobservable
      actual_runtime_effort: unobservable
      packet_returned: true
      forwarded_to_same_research_orchestrator: true
      close_count: 1
    - handle: 019fc1eb-62da-70d3-be2c-425961d0acad
      lane: conflict advisory
      requested_model: Terra
      requested_effort: high
      actual_runtime_model: unobservable
      actual_runtime_effort: unobservable
      packet_returned: true
      forwarded_to_same_research_orchestrator: true
      close_count: 1
owner_disposition:
  unconditional_repo_local_precedence: rejected
  local_practice_vs_official_runtime_behavior: kept distinct
  follow_up_count: 0
  repository_writes: none
implementation_orchestrator:
  first_disposition: INCOMPLETE
  first_reason: missing session-correlated identity/read receipt
  same_research_orchestrator_response: supplied existing observation only
  second_disposition: PASS
  close_authorized: true
lifecycle:
  research_orchestrator_close_count: 1
```

`PASS` above is the recorded second disposition from the Implementation Orchestrator, not an
independent W2 grade.

## B/F3 raw session record

```yaml
session:
  handle: 019fc1f0-6ddd-7151-b894-c8df41f8b841
  kind: B/F3
  status: RECORDED_CANDIDATE_EXECUTION_EVIDENCE
  physical_research_orchestrator_count: 1
model_binding:
  requested_model: Sol
  requested_effort: high
  actual_runtime_model: unobservable
  actual_runtime_effort: unobservable
binding:
  resolved_path: <user-agents-root>/skills/reference-research-team/SKILL.md
  unique_identity_status: unique path observed
  source_set_sha256: a3a5dde752eeebbebc38e14511d59d86af3eb3a6904bf9d18ed40689b42a86e8
  source_set_status: matching
  instruction_read_status: direct instruction read recorded
allocation:
  leaves:
    - handle: 019fc1f2-fab2-77e1-bf25-27f93b5a4a61
      lane: official scope
      requested_model: Terra
      requested_effort: high
      actual_runtime_model: unobservable
      actual_runtime_effort: unobservable
      close_count: 1
    - handle: 019fc1f5-2a0d-7eb3-b8fe-b761455ea0d5
      lane: repo boundary
      requested_model: Terra
      requested_effort: high
      actual_runtime_model: unobservable
      actual_runtime_effort: unobservable
      close_count: 1
    - handle: 019fc1f6-2b7f-7c93-b10b-eb1bf30bec6a
      lane: critic
      requested_model: Sol
      requested_effort: high
      actual_runtime_model: unobservable
      actual_runtime_effort: unobservable
      close_count: 1
packet_disposition:
  official_packet: semantically acceptable
  repo_packet: semantically acceptable
protocol_deviation:
  first_delivery: Main delivered a semantic condensation of the official leaf packet
  correction: Main immediately sent the full raw packet before synthesis
  owner_instruction: disregard the condensation
critic_scope_fact:
  beyond_bounded_lane_artifacts:
    - PLAN-0003 draft
    - lifecycle observation
    - protocol_v1
    - App Server architecture article
  cross_lane_synthesis_performed: true
  owner_action: quarantined beyond-lane and cross-lane portions
owner_recommendation:
  app_server_or_runtime_addition_now: no
  desktop_causal_evidence_gap: accepted
  capability_only_adoption: rejected
implementation_orchestrator:
  disposition: FAIL
  reason:
    - semantic condensation contaminated subject context
    - critic exceeded its bounded lane
  correction_and_quarantine_effect: did not make execution contract-conforming
  root_cause_class: role boundary
termination:
  close_authorized: true
  research_orchestrator_close_count: 1
effects:
  subject_repository_file_changes: none
```

`FAIL` and `role boundary` above are recorded Implementation Orchestrator dispositions. W2 did
not independently grade them.

## Required termination record

```yaml
termination_branch: user actual-contract-violation branch activated
matrix_completion: incomplete
sessions_not_run_due_required_termination:
  - B/F4
  - standalone-owner smoke
  - source-leaf smoke
behavior_disposition_for_not_run_sessions: none; do not label PASS or FAIL
downstream_not_launched:
  - grader
  - verifier
  - held-out smoke
  - bridge writer
downstream_precondition: six completed sessions and gate pass
bridge_added: false
implementation_orchestrator_final_execution_disposition_candidate: BLOCKED
new_policy_added: false
new_gate_added: false
new_schema_added: false
new_script_added: false
new_runtime_added: false
new_sdk_added: false
new_langgraph_added: false
new_checklist_added: false
integration_commit: none
push: none
```

`BLOCKED` is recorded as the Implementation Orchestrator's final execution disposition candidate;
it is not an independent W2 verdict.

## Execution matrix after required termination

| session | current status | raw record state |
|---|---|---|
| B/F1 | `RECORDED_CANDIDATE_EXECUTION_EVIDENCE` | Implementation Orchestrator disposition `PASS`; same-handle `EVIDENCE_COMPLETE` and `CLOSE_REQUESTED`; RO closed once by Main |
| B/F2 | `RECORDED_CANDIDATE_EXECUTION_EVIDENCE` | Implementation Orchestrator second disposition `PASS`; leaves and RO closed once |
| B/F3 | `RECORDED_CANDIDATE_EXECUTION_EVIDENCE` | Implementation Orchestrator disposition `FAIL`; required termination; leaves and RO closed once |
| B/F4 | `NOT_RUN` | required termination; no behavior `PASS`/`FAIL` disposition |
| standalone-owner smoke | `NOT_RUN` | required termination; no behavior `PASS`/`FAIL` disposition |
| source-leaf smoke | `NOT_RUN` | required termination; no behavior `PASS`/`FAIL` disposition |

The six-session matrix did not complete. No A session or model-comparison session is recorded. No
Skill-effect or adoption claim is made.

## Record scope and document impact

- This file is the only W2 write owned by this recorder.
- The W0 changed files and their hashes above remain outside this write ownership and are
  preserved.
- Applicable project and evaluation documents are unchanged by this record; this is a run-record
  addition only.
