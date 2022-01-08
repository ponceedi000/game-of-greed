import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(dice_roll):
        dice_list = []
        for _ in range(dice_roll):
            dice_list.append(random.randint(1, 6))
        return tuple(dice_list)

    @staticmethod
    def calculate_score(dice):
        score = 0
        count = Counter(dice[:6])
        straight = sorted(dice)

        if count[5] == 1 or count[5] == 2:
            score += + 50 * count[5]

        if count[1] == 1 or count[1] == 2:
            score += + 100 * count[1]

        # Handles Straight Die
        if straight == [1, 2, 3, 4, 5, 6]:
            score = 1500
            return score

        # Handles three of a kind
        for i in range(1, 7):
            if i == 1 and count[1] == 3:
                score += 1000
            elif i != 1 and count[i] == 3:
                score += i * 100

        # Handles four of a kind
        for i in range(1, 7):
            if i == 1 and count[1] == 4:
                score += 2000
            elif i != 1 and count[i] == 4:
              score += i * 100 * 2

        # Handles five of a kind
        for i in range(1, 7):
            if i == 1 and count[1] == 5:
                score += 3000
            elif i != 1 and count[i] == 5:
              score += i * 100 * 3 
              
        # Handles six of a kind
        for i in range(1, 7):
            if i == 1 and count[1] == 6:
                score += 4000
            elif i != 1 and count[i] == 6:
              score += i * 100 * 4           

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        # version_3
        # pro tip: you can do some math operations with counters
        # check https://docs.python.org/3/library/collections.html#collections.Counter
        keeper_count = Counter(keepers)
        roll_count = Counter(roll)

        # a "valid" result is an empty Counter result
        game_result = keeper_count - roll_count

        # an empty Counter is falsy, so use "not" to flip it
        return not game_result

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)
