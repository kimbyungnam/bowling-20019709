FRAMES_PER_GAME = 10
REGULAR_FRAMES = FRAMES_PER_GAME - 1
ALL_PINS = 10


class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        roll_index = 0

        def pins_after(offset):
            return self._rolls[roll_index + offset]

        for _ in range(REGULAR_FRAMES):
            is_strike = pins_after(0) == ALL_PINS
            if is_strike:
                strike_bonus = pins_after(1) + pins_after(2)
                total += ALL_PINS + strike_bonus
                roll_index += 1
                continue

            frame_pins = pins_after(0) + pins_after(1)
            is_spare = frame_pins == ALL_PINS
            if is_spare:
                spare_bonus = pins_after(2)
                total += ALL_PINS + spare_bonus
            else:
                total += frame_pins
            roll_index += 2

        total += self._score_last_frame(roll_index)
        return total

    def _score_last_frame(self, roll_index):
        # 10번 프레임은 스트라이크/스페어 시 최대 3회까지 투구가 허용되며,
        # 그 프레임에서 던진 핀 수의 합이 곧 프레임 점수다 (미래 프레임에서
        # 보너스를 빌려올 필요가 없다).
        return sum(self._rolls[roll_index:])
