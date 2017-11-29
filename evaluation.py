from random import SystemRandom


class Evaluation:
    def evaluationFunction(self, gameState, turn):
        """ Simple heuristic to evaluate board configurations
            Heuristic is ...
        """
        if gameState.winner == "X":
            return -1000
        elif gameState.winner == "O":
            return 1000
        else:
            return SystemRandom().random()
