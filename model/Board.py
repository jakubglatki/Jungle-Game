from model.Animal import Animal
from model.Cell import Cell
from model.Player import Player


class Board:
    def __init__(self, isPlayer1Bot: bool, isPlayer2Bot: bool):
        # Generate the board

            self.player1 = Player(1)
            self.player2 = Player(2)
            if isPlayer1Bot == True: self.player1.switchToBot()
            if isPlayer2Bot == True: self.player2.switchToBot()

            m1 = Animal("MOUSE", "M1", 1, self.player1, 4, 4)
            c1 = Animal("CAT", "C1", 2, self.player1, 5, 3)
            d1 = Animal("DOG", "D1", 3, self.player1, 5, 1)
            e1 = Animal("ELEPHANT", "E1", 8, self.player1, 4,0)
            m2 = Animal("MOUSE", "M2", 1, self.player2, 2, 0)
            c2 = Animal("CAT", "C2", 2, self.player2, 1, 3)
            d2 = Animal("DOG", "D2", 3, self.player2, 1, 1)
            e2 = Animal("ELEPHANT", "E2", 8, self.player2, 2, 4)

            self.Animals1 = [e1, d1, c1, m1]
            self.Animals2 = [e2, d2, c2, m2]

            self.player1.animalCollection = self.Animals1
            self.player2.animalCollection = self.Animals2

            self.matrix = [[Cell(1),  Cell(5), Cell(6), Cell(5), Cell(1)],
                           [Cell(1),  Cell(1), Cell(5), Cell(1), Cell(1)],
                           [Cell(1),  Cell(1), Cell(1), Cell(1), Cell(1)],
                           [Cell(1),  Cell(2), Cell(1), Cell(2), Cell(1)],
                           [Cell(1),  Cell(1), Cell(1), Cell(1),  Cell(1)],
                           [Cell(1),  Cell(1), Cell(3), Cell(1),  Cell(1)],
                           [Cell(1),  Cell(3), Cell(4), Cell(3),  Cell(1)]]
            # put the animals in their starting points
            self.matrix[2][0].animal = self.Animals2[3]
            self.matrix[1][3].animal = self.Animals2[2]
            self.matrix[1][1].animal = self.Animals2[1]
            self.matrix[2][4].animal = self.Animals2[0]

            self.matrix[4][4].animal = self.Animals1[3]
            self.matrix[5][3].animal = self.Animals1[2]
            self.matrix[5][1].animal = self.Animals1[1]
            self.matrix[4][0].animal = self.Animals1[0]


    def getDojo1(self):
        return self.matrix[6][2]

    def getDojo2(self):
        return self.matrix[0][2]

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

    def isMenaced(self, animal: Animal):
        x = animal.getX()
        y = animal.getY()
        if x != 0 and self.matrix[x - 1][y].thereIsAnimal() and self.matrix[x - 1][
            y].animal.player != animal.player and (
                self.matrix[x - 1][y].animal.power >= animal.power or animal.inOpponentDojo()): return True
        if x + 1 != len(self.matrix) and self.matrix[x + 1][y].thereIsAnimal() and self.matrix[x + 1][
            y].animal.player != animal.player and (
                self.matrix[x + 1][y].animal.power >= animal.power or animal.inOpponentDojo()): return True
        if y != 0 and self.matrix[x][y - 1].thereIsAnimal() and self.matrix[x][
            y - 1].animal.player != animal.player and (
                self.matrix[x][y - 1].animal.power >= animal.power or animal.inOpponentDojo()): return True
        if y + 1 != len(self.matrix[0]) and self.matrix[x][y + 1].thereIsAnimal() and self.matrix[x][
            y + 1].animal.player != animal.player and (
                self.matrix[x][y + 1].animal.power >= animal.power or animal.inOpponentDojo()): return True
        return False
