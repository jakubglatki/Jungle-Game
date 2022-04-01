import math

from model.State import State

cellValue1 = [[4, 12, 100, 12, 4],
              [3, 8, 12, 8, 4],
              [3, 7, 9, 7, 3],
              [2, 3, 5, 3, 2],
              [1, 2, 3, 2, 1],
              [0, 1, 2, 1, 0],
              [1, 0, 0, 0, 1]]

cellValue2 = [[1, 0, 0, 0, 1],
              [0, 1, 2, 1, 0],
              [1, 2, 3, 2, 1],
              [2, 3, 5, 3, 2],
              [3, 7, 9, 7, 3],
              [3, 8, 12, 8, 4],
              [4, 12, 100, 12, 4]]

cellValueMouse1 = [[8, 50, math.inf, 50, 8],
                   [11, 13, 50, 14, 12],
                   [10, 12, 13, 13, 11],
                   [8, 11, 11, 12, 9],
                   [6, 8, 9, 9, 7],
                   [5, 7, 8, 8, 6],
                   [2, 1, 0, 2, 1]]

cellValueMouse2 = [[2, 1, 0, 1, 2],
                   [6, 8, 8, 7, 5],
                   [7, 9, 9, 8, 6],
                   [9, 12, 11, 11, 8],
                   [11, 13, 13, 12, 10],
                   [12, 14, 50, 13, 11],
                   [8, 50, math.inf, 50, 8]]

cellValueCat1 = [[8, 50, math.inf, 50, 8],
                 [10, 13, 50, 13, 10],
                 [9, 11, 12, 11, 9],
                 [7, 0, 10, 0, 7],
                 [6, 8, 9, 8,6],
                 [5, 15, 5, 15, 5],
                 [8, 3, 0, 3, 8]]

cellValueCat2 = [[8, 3, 0, 3, 8],
                 [5, 15, 5, 15, 5],
                 [6, 8, 9, 8, 6],
                 [7, 0, 10, 0, 7],
                 [9, 11, 12, 11, 9],
                 [10, 13, 50, 13, 10],
                 [8, 50, math.inf, 50, 8]]

cellValueDog1 = [[10, 50, math.inf, 50, 10],
                 [10, 13, 50, 13, 10],
                 [9, 11, 12, 11, 9],
                 [7, 0, 10, 0, 7],
                 [6, 8, 9, 8, 6],
                 [5, 15, 5, 15, 5],
                 [10, 5, 0, 5, 10]]

cellValueDog2 = [[10, 5, 0, 5, 10],
                 [5, 15, 5, 15, 5],
                 [6, 8, 9, 8, 6],
                 [7, 0, 10, 0, 7],
                 [9, 11, 12, 11, 9],
                 [10, 11, 13, 50, 13, 10],
                 [10, 50, math.inf, 50, 10]]


cellValueElephant1 = [[12, 50, math.inf, 50, 12],
                      [15, 17, 50, 17, 15],
                      [14, 17, 16, 17, 14],
                      [12, 0, 13, 0, 12],
                      [8, 6, 8, 6, 8],
                      [2, 3, 3, 3, 2],
                      [2, 2, 0, 2, 2]]

cellValueElephant2 = [[4, 2, 0, 2, 4],
                      [2, 5, 3, 5, 2],
                      [8, 6, 8, 6, 8],
                      [12, 0, 13, 0, 12],
                      [14, 16, 17, 16, 14],
                      [15, 17, 50, 17, 15],
                      [17, 50, math.inf, 50, 17]]



