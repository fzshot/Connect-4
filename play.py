import datetime
from gameboard import *
from ai import *

globalCounter = 0


def main():
    game = GameBoard()
    humanagent = Human()
    randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent(2)
    minimax = MinimaxAgent()
    while True:
        game.print_board()
        if game.get_turn() == "X":
            position = humanagent.play()
        else:
            position = alphBetaMinimax.get_new_state(game)
        try:
            game = game.dropDisc(int(position))
        except Exception:
            pass
        else:
            if game.is_end():
                if game.get_winner() is not None:
                    game.print_board()
                    alphBetaMinimax.save_obj()
                    print("Winner is: ", game.get_winner())
                else:
                    game.print_board()
                    print("Game Tied! No Winner")
                break
    print("Good Bye")


def count_win_rate():
    global globalCounter
    game = GameBoard()
    humanagent = Human()
    randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent(2)
    minimax = MinimaxAgent()
    count = 0
    avg = 0.00
    while True:
        if game.get_turn() == "X":
            position = randomagent.play()
        else:
            start = datetime.datetime.now()
            position = alphBetaMinimax.get_new_state(game)
            end = datetime.datetime.now()
            elapsed = end - start
            print("Time taken: ", elapsed.total_seconds(), "secs")
            avg = avg + elapsed.total_seconds()
            count = count + 1
        game = game.dropDisc(int(position))

        if game.is_end():
            if game.get_winner() is not None:
                print("Average Time for a game: ", avg / count)
                alphBetaMinimax.save_obj()
                if game.get_winner() == "O":
                    globalCounter += 1
                    return "Win"
                elif game.get_winner() == "X":
                    return "Loss"
                else:
                    return "Tied"
            break


if __name__ == "__main__":
    for i in range(1, 501):
        print(str(i) + " " + count_win_rate())
    print(globalCounter / 500.0)
    # main()
