from model.Cell import Cell


class Board:
    def __init__(self, Animals1: list, Animals2: list):
        # Generate the board
        self.matrix = [[Cell(1), Cell(1), Cell(3), Cell(5), Cell(3), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(3), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                       [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                       [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(1), Cell(3), Cell(1), Cell(1), Cell(1)],
                       [Cell(1), Cell(1), Cell(3), Cell(4), Cell(3), Cell(1), Cell(1)]]
        # put the animals in their starting points
        self.matrix[2][0].animal = Animals2[0]
        self.matrix[1][5].animal = Animals2[1]
        self.matrix[1][1].animal = Animals2[2]
        self.matrix[2][4].animal = Animals2[3]
        self.matrix[2][2].animal = Animals2[4]
        self.matrix[0][6].animal = Animals2[5]
        self.matrix[0][0].animal = Animals2[6]
        self.matrix[2][6].animal = Animals2[7]

        self.matrix[6][6].animal = Animals1[0]
        self.matrix[7][1].animal = Animals1[1]
        self.matrix[7][5].animal = Animals1[2]
        self.matrix[6][2].animal = Animals1[3]
        self.matrix[6][4].animal = Animals1[4]
        self.matrix[8][0].animal = Animals1[5]
        self.matrix[8][6].animal = Animals1[6]
        self.matrix[6][0].animal = Animals1[7]

    def killAnimal(self, x1: int, y1: int):
        if (self.matrix[x1][y1].thereIsAnimal()):
            self.matrix[x1][y1].killAnimal()
