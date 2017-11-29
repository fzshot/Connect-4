from board import *
from ai import *

globalCounter = 0


def main():
    game = board()
    humanagent = Human()
    randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent()
    minimax = MinimaxAgent()
    # i =0
    # Inputs to Tie:
    # inputs = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
    #           6, 7, 7, 7, 7, 7, 7]
    while True:
        game.printBoard()
        if game.getTurn() == "X":
            position = humanagent.play()
        else:
            position = alphBetaMinimax.getNewState(game)
        try:
            game = game.dropDisc(int(position))
        except Exception:
            pass
        else:
            # i=i+1
            if game.isEnd():
                if game.getWinner() is not None:
                    game.printBoard()
                    print "Winner is: ", game.getWinner()
                else:
                    game.printBoard()
                    print "Game Tied! No Winner"
                break
    print "Good Bye"

# rtr
def countWinRate():
    global globalCounter
    game = board()
    humanagent = Human()
    randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent()
    minimax = MinimaxAgent()
    while True:
        if game.getTurn() == "X":
            position = minimax.getNewState(game)
        else:
            position = alphBetaMinimax.getNewState(game)

        game = game.dropDisc(int(position))
        if game.isEnd():
            if game.getWinner() is not None:
                if game.getWinner() == "O":
                    globalCounter += 1
                    return "Win"
                elif game.getWinner() == "X":
                    return "Loss"
                else:
                    return "Tied"
            break


if __name__ == "__main__":
    for i in range(1, 11):
        print str(i) + " " + countWinRate()
    print globalCounter / 10.0
    # main()
