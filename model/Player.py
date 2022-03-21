from model.LastMoves import LastMoves


class Player:
    def __init__(self, number: int):
        self.number = number
        self.alive = 8
        self.animalCollection = None
        self.isABot = False
        self.lastMoves = LastMoves()

    def decreaseNumberOfAnimal(self):
        self.alive = self.alive - 1

    def switchToBot(self):
        self.isABot = True
