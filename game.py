class TicTacToe:
    def __init__(self):
        self.gameBoard = [' ' for _ in range(9)] # Single list to format 3x3 board
        self.winner = None   # Track the winner 

    def displayBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range]
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')

    def availableMoves(self):
        moves = []
        for (i,spot) in enumerate(self.gameBoard):
            if spot == ' ':
                moves.append(i) # append the index of the open spot
        return moves 
        