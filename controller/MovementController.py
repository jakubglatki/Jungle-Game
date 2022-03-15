from model.Animal import Animal
from model.Board import Board


class MovementController:

    def killAnimal(self, board: Board, x: int, y: int):
        if board.matrix[x][y].Animal != None:
            board.matrix[x][y].Animal.player.alive = board.matrix[x][y].Animal.player.alive - 1
            board.matrix[x][y].Animal.isAlive = False
            board.matrix[x][y].Animal.x = -1
            board.matrix[x][y].Animal.y = -1

    def moveAnimal(self, animal: Animal, board: Board, x: int, y: int):
        board.matrix[int(animal.x)][int(animal.y)].Animal = None
        board.matrix[x][y].Animal = animal
        animal.x = x
        animal.y = y
