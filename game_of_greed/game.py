from random import choice, randint
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
# from game_logic import GameLogic 

def default_roller(dice=6):
    return GameLogic.roll_dice(dice)

class Game:

    def __init__(self,rounds=1,dice_quantity=6):
        self.banker = Banker()
        self.dice_quantity = dice_quantity
        self.rounds = rounds
        self.start = True

    def play(self,roller=GameLogic.roll_dice):
        self.default_roller = roller
        # handles first test
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')
        while True:
            choice = input('> ')
            if choice == 'n':
               print('OK. Maybe another time')
               break
            # Test two passes within else statement
            elif choice == 'y':
                self.dice_quantity = 6
                self.start_round(roller)
                # Test three solution goes below

    def start_round(self,roller):
        while self.status and self.banker.balance <= 10000:
                
                print(f'Starting round {self.rounds}')
                print(f'Rolling {self.dice_quantity} dice...')
                roll = roller(self.dice_quantity)
                roller_str = ''
                for num in roll:
                 roller_str += str(num) + " "
                print(f'*** {roller_str}***')
                print('Enter dice to keep, or (q)uit:')
                choice = input('> ' )
                if choice == 'q':
                    print('Thanks for playing. You earned 0 points')
                else:
                    pass
                    

        

    
if __name__ == "__main__":
        # rolls = [(4,),(4,),(5,),(2,),(3,),(1,)]
    rolls = [('4','4','5','2','3','1')]
   
    def mock_roller():
        # return rolls.pop(0) if rolls else default_roller()
        return (4,3,1,1)
    Game.play(mock_roller)
    
