# Ariadne Workflow evaluation fixtures

이 디렉터리는 `PLAN-0002`의 no-Skill/with-Skill 비교에 사용하는 고정 fixture다.

B10의 event 이름과 record shape는 lifecycle 구분을 채점하기 위해 만든 **synthetic normalized fixture inputs**다. 공식 Codex/Codex App Server vocabulary나 이 저장소에서 관찰한 host event를 재현한다고 주장하지 않는다. Canonical grader dimensions는 host observation, contract currency, phase semantic disposition, evidence disposition, inspection trigger, close disposition 여섯 개다.

## 실행 원칙

1. baseline과 with-Skill run은 서로의 대화·출력·grading을 보지 못하는 각각의 fresh context에서 시작한다.
2. agent-visible fixture 입력만 매 run마다 새 임시 디렉터리로 복사하고, 복사본에서 Git 저장소를 초기화해 시작 상태를 커밋한다. `scenarios.md`처럼 grader oracle로 지정된 파일은 실행 context와 agent가 접근할 수 있는 복사본에서 제외한다.
3. baseline은 `ariadne-workflow`를 주입하지 않고 `prompts/<case>.md`의 요청만 전달한다.
4. with-Skill run은 baseline과 동일한 model, reasoning effort, permissions, prompt·fixture input, retry budget을 사용한다. 명시적 `ariadne-workflow` Skill injection만 유일한 실험 변수다.
5. grader는 oracle을 두 run 모두 끝날 때까지 숨기고, agent의 자기 보고가 아니라 각 run의 raw response, 복사본 diff, 실제 명령 결과와 작성된 산출물을 직접 확인한 뒤 `rubric.md`로 판정한다.
6. 원시 출력과 실행 증거를 먼저 보존하고 두 run의 판정을 마친 뒤에만 비교 summary artifact를 작성한다.

Fixture 원본은 실행 중 수정하지 않는다. 실행 복사본과 원시 로그는 저장소 밖 임시 디렉터리에 두고, 실행 후 요약된 evidence packet만 `runs/`에 기록한다.

## 초기 범위

- 필수 baseline: B1, B2, B4, B6, B7
- 분류 fixture: B10 lifecycle observation
- 보류: B3, B5, B8, B9, B11
- 현재 목적: Skill이 해결해야 할 실제 누락과 이미 잘 되는 행동을 분리

현재 B10 상태는 **static oracle alignment only; B10 behavior unvalidated.** B10 run 또는 paired behavior 결과는 이 디렉터리의 현재 fixture·rubric만으로 주장하지 않는다.
