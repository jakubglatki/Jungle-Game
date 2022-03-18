from model.Animal import Animal
from model.Cell import Cell
from model.Player import Player


class Board:
    def __init__(self, isPlayer1Bot: bool, isPlayer2Bot: bool):
        # Generate the board
        self.player1 = Player(1)
        self.player2 = Player(2)
        if isPlayer1Bot==True: self.player1.switchToBot()
        if isPlayer2Bot==True: self.player2.switchToBot()

        m1 = Animal("rat", "M1", 1, self.player1, 6, 6)
        c1 = Animal("cat", "C1", 2, self.player1, 7, 1)
        d1 = Animal("dog", "D1", 3, self.player1, 7, 5)
        w1 = Animal("wolf", "W1", 4, self.player1, 6, 2)
        p1 = Animal("panther", "P1", 5, self.player1, 6, 4)
        t1 = Animal("tiger", "T1", 6, self.player1, 8, 0)
        l1 = Animal("lion", "L1", 7, self.player1, 8, 6)
        e1 = Animal("elephant", "E1", 8, self.player1, 6, 0)
        m2 = Animal("rat", "M2", 1, self.player2, 2, 0)
        c2 = Animal("cat", "C2", 2, self.player2, 1, 5)
        d2 = Animal("dog", "D2", 3, self.player2, 1, 1)
        w2 = Animal("wolf", "W2", 4, self.player2, 2, 4)
        p2 = Animal("panther", "P2", 5, self.player2, 2, 2)
        t2 = Animal("tiger", "T2", 6, self.player2, 0, 6)
        l2 = Animal("lion", "L2", 7, self.player2, 0, 0)
        e2 = Animal("elephant", "E2", 8, self.player2, 2, 6)

        self.Animals1 = [m1, c1, d1, w1, p1, t1, l1, e1]
        self.Animals2 = [m2, c2, d2, w2, p2, t2, l2, e2]

        self.player1.animalCollection = self.Animals1
        self.player2.animalCollection = self.Animals2

        self.matrix = [[Cell(1), Cell(1), Cell(5), Cell(6), Cell(5), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(5), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                       [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                       [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(3), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(3), Cell(4), Cell(3), Cell(1), Cell(1)]]
        # put the animals in their starting points
        self.matrix[2][0].animal = self.Animals2[0]
        self.matrix[1][5].animal = self.Animals2[1]
        self.matrix[1][1].animal = self.Animals2[2]
        self.matrix[2][4].animal = self.Animals2[3]
        self.matrix[2][2].animal = self.Animals2[4]
        self.matrix[0][6].animal = self.Animals2[5]
        self.matrix[0][0].animal = self.Animals2[6]
        self.matrix[2][6].animal = self.Animals2[7]

        self.matrix[6][6].animal = self.Animals1[0]
        self.matrix[7][1].animal = self.Animals1[1]
        self.matrix[7][5].animal = self.Animals1[2]
        self.matrix[6][2].animal = self.Animals1[3]
        self.matrix[6][4].animal = self.Animals1[4]
        self.matrix[8][0].animal = self.Animals1[5]
        self.matrix[8][6].animal = self.Animals1[6]
        self.matrix[6][0].animal = self.Animals1[7]

    def getDojo1(self):
        return self.matrix[8][3]

    def getDojo2(self):
        return self.matrix[0][3]

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2



    #def killAnimal(self, x1: int, y1: int):
    #    if (self.matrix[x1][y1].thereIsAnimal()):
    #        self.matrix[x1][y1].killAnimal()
