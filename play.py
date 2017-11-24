from board import *


def main():
    game = board()
    # i =0
    # Inputs to Tie:
    # inputs = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
    #           6, 7, 7, 7, 7, 7, 7]
    while True:
        game.printBoard()
        position = raw_input("Enter the position for " + game.getTurn() + ": ")

        if position == "q":
            break
        game = game.dropDisc(int(position))
        # try:
        #     game.dropDisc(int(position))
        # except Exception:
        #     print "Something Wrong"
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
