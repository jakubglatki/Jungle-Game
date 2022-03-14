class Player:
    def __init__(self, number: int, AnimalCollection: list, robot: str):
        self.number = number
        self.alive = 8
        if (robot=="IA"):
            self.isARobot=True
        else: self.isABot=False




