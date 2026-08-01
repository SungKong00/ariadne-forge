# Ariadne Workflow evaluation fixtures

이 디렉터리는 `PLAN-0002`의 no-Skill/with-Skill 비교에 사용하는 고정 fixture다.

## 실행 원칙

1. `fixtures/<case>`를 매 run마다 새 임시 디렉터리로 복사한다.
2. 복사본에서 Git 저장소를 초기화하고 시작 상태를 커밋한다.
3. baseline은 `ariadne-workflow`를 주입하지 않고 `prompts/<case>.md`의 요청만 전달한다.
4. with-Skill run은 같은 fixture, prompt, model, effort, permission, retry budget을 사용하고 Skill만 명시적으로 주입한다.
5. grader는 agent의 자기 보고가 아니라 복사본의 diff, 명령 결과, 작성된 산출물과 `rubric.md`를 판정한다.

Fixture 원본은 실행 중 수정하지 않는다. 실행 복사본과 원시 로그는 저장소 밖 임시 디렉터리에 두고, 요약된 evidence packet만 `runs/`에 기록한다.

## 초기 범위

- 필수 baseline: B1, B2, B4, B6, B7
- 보류: B3, B5, B8–B11
- 현재 목적: Skill이 해결해야 할 실제 누락과 이미 잘 되는 행동을 분리
