---
id: ADR-0001
kind: decision
status: accepted
authority: decision
scope: ariadne-foundation
owner: project-owner
date: 2026-08-01
last_verified: 2026-08-01
supersedes: null
---

# Codex-native Skill-first clean restart

## Context

Harness Maestro는 코드 중심 오케스트레이션이 커지면서 구현·동작 확인·유지보수가 모두 어려워졌다. Ariadne의 첫 목표는 같은 기능 집합을 다시 만드는 것이 아니라 근거 없는 결정과 거짓 완료를 더 적은 구조로 줄이는 것이다.

현재 Codex는 저장소의 `.agents/skills`, 계층형 `AGENTS.md`, project-scoped `.codex/agents`와 subagent 위임을 공식 지원한다. 반면 Skill 간 결정적 호출, 정확한 fan-out 수, Skill 자체의 모델·추론 강도 강제는 보장되지 않는다.

## Decision drivers

- 사용자에게 효과가 보이기 전 코드 런타임을 만들지 않는다.
- 자연어 절차의 유연성을 보존한다.
- 지원되는 Codex 표면만 사실로 주장한다.
- 작은 평가로 분리·자동화 필요성을 증명한다.
- 저장소 안에서 지침·근거·결정이 추적 가능해야 한다.

## Considered options

| 선택지 | 장점 | 비용·위험 | 판정 |
|---|---|---|---|
| 프롬프트만 사용 | 준비 비용 0 | 반복성·문서 준수·검증 일관성이 낮음 | baseline으로만 사용 |
| 단일 repo Skill + 기존 권위 문서 | 공식 discovery, 중복이 적고 수정 범위가 작음 | 절차적 강제이며 결정적 실행 보장은 없음 | **선택** |
| 여러 Skill과 custom agents를 즉시 구성 | 역할 분리와 재사용 | trigger·체이닝·평가·유지보수 표면이 한꺼번에 늘어남 | 실패 증거가 생길 때까지 보류 |
| 자체 reducer/Action Broker | 상태·권한을 코드로 강제 가능 | Maestro와 같은 복잡성, 호스트 우회·재시도·영속성 문제 | 중단 |
| Codex SDK/App Server, Agents SDK, LangGraph, 기타 runtime graph | thread·event·handoff·관찰 도구 제공 가능 | 현재 필요보다 큰 runtime·dependency·이중 상태 결합 | **현재 구현에서 명시적 제외**; 직접 실패 증거가 생기면 새 decision과 plan으로만 재검토 |

## Decision

1. Skill이 없는 RED baseline을 먼저 실행한다.
2. 그다음 `$REPO_ROOT/.agents/skills/ariadne-workflow/`에 진입 Skill 하나만 만든다.
3. `SKILL.md`는 routing·완료 조건·단계 선택만 담당하고 연구·구현·비판·문서 바인딩의 원본은 repository 권위 문서로 유지한다. 반복 누락이 전방 검증에서 확인될 때만 좁은 Skill reference를 추가한다.
4. 초기에는 persistent custom agent를 만들지 않는다. Skill 지침으로 bounded ad hoc subagent를 사용하고 반복 실패가 측정된 역할만 `.codex/agents`로 승격한다.
5. 스크립트는 링크, 필수 절, 상태 값처럼 결정론적으로 판정 가능한 실패가 반복될 때만 추가한다.
6. PLAN-0002에는 Codex SDK, Codex App Server, OpenAI Agents SDK, LangGraph, runtime observer·graph·state runtime 코드·dependency·config를 넣지 않는다. 이는 active/deferred 구현 phase가 아니며, 반복된 직접 실패나 새 외부 요구가 관찰되면 별도 decision과 plan에서만 재검토한다.

## Consequences

긍정적 결과:

- 저장소 안에서 즉시 버전 관리되고 Codex가 공식 경로로 발견한다.
- 자연어 연구·재계획의 escape hatch를 유지한다.
- 실패가 난 부분만 별도 Skill, custom agent 또는 코드로 승격할 수 있다.

부정적·중립적 결과:

- 초기 완료 게이트는 절차적 계약이며 강제 보안 경계가 아니다.
- 모델이 지침을 누락할 가능성은 forward test로 계속 측정해야 한다.
- Skill이 다른 Skill을 결정적으로 호출한다고 가정할 수 없다.
- 특정 모델·추론 강도 사용은 실제 spawn/config 증거가 있을 때만 주장할 수 있다.

## Revisit when

아래 신호는 현재 구현의 deferred phase를 여는 것이 아니라 새 evidence-backed decision·plan을 검토할 trigger다.

- multi-day crash-resume이나 외부 event trigger가 필수다.
- 20개 이상의 동시 작업 또는 cross-process worker가 필요하다.
- 동일한 scope 위반·거짓 완료가 Skill 개선 후에도 허용 기준을 넘는다.
- 한 Skill의 지침 복잡성 때문에 올바른 단계·도구 선택 실패가 반복된다.
- 배포·결제·외부 메시지처럼 비가역 side effect를 자동화한다.

## Evidence

- [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenAI Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [OpenAI Harness engineering](https://openai.com/index/harness-engineering/)
- [OpenAI A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [`../research/final-plan-validation-20260801.md`](../research/final-plan-validation-20260801.md)
