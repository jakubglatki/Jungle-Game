from model.Animal import Animal
from model.Board import Board


class MovementController:

    def killAnimal(self, board: Board, x: int, y: int):
        if board.matrix[x][y].thereIsAnimal():
            board.matrix[x][y].animal.player.decreaseNumberOfAnimal()
            board.matrix[x][y].animal.kill()

    def moveAnimal(self, animal: Animal, board: Board, x: int, y: int):
        board.matrix[animal.getX()][animal.getY()].removeAnimal()
        board.matrix[x][y].addAnimal(animal)
        animal.move(x, y)
