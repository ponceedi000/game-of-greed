import random
from collections import Counter

class GameLogic:
    def __init__(self):
        pass
# GAME INTRODUCTION --- TO BE FINISHED AFTER MVP'S HAVE BEEN MET
    # def game_intro():
    #     user_response = {'yes', 'no'}
    #     welcome_message = 'Welcome to Game Of Greed'
    #     if user_response[0]: 
    #       print(f'{welcome_message} do you want to play?')
    #     else:
    #         print('ok')

    @staticmethod
    def roll_dice(dice_roll):
        dice_list = []
        for _ in range(dice_roll):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)            

    @staticmethod
    def calculate_score(dice):
        score = 0
        count = Counter(dice[:6])
        straight = sorted(dice)

        if count[5] == 1 or count[5] == 2:
          score = score + 50 * count[5]

        if count[1] == 1 or count[1] == 2:
          score = score + 100 * count[1]

        if straight == [1,2,3,4,5,6]:
          score = 1500
          return score
          # returns 1650 for some reason, may need to make seperate classes for straights



        return score



