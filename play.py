from ai import *

def main():
    game = board()
    # i =0
    # Inputs to Tie:
    # inputs = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
    #           6, 7, 7, 7, 7, 7, 7]
    while True:
        game.printBoard()
        if game.getTurn() == "X":
            print "Thinking... "
            position = ExpectimaxAgent(game,2).play()
        else:
            position = AlphaBeta(game,2).play()

        game = game.dropDisc(int(position))
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


if __name__ == "__main__":
    main()

