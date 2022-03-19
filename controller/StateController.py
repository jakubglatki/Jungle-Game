import copy

from controller.MovementController import MovementController
from model.State import State


class StateController:
    movementController = MovementController()

    def __init__(self, state: State):
        self.state = state

    def stateAfterMove(self, animal, x, y):
        self.state.board = self.movementController.moveAnimal(animal, self.state.board, x, y)
        tempPlayer = copy.copy(self.state.currentPlayer)
        self.state.currentPlayer = self.state.opponentPlayer
        self.state.opponentPlayer = tempPlayer
