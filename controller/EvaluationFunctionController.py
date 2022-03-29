import math

from model.State import State

cellValue1 = [[4, 12, 100, 12, 4],
              [3, 8, 12, 8, 4],
              [3, 7, 9, 7, 3],
              [2, 3, 5, 3, 2],
              [1, 2, 4, 2, 1],
              [0, 1, 2, 1, 0],
              [0, 0, 0, 0, 0]]

cellValue2 = list(reversed(cellValue1))

cellValueMouse1 = [[12, 50, math.inf, 50, 12],
                   [11, 13, 50, 13, 11],
                   [10, 12, 13, 12, 10],
                   [8, 11, 11, 11, 8],
                   [6, 8, 9, 8, 6],
                   [5, 7, 8, 7, 5],
                   [4, 5, 7, 5, 4]]

cellValueMouse2 = list(reversed(cellValueMouse1))

cellValueCat1 = [[11, 12, 50, math.inf, 50, 12, 11],
                 [10, 11, 13, 50, 13, 11, 10],
                 [9, 10, 11, 12, 11, 10, 9],
                 [8, 0, 0, 11, 0, 0, 8],
                 [7, 0, 0, 10, 0, 0, 7],
                 [6, 0, 0, 9, 0, 0, 6],
                 [6, 7, 8, 9, 8, 7, 6],
                 [5, 6, 9, 6, 9, 6, 5],
                 [4, 9, 4, 11, 4, 9, 4]]

cellValueCat2 = [[4, 9, 4, 11, 4, 9, 4],
                 [5, 6, 9, 6, 9, 6, 5],
                 [6, 7, 8, 9, 8, 7, 6],
                 [6, 0, 0, 9, 0, 0, 6],
                 [7, 0, 0, 10, 0, 0, 7],
                 [8, 0, 0, 11, 0, 0, 8],
                 [9, 10, 11, 12, 11, 10, 9],
                 [10, 11, 13, 50, 13, 11, 10],
                 [11, 12, 50, math.inf, 50, 12, 11]]

cellValueDog1 = [[11, 12, 50, math.inf, 50, 12, 11],
                 [10, 11, 13, 50, 13, 11, 10],
                 [9, 10, 11, 12, 11, 10, 9],
                 [8, 0, 0, 11, 0, 0, 8],
                 [7, 0, 0, 10, 0, 0, 7],
                 [6, 0, 0, 9, 0, 0, 6],
                 [6, 7, 8, 9, 8, 7, 6],
                 [5, 6, 8, 7, 8, 6, 5],
                 [4, 8, 5, 10, 5, 8, 4]]

cellValueDog2 = [[4, 8, 5, 10, 5, 8, 4],
                 [5, 6, 8, 7, 8, 6, 5],
                 [6, 7, 8, 9, 8, 7, 6],
                 [6, 0, 0, 9, 0, 0, 6],
                 [7, 0, 0, 10, 0, 0, 7],
                 [8, 0, 0, 11, 0, 0, 8],
                 [9, 10, 11, 12, 11, 10, 9],
                 [10, 11, 13, 50, 13, 11, 10],
                 [11, 12, 50, math.inf, 50, 12, 11]]

cellValueWolf1 = [[12, 13, 50, math.inf, 50, 13, 12],
                  [11, 12, 13, 50, 13, 12, 11],
                  [10, 11, 12, 13, 12, 11, 10],
                  [9, 0, 0, 12, 0, 0, 9],
                  [8, 0, 0, 11, 0, 0, 8],
                  [7, 0, 0, 10, 0, 0, 7],
                  [5, 5, 5, 7, 5, 5, 5],
                  [4, 5, 7, 5, 7, 5, 4],
                  [3, 5, 4, 6, 4, 5, 3]]

cellValueWolf2 = [[3, 5, 4, 6, 4, 5, 3],
                  [4, 5, 7, 5, 7, 5, 4],
                  [5, 5, 5, 7, 5, 5, 5],
                  [7, 0, 0, 10, 0, 0, 7],
                  [8, 0, 0, 11, 0, 0, 8],
                  [9, 0, 0, 12, 0, 0, 9],
                  [10, 11, 12, 13, 12, 11, 10],
                  [11, 12, 13, 50, 13, 12, 11],
                  [12, 13, 50, math.inf, 50, 13, 12]]

