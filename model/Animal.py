from Game.Player import Player

class Animal:
    def __init__(self,name: str, fieldName: str, power: int,player: Player, x: int, y: int):
        self.name = name
        self.fieldName = fieldName
        self.power = power
        self.player = player
        self.x = x
        self.y = y
        self.isAlive = True
