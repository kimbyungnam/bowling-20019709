FRAMES_PER_GAME = 10
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

        for _ in range(FRAMES_PER_GAME):
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

        return total