cellValuePanther1 = [[13, 50, math.inf, 50, 13],
                     [12, 14, 50, 14, 12],
                     [11, 13, 14, 13, 11],
                     [9, 0, 11, 0, 9],
                     [6, 4, 7, 4, 6],
                     [3, 5, 3, 5, 3],
                     [2, 3, 4, 3, 2]]

cellValuePanther2 = list(reversed(cellValuePanther1))

cellValueTiger1 = [[14, 15, 50, math.inf, 50, 15, 14],
                   [14, 15, 16, 50, 16, 15, 14],
                   [13, 14, 15, 15, 15, 14, 13],
                   [12, 0, 0, 11, 0, 0, 12],
                   [11, 0, 0, 10, 0, 0, 11],
                   [10, 0, 0, 11, 0, 0, 10],
                   [6, 10, 10, 9, 10, 10, 6],
                   [2, 3, 4, 2, 4, 3, 2],
                   [1, 3, 2, 2, 2, 3, 1]]

cellValueTiger2 = [[1, 4, 2, 2, 2, 4, 1],
                   [2, 3, 5, 2, 5, 3, 2],
                   [6, 10, 10, 9, 10, 10, 6],
                   [10, 0, 0, 11, 0, 0, 10],
                   [11, 0, 0, 10, 0, 0, 11],
                   [12, 0, 0, 11, 0, 0, 12],
                   [13, 14, 15, 15, 15, 14, 13],
                   [14, 15, 16, 50, 16, 15, 14],
                   [14, 15, 50, math.inf, 50, 15, 14]]

cellValueLion1 = [[14, 50, math.inf, 50, 14],
                  [14, 16, 50, 16, 14],
                  [13, 15, 15, 15, 13],
                  [11, 0, 10, 0, 11],
                  [6, 10, 9, 10, 6],
                  [2, 4, 2, 4, 2],
                  [1, 2, 2, 2, 1]]

cellValueLion2 = list(reversed(cellValueLion1))

cellValueElephant1 = [[16, 50, math.inf, 50, 16],
                      [15, 17, 50, 17, 15],
                      [14, 16, 17, 16, 14],
                      [12, 0, 13, 0, 12],
                      [8, 6, 8, 6, 8],
                      [2, 3, 3, 3, 2],
                      [0, 2, 4, 2, 0]]

cellValueElephant2 = list(reversed(cellValueElephant1))

hardCellValueMouse1 = [[11, 50, math.inf, 50, 13],
                       [11, 13, 50, 13, 13],
                       [10, 11, 13, 13, 13],
                       [8, 9, 11, 12, 12],
                       [8, 8, 9, 10, 10],
                       [8, 8, 9, 9, 9],
                       [8, 8, 0, 8, 8]]

hardCellValueMouse2 = list(reversed(hardCellValueMouse1))

hardCellValueCat1 = [[11, 15, 50, math.inf, 50, 15, 11],
                     [11, 11, 15, 50, 15, 11, 11],
                     [10, 11, 11, 15, 11, 11, 10],
                     [10, 0, 0, 10, 0, 0, 8],
                     [10, 0, 0, 8, 0, 0, 8],
                     [10, 0, 0, 8, 0, 0, 8],
                     [10, 10, 10, 8, 8, 8, 8],
                     [13, 10, 8, 8, 8, 8, 8],
                     [8, 8, 8, 0, 8, 8, 8]]

hardCellValueCat2 = list(reversed(hardCellValueCat1))

hardCellValueDog1 = [[11, 15, 50, math.inf, 50, 15, 11],
                     [10, 11, 15, 50, 15, 11, 10],
                     [9, 10, 11, 15, 11, 10, 9],
                     [9, 0, 0, 10, 0, 0, 9],
                     [8, 0, 0, 8, 0, 0, 8],
                     [8, 0, 0, 8, 0, 0, 8],
                     [8, 8, 10, 8, 8, 8, 8],
                     [8, 12, 13, 8, 8, 8, 8],
                     [8, 12, 12, 0, 8, 8, 8]]

hardCellValueDog2 = list(reversed(hardCellValueDog1))

hardCellValueWolf1 = [[11, 15, 50, math.inf, 50, 15, 11],
                      [10, 11, 15, 50, 15, 11, 10],
                      [9, 10, 11, 15, 11, 10, 9],
                      [9, 0, 0, 10, 0, 0, 9],
                      [8, 0, 0, 8, 0, 0, 8],
                      [8, 0, 0, 8, 0, 0, 8],
                      [8, 8, 8, 8, 8, 8, 8],
                      [8, 8, 8, 8, 13, 10, 8],
                      [8, 8, 8, 0, 12, 12, 8]]

