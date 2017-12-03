# from ai import *
#
# def main():
#     game = board()
#     AB1 = AlphaBeta1()
#     # i =0
#     # Inputs to Tie:
#     # inputs = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
#     #           6, 7, 7, 7, 7, 7, 7]
#     while True:
#         game.printBoard()
#         if game.getTurn() == "X":
#             print "Thinking... "
#             position = AlphaBeta(game, 2).play()
#
#         else:
#             position = RandomAgent(game).play()
#
#         game = game.dropDisc(int(position))
#         # i=i+1
#         if game.isEnd():
#             if game.getWinner() is not None:
#                 game.printBoard()
#                 print "Winner is: ", game.getWinner()
#             else:
#                 game.printBoard()
#                 print "Game Tied! No Winner"
#             break
#     print "Good Bye"
#
#
# if __name__ == "__main__":
#     main()


from board import *
from ai import *

globalCounter = 0


def main():
    game = board()
    # humanagent = Human()
    # randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent()
    # minimax = MinimaxAgent()
    # i =0
    # Inputs to Tie:
    # inputs = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
    #           6, 7, 7, 7, 7, 7, 7]
    while True:
        game.printBoard()
        if game.getTurn() == "X":
            position = Human().play()
        else:

            position = AlphaBeta(game, 3).play()
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


def countWinRate():
    global globalCounter
    game = board()
    # humanagent = Human()
    # randomagent = RandomAgent()
    alphBetaMinimax = MinimaxAlphaBetaAgent()
    # minimax = MinimaxAgent()
    while True:
        if game.getTurn() == "X":
            position = RandomAgent(game).play()

        else:
            # position = AlphaBeta(game, 2).play()
            position = MinimaxAlphaBetaAgent().getAction(game)

        game = game.dropDisc(int(position))
        if game.isEnd():
            if game.getWinner() is not None:
                if game.getWinner() == "X":
                    globalCounter += 1
                    return "Win"
                elif game.getWinner() == "O":
                    return "Loss"
                else:
                    return "Tied"
            break


if __name__ == "__main__":
    # for i in range(1, 11):
    #     print str(i) + " " + countWinRate()
    # print globalCounter / 10.0
    main()
