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

cellValueWolf1 = [[5, 13, 50, math.inf, 50, 13, 5],
                  [11, 12, 13, 50, 13, 12, 11],
                  [10, 11, 12, 13, 12, 11, 10],
                  [9, 0, 0, 12, 0, 0, 9],
                  [8, 0, 0, 11, 0, 0, 8],
                  [7, 0, 0, 10, 0, 0, 7],
                  [5, 5, 5, 7, 5, 5, 5],
                  [4, 5, 9, 6, 9, 5, 4],
                  [0, 8, 4, 0, 4, 8, 0]]

cellValueWolf2 = [[0, 8, 4, 0, 4, 8, 0],
                  [4, 5, 9, 6, 9, 5, 4],
                  [5, 5, 5, 7, 5, 5, 5],
                  [7, 0, 0, 10, 0, 0, 7],
                  [8, 0, 0, 11, 0, 0, 8],
                  [9, 0, 0, 12, 0, 0, 9],
                  [10, 11, 12, 13, 12, 11, 10],
                  [11, 12, 13, 50, 13, 12, 11],
                  [5, 13, 50, math.inf, 50, 13, 5]]

cellValuePanther1 = [[10, 14, 50, math.inf, 50, 14, 10],
                     [12, 13, 14, 50, 14, 13, 12],
                     [11, 12, 13, 14, 13, 12, 11],
                     [10, 0, 0, 12, 0, 0, 10],
                     [9, 0, 0, 11, 0, 0, 9],
                     [8, 0, 0, 10, 0, 0, 8],
                     [6, 4, 4, 7, 4, 4, 6],
                     [3, 4, 5, 4, 5, 4, 3],
                     [0, 5, 3, 0, 3, 5, 0]]

cellValuePanther2 = [[0, 5, 3, 0, 3, 5, 0],
                     [3, 4, 5, 4, 5, 4, 3],
                     [6, 4, 4, 7, 4, 4, 6],
                     [8, 0, 0, 10, 0, 0, 8],
                     [9, 0, 0, 11, 0, 0, 9],
                     [10, 0, 0, 12, 0, 0, 10],
                     [11, 12, 13, 14, 13, 12, 11],
                     [12, 13, 14, 50, 14, 13, 12],
                     [10, 14, 50, math.inf, 50, 14, 10]]

cellValueTiger1 = [[11, 15, 50, math.inf, 50, 15, 11],
                   [14, 15, 16, 50, 16, 15, 14],
                   [13, 14, 15, 15, 15, 14, 13],
                   [12, 0, 0, 11, 0, 0, 12],
                   [11, 0, 0, 10, 0, 0, 11],
                   [10, 0, 0, 11, 0, 0, 10],
                   [6, 10, 10, 9, 10, 10, 6],
                   [2, 3, 4, 2, 4, 3, 2],
                   [0, 3, 2, 0, 2, 3, 0]]

cellValueTiger2 = [[0, 3, 2, 2, 2, 3, 0],
                   [2, 3, 5, 2, 5, 3, 2],
                   [6, 10, 10, 9, 10, 10, 6],
                   [10, 0, 0, 11, 0, 0, 10],
                   [11, 0, 0, 12, 0, 0, 11],
                   [12, 0, 0, 13, 0, 0, 12],
                   [13, 14, 15, 15, 15, 14, 13],
                   [14, 15, 16, 50, 16, 15, 14],
                   [11, 15, 50, math.inf, 50, 15, 11]]

cellValueLion1 = [[11, 15, 50, math.inf, 50, 15, 11],
                  [14, 15, 16, 50, 16, 15, 14],
                  [13, 14, 15, 15, 15, 14, 13],
                  [12, 0, 0, 13, 0, 0, 12],
                  [11, 0, 0, 12, 0, 0, 11],
                  [10, 0, 0, 11, 0, 0, 10],
                  [6, 10, 10, 9, 10, 10, 6],
                  [2, 3, 4, 2, 4, 3, 2],
                  [0, 3, 2, 0, 2, 3, 0]]

cellValueLion2 = [[0, 3, 2, 0, 2, 3, 0],
                  [2, 3, 4, 2, 4, 3, 2],
                  [6, 10, 10, 9, 10, 10, 6],
                  [10, 0, 0, 11, 0, 0, 10],
                  [11, 0, 0, 10, 0, 0, 11],
                  [12, 0, 0, 11, 0, 0, 12],
                  [13, 14, 15, 15, 15, 14, 13],
                  [14, 15, 16, 50, 16, 15, 14],
                  [11, 15, 50, math.inf, 50, 15, 11]]


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

hardCellValueMouse1 = [[11, 13, 50, math.inf, 50, 13, 13],
                       [11, 12, 13, 50, 13, 13, 13],
                       [10, 11, 11, 13, 13, 13, 13],
                       [8, 9, 9, 11, 12, 12, 13],
                       [8, 9, 9, 11, 12, 12, 12],
                       [8, 9, 9, 10, 12, 12, 11],
                       [8, 8, 8, 9, 10, 10, 10],
                       [8, 8, 8, 9, 9, 9, 9],
                       [8, 8, 8, 0, 8, 8, 8]]

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

hardCellValuePanther1 = [[14, 15, 50, math.inf, 50, 15, 14],
                         [13, 14, 15, 50, 15, 14, 13],
                         [13, 13, 14, 15, 14, 13, 13],
                         [12, 0, 0, 15, 0, 0, 12],
                         [11, 0, 0, 14, 0, 0, 11],
                         [10, 0, 0, 13, 0, 0, 10],
                         [9, 9, 9, 10, 10, 9, 9],
                         [9, 9, 9, 9, 9, 9, 9],
                         [9, 9, 9, 0, 9, 9, 9]]

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

hardCellValueLion1 = [[25, 30, 50, math.inf, 50, 30, 25],
                      [25, 25, 30, 50, 30, 25, 25],
                      [18, 20, 20, 30, 20, 20, 18],
                      [15, 0, 0, 15, 0, 0, 15],
                      [15, 0, 0, 15, 0, 0, 15],
                      [15, 0, 0, 15, 0, 0, 15],
                      [14, 16, 16, 14, 16, 16, 14],
                      [12, 12, 12, 12, 12, 14, 12],
                      [10, 12, 12, 0, 12, 12, 10]]

hardCellValueLion2 = list(reversed(hardCellValueLion1))

hardCellValueElephant1 = [[25, 30, 50, math.inf, 50, 30, 25],
                          [25, 25, 30, 50, 30, 25, 25],
                          [18, 20, 20, 30, 20, 20, 18],
                          [16, 0, 0, 16, 0, 0, 16],
                          [14, 0, 0, 14, 0, 0, 14],
                          [12, 0, 0, 12, 0, 0, 12],
                          [10, 15, 14, 14, 14, 14, 12],
                          [11, 11, 11, 11, 11, 11, 11],
                          [11, 11, 11, 0, 11, 11, 11]]

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
        elif difficulty == 3:
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
