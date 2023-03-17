import numpy as np


def print_board_nums():
    number_board = np.arange(1, 10)
    number_board = number_board.reshape((3, 3))
    number_board = number_board.astype('str')
    for i in range(3):
        print('|' + '|'.join(list(number_board[i])) + '|')


class TicTacToe:
    def __init__(self):
        self.game_board = np.ones((3, 3)) * -1
        self.blank = -1
        self.x = 0
        self.o = 1
        self.winner = None
        self.Cross = 'x'
        self.Naught = 'o'

    def __str__(self):
        disp_board = '|'
        for i in range(3):
            for j in range(3):
                if self.game_board[i, j] == self.blank:
                    disp_board += ' |'
                elif self.game_board[i, j] == self.x:
                    disp_board += f'{self.Cross}|'
                else:
                    disp_board += f'{self.Naught}|'
            disp_board += '\n|'
        return disp_board[:-1]

    def available_moves(self):
        return np.argwhere(self.game_board == self.blank)

    def num_empty_squares(self):
        return len(self.available_moves())

    def check_move_validity(self, square):
        if self.game_board[square] == self.blank:
            return True
        else:
            return False

    def make_move(self, square, letter):
        i, j = square
        if self.game_board[i, j] == self.blank:
            if letter == self.Cross:
                self.game_board[i, j] = self.x
                if self.check_winning_move(square):
                    self.winner = self.Cross
            else:
                self.game_board[i, j] = self.o
                if self.check_winning_move(square):
                    self.winner = self.Naught
            return True
        else:
            return False

    def check_winning_move(self, square):
        row, column = square
        if np.all(self.game_board[row] == self.game_board[row, column]):
            return True
        if np.all(self.game_board[:, column] == self.game_board[row, column]):
            return True
        if list(square) in [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]:
            if np.all(self.game_board.diagonal() == self.game_board[row, column]):
                return True
            elif np.all(np.fliplr(self.game_board).diagonal() == self.game_board[row, column]):
                return True
        return False

    def check_winner(self):
        if self.winner is None:
            return False
        else:
            return True

    def get_winner(self):
        return self.winner

    def reset_move(self, square):
        i, j = square
        self.game_board[i, j] = self.blank
        self.winner = None
