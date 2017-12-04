import datetime
from board import *
from ai import *


globalCounter = 0


def main():
    game = board()
    humanagent = Human()
    randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent(2)
    minimax = MinimaxAgent()
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
                    alphBetaMinimax.save_obj()
                    print "Winner is: ", game.getWinner()
                else:
                    game.printBoard()
                    print "Game Tied! No Winner"
                break
    print "Good Bye"


def countWinRate():
    global globalCounter
    game = board()
    humanagent = Human()
    randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent(2)
    minimax = MinimaxAgent()
    count = 0
    avg = 0.00
    while True:
        if game.getTurn() == "X":
            position = randomagent.play()
        else:
            start = datetime.datetime.now()
            position = alphBetaMinimax.getNewState(game)
            end = datetime.datetime.now()
            elapsed = end - start
            print "Time taken: ",elapsed.total_seconds(), "secs"
            avg = avg + elapsed.total_seconds()
            count = count + 1
        game = game.dropDisc(int(position))

        if game.isEnd():
            if game.getWinner() is not None:
                print "Average Time for a game: ", avg/count
                alphBetaMinimax.save_obj()
                if game.getWinner() == "O":
                    globalCounter += 1
                    return "Win"
                elif game.getWinner() == "X":
                    return "Loss"
                else:
                    return "Tied"
            break



if __name__ == "__main__":
    for i in range(1, 501):
        print str(i) + " " + countWinRate()
    print globalCounter / 500.0
    # main()
