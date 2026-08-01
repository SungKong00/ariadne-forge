---
id: CONVENTION-REGISTRY
kind: convention-registry
status: active
authority: normative
scope: repository
owner: project-owner
last_verified: 2026-08-01
---

# Convention 등록부와 작성 형식

## 현재 상태

아직 application code나 product design이 없으므로 active 언어·framework·UI convention은 없다. 기술 stack이 정해지기 전에 Java·React·디자인 규칙을 선제 생성하지 않는다.

| ID | 제목 | status | scope / applies to | 문서 |
|---|---|---|---|---|
| — | 등록된 domain convention 없음 | — | — | — |

프로젝트 전체 작업 방식은 [`../operating-model.md`](../operating-model.md)가 소유한다. 이 등록부에는 구현·테스트·API·문서·디자인처럼 특정 산출물에 적용되는 규칙만 넣는다.

## Convention이 필요한 때

다음 중 하나가 실제로 발생하면 candidate를 만든다.

- 같은 선택을 두 번 이상 반복해서 다시 판단하고 있다.
- 서로 다른 구현이 일관성·유지보수·사용성 문제를 만든다.
- framework·platform·security·accessibility hard constraint를 놓칠 수 있다.
- 외부 style guide만으로는 project context에 맞는 선택을 정할 수 없다.
- design token, component behavior, API boundary처럼 후속 작업에 확산될 결정이다.

일회성 local choice, formatter가 자동 해결하는 형식, 아직 stack이 없는 분야에는 문서를 만들지 않는다.

## 상태 생명주기

```text
draft -> candidate -> active -> deprecated -> superseded
                    \-> rejected
```

- `draft`: 조사·작성 중이며 적용 금지
- `candidate`: 작은 pilot에서 평가 가능하나 기본 규칙은 아님
- `active`: 명시된 scope와 applicability에서 규범
- `deprecated`: 새 사용은 금지하지만 기존 migration 중
- `superseded`: 다른 convention이 대체; replacement ID 필수
- `rejected`: 검토했지만 채택하지 않음; 이유 보존

LLM이나 외부 Skill은 `draft`·`candidate`를 제안할 수 있다. `active` 승격은 근거, pilot/held-out 검증, 독립 검토와 project owner 결정이 필요하다.

## 파일 위치와 이름

```text
docs/conventions/
├── README.md
├── code-<topic>.md
├── test-<topic>.md
├── api-<topic>.md
├── docs-<topic>.md
└── design-<topic>.md
```

하위 디렉터리는 한 디렉터리에 약 12개 이상의 active 문서가 생기거나 명확한 별도 owner·scope가 있을 때만 추가한다.

## 최소 frontmatter

```yaml
---
id: CONV-DESIGN-BUTTON-001
kind: convention
status: candidate
authority: normative
scope:
  - src/ui/**
applies_to:
  - interactive button component
excludes:
  - icon-only toolbar control
owner: frontend-owner
last_verified: 2026-08-01
review_when:
  - design system major version changes
  - three approved exceptions accumulate
aliases:
  - 버튼 규칙
  - button sizing
supersedes: null
---
```

Frontmatter는 inventory·filter·lint를 위한 metadata다. 적용 가능성을 exact string으로 판정하지 않는다. 본문의 scope, 예시, 제외 조건과 실제 작업 맥락을 함께 읽는다.

## 본문 template

```markdown
# 제목

## Rule
짧고 검증 가능한 규칙. MUST/SHOULD/MAY를 필요할 때만 사용한다.

## Why
품질 scenario, 사용자·프로젝트 목적, 채택 근거.

## Applies to
적용 path, component, 상황, version.

## Does not apply to
예외가 아니라 원래 범위 밖인 경우.

## Examples
권장 예시와 이유.

## Counterexamples
금지·위험 예시와 어떤 실패가 생기는지.

## Verification
formatter, lint, test, browser check, manual review 등 실제 판정 방법.

## Exceptions
승인 주체, 기록 형식, 만료·재검토 조건.

## Evidence and alternatives
직접 확인한 source, 프로젝트 pilot, 검토한 대안과 한계.

## Change history
중요한 변경과 replacement link.
```

## 적용 우선순위

Codex 시스템·개발자·사용자 지침과 applicable `AGENTS.md`가 우선한다. 그 아래 저장소 convention끼리는 다음 순서로 해석한다.

1. `status: active`만 자동 적용한다.
2. 대상 path·component·version과 실제로 교집합이 있는지 본다.
3. 더 구체적인 scope가 더 일반적인 scope보다 우선한다.
4. 한 convention이 다른 것을 명시적으로 `supersedes`하면 새 문서를 따른다.
5. 같은 specificity와 applicability에서 충돌하면 날짜나 파일명으로 임의 선택하지 않고 `NEEDS_DECISION`으로 올린다.

`candidate`는 실험 계획에 명시됐을 때만 사용하며 결과를 active 규칙처럼 일반화하지 않는다.

## 검색과 동의어 문제

ID와 label은 관계를 안정적으로 기록하는 수단이지 의미 검색의 전부가 아니다.

1. 대상 path와 artifact 종류로 registry를 좁힌다.
2. ID, title, aliases뿐 아니라 `Rule`, `Applies to`, 예시 본문을 full-text 검색한다.
3. 철자 변형, 한국어·영어, 약어와 상위·하위 개념을 쿼리에 포함한다.
4. 후보 문서를 직접 읽고 적용성을 판단한다.
5. 못 찾았다는 사실을 “규칙이 없다”로 즉시 단정하지 않고 project docs와 인접 코드를 확인한다.

W3C SKOS의 preferred/alternative/hidden label 구분은 aliases를 설계하는 참고 근거다. Ariadne가 RDF나 SKOS 전체를 구현한다는 뜻은 아니다. 실제 recall fixture가 lexical 접근의 한계를 보이기 전에는 semantic index를 만들지 않는다.

## Convention Research 기록

candidate 문서 또는 연결된 research report에는 다음을 남긴다.

- 결정 질문과 실제 실패
- hard constraint와 project context
- source별 정확한 locator·version·한계
- 최소 두 옵션과 trade-off
- prototype/pilot 결과
- critic finding과 disposition
- active 승격 기준과 폐기 조건

버튼의 padding·font·height 같은 값도 외부 screenshot의 숫자를 그대로 권위로 삼지 않는다. 사용자 목적, typography metric, target size, localization, responsive state, 실제 렌더링과 함께 검증한다.

## 기계 검사 승격

문서만으로 반복 위반이 생기면 가장 작은 자동 검사를 추가한다.

- formatter가 소유할 수 있는 것은 formatter로 이동
- AST·dependency boundary는 lint/structural test로 이동
- 접근성·interaction은 자동 검사와 수동/browser scenario를 조합
- taste·제품 적합성은 evidence-backed review로 유지

자동화 뒤에도 이 문서는 규칙의 이유, 적용 범위, 예외와 remediation을 설명한다. 코드와 문서가 서로 다른 규칙을 소유하지 않게 한다.
