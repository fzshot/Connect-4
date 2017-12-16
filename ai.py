from random import randrange
import pickle


class Human():
    """Keyboard Agent"""

    def play(self):
        position = raw_input("Enter the position for " + "X" + ": ")
        return position


class RandomAgent():
    """This strategy plays in an random column."""

    def play(self):
        position = randrange(1, 7)
        print("Random Agent: inserted at", position)
        return position


class GeneralAgents():
    def __init__(self, version):
        self.name = version
        try:
            self.save = self.load_obj(version)
        except Exception:
            self.save = dict()

    # https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file
    def save_obj(self):
        with open("save" + self.name + ".pkl", "wb+") as f:
            pickle.dump(self.save, f, pickle.HIGHEST_PROTOCOL)

    def load_obj(self, version):
        with open("save" + version + ".pkl", "rb") as f:
            return pickle.load(f)


class MinimaxAlphaBetaAgent(GeneralAgents):
    def __init__(self, depth=2):
        self.depth = depth
        self.begin = True
        self.count = 0
        GeneralAgents.__init__(self, "AB" + str(depth))

    def get_action(self, game_state):
        def max_value(state, a, b, depth):
            self.count += 1
            if state.is_end() or depth == self.depth:
                return self.eval_func(state)
            v = float('-inf')
            for action in state.possible_place():
                next_state = state.drop_disc(action)
                score = min_value(next_state, a, b, depth + 1)
                v = max(v, score)
                if v > b:
                    return v
                a = max(a, v)
            return v

        def min_value(state, a, b, depth):
            self.count += 1
            if state.is_end():
                return self.eval_func(state)
            v = float('inf')
            for action in state.possible_place():
                next_state = state.drop_disc(action)
                v = min(v, max_value(next_state, a, b, depth))
                if v < a:
                    return v
                b = min(b, v)
            return v

        current_board = game_state.drawBoard
        if current_board in self.save:
            print("Nodes explored: ", self.count)
            return self.save[current_board]
        else:
            a = float('-inf')
            b = float('inf')
            v = float('-inf')
            move = dict()
            for action in game_state.possible_place():
                next_state = game_state.drop_disc(action)
                score = min_value(next_state, a, b, 1)
                v = max(v, score)
                move[score] = action
                if v > b:
                    print("Nodes explored: ", self.count)
                    return move[v]
                a = max(a, v)
            self.save[current_board] = move[v]
            print("Nodes explored: ", self.count)
            return move[v]

    def get_new_state(self, game_state):
        # if self.begin:
        #     posisions = 4
        #     self.begin = False
        # else:
        posisions = self.get_action(game_state)
        print("Minimax AB Agent: inserted at", posisions)
        return posisions

    def eval_func(self, game_state, player=None):
        weight_matrix = [[3, 4, 5, 7, 5, 4, 3],
                         [4, 6, 8, 10, 8, 6, 4],
                         [5, 8, 11, 13, 11, 8, 5],
                         [5, 8, 11, 13, 11, 8, 5],
                         [4, 6, 8, 10, 8, 6, 4],
                         [3, 4, 5, 7, 5, 4, 3]]
        if game_state.winner == "X":
            return float('-inf')
        elif game_state.winner == "O":
            return float('inf')
        else:
            score_x, score_o = 0, 0
            j = 0
            for x, o in zip(game_state.scoreTrack["X"], game_state.scoreTrack["O"]):
                i = 0
                for xx, oo in zip(x, o):
                    max_xx, max_oo = max(xx), max(oo)
                    if max_xx == 1:
                        score_x += 1 * weight_matrix[j][i]
                    elif max_xx == 2:
                        score_x += 10 * weight_matrix[j][i]
                    else:
                        score_x += 100 * weight_matrix[j][i]
                    if max_oo == 1:
                        score_o += 1 * weight_matrix[j][i]
                    elif max_oo == 2:
                        score_o += 10 * weight_matrix[j][i]
                    else:
                        score_o += 100 * weight_matrix[j][i]
                    i += 1
                j += 1
            return score_o - score_x


class MinimaxAgent(GeneralAgents):
    def __init__(self, depth=2):
        self.depth = depth
        self.begin = True
        GeneralAgents.__init__(self, "minimax" + str(depth))

    def get_action(self, game_state):

        def minimax(state, depth):
            move = dict()
            score = float('-inf')
            for action in state.possible_place():
                next_state = state.drop_disc(action)
                min_score = min_value(next_state, depth)
                score = max(score, min_score)
                move[min_score] = action
            return move[score]

        def max_value(state, depth):
            if state.is_end() or depth == self.depth:
                score = self.eval_func(state)
                return score
            v = float('-inf')
            for action in state.possible_place():
                next_state = state.drop_disc(action)
                score = min_value(next_state, depth + 1)
                v = max(v, score)
            return v

        def min_value(state, depth):
            if state.is_end():
                score = self.eval_func(state)
                return score
            v = float('inf')
            for action in state.possible_place():
                next_state = state.drop_disc(action)
                score = max_value(next_state, depth)
                v = min(v, score)
            return v

        current_board = game_state.drawBoard
        if current_board in self.save:
            return self.save[current_board]
        else:
            return minimax(game_state, 1)

    def get_new_state(self, game_state):
        # if self.begin:
        #     posisions = 4
        #     self.begin = False
        # else:
        posisions = self.get_action(game_state)
        print("Minimax Agent: inserted at", posisions)
        return posisions

    def eval_func(self, game_state, player=None):
        weight_matrix = [[3, 4, 5, 7, 5, 4, 3],
                         [4, 6, 8, 10, 8, 6, 4],
                         [5, 8, 11, 13, 11, 8, 5],
                         [5, 8, 11, 13, 11, 8, 5],
                         [4, 6, 8, 10, 8, 6, 4],
                         [3, 4, 5, 7, 5, 4, 3]]
        if game_state.winner == "X":
            return float('-inf')
        elif game_state.winner == "O":
            return float('inf')
        else:
            score_x, score_o = 0, 0
            j = 0
            for x, o in zip(game_state.scoreTrack["X"], game_state.scoreTrack["O"]):
                i = 0
                for xx, oo in zip(x, o):
                    max_xx, max_oo = max(xx), max(oo)
                    if max_xx == 1:
                        score_x += 1 * weight_matrix[j][i]
                    elif max_xx == 2:
                        score_x += 10 * weight_matrix[j][i]
                    else:
                        score_x += 100 * weight_matrix[j][i]
                    if max_oo == 1:
                        score_o += 1 * weight_matrix[j][i]
                    elif max_oo == 2:
                        score_o += 10 * weight_matrix[j][i]
                    else:
                        score_o += 100 * weight_matrix[j][i]
                    i += 1
                j += 1
            return score_o - score_x
