# Plan

## 목표
`bowling/game.py`에 `Game` 클래스를 새로 만든다. 모든 프레임에서 거터볼(0핀)만 던졌을 때 `score()`가 0을 반환한다.

## 실패하는 테스트
`tests/test_game.py::test_all_gutter_balls_scores_zero`
- `Game()` 인스턴스를 만들고 `roll(0)`을 20번 호출한 뒤 `score() == 0`을 검증한다.
- 현재 `bowling/game.py`가 존재하지 않아 `ModuleNotFoundError`로 실패한다.

## 접근
- `Game` 클래스는 `roll(pins)` 호출 시 던진 핀 수를 내부 리스트에 기록한다.
- `score()`는 지금 단계에서는 기록된 모든 투구의 합을 반환하는 정도로 최소 구현한다 (이 테스트를 통과시키는 데 필요한 만큼만).
- 스트라이크/스페어/10번 프레임 보너스 로직은 이후 사이클에서 각각의 실패하는 테스트로 추가한다.
