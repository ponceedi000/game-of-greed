from random import choice, randint
import sys
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
# <--- UNCOMMENT IMPORTS ABOVE TO RUN PYTEST --->
# <--- UNCOMMENT IMPORTS BELOW TO RUN SCRIPT --->
# from banker import Banker
# from game_logic import GameLogic 




# Game passes majority of tests BUT keep getting following error: 
# TypeError: 'tuple' object is not callable

class Game:

    def __init__(self):
        self.banker = Banker()
        self.dice_quantity = 6
        self.rounds = 0
        self.status = True
    
    def welcome_message(self):
        print('Welcome to Game of Greed')

    def play(self,roller=GameLogic.roll_dice):
        self.welcome_message()
        print('(y)es to play or (n)o to decline')
        choice = input('> ')
        if choice == 'n':
            print('OK. Maybe another time')
            sys.exit()
        elif choice == 'y':
            self.start_round(roller)


    def game_handler(self, roller):
        rolled_dice = self.roll(roller)
        selected_dice = self.validate_dice(rolled_dice, roller)
        self.compile_score(selected_dice)
        self.score_and_dice_quantity()
        self.bank_reroll_quit(roller)
     

    def quit_game(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        sys.exit()         


    def start_round(self, roller):
        self.rounds += 1
        self.dice_quantity= 6
        self.banker.clear_shelf()
        print(f"Starting round {self.rounds}")
        self.game_handler(roller)

        # while self.status and self.banker.balance <= 10000:
        #     self.rounds += 1
                
        #     print(f'Starting round {self.rounds}')
        #     print(f'Rolling {self.dice_quantity} dice...')
        #     # BELOW FORMATS THE NUMS IN A READIBLE STATE FOR USER. SHOWS WHAT DICE WERE ROLLED
        #     # roll = roller(self.dice_quantity)
        #     # roller_str = ''
        #     # for num in roll:
        #     #     roller_str += str(num) + " "
        #     # print(f'*** {roller_str}***')
        #     print('Enter dice to keep, or (q)uit:')
        #     choice = input('> ' )

        #     if choice == 'q':
        #         self.quit_game()
        #     else: 
        #         # WORKED WITH ALEX FOR BELOW LOGIC (ELSE)
        #         user_response = tuple(map(int, list(choice)))
        #         self.dice_quantity -= len(user_response)
        #         # HANDLES USER RESPONSE SUCH AS '1111', CONVERT TO LIST [1,1,1,1] CONVERT TO TUPLE (1,1,1,1)
        #         score = GameLogic.calculate_score(user_response)
        #         self.banker.shelf(score)
        #         # print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
        #         print("(r)oll again, (b)ank your points or (q)uit:")
        #         choice = input("> ")

        #     self.bank_reroll_quit()

    def roll(self, roller):
        print(f"Rolling {self.dice_quantity} dice...")
        roll = roller(self.dice_quantity)
        self.show_dice_rolled(roll)
        return roll

    def show_dice_rolled(self, roller):
        roll = roller(self.dice_quantity)
        roller_str = ''
        for num in roll:
            roller_str += str(num) + " "
        print(f'*** {roller_str}***')



    def validate_dice(self, rolled_dice, roller):

        if GameLogic.calculate_score(rolled_dice) == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
            self.banker.clear_shelf()
            self.bank_earned_points(roller)
            
        else:
            print("Enter dice to keep, or (q)uit:")
            choice = input("> ")
            if choice:
                choice = choice.replace(" ", "")
            else:
                self.validate_dice(rolled_dice, roller)

            if choice == "q":
                self.quit_game()

            while True:
                keeper_values = []
                for char in choice:
                    if char.isnumeric():
                        keeper_values.append(int(char))

                if GameLogic.validate_keepers(rolled_dice, keeper_values):
                    return keeper_values
                else:
                    print("Cheater!!! Or possibly made a typo...")
                    # NEED TO SHOW ROLLED DICE. CODE ALREADY CREATED IN start_round method. REFACTOR SAID CODE AND INVOKE HERE
                    return self.validate_dice(rolled_dice, roller)


    def compile_score(self, user_response):
        user_response = tuple(map(int, list(choice)))
        self.dice_quantity -= len(user_response)
            # HANDLES USER RESPONSE SUCH AS '1111', CONVERT TO LIST [1,1,1,1] CONVERT TO TUPLE (1,1,1,1)
        score = GameLogic.calculate_score(user_response)
        self.banker.shelf(score)
        return score



    def score_and_dice_quantity(self):
        print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining") 

    def bank_reroll_quit(self,roller):

        print("(r)oll again, (b)ank your points or (q)uit:")
        choice = input("> ").replace(" ", "")

        if choice == "q":
            self.quit_game()

        elif choice == "r":
            if self.dice_quantity == 0:
                self.dice_quantity = 6
                self.game_handler(roller)
            else:
                self.game_handler(roller)

        elif choice == "b":
            self.bank_earned_points()

    def bank_earned_points(self, roller):
        print(f"You banked {self.banker.shelved} points in round {self.rounds}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")        
        if self.banker.balance >= 10000:
            print("WINNER")
        else:
            self.start_round(roller)   


    
if __name__ == "__main__":

    game = Game()
    game.play()
    
