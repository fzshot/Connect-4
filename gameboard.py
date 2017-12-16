from copy import deepcopy


class GameBoard:
    def __init__(self):
        self.score_track = {"X": [], "O": []}
        self.turn = "X"
        self.game_board = []
        self.draw_board = None
        self.winner = None
        self.init_board()

    def init_board(self):
        for i in range(6):
            self.game_board.append([" ", " ", " ", " ", " ", " ", " "])
        self.update_draw_board()
        for row in range(6):
            self.score_track["X"].append(
                [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)])
            self.score_track["O"].append(
                [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)])

    def get_board(self):
        return self.game_board

    def update_draw_board(self):
        result = ""
        for raw in self.game_board:
            for place in raw:
                result += "|" + place
            result += "|\n"
        self.draw_board = result

    def print_board(self):
        print("*1*2*3*4*5*6*7*")
        print(self.draw_board)

    def drop_disc(self, column):
        newgamestate = deepcopy(self)
        if column in newgamestate.possible_place():
            for i in range(len(newgamestate.game_board) - 1, -1, -1):
                if newgamestate.game_board[i][column - 1] == " ":
                    newgamestate.game_board[i][column - 1] = newgamestate.turn
                    newgamestate.update_score(newgamestate.turn, i, column - 1)
                    break
            newgamestate.update_draw_board()
            if newgamestate.turn == "X":
                newgamestate.turn = "O"
            else:
                newgamestate.turn = "X"
        return newgamestate

    def possible_place(self):
        place = []
        for i in range(7):
            if self.game_board[0][i] == " ":
                place.append(i + 1)
        return place

    def is_end(self):
        if self.winner is not None:
            result = True
        else:
            for place in self.game_board[0]:
                if place == " ":
                    return False
            result = True
        return result

    def get_winner(self):
        return self.winner

    def update_score(self, player, row, col):
        self.update_horizontal(player, row, col)
        self.update_vertical(player, row, col)
        self.update_diagonal_left(player, row, col)
        self.update_diagonal_right(player, row, col)

    def update_horizontal(self, player, row, col):
        tempmax = 1
        if col - 1 >= 0:
            tempmax += self.score_track[player][row][col - 1][0]
        if col + 1 <= 6:
            tempmax += self.score_track[player][row][col + 1][0]
        if tempmax >= 4:
            self.winner = player
        # else:
        vertical = self.score_track[player][row][col][1]
        diagonal_l = self.score_track[player][row][col][2]
        diagonal_r = self.score_track[player][row][col][3]
        self.score_track[player][row][col] = (tempmax, vertical, diagonal_l, diagonal_r)
        for i in range(col + 1, 7):
            if self.score_track[player][row][i][0] != 0:
                vertical = self.score_track[player][row][i][1]
                diagonal_l = self.score_track[player][row][i][2]
                diagonal_r = self.score_track[player][row][i][3]
                self.score_track[player][row][i] = (tempmax, vertical, diagonal_l, diagonal_r)
            else:
                break
        for i in range(col - 1, -1, -1):
            if self.score_track[player][row][i][0] != 0:
                vertical = self.score_track[player][row][i][1]
                diagonal_l = self.score_track[player][row][i][2]
                diagonal_r = self.score_track[player][row][i][3]
                self.score_track[player][row][i] = (tempmax, vertical, diagonal_l, diagonal_r)
            else:
                break

    def update_vertical(self, player, row, col):
        tempmax = 1
        if row - 1 >= 0:
            tempmax += self.score_track[player][row - 1][col][1]
        if row + 1 <= 5:
            tempmax += self.score_track[player][row + 1][col][1]
        if tempmax >= 4:
            self.winner = player
        # else:
        horizontal = self.score_track[player][row][col][0]
        diagonal_l = self.score_track[player][row][col][2]
        diagonal_r = self.score_track[player][row][col][3]
        self.score_track[player][row][col] = (horizontal, tempmax, diagonal_l, diagonal_r)
        for i in range(row + 1, 6):
            if self.score_track[player][i][col][1] != 0:
                horizontal = self.score_track[player][i][col][0]
                diagonal_l = self.score_track[player][i][col][2]
                diagonal_r = self.score_track[player][i][col][3]
                self.score_track[player][i][col] = (horizontal, tempmax, diagonal_l, diagonal_r)
            else:
                break

    def update_diagonal_left(self, player, row, col):
        tempmax = 1
        if row - 1 >= 0 and col - 1 >= 0:
            tempmax += self.score_track[player][row - 1][col - 1][2]
        if row + 1 <= 5 and col + 1 <= 6:
            tempmax += self.score_track[player][row + 1][col + 1][2]
        if tempmax >= 4:
            self.winner = player
        horizontal = self.score_track[player][row][col][0]
        vertical = self.score_track[player][row][col][1]
        diagonal_r = self.score_track[player][row][col][3]
        self.score_track[player][row][col] = (horizontal, vertical, tempmax, diagonal_r)
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self.score_track[player][i][j][2] != 0:
                horizontal = self.score_track[player][i][j][0]
                vertical = self.score_track[player][i][j][1]
                diagonal_r = self.score_track[player][i][j][3]
                self.score_track[player][i][j] = (horizontal, vertical, tempmax, diagonal_r)
            else:
                break
        for i, j in zip(range(row + 1, 6), range(col + 1, 7)):
            if self.score_track[player][i][j][2] != 0:
                horizontal = self.score_track[player][i][j][0]
                vertical = self.score_track[player][i][j][1]
                diagonal_r = self.score_track[player][i][j][3]
                self.score_track[player][i][j] = (horizontal, vertical, tempmax, diagonal_r)
            else:
                break

    def update_diagonal_right(self, player, row, col):
        tempmax = 1
        if row - 1 >= 0 and col + 1 <= 6:
            tempmax += self.score_track[player][row - 1][col + 1][3]
        if row + 1 <= 5 and col - 1 >= 0:
            tempmax += self.score_track[player][row + 1][col - 1][3]
        if tempmax >= 4:
            self.winner = player
        horizontal = self.score_track[player][row][col][0]
        vertical = self.score_track[player][row][col][1]
        diagonal_l = self.score_track[player][row][col][2]
        self.score_track[player][row][col] = (horizontal, vertical, diagonal_l, tempmax)
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, 7)):
            if self.score_track[player][i][j][3] != 0:
                horizontal = self.score_track[player][i][j][0]
                vertical = self.score_track[player][i][j][1]
                diagonal_l = self.score_track[player][i][j][2]
                self.score_track[player][i][j] = (horizontal, vertical, diagonal_l, tempmax)
            else:
                break
        for i, j in zip(range(row + 1, 6), range(col - 1, -1, -1)):
            if self.score_track[player][i][j][3] != 0:
                horizontal = self.score_track[player][i][j][0]
                vertical = self.score_track[player][i][j][1]
                diagonal_l = self.score_track[player][i][j][2]
                self.score_track[player][i][j] = (horizontal, vertical, diagonal_l, tempmax)
            else:
                break

    def get_turn(self):
        return self.turn
