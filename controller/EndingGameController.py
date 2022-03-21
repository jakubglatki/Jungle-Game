from controller.MovementValidationController import MovementValidationController
from model.Board import Board
from model.Player import Player

WON_THE_GAME_1 = "Player 1 has won the game!"
WON_THE_GAME_2 = "Player 2 has won the game!"
WON_THE_GAME_1_NO_ANIMALS = WON_THE_GAME_1 + " Player 2 has no valid moves left"
WON_THE_GAME_2_NO_ANIMALS = WON_THE_GAME_2 + " Player 1 has no valid moves left"


class EndingGameController:
    movementValidationController = MovementValidationController()

    def testFinalGame(self, p1: Player, p2: Player, board: Board, calledFromGameController: bool):
        if p1.alive == 0:
            if calledFromGameController:
                print(WON_THE_GAME_2_NO_ANIMALS)
            return True
        elif p2.alive == 0:
            if calledFromGameController:
                print(WON_THE_GAME_1_NO_ANIMALS)
            return True
        elif board.matrix[0][3].thereIsAnimal() and board.matrix[0][3].animal.player.number == 1:
            if calledFromGameController:
                print(WON_THE_GAME_1)
            return True
        elif board.matrix[8][3].thereIsAnimal() and board.matrix[8][3].animal.player.number == 2:
            if calledFromGameController:
                print(WON_THE_GAME_2)
            return True
        else:
            return False

    def noPossibleMoveForPlayer(self, player: Player, board: Board):
        for animal in player.animalCollection:
            if animal.isAlive:
                if not self.movementValidationController.checkIfAnimalHasAnyViableMoves(animal, board, animal.x, animal.y):
                    return True
        return False
