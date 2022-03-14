from model.Cell import Cell


class Board:
    def __init__(self, Animals1: list, Animals2: list):
        #Generate the board
        self.matrix = [[Cell(1), Cell(1), Cell(3), Cell(5), Cell(3), Cell(1), Cell(1)],
                  [Cell(1), Cell(1), Cell(1), Cell(3), Cell(1), Cell(1), Cell(1)],
                  [Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1)],
                  [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                  [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                  [Cell(1), Cell(2), Cell(2), Cell(1), Cell(2), Cell(2), Cell(1)],
                  [Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1), Cell(1)],
                  [Cell(1), Cell(1), Cell(1), Cell(3), Cell(1), Cell(1), Cell(1)],
                  [Cell(1), Cell(1), Cell(3), Cell(4), Cell(3), Cell(1), Cell(1)]]
        #put the animals in their starting points
        self.matrix[0][3].Animal=Animals2[0]
        self.matrix[1][5].Animal=Animals2[1]
        self.matrix[1][1].Animal=Animals2[2]
        self.matrix[2][4].Animal=Animals2[3]
        self.matrix[2][2].Animal=Animals2[4]
        self.matrix[0][6].Animal=Animals2[5]
        self.matrix[0][0].Animal=Animals2[6]
        self.matrix[2][6].Animal=Animals2[7]

        self.matrix[6][6].Animal=Animals1[0]
        self.matrix[7][1].Animal=Animals1[1]
        self.matrix[7][5].Animal=Animals1[2]
        self.matrix[6][2].Animal=Animals1[3]
        self.matrix[6][4].Animal=Animals1[4]
        self.matrix[8][0].Animal=Animals1[5]
        self.matrix[8][6].Animal=Animals1[6]
        self.matrix[6][0].Animal=Animals1[7]
