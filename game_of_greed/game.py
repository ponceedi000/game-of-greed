from random import randint
from game_of_greed import game_logic 

def mock_roller():
    return randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)

class Game:
    def play(self, roller=mock_roller):
        while True:
            print('Welcome to Game of Greed')
            print('(y)es to play or (n)o to decline')
            choice = input('> ')
            if choice == 'n':
               print('OK. Maybe another time')
            break
            # else:

if __name__ == "__main__":
    pass
