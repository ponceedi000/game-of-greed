from random import choice, randint
import sys
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
# <--- UNCOMMENT IMPORTS ABOVE TO RUN PYTEST --->
# <--- UNCOMMENT IMPORTS BELOW TO RUN SCRIPT --->
# from banker import Banker
# from game_logic import GameLogic 


# class Game:

#     def __init__(self):
#         self.banker = Banker()
#         self.dice_quantity = 6
#         self.rounds = 0
#         self.status = True

#     def default_roller(self):
#         GameLogic.roll_dice(self.dice_quantity)

#     def play(self,roller=GameLogic.roll_dice):
#         self.default_roller = roller
#         print('Welcome to Game of Greed')
#         print('(y)es to play or (n)o to decline')
#         while True:
#             choice = input('> ')
#             if choice == 'n':
#                print('OK. Maybe another time')
#                break
#             elif choice == 'y':
#                 # self.dice_quantity = 6
#                 self.start_round(roller)
#                 # Test three solution goes below

#     def bank_earned_points(self, roller):
#         print(f"You banked {self.banker.shelved} points in round {self.rounds}")
#         self.banker.bank()
#         print(f"Total score is {self.banker.balance} points")        
#         if self.banker.balance >= 10000:
#             print("WINNER")
#         else:
#             self.start_round(roller)            


#     def validate_dice(self, rolled_dice, roller):
#         if GameLogic.calculate_score(rolled_dice) == 0:
#             print("****************************************")
#             print("**        Zilch!!! Round over         **")
#             print("****************************************")
#             self.banker.clear_shelf()
#             self.bank_earned_points()
#         else:
#             print("Enter dice to keep, or (q)uit:")
#             choice = input("> ")
#             if choice:
#                 choice = choice.replace(" ", "")
#             else:
#                 self.validate_dice(rolled_dice, roller)

#             if choice == "q":
#                 print(f"Thanks for playing. You earned {self.banker.balance} points")
#                 sys.exit()
#             # COME UP WITH LOGIC THAT ENSURES CHEATING IS HANDLED PROPERLY
#             # CODE BLOCK GOES HERE
#             # ---
#             # ---
#             else:
#                 print("Cheater!!! Or possibly made a typo...")
#                 # NEED TO SHOW ROLLED DICE. CODE ALREADY CREATED IN start_round method. REFACTOR SAID CODE AND INVOKE HERE
#                 return self.validate_dice(rolled_dice, roller)

#     def start_round(self,roller):

#         while self.status and self.banker.balance <= 10000:
#             self.rounds += 1
                
#             print(f'Starting round {self.rounds}')
#             print(f'Rolling {self.dice_quantity} dice...')
#             # BELOW FORMATS THE NUMS IN A READIBLE STATE FOR USER. SHOWS WHAT DICE WERE ROLLED
#             roll = roller(self.dice_quantity)
#             roller_str = ''
#             for num in roll:
#                 roller_str += str(num) + " "
#             print(f'*** {roller_str}***')
#             print('Enter dice to keep, or (q)uit:')
#             choice = input('> ' )

#             if choice == 'q':
#                 print(f'Thanks for playing. You earned {self.banker.balance} points')
#                 sys.exit()
#             else: 
#                 # WORKED WITH ALEX FOR BELOW LOGIC (ELSE)
#                 user_response = tuple(map(int, list(choice)))
#                 self.dice_quantity -= len(user_response)
#                 # HANDLES USER RESPONSE SUCH AS '1111', CONVERT TO LIST [1,1,1,1] CONVERT TO TUPLE (1,1,1,1)
#                 score = GameLogic.calculate_score(user_response)
#                 self.banker.shelf(score)
#                 print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
#                 print("(r)oll again, (b)ank your points or (q)uit:")
#                 choice = input("> ")

#             if choice == "b":
#                 self.banker.bank()
#                 self.dice_quantity = 6
#                 print(f"You banked {score} points in round {self.rounds}")
#                 print(f"Total score is {self.banker.balance} points")
 
#             elif choice == "r":
#                 if self.dice_quantity == 0:
#                     self.dice_quantity = 6
#                 continue # reroll with the remaining dice on the board
            
#             elif choice == "q":
#                 print(f"Thanks for playing. You earned {self.banker.balance} points")          
#                 sys.exit()

        

    
# if __name__ == "__main__":
#         # rolls = [(4,),(4,),(5,),(2,),(3,),(1,)]
#     # rolls = [('4','4','5','2','3','1')]
   
#     # def mock_roller():
#     #     # return rolls.pop(0) if rolls else default_roller()
#     #     return (4,3,1,1)
#     # Game.play(mock_roller)
#     game = Game()
#     game.play()

'''
CODE BELOWS IS FROM ROGER IOT TO COMPLETE LAB 4
CODE WILL BE DELETED BEFORE RESUBMITING LAB 3
'''

class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        else:
            for round_num in range(1, self.num_rounds + 1):
                self.start_round(round_num)

            self.end_game()

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def start_round(self, round_num):
        num_dice = 6
        print(f"Starting round {round_num}")
        round_score = 0

        while True:
            print(f"Rolling {num_dice} dice...")

            roll = self._roller(num_dice)
            roll_string = " ".join([str(value) for value in roll])
            print(f"*** {roll_string} ***")

            preliminary_score = GameLogic.calculate_score(roll)

            if preliminary_score == 0:
                self.zilch(round_num)
                return

            keeper_values = self.validate_keepers(roll, roll_string)

            keeper_score = GameLogic.calculate_score(keeper_values)

            round_score += keeper_score

            num_dice -= len(keeper_values)

            print(
                f"You have {round_score} unbanked points and {num_dice} dice remaining"
            )
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")

            if response == "b":
                self.banker.shelf(round_score)
                banked_points = self.banker.bank()
                self.end_round(round_num, banked_points)
                break
            elif response == "r":
                if num_dice == 0:
                    num_dice = 6
            elif response == "q":
                self.end_game()

    def zilch(self, round_num):
        """Zero scoring dice were rolled so end round with 0 points"""
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

        self.end_round(round_num, 0)

    def end_round(self, round_num, banked_points):
        """bank points and finish round"""
        print(f"You banked {banked_points} points in round {round_num}")
        print(f"Total score is {self.banker.balance} points")

    def validate_keepers(self, roll, roll_string):
        """ensures that kept dice are valid for the roll
        Args:
            roll
            roll_string
        Returns:
            valid keeper values
        """
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.end_game()
                break

            keeper_values = []
            for char in response:
                if char.isnumeric():
                    keeper_values.append(int(char))

            if GameLogic.validate_keepers(roll, keeper_values):
                return keeper_values
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {roll_string} ***")


if __name__ == "__main__":
    game = Game()
    game.play()
