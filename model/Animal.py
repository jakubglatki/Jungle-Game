from Game.Player import Player


class Animal:
    def __init__(self,name: str,power: int,player: Player, x: int, y: int):
        self.name = name
        self.power = power
        self.player = player
        self.x = x
        self.y = y
        self.isAlive = True



