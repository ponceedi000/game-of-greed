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

class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self,num):
        self.shelved += num
        return self.shelved

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
