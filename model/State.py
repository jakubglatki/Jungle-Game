from controller.GameController import GameController
from model.Board import Board
from model.Player import Player


class State:
    gameController = GameController()

    def __init__(self, board: Board, currentPlayer: Player, opponentPlayer: Player, amIPlayer1: bool):
        self.board = board
        self.currentPlayer = currentPlayer
        self.opponentPlayer = opponentPlayer
        if amIPlayer1:
            self.player1 = True
        else:
            self.player1 = False

    def checkWinner(self):
        return self.gameController.winner
