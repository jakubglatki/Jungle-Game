from model.Animal import Animal
from model.Board import Board
from model.Player import Player


def mouseMovementEndingPoint(animal, board, x, y, startingX, startingY):
    if (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
        if board.matrix[x][y].thereIsAnimal():
            if board.matrix[x][y].animal.power == 8:
                if board.matrix[startingX][startingY].kind == 2:
                    if board.matrix[x][y].kind == 2:
                        return True
                    else:
                        return False
            elif animal.power >= board.matrix[x][y].animal.power:
                return True
            else:
                return False
    else:
        return False
    return True


def checkIfThereIsAnimalBlockingWay(animal, board, x, y):
    if board.matrix[x][y].thereIsAnimal():
        if animal.power >= board.matrix[x][y].animal.power:
            return True
    else:
        return True
    return False


def checkIfThereIsMouseBlockingJump(board: Board, x: int, y: int, isHorizontal: bool):
    blockingMouse = False
    if isHorizontal:
        for i in range(x + 1, x + 4):
            if board.matrix[i][y].thereIsAnimal():
                blockingMouse = True
    else:
        for i in range(y + 1, y + 3):
            if board.matrix[x][i].thereIsAnimal():
                blockingMouse = True
    return blockingMouse


def lionTigerWaterInteractionEndingPoint(animal, board, x, y, startingX, startingY):
    if board.matrix[startingX + 1][startingY].kind == 2 and x == startingX + 4:
        if not checkIfThereIsMouseBlockingJump(board, startingX, startingY, True):
            return checkIfThereIsAnimalBlockingWay(animal, board, x, y)
    elif board.matrix[startingX - 1][startingY].kind == 2 and x == startingX - 4:
        if not checkIfThereIsMouseBlockingJump(board, startingX - 4, startingY, True):
            return checkIfThereIsAnimalBlockingWay(animal, board, x, y)
    elif board.matrix[startingX][startingY + 1].kind == 2 and y == startingY + 3:
        if not checkIfThereIsMouseBlockingJump(board, startingX, startingY, False):
            return checkIfThereIsAnimalBlockingWay(animal, board, x, y)
    elif board.matrix[startingX][startingY - 1].kind == 2 and y == startingY - 3:
        if not checkIfThereIsMouseBlockingJump(board, startingX - 4, startingY, False):
            return checkIfThereIsAnimalBlockingWay(animal, board, x, y)


def checkIfIsNotNextToWater(board: Board, startingX: int, startingY: int):
    if startingX == 0 and startingY == 0:
        if board.matrix[startingX + 1][startingY].kind != 2 and board.matrix[startingX][startingY + 1].kind != 2:
            return True
    elif startingX == 0 and startingY + 1 == len(board.matrix[0]):
        if board.matrix[startingX + 1][startingY].kind != 2 and board.matrix[startingX][startingY - 1].kind != 2:
            return True
    elif startingX + 1 == len(board.matrix) and startingY == 0:
        if board.matrix[startingX - 1][startingY].kind != 2 and board.matrix[startingX][startingY + 1].kind != 2:
            return True
    elif startingX + 1 == len(board.matrix) and startingY + 1 == len(board.matrix[0]):
        if board.matrix[startingX - 1][startingY].kind != 2 and board.matrix[startingX][startingY - 1].kind != 2:
            return True
    elif startingX == 0:
        if board.matrix[startingX + 1][startingY].kind != 2 and (
                board.matrix[startingX][startingY + 1].kind != 2 and board.matrix[startingX][startingY - 1].kind != 2):
            return True
    elif startingX + 1 == len(board.matrix):
        if board.matrix[startingX - 1][startingY].kind != 2 and (
                board.matrix[startingX][startingY + 1].kind != 2 and board.matrix[startingX][startingY - 1].kind != 2):
            return True
    elif startingY == 0:
        if (board.matrix[startingX + 1][startingY].kind != 2 and board.matrix[startingX - 1][startingY].kind != 2) and \
                board.matrix[startingX][startingY + 1].kind != 2:
            return True
    elif startingY + 1 == len(board.matrix[0]):
        if (board.matrix[startingX + 1][startingY].kind != 2 and board.matrix[startingX - 1][startingY].kind != 2) and \
                board.matrix[startingX][startingY - 1].kind != 2:
            return True
    else:
        return False


def validLionTigerMoveWithoutJumping(animal: Animal, board: Board, x: int, y: int, startingX: int, startingY: int):
    if board.matrix[x][y].thereIsAnimal():
        if animal.power >= board.matrix[x][y].animal.power:
            return True
    else:
        return True
    return False


def lionTigerMovementEndingPoint(animal, board, x, y, startingX, startingY):
    if checkIfIsNotNextToWater(board, startingX, startingY):
        if (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
            return validLionTigerMoveWithoutJumping(animal, board, x, y, startingX, startingY)
    elif (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
        return validLionTigerMoveWithoutJumping(animal, board, x, y, startingX, startingY)
    else:
        return lionTigerWaterInteractionEndingPoint(animal, board, x, y, startingX, startingY)
    return False


def specialMovementAnimalsEndingPoint(animal, board, x, y, startingX, startingY):
    if animal.power == 1:
        return mouseMovementEndingPoint(animal, board, x, y, startingX, startingY)
    else:
        return lionTigerMovementEndingPoint(animal, board, x, y, startingX, startingY)


def checkIfIsWalkingIntoOwnTrap(animal, board, x, y, startingX, startingY):
    if (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
        if (animal.player.number == 1 and board.matrix[x][y].kind == 3) or (
                animal.player.number == 2 and board.matrix[x][y].kind == 5):
            return True
    return False


class MovementValidationController:

    def isValidStartingPoint(self, player: Player, board: Board, x: int, y: int):
        if board.matrix[x][y].thereIsAnimal():
            if player == board.matrix[x][y].animal.player:
                if self.checkIfAnimalHasAnyViableMoves(board.matrix[x][y].animal, board, x, y):
                    return True
        return False

    def isValidEndingPoint(self, animal: Animal, board: Board, x: int, y: int, startingX: int, startingY: int):
        specialMovementAnimals = [1, 6, 7]
        if len(board.matrix) > x >= 0 and y < len(board.matrix[0]) and y >= 0:
            if checkIfIsWalkingIntoOwnTrap(animal, board, x, y, startingX, startingY):
                return True
            if (animal.player.number == 1 and board.matrix[x][y].kind != 4) or (
                    animal.player.number == 2 and board.matrix[x][y].kind != 6):
                if board.matrix[x][y].thereIsAnimal():
                    if animal.player != board.matrix[x][y].animal.player:
                        if animal.power not in specialMovementAnimals:
                            if (x + 1 == startingX or x - 1 == startingX) is not (
                                    y + 1 == startingY or y - 1 == startingY):
                                if board.matrix[x][y].kind != 2:  # water
                                    if animal.power >= board.matrix[x][y].animal.power:
                                        return True
                        else:
                            return specialMovementAnimalsEndingPoint(animal, board, x, y, startingX, startingY)
                elif animal.power not in specialMovementAnimals:
                    if (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
                        if board.matrix[x][y].kind != 2:  # water
                            return True
                else:
                    return specialMovementAnimalsEndingPoint(animal, board, x, y, startingX, startingY)

        return False

    def checkIfAnimalHasAnyViableMoves(self, animal: Animal, board: Board, x: int, y: int):
        if x == 0 and y == 0:
            if self.isValidEndingPoint(animal, board, x + 1, y, x, y) or self.isValidEndingPoint(animal, board, x, y + 1, x, y):
                return True
        elif x == 0 and y + 1 == len(board.matrix[0]):
            if self.isValidEndingPoint(animal, board, x + 1, y, x, y) or self.isValidEndingPoint(animal, board, x, y - 1, x, y):
                return True
        elif x + 1 == len(board.matrix) and y == 0:
            if self.isValidEndingPoint(animal, board, x - 1, y, x, y) or self.isValidEndingPoint(animal, board, x, y + 1, x, y):
                return True
        elif x + 1 == len(board.matrix) and y + 1 == len(board.matrix[0]):
            if self.isValidEndingPoint(animal, board, x - 1, y, x, y) or self.isValidEndingPoint(animal, board, x, y - 1, x, y):
                return True
        elif x == 0:
            if self.isValidEndingPoint(animal, board, x + 1, y, x, y) or self.isValidEndingPoint(animal, board, x, y - 1, x, y)\
                    or self.isValidEndingPoint(animal, board, x, y + 1, x, y):
                return True
        elif x + 1 == len(board.matrix):
            if self.isValidEndingPoint(animal, board, x - 1, y, x, y) or self.isValidEndingPoint(animal, board, x, y - 1, x, y)\
                    or self.isValidEndingPoint(animal, board, x, y + 1, x, y):
                return True
        elif y == 0:
            if self.isValidEndingPoint(animal, board, x + 1, y, x, y) or self.isValidEndingPoint(animal, board, x - 1, y, x, y)\
                    or self.isValidEndingPoint(animal, board, x, y + 1, x, y):
                return True
        elif y + 1 == len(board.matrix[0]):
            if self.isValidEndingPoint(animal, board, x + 1, y, x, y) or self.isValidEndingPoint(animal, board, x - 1, y, x, y)\
                    or self.isValidEndingPoint(animal, board, x, y - 1, x, y):
                return True
        else:
            if self.isValidEndingPoint(animal, board, x + 1, y, x, y) or self.isValidEndingPoint(animal, board, x - 1, y, x, y)\
                    or self.isValidEndingPoint(animal, board, x, y + 1, x, y) or self.isValidEndingPoint(animal, board, x, y - 1, x, y):
                return True
        return False
