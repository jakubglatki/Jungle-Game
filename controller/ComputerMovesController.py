from controller.MovementController import MovementController
from controller.MovementValidationController import MovementValidationController
from model.Animal import Animal
from model.Board import Board
from model.Player import Player


def checkViableMovesOfAnimal(animal: Animal, board: Board, x: int, y: int,
                             movementValidationController: MovementValidationController,
                             movementController: MovementController):
    validMoves = []
    if x == 0 and y == 0:
        if movementValidationController.isValidEndingPoint(animal, board, x + 1, y, x, y):
            validMoves += [movementController.moveAnimal(animal, board, x + 1, y),
        if movementValidationController.isValidEndingPoint(animal, board, x, y + 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y + 1)
        return validMoves
    elif x == 0 and y + 1 == len(board.matrix[0]):
        if movementValidationController.isValidEndingPoint(animal, board, x + 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x + 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y - 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y - 1)
            return validMoves
    elif x + 1 == len(board.matrix) and y == 0:
        if movementValidationController.isValidEndingPoint(animal, board, x - 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x - 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y + 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y + 1)
        return validMoves
    elif x + 1 == len(board.matrix) and y + 1 == len(board.matrix[0]):
        if movementValidationController.isValidEndingPoint(animal, board, x - 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x - 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y - 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y - 1)
        return validMoves
    elif x == 0:
        if movementValidationController.isValidEndingPoint(animal, board, x + 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x + 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y + 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y + 1)
        if movementValidationController.isValidEndingPoint(animal, board, x, y - 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y - 1)
        return validMoves
    elif x + 1 == len(board.matrix):
        if movementValidationController.isValidEndingPoint(animal, board, x - 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x - 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y + 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y + 1)
        if movementValidationController.isValidEndingPoint(animal, board, x, y - 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y - 1)
        return validMoves
    elif y == 0:
        if movementValidationController.isValidEndingPoint(animal, board, x + 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x + 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x - 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x - 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y + 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y + 1)
        return validMoves
    elif y + 1 == len(board.matrix[0]):
        if movementValidationController.isValidEndingPoint(animal, board, x + 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x + 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x - 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x - 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y - 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y - 1)
        return validMoves
    else:
        if movementValidationController.isValidEndingPoint(animal, board, x + 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x + 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x - 1, y, x, y):
            validMoves += movementController.moveAnimal(animal, board, x - 1, y)
        if movementValidationController.isValidEndingPoint(animal, board, x, y + 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y + 1)
        if movementValidationController.isValidEndingPoint(animal, board, x, y - 1, x, y):
            validMoves += movementController.moveAnimal(animal, board, x, y - 1)
        return validMoves


class ComputerMovesController:
    movementValidationController = MovementValidationController()
    movementController = MovementController()

    def listOfPossibleMoves(self, player: Player, board: Board):
        directions = ['u','d','l','r']
        viableMoves = []
        for animal in player.animalCollection:
            if animal.isAlive:
                for direction in directions:
                    if self.movementController.calculateMove(animal, board, direction) is not None:
                        return
                viableMoves += checkViableMovesOfAnimal(animal, board, animal.x, animal.y, self.movementValidationController, self.movementController)
        return viableMoves
