import math

from model.State import State

cellValuePlayer1 = [[4, 7, 12, 10000, 12, 7, 4],
                    [3, 6, 8, 12, 8, 6, 4],
                    [3, 5, 7, 9, 7, 5, 3],
                    [2, 3, 4, 6, 4, 3, 2],
                    [2, 2, 3, 5, 3, 2, 2],
                    [1, 2, 2, 4, 2, 2, 1],
                    [0, 1, 2, 3, 2, 1, 0],
                    [0, 0, 1, 2, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]

cellValuePlayer2 = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 2, 1, 0, 0],
                    [0, 1, 2, 3, 2, 1, 0],
                    [1, 2, 2, 4, 2, 2, 1],
                    [2, 2, 3, 5, 3, 2, 2],
                    [2, 3, 4, 6, 4, 3, 2],
                    [3, 5, 7, 9, 7, 5, 3],
                    [3, 6, 8, 12, 8, 6, 4],
                    [4, 7, 12, 10000, 12, 7, 4]]


class EvaluationFunctionController:

    # First evaluation function, it consider only the power of every animal and nothing else
    def evaluationFunction_onlyAnimalPower(self, state: State):
        value = 0
        for animal in state.currentPlayer.animalCollection:
            if animal.isAlive: value = value + animal.power
        for animal in state.opponentPlayer.animalCollection:
            if animal.isAlive: value = value - animal.power
        return value

    def evaluationFunction_firstEvaluationFunction(self, state: State):
        # Dojo control if I am player1
        # if state.currentPlayer.number == 1:
        #     if state.board.getDojo2().thereIsAnimal() and state.board.getDojo2().animal.player == 1:
        #         value = math.inf
        #         return value
        #     if state.board.getDojo1().thereIsAnimal() and state.board.getDojo1().animal.player == 2:
        #         value = -math.inf
        #         return value
        # # Dojo control if I am player2
        # else:
        #     if state.board.getDojo1().thereIsAnimal() and state.board.getDojo1().animal.player == 2:
        #         value = math.inf
        #         return value
        #     if state.board.getDojo2().thereIsAnimal() and state.board.getDojo2().animal.player == 1:
        #         value = -math.inf
        #         return value

        value = 0
        for animal in state.currentPlayer.animalCollection:
            if animal.isAlive:
                if animal.power == 1:
                    value += animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                elif animal.power == 6 or animal.power == 7:
                    value += animal.power + 2
                else:
                    value += animal.power
        for animal in state.opponentPlayer.animalCollection:
            if animal.isAlive:
                if animal.power == 1:
                    value -= animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                elif animal.power == 6 or animal.power == 7:
                    value -= animal.power + 2
                else:
                    value -= animal.power
        return value

    # Now the idea is to give importance also in the positioning of each animal, creating some kind of "hot zone" in which some animals are stronger

    def evaluationFunctionWithMeaningfulDistanceToDojo(self, state: State):
        value = self.evaluationFunction_firstEvaluationFunction(state)
        if state.currentPlayer.number == 1:
            cellValue = cellValuePlayer1
            opponentCellValue = cellValuePlayer2
        else:
            cellValue = cellValuePlayer2
            opponentCellValue = cellValuePlayer1

        for j in range(len(state.board.matrix[0])):
            for i in range(len(state.board.matrix)):
                for animal in state.currentPlayer.animalCollection:
                    if state.board.matrix[i][j].animal is not None and state.board.matrix[i][j].animal == animal:
                        value += cellValue[i][j]
                for animal in state.opponentPlayer.animalCollection:
                    if state.board.matrix[i][j].animal is not None and state.board.matrix[i][j].animal == animal:
                        value -= opponentCellValue[i][j] / 3

        return value
