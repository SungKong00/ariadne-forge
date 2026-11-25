# Ariadne Forge 첫 실행

이 예제는 공개 저장소의 스킬을 좁은 작업에 적용해 보는 첫 단계다. README에 소개한 별도 연구 실험을 재현하지 않는다.

Git과 Codex가 필요하다. 공개 버전의 예제를 복제한 뒤 해당 폴더를 Codex에서 연다. 스킬을 전역에 설치할 필요는 없다.

```bash
git clone https://github.com/SungKong00/ariadne-forge.git
cd ariadne-forge
git switch --detach 185fc97c4400d0158090f5d182a6b0e3f5d1ac2a
```

Codex의 스킬 목록에서 `ariadne-workflow`를 선택하고 아래 요청을 보낸다. 목록에 안 보이면 저장소를 연 상태인지 확인한다. [Codex 스킬 사용법](https://developers.openai.com/codex/skills)

```text
ariadne-workflow 스킬을 사용해 evals/ariadne-workflow/fixtures/b1-quick/src/greeting.txt의
hello를 annyeong으로 바꿔줘. 그 예제 디렉터리에서 sh test.sh를 실행하고
바뀐 파일과 종료 코드를 알려줘. 커밋은 하지 마.
```

확인 기준은 **인사말 파일만 변경되고 테스트는 종료 코드 0**이다. 검토자는 같은 예제 디렉터리에서 `sh test.sh`를 직접 실행해 확인할 수 있다.

[README로 돌아가기](../../../README.md)
