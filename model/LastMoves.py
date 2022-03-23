from model.Move import Move


class LastMoves:
    def __init__(self, n = None):
        if n == None: self.n = 5 #save the last 5 moves
        else: self.n = n
        self.actual = 0
        self.list = []
        self.max = 0

    def addValue(self,move: Move):
        self.list.append(Move(move.endingX, move.endingY, move.startingX, move.startingY,move.animal))
        if self.actual == self.n: self.list.pop(0)
        else: self.actual = self.actual + 1

    def push(self, move: Move):
        self.list.append(move)
        self.actual = self.actual + 1

    def pop(self):
        self.actual = self.actual - 1
        self.list.pop(self.actual)

    def isARecentMove(self, m : Move):
        for move in self.list:
            if move.animal == m.animal and move.compareCouples(m.startingX,m.startingY,m.endingX,m.endingY):
                return True
        return False


