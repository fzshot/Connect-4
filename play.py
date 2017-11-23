from board import *


def main():
    game = board()
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
        if game.isEnd():
            if game.getWinner() is not None:
                game.printBoard()
                print "Winner is: ", game.getWinner()
            break
    print "Good Bye"


if __name__ == "__main__":
    main()