hardCellValueWolf2 = list(reversed(hardCellValueWolf1))

hardCellValuePanther1 = [[14, 50, math.inf, 50, 14],
                         [13, 15, 50, 15, 13],
                         [13, 14, 15, 14, 13],
                         [11, 0, 14, 0, 11],
                         [9, 9, 10, 10, 9],
                         [9, 9, 9, 9, 9],
                         [9, 9, 0, 9, 9]]

hardCellValuePanther2 = list(reversed(hardCellValuePanther1))

hardCellValueTiger1 = [[25, 30, 50, math.inf, 50, 30, 25],
                       [25, 25, 30, 50, 30, 25, 25],
                       [18, 20, 20, 30, 20, 20, 18],
                       [15, 0, 0, 15, 0, 0, 15],
                       [15, 0, 0, 15, 0, 0, 15],
                       [15, 0, 0, 15, 0, 0, 15],
                       [14, 16, 16, 14, 16, 16, 14],
                       [12, 14, 12, 12, 12, 12, 12],
                       [10, 12, 12, 0, 12, 12, 10]]

hardCellValueTiger2 = list(reversed(hardCellValueTiger1))

hardCellValueLion1 = [[25, 50, math.inf, 50, 25],
                      [25, 30, 50, 30, 25],
                      [18, 20, 30, 20, 18],
                      [15, 0, 15, 0, 15],
                      [14, 16, 14, 16, 14],
                      [12, 12, 12, 12, 12],
                      [10, 12, 0, 12, 10]]

hardCellValueLion2 = list(reversed(hardCellValueLion1))

hardCellValueElephant1 = [[25, 50, math.inf, 50, 25],
                          [25, 30, 50, 30, 25],
                          [18, 20, 30, 20, 18],
                          [14, 0, 14, 0, 14],
                          [10, 14, 14, 14, 12],
                          [11, 11, 11, 11, 11],
                          [11, 11, 0, 11, 11]]

