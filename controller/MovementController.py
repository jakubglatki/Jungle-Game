from controller.MovementValidationController import checkIfIsWalkingIntoOwnTrap, specialMovementAnimalsEndingPoint
from model.Animal import Animal
from model.Board import Board


class MovementController:

    def killAnimal(self, board: Board, x: int, y: int):
        if board.matrix[x][y].thereIsAnimal():
            board.matrix[x][y].animal.player.decreaseNumberOfAnimal()
            board.matrix[x][y].animal.kill()

    def moveAnimal(self, animal: Animal, board: Board, x: int, y: int):
        self.killAnimal(board, x, y)
        board.matrix[animal.getX()][animal.getY()].removeAnimal()
        board.matrix[x][y].addAnimal(animal)
        animal.move(x, y)

    def calculateMove(self, animal: Animal, board: Board, string: str):
        string = string.lower()
        x = -1; y = -1
        if string == "u": x = animal.getX()-1; y = animal.getY()
        if string == "r": x = animal.getX(); y = animal.getY()+1
        if string == "l": x = animal.getX(); y = animal.getY()-1
        if string == "d": x = animal.getX()+1; y = animal.getY()
        specialMovementAnimals = [1, 7]
        if x < len(board.matrix) and x >= 0 and y < len(board.matrix[0]) and y >= 0:
            if checkIfIsWalkingIntoOwnTrap(animal, board, x, y, animal.getX(), animal.getY()):
                return str(x)+str(y)
            elif (animal.player.number == 1 and board.matrix[x][y].kind != 4) or (
                    animal.player.number == 2 and board.matrix[x][y].kind != 6):
                if board.matrix[x][y].thereIsAnimal():
                    if animal.player != board.matrix[x][y].animal.player:
                        if animal.power not in specialMovementAnimals:
                            if (x + 1 == animal.getX() or x - 1 == animal.getX()) is not (
                                    y + 1 == animal.getY() or y - 1 == animal.getY()):
                                if board.matrix[x][y].kind != 2:  # water
                                    if animal.power >= board.matrix[x][y].animal.power:
                                        return str(x)+str(y)
                        else:
                            #In case of jump
                            if animal.power == 6 or animal.power == 7:
                                if board.matrix[x][y].kind==2: #he is going into the water
                                    if string == "u": x = x-3
                                    if string == "d": x = x+3
                                    if string == "l": y = y-2
                                    if string == "r": y = y+2
                            if specialMovementAnimalsEndingPoint(animal, board, x, y, animal.getX(), animal.getY()): return str(x)+str(y)
                elif animal.power not in specialMovementAnimals:
                    if (x + 1 == animal.getX() or x - 1 == animal.getX()) is not (y + 1 == animal.getY() or y - 1 == animal.getY()):
                        if board.matrix[x][y].kind != 2:  # water
                            return str(x)+str(y)
                else:
                    #In case of jump
                    if animal.power == 6 or animal.power == 7:
                        if board.matrix[x][y].kind==2: #he is going into the water
                            if string == "u": x = x-3
                            if string == "d": x = x+3
                            if string == "l": y = y-2
                            if string == "r": y = y+2
                    if specialMovementAnimalsEndingPoint(animal, board, x, y, animal.getX(), animal.getY()): return str(x)+str(y)

        return None