class EvaluationFunctionController:

    # First evaluation function, it consider only the power of every animal and nothing else
    def evaluationFunction_onlyAnimalPower(self, state: State):
        value = 0
        for animal in state.playerWhoMoves.animalCollection:
            if animal.isAlive: value = value + animal.power
        for animal in state.playerWhoNotMoves.animalCollection:
            if animal.isAlive: value = value - animal.power
        return value

    def evaluationFunction_firstEvaluationFunction(self, state: State):
        # Dojo control if I am player1
        if state.playerWhoMoves.number == 1:
            if state.board.getDojo2().thereIsAnimal() and state.board.getDojo2().animal.player == 1:
                value = math.inf
                return value
            if state.board.getDojo1().thereIsAnimal() and state.board.getDojo1().animal.player == 2:
                value = -math.inf
                return value
        # Dojo control if I am player2
        else:
            if state.board.getDojo1().thereIsAnimal() and state.board.getDojo1().animal.player == 2:
                value = math.inf
                return value
            if state.board.getDojo2().thereIsAnimal() and state.board.getDojo2().animal.player == 1:
                value = -math.inf
                return value

        value = 0
        for animal in state.playerWhoMoves.animalCollection:
            if animal.isAlive:
                if animal.power == 1:
                    value += animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                elif animal.power == 6 or animal.power == 7:
                    value += animal.power + 2
                else:
                    value += animal.power
        for animal in state.playerWhoNotMoves.animalCollection:
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
        if state.playerWhoMoves.number == 1:
            cellValue = cellValue1
            opponentCellValue = cellValue2
        else:
            cellValue = cellValue2
            opponentCellValue = cellValue1

        for animal in state.playerWhoMoves.animalCollection:
            if animal.isAlive:  # and doesnt' have a opponent animal in the adiacent square  through the not menaced function inside animal

                if state.playerWhoMoves.number == 1:
                    if animal.name == "MOUSE":
                        value += cellValueMouse1[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += cellValueCat1[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += cellValueDog1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += cellValueElephant1[animal.getX()][animal.getY()]
                else:
                    if animal.name == "MOUSE":
                        value += cellValueMouse2[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += cellValueCat2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += cellValueDog2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += cellValueElephant2[animal.getX()][animal.getY()]

        for animal in state.playerWhoNotMoves.animalCollection:
            if animal.isAlive:
                if state.opponentPlayer.number == 1:
                    if animal.name == "MOUSE":
                        value -= cellValueMouse1[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value -= cellValueCat1[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value -= cellValueLion1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= cellValueElephant1[animal.getX()][animal.getY()]
                else:
                    if animal.name == "MOUSE":
                        value -= cellValueMouse2[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value -= cellValueCat2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value -= cellValueDog2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= cellValueElephant2[animal.getX()][animal.getY()]
        return value

    def evaluationFunctionWithIsMenacedFunction(self, state: State, difficulty: int):

        if difficulty == 1:
            return self.evaluationFunction_firstEvaluationFunction(state)


        mouseBoard1 = cellValueMouse1
        catBoard1 = cellValueCat1
        dogBoard1 = cellValueDog1
        elephantBoard1 = cellValueElephant1
        mouseBoard2 = cellValueMouse2
        catBoard2 = cellValueCat2
        dogBoard2 = cellValueDog2
        elephantBoard2 = cellValueElephant2

        totalValue = 0
        value = 0
        for animal in state.playerWhoMoves.animalCollection:
            if animal.isAlive:
                value = 0
                if difficulty == 3:
                    if animal.power == 1:
                        value += animal.power * 100 + 400  # Mouse can stay in water and also eat Elephant, for sure has more value
                    elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                        value += animal.power * 100 + 200
                    else:
                        value += animal.power * 100
                else:
                    if animal.power == 1:
                        value += animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                    elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                        value += animal.power + 2
                    else:
                        value += animal.power
                if state.playerWhoMoves.number == 1:
                    # value += cellValuePlayer1[animal.getX()][animal.getY()]
                    if animal.name == "MOUSE":
                        value += mouseBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += catBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += dogBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += elephantBoard1[animal.getX()][animal.getY()]
                else:
                    # value += cellValuePlayer2[animal.getX()][animal.getY()]
                    if animal.name == "MOUSE":
                        value += mouseBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += catBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += dogBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += elephantBoard2[animal.getX()][animal.getY()]
                if state.board.isMenaced(animal):
                    value = value * (3 / 5)
                totalValue += value

        for animal in state.playerWhoNotMoves.animalCollection:
            if animal.isAlive:
                value = 0
                if difficulty == 3:
                    if animal.power == 1:
                        value -= animal.power * 100 + 400  # Mouse can stay in water and also eat Elephant, for sure has more value
                    elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                        value -= animal.power * 100 + 200
                    else:
                        value -= animal.power * 100
                else:
                    if animal.power == 1:
                        value -= animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                    elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                        value -= animal.power + 2
                    else:
                        value -= animal.power
                if state.opponentPlayer.number == 1:
                    # value -= cellValuePlayer1[animal.getX()][animal.getY()] * 2/3
                    if animal.name == "MOUSE":
                        value -= mouseBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value -= catBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value -= dogBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= elephantBoard1[animal.getX()][animal.getY()]
                else:
                    # value -= cellValuePlayer2[animal.getX()][animal.getY()] * 2/3
                    if animal.name == "MOUSE":
                        value -= mouseBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value -= catBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value -= dogBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= elephantBoard2[animal.getX()][animal.getY()]
                totalValue += value

        return totalValue

    def evaluationFunctionWithIsMenacedFunctionWithoutEnemyDiminuition(self, state: State, difficulty: int):

        if difficulty == 3 or difficulty == 4:
            mouseBoard1 = cellValueMouse1
            catBoard1 = cellValueCat1
            dogBoard1 = cellValueDog1
            elephantBoard1 = cellValueElephant1
            mouseBoard2 = cellValueMouse2
            catBoard2 = cellValueCat2
            dogBoard2 = cellValueDog2
            elephantBoard2 = cellValueElephant2
        else:
            mouseBoard1 = cellValue1
            catBoard1 = cellValue1
            dogBoard1 = cellValue1
            elephantBoard1 = cellValue1
            mouseBoard2 = cellValue2
            catBoard2 = cellValue2
            dogBoard2 = cellValue2
            elephantBoard2 = cellValue2


        totalValue = 0
        value = 0
        if difficulty == 2:
            powerIncrease = 100
        else:
            powerIncrease = 1000

        for animal in state.playerWhoMoves.animalCollection:
            if animal.isAlive:
                value = 0
                if animal.power == 1:
                    value += animal.power * powerIncrease + 4 * powerIncrease  # Mouse can stay in water and also eat Elephant, for sure has more value
                elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                    value += animal.power * powerIncrease + 2 * powerIncrease
                else:
                    value += animal.power * powerIncrease
                if state.playerWhoMoves.number == 1:
                    # value += cellValuePlayer1[animal.getX()][animal.getY()]
                    if animal.name == "MOUSE":
                        value += mouseBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += catBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += dogBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += elephantBoard1[animal.getX()][animal.getY()]
                else:
                    # value += cellValuePlayer2[animal.getX()][animal.getY()]
                    if animal.name == "MOUSE":
                        value += mouseBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += catBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += dogBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += elephantBoard2[animal.getX()][animal.getY()]
            if state.board.isMenaced(animal):
                value = value * (3 / 5)
            totalValue += value

        for animal in state.playerWhoNotMoves.animalCollection:
            if animal.isAlive:
                value = 0
                if difficulty == 3:
                    if animal.power == 1:
                        value -= animal.power * powerIncrease + 4 * powerIncrease  # Mouse can stay in water and also eat Elephant, for sure has more value
                    elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                        value -= animal.power * powerIncrease + 2 * powerIncrease
                    else:
                        value -= animal.power * powerIncrease
                else:
                    if animal.power == 1:
                        value -= animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                    elif animal.power == 6 or animal.power == 7 or animal.power == 8:
                        value -= animal.power + 2
                    else:
                        value -= animal.power
                if state.opponentPlayer.number == 1:
                    # value -= cellValuePlayer1[animal.getX()][animal.getY()] * 2/3
                    if animal.name == "MOUSE":
                        value -= mouseBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value -= catBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value -= dogBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= elephantBoard1[animal.getX()][animal.getY()]
                else:
                    # value -= cellValuePlayer2[animal.getX()][animal.getY()] * 2/3
                    if animal.name == "MOUSE":
                        value -= (mouseBoard2[animal.getX()][animal.getY()])
                    elif animal.name == "CAT":
                        value -= catBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value -= dogBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= elephantBoard2[animal.getX()][animal.getY()]
            totalValue += value

        return totalValue
