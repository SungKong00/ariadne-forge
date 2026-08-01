# Ariadne Forge 작업 지침

이 파일은 지침의 본문이 아니라 저장소 지식의 지도다. 세부 규칙은 링크된 문서를 읽는다.

## 먼저 읽을 문서

- 모든 작업: [`docs/README.md`](docs/README.md)
- 모든 변경 작업: [`docs/project.md`](docs/project.md), [`docs/operating-model.md`](docs/operating-model.md)
- Standard/Deep 작업: [`docs/model-selection.md`](docs/model-selection.md)
- subagent 위임 작업: [`docs/agent-orchestration.md`](docs/agent-orchestration.md)와 [`docs/model-selection.md`](docs/model-selection.md)
- 구조·dependency·상태·권한 경계 변경: [`docs/architecture.md`](docs/architecture.md)와 관련 accepted decision
- 구현·설계: [`docs/conventions/README.md`](docs/conventions/README.md)에서 대상 경로에 적용되는 active convention 확인
- 현재 기반 구현: [`docs/plans/active/0002-codex-native-skill-first-plan.md`](docs/plans/active/0002-codex-native-skill-first-plan.md)

`PLAN-0001`은 superseded 기록이며 구현 기준이 아니다.

## 작업 원칙

1. 요구사항과 변경 대상을 확인한 뒤 Quick, Standard, Deep 중 임시 경로를 정한다. 불확실하면 상위 경로로 올리고 진행 중에도 재분류할 수 있다.
2. workflow route와 모델 선택을 같은 분류로 취급하지 않는다. Standard/Deep 역할은 위험 하한·검증 가능성에 따라 model profile과 reasoning effort를 추천하고, 실제 적용값을 확인 가능한 범위에서 기록한다.
3. 코드나 문서를 바꾸기 전에 적용 문서를 `Document Binding`으로 명시한다. 관련 문서가 없거나 충돌·노후화됐으면 조용히 추측하지 말고 계획에 해결 단계를 넣는다.
4. 중요한 결정은 사용자 요구, 프로젝트 규범, 현재 저장소 사실, 실행 결과 또는 직접 확인한 외부 근거와 연결한다. 사소한 문법 선택마다 별도 기록을 만들 필요는 없다.
5. 외부 사실이 최신성·정확성에 영향을 주거나 기존 근거가 충돌하면 연구를 연다. 닫힌 키워드 목록만으로 연구 필요성을 판정하지 않는다.
6. Standard/Deep 작업은 완료 계약을 먼저 쓰고, 계획 또는 결과를 독립 시각으로 검토한다. 비판을 억지로 반박하거나 무조건 수용하지 않는다.
7. 병렬 작업은 읽기 중심을 우선한다. 쓰기는 겹치지 않는 소유 범위를 선언하고, 같은 파일·같은 책임 범위에는 동시에 한 명만 쓴다.
8. Standard/Deep의 연구·구현 phase는 물리적으로 분리된 Research/Implementation Orchestrator가 분해·packet 판정·후속 작업을 소유한다. 현재 surface에서 main은 이들이 요청한 spawn·send·wait·stop·close를 안전 검사 후 대행하고 packet을 재종합하지 않은 채 전달한다. direct nested control이나 자동 cleanup을 전제로 설계하지 않는다.
9. 완료 보고는 실제 산출물, diff, 명령 결과, 테스트와 남은 위험을 근거로 한다. 스키마나 링크 검사만으로 내용의 진실성이 검증됐다고 표현하지 않는다.
10. 변경 후 관련 문서의 `update / create / unchanged / supersede` 판단을 남긴다.

## 안전 경계

- 사용자 요청 없이 commit, push, 배포, 외부 메시지 전송, 비가역 작업을 하지 않는다.
- 작업 시작 시 writable 범위와 금지 범위를 정한다. 범위를 벗어난 기존 변경은 보존한다.
- 비밀·토큰·개인정보를 연구 packet, 로그, 예시 또는 프롬프트에 복사하지 않는다.
- 외부 Skill은 제안·수집·검사 도구다. 프로젝트 규범이나 완료 판정 권한을 넘기지 않는다.

## 문서 권위

시스템·개발자·사용자 지침과 Codex의 `AGENTS.md` 계층이 항상 우선한다. 저장소 내부에서는 active project policy와 적용 범위가 맞는 active convention을 따르고, accepted decision은 그 배경을 설명한다. 계획은 실행 의도, 연구는 advisory evidence다. 같은 권위와 적용 범위가 충돌하면 임의로 하나를 고르지 말고 `NEEDS_DECISION`으로 올린다.
