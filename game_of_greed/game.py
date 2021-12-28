from random import randint
from game_of_greed.game_logic import GameLogic 

def default_roller(dice=6):
    return GameLogic.roll_dice(dice)

class Game:
    def play(self,roller=default_roller):
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')
        while True:
            count = 0
            choice = input('> ')
            if choice == 'n':
               print('OK. Maybe another time')
               break
            else:
                count += 1
                roll = roller(self)
                roller_str = ''
                for num in roll:
                    roller_str += str(num) + ' '
                print(f'Starting round {count}')
                print(f'Rolling {6} dice...')
                print(f'*** {roller_str}***')
                print('Enter dice to keep, or (q)uit:')
                quit = input('> ' )
                
                print('Thanks for playing. You earned 0 points' if quit == 'q' else None) 
                
            
# figure out how to implement game.logic into game
# keep mock roller logic outside of main gate


if __name__ == "__main__":
        # rolls = [(4,),(4,),(5,),(2,),(3,),(1,)]
    rolls = [(4,4,5,2,3,1)]
   
    def mock_roller():
                # return rolls.pop(0) if rolls else default_roller()
        return (4,3,1,1)
    Game.play(mock_roller)
