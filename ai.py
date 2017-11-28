from random import randrange, choice, random, SystemRandom
import math


class Human():
    """Keyboard Agent"""

    def play(self):
        position = raw_input("Enter the position for " + "X" + ": ")
        return position


class RandomAgent():
    """This strategy plays in an random column."""

    def play(self):
        position = randrange(1, 7)
        print "Random Agent: inserted at", position
        return position


class MinimaxAlphaBetaAgent():
    def __init__(self, depth=2):
        self.depth = depth

    def getAction(self, gameState):

        def maxValue(state, a, b, depth):
            if state.isEnd() or depth == self.depth:
                return self.evalFunc(state)
            v = float('-inf')
            for action in state.possiblePlace():
                nextState = state.dropDisc(action)
                score = minValue(nextState, a, b, depth + 1)
                v = max(v, score)
                if v > b:
                    return v
                a = max(a, v)
            return v

        def minValue(state, a, b, depth):
            if state.isEnd():
                return self.evalFunc(state)
            v = float('inf')
            for action in state.possiblePlace():
                nextState = state.dropDisc(action)
                v = min(v, maxValue(nextState, a, b, depth))
                if v < a:
                    return v
                b = min(b, v)
            return v

        a = float('-inf')
        b = float('inf')
        v = float('-inf')
        move = dict()
        for action in gameState.possiblePlace():
            nextState = gameState.dropDisc(action)
            score = minValue(nextState, a, b, 1)
            v = max(v, score)
            move[score] = action
            if v > b:
                return move[v]
            a = max(a, v)
        return move[v]

    def getNewState(self, gameState):
        posisions = self.getAction(gameState)
        print "Minimax AB Agent: inserted at", posisions
        return posisions

    def evalFunc(self, gameState, player=None):
        if gameState.winner == "X":
            return -1000
        elif gameState.winner == "O":
            return 1000
        else:
            # scoreX, scoreO = 0, 0
            # for x, o in zip(gameState.scoreTrack["X"], gameState.scoreTrack["O"]):
            #     for xx, oo in zip(x, o):
            #         scoreX = max(max(xx), scoreX)
            #         scoreO = max(max(oo), scoreO)
            # if scoreX >= 3:
            #     return -99999
            # else:
            #     return scoreO - scoreX - random()
            return SystemRandom().random()


class MinimaxAgent():
    def __init__(self, depth=2):
        self.depth = depth

    def getAction(self, gameState):

        def minimax(state, depth):
            move = dict()
            score = float('-inf')
            for action in state.possiblePlace():
                nextState = state.dropDisc(action)
                minScore = minValue(nextState, depth)
                score = max(score, minScore)
                move[minScore] = action
            return move[score]

        def maxValue(state, depth):
            if state.isEnd() or depth == self.depth:
                score = self.evalFunc(state)
                return score
            v = float('-inf')
            for action in state.possiblePlace():
                nextState = state.dropDisc(action)
                score = minValue(nextState, depth + 1)
                v = max(v, score)
            return v

        def minValue(state, depth):
            if state.isEnd():
                score = self.evalFunc(state)
                return score
            v = float('inf')
            for action in state.possiblePlace():
                nextState = state.dropDisc(action)
                score = maxValue(nextState, depth)
                v = min(v, score)
            return v

        return minimax(gameState, 1)

    def getNewState(self, gameState):
        posisions = self.getAction(gameState)
        print "Minimax Agent: inserted at", posisions
        return posisions

    def evalFunc(self, gameState, player=None):
        if gameState.winner == "X":
            return -1000
        elif gameState.winner == "O":
            return 1000
        else:
            # scoreX, scoreO = 0, 0
            # for x, o in zip(gameState.scoreTrack["X"], gameState.scoreTrack["O"]):
            #     for xx, oo in zip(x, o):
            #         scoreX += sum(xx)
            #         scoreO += sum(oo)
            # scoreX, scoreO = scoreX / 3.0, scoreO / 3.0
            # scoreX = math.floor(scoreX) * 10.0 + (scoreX - math.floor(scoreX)) * 2.0
            # scoreO = math.floor(scoreO) * 10.0 + (scoreO - math.floor(scoreO)) * 2.0
            return SystemRandom().random()
