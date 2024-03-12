import random
import math


class Player:
    def __init__(self, letter): # letter is either X or O
        self.letter = letter

    def move(self, game):
        pass


class ComputerPlayer(Player):  # Computer class
    def __init__(self, letter):
        super().__init__(letter)   # use initial constructor in player class 

    def move(self, game):
        emptySquare = random.choice(game.availableMoves()) # choose a random empty square on the board 
        return emptySquare
        
class HumanPlayer(Player):  # Human class
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, game):
        validSquare = False
        value = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                value = int(square)
                if value not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid square. Try again!')
