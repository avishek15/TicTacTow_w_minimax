from Game import TicTacToe
from Gameplay import play
from Players import RandomComputerPlayer, AIPlayer, HumanPlayer

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
