
from core.aesthetics import *
from random import *
from core.system import *

tictactoe = \
"""
  _______ _   _______      _______
 |__   __(_) |__   __|    |__   __|
    | |   _  ___| | __ _  ___| | ___   ___
    | |  | |/ __| |/ _` |/ __| |/ _ \ / _ \\
    | |  | | (__| | (_| | (__| | (_) |  __/
    |_|  |_|\___|_|\__,_|\___|_|\___/ \___|
"""

class TicTacToeConsole:

    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.game_colors = [
            "blue",
            "red",
            "green",
            "yellow"
        ]
        self.playerX_color = 'blue'
        self.playerO_color = 'green'
        self.board_color = 'yellow'

    def PlayGame(self):
        while True:
            clearscreen()
            print(ConsoleColored(tictactoe, choice(self.game_colors)))
            print(f"Turn: player {self.player}\n")
            print(self.ReturnBoardColored())

            try:
                x, y = map(int, input("Enter coordinates:\n").strip().split())
            except:
                continue
            if not 0 <= x <= 2 or not 0 <= y <= 2:
                continue

            if self.board[x][y] == "":
                self.board[x][y] = self.player
                result, coords = self.VerifyWinner(self.player)
                if result:
                    clearscreen()
                    print(ConsoleColored(tictactoe, choice(self.game_colors)))
                    print()
                    print(f"\nPlayer: {self.player} won!!")
                    print(self.ReturnBoardColored())
                    print(f"Player: {self.player} won!!\n")
                    break
                elif not result and self.BoardNotEmpty():
                    clearscreen()
                    print(ConsoleColored(tictactoe, choice(self.game_colors)))
                    print("\nWe have a draw.")
                    print(self.ReturnBoardColored())
                    print("We have a draw.\n")
                    break
            else:
                #print(f"You cant place value there.")
                continue

            if self.player == 'X':
                self.player = 'O'
            elif self.player == 'O':
                self.player = 'X'

        pauseprogram()

    def VerifyWinner(self, symbol):
        # on principal diagonal
        coords = []
        win = True
        for index in range(3):
            if self.board[index][index] != symbol:
                win = False
            else:
                coords.append((index, index))
        if win:
            return True, coords

        # on second diagonal
        coords = []
        win = True
        for index in range(3):
            if self.board[index][2 - index] != symbol:
                win = False
            else:
                coords.append((index, 2 - index))
        if win:
            return True, coords

        # on first line
        coords = []
        win = True
        for index in range(3):
            if self.board[0][index] != symbol:
                win = False
            else:
                coords.append((0, index))
        if win:
            return True, coords

        # on second line
        coords = []
        win = True
        for index in range(3):
            if self.board[1][index] != symbol:
                win = False
            else:
                coords.append((1, index))
        if win:
            return True, coords

        # on third line
        coords = []
        win = True
        for index in range(3):
            if self.board[2][index] != symbol:
                win = False
            else:
                coords.append((2, index))
        if win:
            return True, coords

        # on fist column
        coords = []
        win = True
        for index in range(3):
            if self.board[index][0] != symbol:
                win = False
            else:
                coords.append((index, 0))
        if win:
            return True, coords

        # on second column
        coords = []
        win = True
        for index in range(3):
            if self.board[index][1] != symbol:
                win = False
            else:
                coords.append((index, 1))
        if win:
            return True, coords

        # on third column
        coords = []
        win = True
        for index in range(3):
            if self.board[index][2] != symbol:
                win = False
            else:
                coords.append((index, 2))
        if win:
            return True, coords

        # if no option we return False and []
        return False, []

    def BoardNotEmpty(self):
        for line in self.board:
            for elem in line:
                if elem == "":
                    return False
        return True

    def ReturnBoardColored(self):
        """ Returns board in string format with beautiful colored effects. """
        board = ""
        for i in range(3):
            for j in range(3):
                if j == 0 or j == 1:
                    if self.board[i][j] == "":
                        board += ConsoleColored("   |", color=self.board_color)
                    else:
                        if self.board[i][j] == "X":
                            symbol = ConsoleColored("X", color=self.playerX_color)
                        else:
                            symbol = ConsoleColored("O", color=self.playerO_color)

                        board += f" {symbol} " + ConsoleColored("|", color=self.board_color)
                else:
                    if self.board[i][j] == "":
                        board += ConsoleColored("   ", color=self.board_color)
                    else:
                        if self.board[i][j] == "X":
                            symbol = ConsoleColored("X", color=self.playerX_color)
                        else:
                            symbol = ConsoleColored("O", color=self.playerO_color)
                        board += f" {symbol} "
            board += '\n'
            if i == 0 or i == 1:
                board += ConsoleColored('-' * 3 + '|' + '-' * 3 + '|' + '-' * 3 + '\n',
                                 color=self.board_color)
        return board

if __name__ == '__main__':
    game = TicTacToeConsole()
    game.PlayGame()