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

        for _ in range(FRAMES_PER_GAME):
            first, second = self._rolls[roll_index], self._rolls[roll_index + 1]
            if first + second == ALL_PINS:
                total += ALL_PINS + self._rolls[roll_index + 2]
            else:
                total += first + second
            roll_index += 2

        return total