hardCellValueElephant2 = list(reversed(hardCellValueElephant1))


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
                elif animal.power == 7:
                    value += animal.power + 2
                else:
                    value += animal.power
        for animal in state.playerWhoNotMoves.animalCollection:
            if animal.isAlive:
                if animal.power == 1:
                    value -= animal.power + 5  # Mouse can stay in water and also eat Elephant, for sure has more value
                elif animal.power == 7:
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
                    elif animal.name == "WOLF":
                        value += cellValueWolf1[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value += cellValuePanther1[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value += cellValueTiger1[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value += cellValueLion1[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value += cellValueElephant1[animal.getX()][animal.getY()]
                else:
                    if animal.name == "MOUSE":
                        value += cellValueMouse2[animal.getX()][animal.getY()]
                    elif animal.name == "CAT":
                        value += cellValueCat2[animal.getX()][animal.getY()]
                    elif animal.name == "DOG":
                        value += cellValueDog2[animal.getX()][animal.getY()]
                    elif animal.name == "WOLF":
                        value += cellValueWolf2[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value += cellValuePanther2[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value += cellValueTiger2[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value += cellValueLion2[animal.getX()][animal.getY()]
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
                        value -= cellValueDog1[animal.getX()][animal.getY()]
                    elif animal.name == "WOLF":
                        value -= cellValueWolf1[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value -= cellValuePanther1[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value -= cellValueTiger1[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
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
                    elif animal.name == "WOLF":
                        value -= cellValueWolf2[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value -= cellValuePanther2[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value -= cellValueTiger2[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value -= cellValueLion2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= cellValueElephant2[animal.getX()][animal.getY()]
        return value

    def evaluationFunctionWithIsMenacedFunction(self, state: State, difficulty: int):

        if difficulty == 1:
            return self.evaluationFunction_firstEvaluationFunction(state)

        if difficulty == 3:
            mouseBoard1 = hardCellValueMouse1
            catBoard1 = hardCellValueCat1
            dogBoard1 = hardCellValueDog1
            wolfBoard1 = hardCellValueWolf1
            pantherBoard1 = hardCellValuePanther1
            tigerBoard1 = hardCellValueTiger1
            lionBoard1 = hardCellValueLion1
            elephantBoard1 = hardCellValueElephant1
            mouseBoard2 = hardCellValueMouse2
            catBoard2 = hardCellValueCat2
            dogBoard2 = hardCellValueDog2
            wolfBoard2 = hardCellValueWolf2
            pantherBoard2 = hardCellValuePanther2
            tigerBoard2 = hardCellValueTiger2
            lionBoard2 = hardCellValueLion2
            elephantBoard2 = hardCellValueElephant2
        else:
            mouseBoard1 = cellValueMouse1
            catBoard1 = cellValueCat1
            dogBoard1 = cellValueDog1
            wolfBoard1 = cellValueWolf1
            pantherBoard1 = cellValuePanther1
            tigerBoard1 = cellValueTiger1
            lionBoard1 = cellValueLion1
            elephantBoard1 = cellValueElephant1
            mouseBoard2 = cellValueMouse2
            catBoard2 = cellValueCat2
            dogBoard2 = cellValueDog2
            wolfBoard2 = cellValueWolf2
            pantherBoard2 = cellValuePanther2
            tigerBoard2 = cellValueTiger2
            lionBoard2 = cellValueLion2
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
                    elif animal.name == "WOLF":
                        value += wolfBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value += pantherBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value += tigerBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value += lionBoard1[animal.getX()][animal.getY()]
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
                    elif animal.name == "WOLF":
                        value += wolfBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value += pantherBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value += tigerBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value += lionBoard2[animal.getX()][animal.getY()]
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
                    elif animal.name == "WOLF":
                        value -= wolfBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value -= pantherBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value -= tigerBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value -= lionBoard1[animal.getX()][animal.getY()]
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
                    elif animal.name == "WOLF":
                        value -= wolfBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value -= pantherBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value -= tigerBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value -= lionBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= elephantBoard2[animal.getX()][animal.getY()]
                totalValue += value

        return totalValue

    def evaluationFunctionWithIsMenacedFunctionWithoutEnemyDiminuition(self, state: State, difficulty: int):

        if difficulty == 4:
            mouseBoard1 = hardCellValueMouse1
            pantherBoard1 = hardCellValuePanther1
            lionBoard1 = hardCellValueLion1
            elephantBoard1 = hardCellValueElephant1
            mouseBoard2 = hardCellValueMouse2
            pantherBoard2 = hardCellValuePanther2
            lionBoard2 = hardCellValueLion2
            elephantBoard2 = hardCellValueElephant2
        elif difficulty == 3:
            mouseBoard1 = cellValueMouse1
            pantherBoard1 = cellValuePanther1
            lionBoard1 = cellValueLion1
            elephantBoard1 = cellValueElephant1
            mouseBoard2 = cellValueMouse2
            catBoard2 = cellValueCat2
            dogBoard2 = cellValueDog2
            wolfBoard2 = cellValueWolf2
            pantherBoard2 = cellValuePanther2
            tigerBoard2 = cellValueTiger2
            lionBoard2 = cellValueLion2
            elephantBoard2 = cellValueElephant2
        else:
            mouseBoard1 = cellValue1
            catBoard1 = cellValue1
            dogBoard1 = cellValue1
            wolfBoard1 = cellValue1
            pantherBoard1 = cellValue1
            tigerBoard1 = cellValue1
            lionBoard1 = cellValue1
            elephantBoard1 = cellValue1
            mouseBoard2 = cellValue2
            catBoard2 = cellValue2
            dogBoard2 = cellValue2
            wolfBoard2 = cellValue2
            pantherBoard2 = cellValue2
            tigerBoard2 = cellValue2
            lionBoard2 = cellValue2
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
                    elif animal.name == "WOLF":
                        value += wolfBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value += pantherBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value += tigerBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value += lionBoard1[animal.getX()][animal.getY()]
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
                    elif animal.name == "WOLF":
                        value += wolfBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value += pantherBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value += tigerBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value += lionBoard2[animal.getX()][animal.getY()]
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
                    elif animal.name == "WOLF":
                        value -= wolfBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value -= pantherBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value -= tigerBoard1[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value -= lionBoard1[animal.getX()][animal.getY()]
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
                    elif animal.name == "WOLF":
                        value -= wolfBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "PANTHER":
                        value -= pantherBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "TIGER":
                        value -= tigerBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "LION":
                        value -= lionBoard2[animal.getX()][animal.getY()]
                    elif animal.name == "ELEPHANT":
                        value -= elephantBoard2[animal.getX()][animal.getY()]
            totalValue += value

        return totalValue
