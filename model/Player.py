from model.LastMoves import LastMoves


class Player:
    def __init__(self, number: int, difficulty=3):
        self.difficulty = difficulty
        self.number = number
        self.alive = 8
        self.animalCollection = None
        self.isABot = False
        self.lastMoves = LastMoves()
        self.clock = 0
        self.nclock = 0
        self.victories = 0

    def decreaseNumberOfAnimal(self):
        self.alive = self.alive - 1

    def switchToBot(self):
        self.isABot = True

    def showTimeInfo(self):
        print("Player " +str(self.number)+ " average time of a turn: "+str(self.clock/self.nclock))
