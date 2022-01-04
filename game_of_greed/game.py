from random import choice, randint
import sys
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
# <--- UNCOMMENT IMPORTS ABOVE TO RUN PYTEST --->
# <--- UNCOMMENT IMPORTS BELOW TO RUN SCRIPT --->
# from banker import Banker
# from game_logic import GameLogic 


class Game:

    def __init__(self):
        self.banker = Banker()
        self.dice_quantity = 6
        self.rounds = 0
        self.status = True

    def default_roller(self):
        GameLogic.roll_dice(self.dice_quantity)

    def play(self,roller=GameLogic.roll_dice):
        self.default_roller = roller
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')
        while True:
            choice = input('> ')
            if choice == 'n':
               print('OK. Maybe another time')
               break
            elif choice == 'y':
                # self.dice_quantity = 6
                self.start_round(roller)
                # Test three solution goes below

    def start_round(self,roller):

        while self.status and self.banker.balance <= 10000:
            self.rounds += 1
                
            print(f'Starting round {self.rounds}')
            print(f'Rolling {self.dice_quantity} dice...')
            # BELOW FORMATS THE NUMS IN A READIBLE STATE FOR USER. SHOWS WHAT DICE WERE ROLLED
            roll = roller(self.dice_quantity)
            roller_str = ''
            for num in roll:
                roller_str += str(num) + " "
            print(f'*** {roller_str}***')
            
            if GameLogic.calculate_score(roll) == 0:
                print("Farkled")
                continue

            print('Enter dice to keep, or (q)uit:')
            choice = input('> ' )

            if choice == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                sys.exit()
            else: 
                # WORKED WITH ALEX FOR BELOW LOGIC (ELSE)
                user_response = tuple(map(int, list(choice)))
                self.dice_quantity -= len(user_response)
                # HANDLES USER RESPONSE SUCH AS '1111', CONVERT TO LIST [1,1,1,1] CONVERT TO TUPLE (1,1,1,1)
                score = GameLogic.calculate_score(user_response)
                self.banker.shelf(score)
                print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                choice = input("> ")

            if choice == "b":
                self.banker.bank()
                self.dice_quantity = 6
                print(f"You banked {score} points in round {self.rounds}")
                print(f"Total score is {self.banker.balance} points")
 
            elif choice == "r":
                if self.dice_quantity == 0:
                    self.dice_quantity = 6
                continue # reroll with the remaining dice on the board
            
            elif choice == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")          
                sys.exit()

        

    
if __name__ == "__main__":
        # rolls = [(4,),(4,),(5,),(2,),(3,),(1,)]
    # rolls = [('4','4','5','2','3','1')]
   
    # def mock_roller():
    #     # return rolls.pop(0) if rolls else default_roller()
    #     return (4,3,1,1)
    # Game.play(mock_roller)
    game = Game()
    game.play()
    
