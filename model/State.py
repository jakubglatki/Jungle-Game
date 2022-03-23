from model.Board import Board
from model.Player import Player


class State:

    def __init__(self, board: Board, currentPlayer: Player, opponentPlayer: Player, playerWhoMoves: Player, playerWhoNotMoves: Player):
        self.board = board
        # Use this for the movement part (to get the moves)
        self.currentPlayer = currentPlayer
        self.opponentPlayer = opponentPlayer
        # Use these for the evaluation function part
        self.playerWhoMoves = playerWhoMoves
        self.playerWhoNotMoves = playerWhoNotMoves

