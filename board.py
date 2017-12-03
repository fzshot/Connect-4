from copy import deepcopy


class board():
    def __init__(self):
        self.scoreTrack = {"X": [], "O": []}
        self.turn = "X"
        self.board = []
        self.drawBoard = None
        self.winner = None
        self.initBoard()

    def initBoard(self):
        for i in range(6):
            self.board.append([" ", " ", " ", " ", " ", " ", " "])
        self.updateDrawBoard()
        for row in range(6):
            self.scoreTrack["X"].append(
                [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)])
            self.scoreTrack["O"].append(
                [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)])

    def getBoard(self):
        return self.board

    def updateDrawBoard(self):
        result = ""
        for raw in self.board:
            for place in raw:
                result += "|" + place
            result += "|\n"
        self.drawBoard = result

    def printBoard(self):
        print self.drawBoard

    def dropDisc(self, column):
        newgamestate = deepcopy(self)
        if column in newgamestate.possiblePlace():
            for i in range(len(newgamestate.board) - 1, -1, -1):
                if newgamestate.board[i][column - 1] == " ":
                    newgamestate.board[i][column - 1] = newgamestate.turn
                    newgamestate.updateScore(newgamestate.turn, i, column - 1)
                    break
            newgamestate.updateDrawBoard()
            if newgamestate.turn == "X":
                newgamestate.turn = "O"
            else:
                newgamestate.turn = "X"
        return newgamestate

    def possiblePlace(self):
        place = []
        for i in range(7):
            if self.board[0][i] == " ":
                place.append(i + 1)
        return place

    def isEnd(self):
        if self.winner is not None:
            result = True
        else:
            for place in self.board[0]:
                if place == " ":
                    return False
            result = True
        return result

    def getWinner(self):
        return self.winner

    def updateScore(self, player, row, col):
        self.updateHorizontal(player, row, col)
        self.updateVertical(player, row, col)
        self.updateDiagonalL(player, row, col)
        self.updateDiagonalR(player, row, col)
        # print ""

    def updateHorizontal(self, player, row, col):
        tempmax = 1
        if col - 1 >= 0:
            tempmax += self.scoreTrack[player][row][col - 1][0]
        if col + 1 <= 6:
            tempmax += self.scoreTrack[player][row][col + 1][0]
        if tempmax >= 4:
            self.winner = player
        # else:
        vertical = self.scoreTrack[player][row][col][1]
        diagonalL = self.scoreTrack[player][row][col][2]
        diagonalR = self.scoreTrack[player][row][col][3]
        self.scoreTrack[player][row][col] = (tempmax, vertical, diagonalL, diagonalR)
        for i in range(col + 1, 7):
            if self.scoreTrack[player][row][i][0] != 0:
                vertical = self.scoreTrack[player][row][i][1]
                diagonalL = self.scoreTrack[player][row][i][2]
                diagonalR = self.scoreTrack[player][row][i][3]
                self.scoreTrack[player][row][i] = (tempmax, vertical, diagonalL, diagonalR)
            else:
                break
        for i in range(col - 1, -1, -1):
            if self.scoreTrack[player][row][i][0] != 0:
                vertical = self.scoreTrack[player][row][i][1]
                diagonalL = self.scoreTrack[player][row][i][2]
                diagonalR = self.scoreTrack[player][row][i][3]
                self.scoreTrack[player][row][i] = (tempmax, vertical, diagonalL, diagonalR)
            else:
                break

    def updateVertical(self, player, row, col):
        tempmax = 1
        if row - 1 >= 0:
            tempmax += self.scoreTrack[player][row - 1][col][1]
        if row + 1 <= 5:
            tempmax += self.scoreTrack[player][row + 1][col][1]
        if tempmax >= 4:
            self.winner = player
        # else:
        horizontal = self.scoreTrack[player][row][col][0]
        diagonalL = self.scoreTrack[player][row][col][2]
        diagonalR = self.scoreTrack[player][row][col][3]
        self.scoreTrack[player][row][col] = (horizontal, tempmax, diagonalL, diagonalR)
        for i in range(row + 1, 6):
            if self.scoreTrack[player][i][col][1] != 0:
                horizontal = self.scoreTrack[player][i][col][0]
                diagonalL = self.scoreTrack[player][i][col][2]
                diagonalR = self.scoreTrack[player][i][col][3]
                self.scoreTrack[player][i][col] = (horizontal, tempmax, diagonalL, diagonalR)
            else:
                break

    def updateDiagonalL(self, player, row, col):
        tempmax = 1
        if row - 1 >= 0 and col - 1 >= 0:
            tempmax += self.scoreTrack[player][row - 1][col - 1][2]
        if row + 1 <= 5 and col + 1 <= 6:
            tempmax += self.scoreTrack[player][row + 1][col + 1][2]
        if tempmax >= 4:
            self.winner = player
        horizontal = self.scoreTrack[player][row][col][0]
        vertical = self.scoreTrack[player][row][col][1]
        diagonalR = self.scoreTrack[player][row][col][3]
        self.scoreTrack[player][row][col] = (horizontal, vertical, tempmax, diagonalR)
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self.scoreTrack[player][i][j][2] != 0:
                horizontal = self.scoreTrack[player][i][j][0]
                vertical = self.scoreTrack[player][i][j][1]
                diagonalR = self.scoreTrack[player][i][j][3]
                self.scoreTrack[player][i][j] = (horizontal, vertical, tempmax, diagonalR)
            else:
                break
        for i, j in zip(range(row + 1, 6), range(col + 1, 7)):
            if self.scoreTrack[player][i][j][2] != 0:
                horizontal = self.scoreTrack[player][i][j][0]
                vertical = self.scoreTrack[player][i][j][1]
                diagonalR = self.scoreTrack[player][i][j][3]
                self.scoreTrack[player][i][j] = (horizontal, vertical, tempmax, diagonalR)
            else:
                break

    def updateDiagonalR(self, player, row, col):
        tempmax = 1
        if row - 1 >= 0 and col + 1 <= 6:
            tempmax += self.scoreTrack[player][row - 1][col + 1][3]
        if row + 1 <= 5 and col - 1 >= 0:
            tempmax += self.scoreTrack[player][row + 1][col - 1][3]
        if tempmax >= 4:
            self.winner = player
        horizontal = self.scoreTrack[player][row][col][0]
        vertical = self.scoreTrack[player][row][col][1]
        diagonalL = self.scoreTrack[player][row][col][2]
        self.scoreTrack[player][row][col] = (horizontal, vertical, diagonalL, tempmax)
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, 7)):
            if self.scoreTrack[player][i][j][3] != 0:
                horizontal = self.scoreTrack[player][i][j][0]
                vertical = self.scoreTrack[player][i][j][1]
                diagonalL = self.scoreTrack[player][i][j][2]
                self.scoreTrack[player][i][j] = (horizontal, vertical, diagonalL, tempmax)
            else:
                break
        for i, j in zip(range(row + 1, 6), range(col - 1, -1, -1)):
            if self.scoreTrack[player][i][j][3] != 0:
                horizontal = self.scoreTrack[player][i][j][0]
                vertical = self.scoreTrack[player][i][j][1]
                diagonalL = self.scoreTrack[player][i][j][2]
                self.scoreTrack[player][i][j] = (horizontal, vertical, diagonalL, tempmax)
            else:
                break

    def getTurn(self):
        return self.turn

    def getOpponent(self):
        if self.turn is "X":
            return "Y"
        else:
            return "X"

    def generateSuccessor(self, player, position):
        return self.dropDisc(position)