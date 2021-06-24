
from tkinter import *
from datetime import datetime
from time import *
from core.gui.objects import *

class TicTacToeGUI:
    general_size = 600

    # window size
    screen_width = general_size
    screen_height = general_size
    dim = (screen_width, screen_height)

    # positioning on the screen
    left_to_right = 700
    up_to_down = 300
    pos = (left_to_right, up_to_down)

    # <<<style>>>
    # font: type and size and (bold or itallic)
    font_config = ('Consolas', 20, 'bold')
    background_color = "yellow"
    foreground_color = "blue"

    # buttons config
    button_back = 'lightgreen'
    button_fore = 'blue'
    button_config = ('Consolas', 40, 'bold')

    # creating window and setting up the format
    def __init__(self):
        # game factors
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.active_game = True

        self.game_window = Tk()
        self.game_window.title("TicTacToe")
        self.game_window.geometry(f"{self.dim[0]}x{self.dim[1]}+{self.pos[0]}+{self.pos[1]}")

        # player turns and time information
        self.labels_frame = NewFrame(self.game_window, TOP)

        self.player = "X"

        # duration label
        self.duration_time = -1
        self.duration_label = NewLabel(self.labels_frame, f"Duration: {self.duration_time} sec", LEFT)
        self.duration_label.config(font=self.font_config)
        self.duration_label.config(justify=LEFT)
        self.duration_label.config(foreground=self.foreground_color, background=self.background_color)

        # shows the current time
        self.time_label = NewLabel(self.labels_frame, "Current time", LEFT)
        self.time_label.config(font=self.font_config)
        self.time_label.config(justify=RIGHT)
        self.time_label.config(foreground=self.foreground_color, background=self.background_color)

        # shows the turn of the player
        self.turn_label = NewLabel(self.game_window, f"Turn: Player X", TOP)
        self.turn_label.config(font=self.font_config)
        self.turn_label.config(justify=LEFT)
        self.turn_label.config(foreground=self.foreground_color, background=self.background_color)

        # useful for storage and transmiting the button to itself when pressed
        from collections import OrderedDict
        from functools import partial

        # this guys helps us to track the buttons coordinates
        self.buttons_dict = OrderedDict()

        # generating the buttons
        for index in range(3):
            exec(f"self.line{index + 1}_frame = NewFrame(self.game_window, TOP)")
            for jndex in range(3):
                command = ""
                command += f"button{index} = NewButton(self.line{index + 1}_frame, \" \", None, LEFT)\n"
                command += f"button{index}.config(font=self.button_config)\n"
                command += f"button{index}.config(foreground=self.button_fore, background=self.button_back)\n"
                command += f"button{index}.config(command=partial(self.ButtonsFunctions, button{index}))"
                exec(command)
                self.buttons_dict[eval(f"button{index}")] = (index, jndex)

        # information label
        self.info_label1 = NewLabel(self.game_window, "Playing the game...", TOP)
        self.info_label1.config(font=self.font_config)
        self.info_label1.config(foreground = 'blue', background = 'yellow')

        # another one
        self.info_label2 = NewLabel(self.game_window, "-" * 20, TOP)
        self.info_label2.config(font=self.font_config)
        self.info_label2.config(foreground = 'blue', background = 'yellow')

        self.restartgame_button = NewButton(self.game_window, "restart game", self.RestartGame, TOP)
        self.restartgame_button.config(font=self.font_config)
        self.restartgame_button.config(foreground ='blue', background ='yellow')

        # setting up the timer
        self.SetCurrentTime()

    def RestartGame(self):
        self.game_window.destroy()
        del self
        new_game = TicTacToeGUI()
        new_game.StartGame()
        del new_game

    # timer
    def SetCurrentTime(self):
        # updating time
        current_time = datetime.now().strftime("Time: %H:%M:%S")
        self.time_label.config(text=current_time)
        self.game_window.after(1000, self.SetCurrentTime)

        # updating duration time
        if self.active_game:
            self.duration_time += 1
            if self.duration_time < 10:
                self.duration_label.config(text=f"Duration: 0{self.duration_time} sec")
            else:
                self.duration_label.config(text=f"Duration: {self.duration_time} sec")

    def ButtonsFunctions(self, self_button):
        if self.active_game:
            self.info_label1['foreground'] = 'blue'
            if self_button['text'] == " ":
                self.info_label1['text'] = "Playing the game..."
                self_button['text'] = self.player
                for button in self.buttons_dict:
                    if button == self_button:
                        x, y = self.buttons_dict[button]
                        break
                self.board[x][y] = self.player
                result, coords = self.VerifyWinner(self.player)
                if result:
                    print(f"Winner's coordinates: {coords}")
                    self.info_label1['text'] = f"The winner is: Player {self.player}!!"
                    self.turn_label['text'] = self.info_label1['text']
                    self.active_game = False
                    self.info_label2['text'] = "Game ended"
                    for pair in coords:
                        for button in self.buttons_dict:
                            if self.buttons_dict[button] == pair:
                                button.config(foreground="red")
                    return
                elif not result and self.BoardNotEmpty():
                    self.info_label1['text'] = "There is a draw"
                    self.turn_label['text'] = self.info_label1['text']
                    self.active_game = False
                    self.info_label2['text'] = "Game ended"
                    for button in self.buttons_dict:
                        button.config(foreground='red')
                    return
            else:
                self.info_label1['text'] = "You cannot place value there"
                self.info_label1['foreground'] = 'red'
                return

            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'
            self.turn_label['text'] = f"Turn: Player {self.player}"
        else:
            #self.RestartGame()
            pass

    def BoardNotEmpty(self):
        for line in self.board:
            for elem in line:
                if elem == "":
                    return False
        return True

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

    def StartGame(self):
        self.game_window.mainloop()

if __name__ == '__main__':
    game = TicTacToeGUI()
    game.StartGame()