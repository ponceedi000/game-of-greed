# import random
# from collections import Counter


# class GameLogic:
#     def __init__(self):
#         pass
# # GAME INTRODUCTION --- TO BE FINISHED AFTER MVP'S HAVE BEEN MET
#     # def game_intro():
#     #     user_response = {'yes', 'no'}
#     #     welcome_message = 'Welcome to Game Of Greed'
#     #     if user_response[0]:
#     #       print(f'{welcome_message} do you want to play?')
#     #     else:
#     #         print('ok')

#     @staticmethod
#     def roll_dice(dice_roll):
#         dice_list = []
#         for _ in range(dice_roll):
#             dice_list.append(random.randint(1, 6))
#         return tuple(dice_list)

#     @staticmethod
#     def calculate_score(dice):
#         score = 0
#         count = Counter(dice[:6])
#         straight = sorted(dice)

#         if count[5] == 1 or count[5] == 2:
#             score += + 50 * count[5]

#         if count[1] == 1 or count[1] == 2:
#             score += + 100 * count[1]

#         # Handles Straight Die
#         if straight == [1, 2, 3, 4, 5, 6]:
#             score = 1500
#             return score

#         # Handles three of a kind
#         for i in range(1, 7):
#             if i == 1 and count[1] == 3:
#                 score += 1000
#             elif i != 1 and count[i] == 3:
#                 score += i * 100

#         # Handles four of a kind
#         for i in range(1, 7):
#             if i == 1 and count[1] == 4:
#                 score += 2000
#             elif i != 1 and count[i] == 4:
#               score += i * 100 * 2

#         # Handles five of a kind
#         for i in range(1, 7):
#             if i == 1 and count[1] == 5:
#                 score += 3000
#             elif i != 1 and count[i] == 5:
#               score += i * 100 * 3 
              
#         # Handles six of a kind
#         for i in range(1, 7):
#             if i == 1 and count[1] == 6:
#                 score += 4000
#             elif i != 1 and count[i] == 6:
#               score += i * 100 * 4           

#         return score


'''
CODE BELOWS IS FROM ROGER IOT TO COMPLETE LAB 4
CODE WILL BE DELETED BEFORE RESUBMITING LAB 3
'''
from collections import Counter
from random import randint


class GameLogic:
    @staticmethod
    def roll_dice(num=6):
        # version_1

        return tuple([randint(1, 6) for _ in range(num)])

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers that represent the user's selected dice pulled out from current roll
        """
        # version_1

        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        counts = Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                # handle 4,5,6 of a kind
                pips_beyond_3 = pip_count - 3

                score += score * pips_beyond_3

                # bug if 2 threesomes? Let's test it

                # 1s are worth 10x
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        # version_3

        # pro tip: you can do some math operations with counters
        # check https://docs.python.org/3/library/collections.html#collections.Counter
        keeper_counter = Counter(keepers)
        roll_counter = Counter(roll)

        # a "valid" result is an empty Counter result
        result = keeper_counter - roll_counter

        # an empty Counter is falsy, so use "not" to flip it
        return not result

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