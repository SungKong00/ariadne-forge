---
id: RESEARCH-FINAL-20260801
kind: validation-report
status: completed
authority: advisory-evidence
scope: PLAN-0002
owner: workflow-owner
checked_at: 2026-08-01
evidence_status: source-backed-with-explicit-inferences
behavior_status: unvalidated-until-forward-tests
---

# 최종 계획 검증 보고서

## 판정

`PLAN-0002`의 방향은 **조건부 채택**한다. 첫 버전은 코드 기반 그래프·상태 머신이 아니라 다음 네 요소로 제한한다.

1. 짧은 저장소 루트 `AGENTS.md`
2. 구조화된 프로젝트·운영·convention 문서
3. RED baseline 이후 만드는 저장소 전용 진입 Skill 하나
4. 실제 작업으로 측정하는 전방 검증

이 결론은 “이 구조가 이미 잘 동작한다”는 뜻이 아니다. 공식 지원 범위와 문서 운영 원칙은 확인했지만, Ariadne의 행동 효과는 아직 실행 전이다. `behavior_status`는 RED/forward test가 끝날 때까지 `unvalidated`로 유지한다.

## 연구 질문

- 사용자가 원하는 근거 중심 개발 흐름을 Codex에서 과도한 코드 하네스 없이 구현할 수 있는가?
- Skill, `AGENTS.md`, subagent, custom agent의 실제 지원 경계는 어디인가?
- 연구·비판·구현·검증 흐름을 얼마나 규칙화하고 어디를 판단 가능 영역으로 남겨야 하는가?
- 프로젝트 문서와 convention은 어떤 형식·권위·수명주기로 관리해야 하는가?
- 문자열 라벨 불일치, 디자인 근거 부족, 비판의 형식적 반박 같은 실패를 어떻게 줄일 것인가?

## 범위와 비범위

### 범위

- Codex-native 구성의 타당성
- 계획 대안과 트레이드오프
- 문서 권위·구조·검색·갱신 원칙
- 연구, 비판, 구현, 디자인 QA의 운영 규칙
- 구현 전 RED/forward-test 계획

### 비범위

- 실제 Skill 또는 custom agent 구현
- 사용자 프로젝트에 대한 행동 효과 입증
- 모든 언어·프레임워크 convention의 사전 정의
- 장기 실행·분산 복구 runtime 구현
- MengTo/Skills 전체 설치 또는 vendoring

## 조사 방법

공식 문서와 1차 자료를 먼저 확인하고, 문서 설계 방법론은 해당 프로젝트의 원문을 확인했다. 커뮤니티·저장소 사례는 공식 기능 보장이 아니라 실무 선택지를 보충하는 용도로만 사용했다. 세 개의 bounded lane을 사용했다.

최종 교정에서는 OpenAI의 Codex manual helper로 2026-08-01 현재 manual을 새로 받아 `Build skills`, `Custom instructions with AGENTS.md`, `Multi-agent operations` 절을 다시 확인했다. 따라서 repo Skill 위치, optional `agents/openai.yaml`, project custom agent 설정, AGENTS 계층에 관한 판정은 검색 snippet이 아니라 같은 시점의 공식 manual 본문과 대조됐다.

| lane | 질문 | 결과 |
|---|---|---|
| Codex capability | Skill·AGENTS·subagent·모델 설정의 공식 지원 경계 | 공식 지원과 비보장 영역 분리 |
| Documentation | docs-as-code, ADR, arc42, C4, Diátaxis의 적용 범위 | 얇은 지도 + 목적별 문서 + 최소 템플릿 채택 |
| Independent risk review | 과도한 구조, 우회 경로, 자기 승인, 검증 누락 | 다중 Skill 선구축과 늦은 보안을 중단하고 RED-first로 수정 |

