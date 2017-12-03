from random import randrange, random, shuffle
from board import *
from evaluation import Evaluation


class Human:
    """Keyboard Agent"""

    def __init__(self):
        pass

    def play(self):
        position = raw_input("Enter the position for " + "X" + ": ")
        return position


class RandomAgent:
    """This strategy plays in an random column."""

    def __init__(self, game):
        self.game = game

    def play(self):
        position = randrange(1, 8)
        print "Random Agent: inserted at", position
        return position


class MinMaxAgent:

    def __init__(self, gameState, depth):
        self.gameState = gameState
        self.depth = depth
        self.turn = gameState.getTurn()
        self.opponent = gameState.getOpponent()

    def play(self):
        position = self.value(self.gameState, self.turn, self.depth)[1]
        print "MinMax Agent Drops in ", position
        return position

    def value(self, gameState, turn, depth):
        if gameState.isEnd() or depth == 0:
            return Evaluation().evaluationFunction(gameState, turn), "None"
        if turn == self.turn:
            return self.max_value(gameState, turn, depth)
        else:
            return self.min_value(gameState, turn, depth)

    def max_value(self, gameState, turn, depth):

        v = -float("inf")
        BestState = 0
        actions = gameState.possiblePlace()
        successorStates = []
        if turn is "X":
            opponent = "O"
        else:
            opponent = "X"
        # Generating successor states for each legal action.
        for action in actions:
            successorStates.append(gameState.generateSuccessor(turn, action))

        # Loop to check the maxima for each successor state.
        i = 0
        for successorState in successorStates:

            if v < self.value(successorState, opponent, depth)[0]:
                BestState = i
                v = self.value(successorState, opponent, depth)[0]
            i += 1

        # return evaluation value of the chosen successor node ,
        # and the action associated to get to that successor state.
        return v, actions[BestState]

    def min_value(self, gameState, turn, depth):

        v = float("inf")
        BestState = 0
        successorStates = []
        actions = gameState.possiblePlace()
        if turn is "X":
            opponent = "O"
        else:
            opponent = "X"

        # Generating successor states for each legal action.
        for action in actions:
            successorStates.append(gameState.generateSuccessor(turn, action))
        i = 0
        # Loop to check the minima for each successor state.
        for successorState in successorStates:

            if v > self.value(successorState, opponent, depth-1)[0]:
                BestState = i
                v = self.value(successorState, opponent, depth-1)[0]
            i += 1

        # return evaluation value of the chosen successor node ,
        # and the action associated to get to that successor state.
        return v, actions[BestState]


class AlphaBeta:

    def __init__(self, gameState, depth):
        self.gameState = gameState
        self.depth = depth
        self.turn = gameState.getTurn()
        self.opponent = gameState.getOpponent()
        self.order = dict(zip(range(1,8), [0, 2, 4, 8, 5, 3, 1]))
        self.count = 0

    def play(self):
        alpha = -float('inf')
        beta = float('inf')
        position = self.value(self.gameState, self.turn, self.depth, alpha, beta)[1]
        print "AlphaBeta Agent Drops in ", position
        print "count:", self.count
        return position

    def value(self, gameState, turn, depth, alpha, beta):
        self.count = self.count + 1
        if gameState.isEnd() or depth == 0:
            return Evaluation().evaluationFunction(gameState, turn), "None"
        if turn == self.turn:
            return self.max_value(gameState, turn, depth, alpha, beta)
        else:
            return self.min_value(gameState, turn, depth, alpha, beta)

    def max_value(self, gameState, turn, depth, alpha, beta):

        v = -float("inf")
        bestScore = -float('inf')

        actions = gameState.possiblePlace()
        # if self.count > 7000:
        #     actions.sort(self.moveOrder)
        # else:
        #     shuffle(actions)
        if turn is "X":
            opponent = "O"
        else:
            opponent = "X"

        for action in actions:
            successorState = gameState.generateSuccessor(turn, action)
            v = max(v, self.value(successorState, opponent, depth, alpha, beta)[0])
            if v > beta:
                return v, action
            alpha = max(alpha, v)

            if v > bestScore:
                bestScore = v
                bestAction = action

        return bestScore, bestAction

    def moveOrder(self, x, y):
        if self.order[x] < self.order[y]:
            return 1
        if self.order[x] > self.order[y]:
            return -1
        else:
            return 0

    def min_value(self, gameState, turn, depth, alpha, beta):

        v = float('inf')
        bestScore = float('inf')

        actions = gameState.possiblePlace()
        # shuffle(actions)
        # if self.count > 7000:
        #     actions.sort(self.moveOrder)
        # else:
        #     shuffle(actions)
        if turn is "X":
            opponent = "O"
        else:
            opponent = "X"

        for action in actions:
            successorState = gameState.generateSuccessor(turn, action)
            v = min(v, self.value(successorState, opponent, depth - 1, alpha, beta)[0])

            if v < alpha:
                return v, action
            beta = min(beta, v)

            if bestScore > v:
                bestScore = v
                bestAction = action

        return bestScore, bestAction



