from model.Board import Board
from model.Player import Player


class State:
    def __init__(self, board:Board, me:Player, oppenent:Player, amIPlayer1: bool):
        self.board = board
        self.me = me
        self.oppenent = oppenent
        if amIPlayer1: self.player1 = True
        else: self.player1 = False
