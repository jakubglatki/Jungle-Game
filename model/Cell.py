class Cell:
    def __init__(self,kind):
        self.kind = kind
        # 1: grass - 2: water - 3: traps - 4: dojo1 - 5: dojo2
    Animal = None
    def addAnimal(self,Animal: Animal):
        self.Animal = Animal
    def removeAnimal(self):
        self.Animal = None
    def thereIsAnimal(self):
        if(self.Animal!=None): return True
        else: return False

    def killAnimal(self):
        self.Animal.x=-1
        self.Animal.y=-1
        self.Animal.isAlive=False
        self.Animal.player.alive=self.Animal.player.alive-1