class ExpectimaxAgent:
    """
    expectimax agent

    """
    def __init__(self, gameState, depth):
        self.gameState = gameState
        self.depth = depth
        self.turn = gameState.getTurn()
        self.opponent = gameState.getOpponent()


    def play(self):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
        """

        position = self.value(self.gameState, self.turn, self.depth)[1]
        print "Expectimax Agent Drops in ", position
        return position

    def value(self, gameState, turn, depth):
        if gameState.isEnd() or depth == 0:
            return Evaluation().evaluationFunction(gameState, turn), "None"
        if self.turn == turn:
            return self.max_value(gameState, turn, depth)
        else:
            return self.exp_value(gameState, turn, depth)

    def max_value(self, gameState, turn, depth):

        v = -float("inf")
        actions = gameState.possiblePlace()
        successorStates = []

        # Generating successor states for each legal action.
        for action in actions:
            successorStates.append(gameState.generateSuccessor(turn, action))

        if turn == "X": turn = "Y"
        else: turn = "X"
        # Loop to check the maxima for each successor state.
        i = 0
        for successorState in successorStates:

            if v < self.value(successorState, turn, depth)[0]:
                BestState = i
                v = self.value(successorState, turn, depth)[0]
            i += 1

        # return evaluation value of the chosen successor node ,
        # and the action associated to get to that successor state.
        return v, actions[BestState]

    def exp_value(self, gameState, turn, depth):
        evals = []
        successorStates = []
        actions = gameState.possiblePlace()
        if turn == "X": turn = "Y"
        else: turn = "X"

        # Generating successor states for each legal action.
        for action in actions:
            successorStates.append(gameState.generateSuccessor(turn, action))

            # Loop to check the minima for each successor state.
        for successorState in successorStates:
            evals.append(self.value(successorState, self.turn, depth - 1)[0])
            #BestState = i
            #v = self.value(successorState, 0, depth - 1)[0]
            #i += 1

        # return evaluation value of the chosen successor node ,
        # and the action associated to get to that successor state.
        return float(sum(evals)/len(evals)), 'None'

class MinimaxAlphaBetaAgent:
    def __init__(self, depth=3):
        self.depth = depth
        self.begin = True
        self.count = 0
        self.order = dict(zip(range(1, 8), [0, 4, 2, 8, 3, 5, 1]))

    def getAction(self, gameState):
        def moveOrder(x, y):
            if self.order[x] < self.order[y]:
                return 1
            if self.order[x] > self.order[y]:
                return -1
            else:
                return 0

        def maxValue(state, a, b, depth):
            if state.isEnd() or depth == self.depth:
                return Evaluation().evaluationFunction(state)
            v = float('-inf')
            actions = state.possiblePlace()
            if self.count > 200:
                actions.sort(moveOrder)
            else:
                shuffle(actions)
            for action in actions:
                nextState = state.dropDisc(action)
                score = minValue(nextState, a, b, depth + 1)
                v = max(v, score)
                if v > b:
                    return v
                a = max(a, v)
            return v

        def minValue(state, a, b, depth):
            self.count = self.count + 1
            if state.isEnd():
                return Evaluation().evaluationFunction(state)
            v = float('inf')
            actions = state.possiblePlace()
            if self.count > 200:
                actions.sort(moveOrder)
            else:
                shuffle(actions)
            for action in actions:
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
        print "abc inserted at ", move[v]
        print "count",self.count
        return move[v]
