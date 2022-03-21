class Move:
    def __init__(self, startingX: int, startingY: int, endingX: int, endingY: int):
        self.startingX = startingX
        self.startingY = startingY
        self.endingX = endingX
        self.endingY = endingY

    def compareCouples(self, x1:int, y1:int, x2:int, y2:int):
        if self.startingX == x1 and self.startingY == y1 and self.startingX == x2 and self.startingY == y2: return True
        elif self.endingX == x1 and self.endingY == y1 and self.endingX == x2 and self.endingY == y2: return True
        return False





