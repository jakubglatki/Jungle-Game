from model.Animal import Animal


class Cell:
    def __init__(self, kind):
        self.kind = kind
        # 1: grass - 2: water - 3: traps - 4: dojo1 - 5: dojo2

    animal = None

    def addAnimal(self, animal: Animal):
        self.animal = animal

    def removeAnimal(self):
        self.animal = None

    def thereIsAnimal(self):
        if (self.animal != None):
            return True
        else:
            return False

    def killAnimal(self):
        self.animal.x = -1
        self.animal.y = -1
        self.animal.isAlive = False
        self.animal.player.alive = self.animal.player.alive - 1
