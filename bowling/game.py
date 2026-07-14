FRAMES_PER_GAME = 10
REGULAR_FRAMES = FRAMES_PER_GAME - 1
ALL_PINS = 10
STRIKE_ROLLS = 1
OPEN_OR_SPARE_ROLLS = 2


class Game:
    def __init__(self) -> None:
        self._rolls: list[int] = []

    def roll(self, pins: int) -> None:
        self._rolls.append(pins)

    def score(self) -> int:
        total = 0
        roll_index = 0

        for _ in range(REGULAR_FRAMES):
            frame_score, rolls_used = self._score_frame(roll_index)
            total += frame_score
            roll_index += rolls_used

        total += self._score_last_frame(roll_index)
        return total

    def _score_frame(self, roll_index: int) -> tuple[int, int]:
        if self._is_strike(roll_index):
            return self._score_strike(roll_index), STRIKE_ROLLS

        if self._is_spare(roll_index):
            return self._score_spare(roll_index), OPEN_OR_SPARE_ROLLS

        return self._score_open_frame(roll_index), OPEN_OR_SPARE_ROLLS

    def _is_strike(self, roll_index: int) -> bool:
        return self._rolls[roll_index] == ALL_PINS

    def _is_spare(self, roll_index: int) -> bool:
        return self._rolls[roll_index] + self._rolls[roll_index + 1] == ALL_PINS

    def _score_strike(self, roll_index: int) -> int:
        return ALL_PINS + self._rolls[roll_index + 1] + self._rolls[roll_index + 2]

    def _score_spare(self, roll_index: int) -> int:
        return ALL_PINS + self._rolls[roll_index + 2]

    def _score_open_frame(self, roll_index: int) -> int:
        return self._rolls[roll_index] + self._rolls[roll_index + 1]

    def _score_last_frame(self, roll_index: int) -> int:
        # 10번 프레임은 스트라이크/스페어 시 최대 3회까지 투구가 허용되며,
        # 그 프레임에서 던진 핀 수의 합이 곧 프레임 점수다 (미래 프레임에서
        # 보너스를 빌려올 필요가 없다).
        return sum(self._rolls[roll_index:])
