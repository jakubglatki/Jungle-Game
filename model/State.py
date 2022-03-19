from model.Board import Board
from model.Player import Player


class State:

    def __init__(self, board: Board, currentPlayer: Player, opponentPlayer: Player):
        self.board = board
        self.currentPlayer = currentPlayer
        self.opponentPlayer = opponentPlayer

