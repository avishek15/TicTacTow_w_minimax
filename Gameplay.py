import time

from Game import TicTacToe, print_board_nums
from Players import Player


def play(game: TicTacToe, x_player: Player, o_player: Player, print_game: bool = True):
    start_with = game.Cross
    if print_game:
        print_board_nums()
    while game.num_empty_squares() > 0:
        if start_with == game.Cross:
            moved = game.make_move(x_player.get_move(game), 'x')
        else:
            moved = game.make_move(o_player.get_move(game), 'o')
        if print_game:
            print(game)
            time.sleep(0.8)
        if moved:
            if game.check_winner():
                break
            start_with = game.Naught if start_with == game.Cross else game.Cross

    winner = game.get_winner()
    if print_game:
        if winner is None:
            print('Oops, it\'s a tie')
        else:
            print(f'{winner} won!')