문서 연구 lane의 첫 실행은 종료 요청을 받았지만 그 요청을 처리한 뒤 최종 결과를 반환했다. 세 lane 모두 최종 산출물을 회수했으며 추가 연구 wave는 열지 않았다. 독립 검토 결과는 그대로 수용하지 않고 원자료·현재 요구와 다시 대조했다.

### 질의 묶음

- `Codex repository skills .agents/skills official`
- `Codex AGENTS.md hierarchy override official`
- `Codex subagents custom agents model reasoning effort official`
- `OpenAI harness engineering AGENTS.md repository knowledge`
- `OpenAI practical guide agents incremental orchestration`
- `Agents SDK sessions resume official`, `LangGraph interrupts persistence official`
- `docs as code ADR MADR arc42 C4 Diataxis official`
- `SKOS preferred alternative labels W3C`
- `NIST secure software development framework`
- `MengTo Skills repository design workflow`

## 출처 계획과 근거 표

Tier 1은 제품·표준·방법론의 공식 문서, Tier 2는 제작자의 공개 저장소·실무 지침이다. 확인일은 모두 2026-08-01이다.

| ID | 출처 | Tier | locator | 직접 뒷받침하는 내용 | 한계·신선도 |
|---|---|---:|---|---|---|
| S00 | [OpenAI: Codex manual](https://developers.openai.com/codex/codex-manual.md) | 1 | Build skills; Custom instructions with AGENTS.md; Multi-agent operations | Codex customization 표면의 현재 종합 설명 | 지속 갱신 문서이므로 구현·평가 시 다시 fetch 필요 |
| S01 | [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | 1 | skill structure, progressive disclosure, testing sections | Skill 구조, progressive disclosure, trigger 테스트, instructions-first | 기능은 바뀔 수 있어 구현 시 재확인 필요 |
| S02 | [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 1 | discovery·precedence·size sections | root-to-leaf 탐색과 override 우선순위, 크기 제한 | 문서 내용이 행동 성공을 보장하지 않음 |
| S03 | [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 1 | custom-agent configuration and delegation sections | subagent와 project custom agent, 모델·reasoning 설정 | Skill 간 결정적 직접 호출 순서는 보장하지 않음 |
| S04 | [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/) | 1 | repository knowledge and `AGENTS.md` discussion | 거대한 단일 지침보다 짧은 지도와 구조화된 저장소 지식 | 특정 OpenAI 팀의 사례이며 보편 법칙은 아님 |
| S05 | [OpenAI: A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | 1 | orchestration and incremental adoption guidance | 단일 agent부터 시작하고 필요가 입증될 때 분리하는 점진 접근 | 일반 guide이며 Codex 저장소 설정의 세부 계약은 아님 |
| S06 | [OpenAI Agents SDK: Sessions](https://openai.github.io/openai-agents-js/guides/sessions/) | 1 | Core session behavior; Resumable runs | 세션 기반 대화 이력과 interrupted `RunState` 재개 | Ariadne에 SDK가 필요하다는 근거는 아님 |
| S07 | [OpenAI Agents SDK: Agents](https://openai.github.io/openai-agents-python/agents/) | 1 | basic configuration and handoffs | agent 구성과 handoff 등 SDK 선택지 | Codex-native Skill과 별도 runtime임 |
| S08 | [LangGraph: Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | 1 | interrupts and human-in-the-loop sections | 동적 중단과 human-in-the-loop 가능 | 도입 비용·적합성은 프로젝트별 측정 필요 |
| S09 | [LangGraph: Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | 1 | checkpoints, threads, replay sections | checkpoint·thread 기반 지속 상태 | 기능 존재가 현재 도입 필요성을 뜻하지 않음 |
| S10 | [Write the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/) | 2 | workflow and benefits sections | 버전 관리·리뷰·자동 검사 가능한 문서 운영 | 권위 충돌 규칙까지 제공하지 않음 |
| S11 | [Diátaxis](https://diataxis.fr/start-here/) | 1 | four forms of documentation | tutorial/how-to/reference/explanation 목적 분리 | 프로젝트 권위·상태 모델로 쓰는 체계는 아님 |
| S12 | [arc42 overview](https://arc42.org/overview/) | 1 | overview and template sections | 목표·제약·맥락·품질·위험을 포함한 아키텍처 관점 | 전체 12개 section은 현 단계에 과함 |
| S13 | [arc42: Architecture decisions](https://docs.arc42.org/section-9/) | 1 | section 9 | 중요한 결정의 별도 기록 | 모든 사소한 선택을 ADR로 만들라는 뜻은 아님 |
| S14 | [MADR](https://adr.github.io/madr/) | 1 | template and examples | 간결한 ADR 템플릿과 상태·대안·결과 | repository별 lifecycle은 별도 정의 필요 |
| S15 | [Michael Nygard: Documenting architecture decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | 1 | proposed ADR template | 결정의 맥락·결정·결과 기록 | 오래된 글이지만 원칙 자료로 사용; 도구 사실에는 사용하지 않음 |
| S16 | [C4 model](https://c4model.com/diagrams) | 1 | diagram types | 실제 시스템 경계를 계층적으로 설명하는 도식 | 아직 구현이 없는 단계에는 상세 component diagram이 추측이 됨 |
| S17 | [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/) | 1 | section 5 lexical labels | preferred·alternative·hidden label 개념 | RDF/SKOS 구현 필요성을 뒷받침하지 않음 |
| S18 | [NIST SSDF](https://csrc.nist.gov/Projects/ssdf) | 1 | SSDF overview and publications | 개발 수명주기 전반의 보안 관행 | 구체적인 Ariadne 명령 정책은 내부 설계 필요 |
| S19 | [MengTo/Skills](https://github.com/MengTo/Skills) | 2 | repository README and Skill catalog | 재사용 가능한 디자인 Skill 사례와 선택지 | 프로젝트 전체 권위나 디자인 품질 보증이 아님 |
| S20 | [OpenAI: trustworthy evaluation foundations](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) | 1 | independence, transparency, reproducibility principles | 평가 독립성·투명성·검증 가능성의 중요성 | Ariadne 전용 benchmark를 제공하지 않음 |
| S21 | [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/) | 1 | perceivable·operable criteria, focus and target-size criteria | 디자인 QA에 시각 외 접근성·입력 상태가 필요한 근거 | 제품별 UX 적합성과 미적 품질을 대신하지 않음 |
| S22 | [Playwright: Visual comparisons](https://playwright.dev/docs/test-snapshots) | 1 | Introduction and rendering-environment warning | 브라우저 screenshot baseline 비교와 환경 고정 필요성 | pixel diff만으로 사용성·접근성·의도를 판정할 수 없음 |
| S23 | [Google: Web Vitals](https://web.dev/articles/vitals) | 1 | Core Web Vitals and lab/field measurement sections | loading·interactivity·visual stability를 측정하는 성능 축 | 지표·threshold가 바뀔 수 있고 lab은 field를 대체하지 않음 |
| S24 | [Design Tokens Community Group: Format 2025.10](https://www.designtokens.org/tr/2025.10/format/) | 1 | sections 4–6 | token의 교환 형식·type·group·reference 선택지 | token 값이나 디자인 품질을 정해 주는 규격은 아님 |
| S25 | [Playwright: Screenshots](https://playwright.dev/docs/screenshots) | 1 | full-page and element screenshot sections | page context와 section evidence를 다른 범위로 캡처 가능 | capture 존재가 디자인 적합성을 보장하지 않음 |
| S26 | [Playwright: Trace Viewer](https://playwright.dev/docs/trace-viewer) | 1 | recording guidance; actions, snapshots, console, network, metadata | 실패·상호작용 원인을 screenshot보다 넓게 조사 가능 | 모든 run의 trace는 성능 비용이 있어 공식 문서도 상시 `on`을 권장하지 않음 |
| S27 | [Playwright: Emulation](https://playwright.dev/docs/emulation) | 1 | devices, viewport, locale/timezone/color scheme | 재현 metadata와 coverage axis | emulation이 실제 모든 기기·사용자 환경을 대체하지 않음 |
| S28 | [Playwright: Authentication](https://playwright.dev/docs/auth) | 1 | core concepts and storage-state warning | evidence bundle에서 raw auth state를 제외해야 하는 근거 | 프로젝트별 fixture·secret 정책은 별도 필요 |
| S29 | [Playwright: Videos](https://playwright.dev/docs/videos) | 1 | recording modes and context-closure behavior | interaction video의 선택적 수집과 완료 조건 | 기본 비활성이고 video만으로 상태·접근성을 판정하지 못함 |
| S30 | [W3C: PROV-O](https://www.w3.org/TR/prov-o/) | 1 | entity/activity/agent and generation/derivation relations | artifact·capture activity·source/actor를 연결하는 provenance 개념 | RDF/OWL 구현 필요성을 뜻하지 않음 |

## Claim matrix

| Claim | 상태 | 근거 | 적용 판정 |
|---|---|---|---|
| 저장소 전용 Skill을 `.agents/skills`에 둘 수 있다. | supported | S00, S01 | 첫 구현 경로로 사용 가능 |
| `AGENTS.md`는 경로 계층과 override 우선순위를 가진다. | supported | S00, S02 | 루트 파일은 짧은 지도와 invariant만 보유 |
| subagent와 project custom agent를 구성할 수 있다. | supported | S00, S03 | 측정 후 필요 역할만 추가 가능 |
| Skill이 다른 Skill을 결정적 순서로 직접 호출한다. | unsupported | S01~S03에 해당 보장 없음 | 메인 Codex agent가 조정하고 exact chain을 전제하지 않음 |
| Skill 문구만으로 모델·추론 강도가 항상 강제된다. | unsupported/partial | S03은 custom agent 설정을 지원 | 필요 시 `.codex/agents/*.toml`에서 명시; 초기에는 만들지 않음 |
| 처음부터 여러 전문 Skill이 단일 Skill보다 낫다. | hypothesis, weak | S05는 점진 분리를 권고 | 초기 6-Skill 구조 중단 |
| 거대한 `AGENTS.md`가 세부 규칙을 가장 잘 전달한다. | disputed | S02의 크기 한계, S04의 실무 사례 | 얇은 지도 + 구조화된 docs 선택 |
| LangGraph는 정적으로 적힌 흐름만 실행해 유연하지 않다. | contradicted | S08, S09 | 이 주장을 배제 근거에서 제거 |
| Agents SDK는 session·resume 능력이 없다. | stale/contradicted | S06 | 이 주장을 배제 근거에서 제거 |
| 지금 graph runtime을 보류해야 한다. | inference | S05, S06~S09 + 현재 요구 | 기능 부족 때문이 아니라 durable 실행 요구가 아직 측정되지 않았기 때문 |
| docs-as-code와 ADR가 근거·변경 이력을 보존하는 데 적합하다. | supported | S10, S13~S15 | 채택하되 ADR은 material decision만 사용 |
| Diátaxis 하나로 모든 프로젝트 문서의 권위와 lifecycle을 해결한다. | unsupported | S11의 범위 밖 | 사용자 문서 분류에만 선택적으로 사용 |
| canonical JSON label만 있으면 의미가 같은 다른 표현도 안정적으로 찾는다. | contradicted by design analysis | S17은 alternative label 개념만 제공 | path/scope + registry + alias + 본문 검색 + LLM 확인 사용 |
| semantic/vector index가 처음부터 필요하다. | hypothesis, unproven | recall gap 데이터 없음 | held-out miss가 측정될 때만 spike |
| MengTo/Skills를 사용하면 디자인 문제가 대부분 자동 해결된다. | unsupported | S19 | 첫 UI pilot의 design-only adapter로만 평가 |
| 디자인은 reference·execution contract·rendered QA를 묶어야 한다. | mixed: standards/tool facts + project inference | S19, S21~S30과 현재 요구 | 채택하되 재현 metadata와 접근성·상태·반응형·성능·독창성 축 추가; screenshot diff 단독 판정 금지 |
| 기존 JSON validator가 출처 의미까지 검증한다. | false | 로컬 validator가 shape·참조·URL 형태만 검사 | semantic/source-content validation 표현 금지 |

## 선택지와 트레이드오프

### 실행 구조

| 선택지 | 장점 | 단점 | 판정 |
|---|---|---|---|
| 프롬프트만 사용 | 가장 가볍고 즉시 시작 | 재현성·문서 강제력이 약함 | baseline으로만 사용 |
| 문서 + 단일 repo Skill | 가볍고 Codex-native이며 점진 확장 가능 | 행동 보장은 없어 테스트 필요 | **채택** |
| 여러 Skill/custom agent 선구축 | 역할이 명확해 보이고 프롬프트 재사용 가능 | trigger 충돌·관찰성 저하·유지보수 증가 | 측정 전 중단 |
| Python/LangGraph/Agents SDK runtime | durable state·명시적 제어·재개에 유리 | schema·복구·migration·운영 코드가 다시 제품이 됨 | 요구가 발생할 때 비교 spike |

### 문서 구조

| 선택지 | 장점 | 단점 | 판정 |
|---|---|---|---|
| 단일 거대 `AGENTS.md` | 한 파일에서 모두 보임 | 크기·중복·갱신·컨텍스트 비용 | 중단 |
| 얇은 `AGENTS.md` + 권위별 Markdown | 검색·리뷰·경로별 확장에 유리 | registry와 링크 관리 필요 | **채택** |
| JSON/YAML을 문서 원본으로 사용 | 기계 검증이 쉬움 | 자유로운 근거·예외·맥락 기록이 불편 | metadata와 향후 trace에만 제한 |
| 외부 wiki/DB를 원본으로 사용 | UI와 협업 기능 | 코드 버전과 분리되고 에이전트 접근 경로가 늘어남 | 초기 제외 |

### 라우팅·연구·검색

| 문제 | 경직된 선택 | 무제한 판단 | 채택한 중간안 |
|---|---|---|---|
| 작업 규모 | 숫자 threshold만 사용 | LLM 직감만 사용 | 예시 anchor + 위험 signal + abstain/escalate |
| 연구 실행 | 닫힌 trigger 목록 | 필요해 보이면 항상 조사 | open signal + 생략 이유 + skip 표본 감사 + 누구나 reopen |
| 문서 검색 | exact ID/label | 모든 문서 전부 읽기 | path/scope → registry → alias/용어 → 본문 검색 → 후보 본문 확인 |
| 비판 대응 | 무조건 반박 | 무조건 수용 | 근거 있는 rebuttal 시도 후 accept/partial/unresolved/resolver |

### 디자인 경로

| 선택지 | 장점 | 단점 | 판정 |
|---|---|---|---|
| 일반 구현 agent에게 위임 | 단순함 | 세부 디자인 근거·시각 QA가 빠질 수 있음 | 단독 사용 금지 |
| MengTo/Skills에 전면 위임 | 디자인 prompt 재사용 | 프로젝트 맥락·접근성·독창성·품질을 보장하지 않음 | 중단 |
| Reference Evidence + Execution Contract + Multi-axis Visual QA | 결정과 결과를 비교 가능 | evidence 수집과 browser QA 비용 | **디자인 materiality가 있을 때 채택** |

시각 반복은 “매번 CSS 속성 하나”가 아니라 **검증 가능한 가설 하나**만 바꾼다. 연관된 토큰·레이아웃 값은 같은 가설 안에서 함께 바꿀 수 있고, 스크린샷뿐 아니라 상호작용 상태·반응형·현지화·접근성/reduced motion·성능·브랜드 독창성을 함께 검사한다. screenshot 비교 환경은 browser·OS·font·viewport를 고정하거나 차이를 기록한다.

## 독립 검토와 처리

독립 위험 검토는 다음을 요구했다.

| Finding | 최종 disposition | 이유 |
|---|---|---|
| 자기 승인과 self-`DONE`을 금지하라 | keep | 구현자 주장과 검증 판정을 분리해야 확증 편향을 줄임 |
| 연구 재개와 비판의 근거 요구를 유지하라 | keep | 닫힌 trigger와 형식적 반박을 동시에 피함 |
| 18-state reducer를 줄여라 | keep-as-stopped | 첫 버전에는 reducer 자체가 없음 |
| JSON을 canonical truth로 두지 마라 | modify | Markdown이 맥락 원본, JSON은 향후 trace/검사용 projection만 가능 |
| global single writer를 수정하라 | modify | 겹치는 write-set/file별 한 명, disjoint file은 병렬 가능 |
| broad action broker를 제거하라 | keep-as-stopped | 초기 Skill은 직접 코딩 경로를 만들지 않음 |
| 6개 Skill을 한 번에 만들지 마라 | accepted | RED baseline 뒤 단일 진입 Skill만 구현 |
| 보안을 마지막 단계로 미루지 마라 | accepted | 첫 mutation 전 scope·secret·destructive-action 규칙 적용 |
| deterministic applicator부터 만들어라 | partial/rejected | scope 실패가 RED에서 관측될 때만 좁은 validator/applicator를 추가; 선구축은 새 하네스 위험 |

## KEEP / MODIFY / STOP 기록

### 최종 completion gate

첫 읽기 전용 완료 판정은 전체 방향·단계·검증 경계를 통과시켰지만 문서 형식의 두 불일치 때문에 `CONTINUE`를 반환했다.

- 공통 authority 값과 convention 예시가 달랐다 → convention 예시를 `authority: normative`로 통일하고 `status: active`가 구속력을 결정하게 수정했다.
- `validation-report` kind의 최소 본문 계약이 없었다 → research 계약에 판정, 검증 범위·비범위, KEEP/MODIFY/STOP, 잔여 위험을 더한 행을 등록했다.

수정 후 새 읽기 전용 판정자가 두 항목과 인접 문서를 다시 확인해 `Decision: DONE`, material finding 없음으로 판정했다. 이 `DONE`은 이번 **계획 문서 완성 계약**에 대한 판정이며 Ariadne Skill의 행동 검증은 아니다.

이후 추가한 browser evidence manifest와 Playwright/W3C provenance 근거도 같은 판정자가 좁게 재검토해 다시 `Decision: DONE`, material finding 없음으로 판정했다.

### KEEP

- material decision은 claim·evidence·limitation·confidence·owner와 연결한다.
- 연구자는 다양한 출처 lane을 사용하고, synthesizer는 충돌을 숨기지 않는다.
- 비판자는 반증을 시도하며, 원 작성자는 근거 있는 반박을 먼저 검토한다.
- 반박이 약하면 억지로 방어하지 않고 수용·부분 수용·미해결로 처리한다.
- 구현자와 최종 verifier를 분리하며 구현자 스스로 완료 판정을 내리지 않는다.
- convention과 project docs는 계획·구현 전에 반드시 binding한다.
- 디자인에는 Reference Evidence System, Design Execution Contract, rendered QA loop를 사용한다.

### MODIFY

- 고정형 complexity classifier → 예시 기반 Quick/Standard/Deep + risk signal + abstain.
- 연구 whitelist → open signal, skip reason, reopen, false-negative audit.
- 전역 single writer → 겹치는 write-set별 single owner.
- exact one-change visual loop → one-testable-hypothesis loop.
- JSON canonical knowledge → Markdown canonical, 구조화 metadata는 식별·scope·lifecycle 용도.
- “모든 결정에 외부 출처” → material decision에 적합한 evidence burden; 로컬 코드·테스트·사용자 요구도 유효 근거.

### STOP

- 첫 버전에 LangGraph/Agents SDK/Python state machine을 구축하는 일.
- reducer·event store·action broker·custom UI를 선구축하는 일.
- 6개 역할 Skill과 custom agent를 동시에 만드는 일.
- giant `AGENTS.md`, 빈 문서 트리, 모든 선택의 ADR화.
- canonical ID exact match만으로 convention을 찾는 일.
- source URL과 schema가 있다는 이유로 semantic validation을 주장하는 일.
- MengTo/Skills를 프로젝트 전역 권위로 위임하거나 전체 vendoring하는 일.

## 채택한 최종 결정

1. **RED-first**: Skill 없는 동일 작업을 먼저 수행해 실제 실패를 기록한다.
2. **one-file entry Skill**: 실패가 확인된 뒤 `.agents/skills/ariadne-workflow/SKILL.md` 하나만 만든다. 기존 권위 문서를 복제하지 않고, 반복 누락이 측정될 때만 reference나 `agents/openai.yaml`을 추가한다.
3. **main-agent coordination**: Skill 간 직접 호출 그래프를 가정하지 않고 메인 Codex agent가 연구·구현·검증 역할을 조정한다.
4. **thin map, authoritative docs**: `AGENTS.md`는 지도와 invariant만, 상세 규칙은 권위 문서에 둔다.
5. **evidence proportionality**: 결정의 영향·가역성·불확실성에 비례해 근거 부담을 높인다.
6. **adaptive routing**: Quick/Standard/Deep는 판정 보조 수단이며 불확실하면 상향·재연구할 수 있다.
7. **evidence-contested critique**: 반박을 시도하되 근거가 약하면 수용하며 unresolved는 독립 resolver에 올린다.
8. **convention lifecycle**: draft → candidate → active → deprecated/superseded/rejected를 사용하고 active만 기본 구속력을 갖는다.
9. **semantic retrieval without premature embeddings**: registry·scope·alias·본문 검색 후 LLM이 후보를 읽는다. recall miss가 측정될 때만 semantic index를 실험한다.
10. **design adapter boundary**: MengTo/Skills는 첫 UI pilot의 제안 재료이며 프로젝트 문서와 QA contract가 우선한다.
11. **runtime escalation by need**: crash-resume, 장기 human wait, 다중 프로세스, 감사 가능한 replay 요구가 반복될 때 Agents SDK/LangGraph/직접 구현을 같은 vertical slice로 비교한다.

## 문서 구조 판정

현재 필요한 문서만 만든다.

```text
AGENTS.md                          # 짧은 진입 지도와 불변 규칙
docs/
├── README.md                     # 권위·상태·탐색 registry
├── project.md                    # 목표, 비목표, 품질, 성공·중단 기준
├── architecture.md               # 현재 구조, 경계, 확장 trigger
├── operating-model.md            # 연구·비판·구현·검증의 규범 흐름
├── conventions/
│   └── README.md                 # 형식, scope, lifecycle, 검색 규칙
├── decisions/
│   └── 0001-...md                # material decision의 ADR
├── plans/active/
│   └── 0002-...md                # 실행 순서와 acceptance criteria
└── research/
    └── final-plan-validation-...md # 근거·충돌·한계; advisory
```

문서 권위는 `사용자 요구 > 더 가까운 AGENTS.md > active convention/project/architecture/operating-model > accepted ADR > active plan > research` 순서다. 충돌이 material하면 임의 선택하지 않고 작업을 멈춰 owner 또는 resolver에게 올린다. research는 결정 재료이지 자동 규칙이 아니며, plan은 현재 할 일을 말하지만 장기 규범을 덮어쓰지 않는다.

Convention은 짧은 metadata와 사람이 읽을 수 있는 본문을 함께 사용한다. 필수 metadata는 `id`, `kind`, `status`, `scope`, `applies_to`, `owner`, `last_verified`, `supersedes`, `aliases`이다. 본문에는 규칙, 이유, 예외, 좋은/나쁜 예, 검증 방법, 근거, 재검토 조건을 둔다. 아직 정하지 않은 규칙은 빈 active convention으로 만들지 않고 research → candidate → pilot → review 후 활성화한다.

## 구현 전 검증 기준

### RED baseline

- B1: 구현자가 자신의 결과를 `DONE`으로 확정하는가?
- B2: 관련 convention/project 문서를 읽지 않고 계획하는가?
- B3: 외부·로컬 근거 없이 material decision을 확정하는가?
- B4: 비판을 무조건 수용하거나 억지로 반박하는가?
- B5: 겹치는 write-set에 두 writer가 생기는가?
- B6: 실패한 test나 stale evidence digest를 두고 완료하는가?
- B7: 다른 표기의 convention을 검색에서 놓치는가?
- B8: 디자인 결과가 reference/contract/다축 QA 없이 승인되는가?

### Forward test

같은 task·환경·budget에서 baseline과 단일 Skill을 비교한다. task별 raw transcript/명령/파일 diff/verifier 결과를 보존하고, 요약만으로 통과시키지 않는다. 최소 평가 축은 document binding recall, unsupported material-decision rate, research false-negative rate, critique disposition quality, scope violation, verifier independence, 완료 오탐, 사용자 개입 비용이다.

Skill 도입 뒤 RED 실패가 재현되지 않거나 새로운 우회가 생기면 즉시 구현을 중단하고 규칙 또는 구조를 수정한다. 실패 유형이 문구로 해결되지 않을 때만 좁은 deterministic check를 추가한다.

## 충돌·미해결·재확인 조건

| 항목 | 현재 상태 | 다음 판정 조건 |
|---|---|---|
| Quick/Standard/Deep 분류 정확도 | hypothesis | 사용자 라벨 task set과 false-negative 결과 |
| 한 개 Skill의 trigger/준수 효과 | unvalidated | RED와 같은 held-out forward test |
| alias + full-text 검색 recall | unvalidated | 철자·한영·동의어가 다른 convention fixture |
| custom agent 필요성 | deferred | 역할 혼선 또는 verifier 독립 실패가 반복될 때 |
| deterministic validator 필요성 | deferred | prompt/doc 규칙의 scope·completion 우회가 관측될 때 |
| LangGraph/Agents SDK 필요성 | deferred | durable wait/resume/replay 요구와 spike 비교 결과 |
| MengTo/Skills 효과 | unvalidated | 첫 UI pilot의 품질·접근성·수정 비용 비교 |
| 보고서 최적 형식 | provisional | 실제 구현 agent의 retrieval·근거 추적 실패를 관찰할 때 |

## 신뢰도와 한계

- **공식 기능 경계:** 높음. 공식 OpenAI 문서를 직접 확인했다. 단, 제품 변경 가능성이 있으므로 구현 시작 시 다시 확인한다.
- **문서 구조 선택:** 중상. 여러 공식 방법론과 현재 프로젝트 규모가 일치하지만 실제 유지 비용은 pilot 전이다.
- **단일 Skill이 행동을 개선한다는 주장:** 낮음/미검증. 이것이 RED-first의 이유다.
- **graph runtime 보류:** 중상. 현재 요구에는 타당하지만 장기 resume/replay 요구가 생기면 재검토해야 한다.
- **디자인 adapter 효과:** 낮음/미검증. 저장소 존재와 품질 효과는 다른 주장이다.

이 보고서는 출처 URL 존재, schema 적합성, 독립 검토를 근거로 **semantic validation 또는 행동 검증을 주장하지 않는다**. 최종 동작 판정은 `PLAN-0002`의 RED baseline과 forward test에서만 내려진다.
