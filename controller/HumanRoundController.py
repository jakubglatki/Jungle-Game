from model.Animal import Animal
from model.Player import Player
from model.Board import Board
from controller.MovementController import MovementController


def mouseMovementEndingPoint(animal, board, x, y, startingX, startingY):
    if (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
        if board.matrix[x][y].thereIsAnimal():
            if board.matrix[x][y].animal.power == 8 or animal.power >= board.matrix[x][y].animal.power:
                if board.matrix[startingX][startingY].kind == 2:
                    if board.matrix[x][y].kind == 2:
                        return True
                    else:
                        return False
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


def isValidEndingPoint(animal: Animal, board: Board, x: int, y: int, startingX: int, startingY: int):
    specialMovementAnimals = [1, 6, 7]
    if x <= len(board.matrix) and y <= len(board.matrix[0]):
        if (animal.player.number == 1 and board.matrix[x][y].kind != 4) or (
                animal.player.number == 2 and board.matrix[x][y].kind != 5):
            if board.matrix[x][y].thereIsAnimal():
                if animal.player != board.matrix[x][y].animal.player:
                    if animal.power not in specialMovementAnimals:
                        if (x + 1 == startingX or x - 1 == startingX) is not (y + 1 == startingY or y - 1 == startingY):
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


def isValidStartingPoint(player: Player, board: Board, x: int, y: int):
    if board.matrix[x][y].thereIsAnimal():
        if player == board.matrix[x][y].animal.player:
            return True
    return False


class HumanRoundController:
    movementController = MovementController()

    def round(self, player: Player, board: Board):
        # first while for choosing a valid starting point
        movementController = MovementController()
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1
        tempAnimal = None
        flag = False
        while (flag == False):
            print("select starting point of your move: ")
            sp = str(input())
            # sp = "a7"
            x1 = int(sp[1]) - 1
            y1 = ord(sp[0].lower()) - 97
            if (isValidStartingPoint(player, board, x1,
                                     y1)):  # In this test we see if in the selected area there is one of your animal and if he can move
                tempAnimal = board.matrix[x1][y1].animal
                flag = True
            else:
                print("You did not choose a valid starting point. The starting point has to contain your animal.")
        # second while for chosing a valid ending point
        flag = False
        while (flag == False):
            print("select ending point of your move: ")
            ep = str(input())
            # ep="a6"
            x2 = int(ep[1]) - 1
            y2 = ord(ep[0].lower()) - 97
            if (isValidEndingPoint(tempAnimal, board, x2,
                                   y2, x1,
                                   y1)):  # In this test we see if: the animal can go there, if there is another weaker opponent animal (in case of one of yours or in case of stronger you can't), if there is some special rule applied
                flag = True
            else:
                print("The selected ending point is incorrect.")

        # The movement is valid, now we have just to make it and verify if, at the end of the movement, the player have eaten something off the other one
        # In case in the ending point there is another animal, kill it
        movementController.killAnimal(board, x2, y2)
        movementController.moveAnimal(tempAnimal, board, x2,
                                      y2)  # to do, simply move the animal from (x1,y1) to (x2,y2)
