from model.Player import Player


class Animal:
    def __init__(self,name: str, fieldName: str, power: int,player: Player, x: int, y: int):
        self.name = name
        self.fieldName = fieldName
        self.power = power
        self.player = player
        self.x = x
        self.y = y
        self.isAlive = True

    def kill(self):
        self.x = -1
        self.y = -1
        self.isAlive = False

    def move(self, x:int, y:int):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def isMe(self, name: str):
        name = name.upper()
        if self.fieldName == name or self.name == name or self.fieldName[0] == name:
            return True
        return False

    def inOpponentDojo(self):
        if self.player.number==1:
            if self.x == 0 and (self.y == 2 or self.y == 4): return True
            elif self.x == 1 and self.y == 3: return True
        else:
            if self.x == 8 and (self.y == 2 or self.y == 4): return True
            elif self.x == 7 and self.y == 3: return True
        return False


