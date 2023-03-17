import random

import numpy as np

from Game import TicTacToe


class Player:
    def __init__(self, letter, talk: bool = True):
        self.letter: str = letter
        self.talk = talk

    def get_move(self, game: TicTacToe):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter, talk: bool = True):
        super().__init__(letter, talk)

    def get_move(self, game: TicTacToe):
        square = random.choice(game.available_moves())
        if self.talk:
            print('Random BOT Playing!')
        return square


class HumanPlayer(Player):
    def __init__(self, letter, talk: bool = True):
        super().__init__(letter, talk)

    def get_move(self, game: TicTacToe):

        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + f'\'s turn. Input move (1-9):')
            try:
                square = int(square)
                i, j = (square - 1) // 3, (square - 1) % 3
                if not game.check_move_validity((i, j)):
                    raise ValueError
                else:
                    val = (i, j)
                    valid_square = True
            except ValueError:
                pass
        return val


class AIPlayer(Player):
    def __init__(self, letter, talk: bool = True):
        super().__init__(letter, talk)
        self.difficulty = 6

    def get_move(self, game: TicTacToe):
        if self.talk:
            print('AI BOT Playing!')
        if game.num_empty_squares() == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state: TicTacToe, player: str, lookahead: int = 1):
        max_player = self.letter
        other_player = state.Cross if player == state.Naught else state.Naught

        if lookahead >= self.difficulty:
            if state.get_winner() == other_player:
                return {'position': None,
                        'score': 1 * (state.num_empty_squares() + 1)
                        if other_player == max_player
                        else
                        -1 * (state.num_empty_squares() + 1)
                        }
            else:
                return {'position': None,
                        'score': 0}

        if state.get_winner() == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1)
                    if other_player == max_player
                    else
                    -1 * (state.num_empty_squares() + 1)
                    }
        elif state.num_empty_squares() == 0:
            return {'position': None,
                    'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -np.inf}  # try to maximize this
        else:
            best = {'position': None, 'score': np.inf}  # try to minimize this

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)

            sim_score = self.minimax(state, other_player, lookahead + 1)

            state.reset_move(possible_move)
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
