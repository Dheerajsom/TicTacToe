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
        pass
        
class HumanPlayer(Player):  # Human class
    def __init__(self, letter):
        super().__init__(letter)