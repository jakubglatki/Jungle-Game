class Player:
    def __init__(self, number: int, robot: str):
        self.number = number
        self.alive = 8
        if robot == "IA":
            self.isABot = True
        else:
            self.isABot = False
        self.animalCollection = None

    def decreaseNumberOfAnimal(self):
        self.alive = self.alive - 1
