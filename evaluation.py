from random import SystemRandom


class Evaluation:
    def evaluationFunction(self, gameState, turn):
        """ Simple heuristic to evaluate board configurations
            Heuristic is ...
        """
        weightMatrix = [[3, 4, 5, 7, 5, 4, 3],
                        [4, 6, 8, 10, 8, 6, 4],
                        [5, 8, 11, 13, 11, 8, 5],
                        [5, 8, 11, 13, 11, 8, 5],
                        [4, 6, 8, 10, 8, 6, 4],
                        [3, 4, 5, 7, 5, 4, 3]]
        if gameState.winner == "X":
            return 9999999999
        elif gameState.winner == "O":
            return -999999999
        else:
            scoreX, scoreO = 0, 0
            j = 0
            for x, o in zip(gameState.scoreTrack["X"], gameState.scoreTrack["O"]):
                i = 0
                for xx, oo in zip(x, o):
                    max_xx, max_oo = max(xx), max(oo)
                    if max_xx == 0:
                        pass
                    elif max_xx == 1:
                        scoreX += 1 * weightMatrix[j][i]
                    elif max_xx == 2:
                        scoreX += 10 * weightMatrix[j][i]
                    else:
                        scoreX += 100 * weightMatrix[j][i]
                    if max_oo == 0:
                        pass
                    elif max_oo == 1:
                        scoreO += 1 * weightMatrix[j][i]
                    elif max_oo == 2:
                        scoreO += 10 * weightMatrix[j][i]
                    else:
                        scoreO += 100 * weightMatrix[j][i]
                    i += 1
                j += 1
            return scoreO - scoreX
