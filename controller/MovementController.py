from model.Animal import Animal
from model.Board import Board


class MovementController:

    def killAnimal(self, board: Board, x: int, y: int):
        if board.matrix[x][y].animal != None:
            board.matrix[x][y].animal.player.alive = board.matrix[x][y].animal.player.alive - 1
            board.matrix[x][y].animal.isAlive = False
            board.matrix[x][y].animal.x = -1
            board.matrix[x][y].animal.y = -1

    def moveAnimal(self, animal: Animal, board: Board, x: int, y: int):
        board.matrix[int(animal.x)][int(animal.y)].animal = None
        board.matrix[x][y].animal = animal
        animal.x = x
        animal.y = y
