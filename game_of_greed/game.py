from random import randint
from game_of_greed import game_logic 

def default_roller():
    return randint( (1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6) )

class Game:
    def play(self,roller=default_roller):
        while True:
            print('Welcome to Game of Greed')
            print('(y)es to play or (n)o to decline')
            choice = input('> ')
            if choice == 'n':
               print('OK. Maybe another time')
               break
            else:
                roll = roller()
                roller_str = ''
                for num in roll:
                    roller_str += str(num) + ' '
                print(f'*** {roller_str}***')

# figure out how to implement game.logic into game
# keep mock roller logic outside of main gate


if __name__ == "__main__":
   
    def mock_roller():
        rolls = [(4,),(4,),(5,),(2,),(3,),(1,)]
        return rolls.pop(0) if rolls else default_roller()

    Game.play(mock_roller)
