class TicTacToe:
    def __init__(self):
        self.gameBoard = [' ' for _ in range(9)] # Single list to format 3x3 board
        self.winner = None   # Track the winner 

    def displayBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')