from model.Board import Board


class BoardViewer:
    ROWS = 9
    COLUMNS = 7

    def __init__(self, board: Board):
        self.board = board

    def showBoard(self):
        boardView = ""
        for index1, row in enumerate(reversed(self.board.matrix)):
            for index2, cell in enumerate(row):
                boardView += self.putAnimalOnBoard(index1, index2, cell)
            boardView += "  " + str(index1 + 1)
            boardView += "\n"
        boardView += "\n A   B   C   D   E \n"
        print(boardView)
        return boardView

    def putAnimalOnBoard(self, x: int, y: int, cell):
        if self.board.matrix[x][y].animal is not None:
            return " " + self.board.matrix[x][y].animal.fieldName + " "
        else:
            return " XX " if cell.kind == 1 else " ~~ " if cell.kind == 2 else " ## " \
                if (cell.kind == 3 or cell.kind == 5) else " ** "
