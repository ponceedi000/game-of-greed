import random
from collections import Counter

# Used Roger's Game_Logic Code for this module
class GameLogic:

  @staticmethod
  def calculate_stuff(tuple_of_dice, type_of_return):

    score = 0
    scoring_dice = []
    counts = Counter(tuple_of_dice)

    if tuple_of_dice and set(tuple_of_dice) == set((1, 2, 3, 4, 5, 6)):
        score += 1500
        scoring_dice.extend([*tuple_of_dice])
    elif len(counts) == 3 and set(counts.values()) == set((2,)):
        score += 1500
        scoring_dice.extend([*tuple_of_dice])
    else:
        # Counter([1, 1, 1, 1, 2]) --> {key: count, key: count} --> counts = {1: 4, 2: 1}
        # {1: 4, 2: 1} --> key = 1, count = 4 --> key = 2, count = 1
        for key, count in counts.items():
            if count >= 3:
                if key == 1:
                    score += (count - 2) * 1000
                    scoring_dice.extend([key for _ in range(count)])
                else:
                    score += (count - 2) * key * 100
                    scoring_dice.extend([key for _ in range(count)])
            else:
                if key == 5:
                    score += 50 * count
                    scoring_dice.extend([key for _ in range(count)])
                if key == 1:
                    score += 100 * count
                    scoring_dice.extend([key for _ in range(count)])

    if type_of_return == 'score':
        return score
    elif type_of_return == 'scoring_dice':
        return tuple(scoring_dice)

  @staticmethod
  def calculate_score(tuple_of_dice):
        return GameLogic.calculate_stuff(tuple_of_dice, 'score')

  @staticmethod
  def get_scorers(tuple_of_dice):
        return GameLogic.calculate_stuff(tuple_of_dice, 'scoring_dice')

  @staticmethod
  def roll_dice(amount_of_dice_1_to_6):

    temporary_list = []

    for _ in range(amount_of_dice_1_to_6):
        temporary_list.append(random.randint(1, 6))

    return tuple(temporary_list)

  @staticmethod
  def validate_keepers(tuple_of_rolled_dice,tuple_of_keepers_possible):
    actual = sorted(list(GameLogic.get_scorers(tuple_of_rolled_dice)))
    expected = sorted(list(tuple_of_keepers_possible))

    if actual == expected:
      return True
    else:
      return False

  @staticmethod
  def validate_input(tuple_of_rolled_dice, user_input):
    counter_rolled = Counter(tuple_of_rolled_dice)
    counter_input = Counter(user_input)

    for key, user_count in counter_input.items():
        if user_count > counter_rolled[key]:
            return False
    
    return True


# class GameLogic:

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
