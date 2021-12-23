import random
from collections import Counter
class GameLogic:

    def __init__(self):
        pass

    def game_intro():
        user_response = {'yes', 'no'}
        welcome_message = 'Welcome to Game Of Greed'
        if user_response[0]: 
          print(f'{welcome_message} do you want to play?')

        else:
            print('ok')

    @staticmethod
    def calculate_score(self, dice):
        score = 0
        count = Counter(dice[:6])




    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)




if name == '__main__':
