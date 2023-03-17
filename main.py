from Game import TicTacToe, print_board_nums
from Players import RandomComputerPlayer, HumanPlayer, Player, AIPlayer
import time


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


if __name__ == '__main__':
    sample_game = TicTacToe()
    player1 = RandomComputerPlayer(sample_game.Cross, talk=False)
    player2 = AIPlayer(sample_game.Naught, talk=False)
    # player1 = HumanPlayer(sample_game.Cross)
    ai_wins = 0
    random_wins = 0
    ties = 0
    total_games = 1000
    for _ in range(total_games):
        sample_game = TicTacToe()
        play(sample_game, player1, player2, print_game=False)
        if sample_game.winner == player2.letter:
            ai_wins += 1
        elif sample_game.winner == player1.letter:
            random_wins += 1
        else:
            ties += 1

    print(f"AI wins : {100 * ai_wins / total_games} %"
          f"\nRandom wins : {100 * random_wins / total_games} %"
          f"\nTies : {100 * ties / total_games} %")
