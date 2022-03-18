from view.BoardViewer import BoardViewer
from view.GameViewer import GameViewer
from model.Player import Player
from model.Board import Board
from controller.HumanRoundController import HumanRoundController


class GameController:
    humanRoundController = HumanRoundController()

    def __init__(self, boardViewer: BoardViewer):
        self.boardViewer = boardViewer

    def chooseGameMode(self):
        gameViewer = GameViewer()
        mode = gameViewer.showChoosingGameModeMenu()
        print("\n")

        if mode == 1:
            self.PlayerVsPlayer()
        elif mode == 2:
            self.PlayerVsComputer()
        elif mode == 3:
            self.ComputerVsComputer()

    def PlayerVsPlayer(self):
        self.boardViewer.showBoard()
        return

    def PlayerVsComputer(self):
        self.boardViewer.showBoard()
        return

    def ComputerVsComputer(self):
        self.boardViewer.showBoard()
        return

    def testFinalGame(self, p1: Player, p2: Player, board: Board):
        if p1.alive == 0:
            print("Player 2 has won the game!")
            return True
        elif p2.alive == 0:
            print("Player 1 has won the game!")
            return True
        elif board.matrix[0][3].thereIsAnimal() and board.matrix[0][3].animal.player.number == 1:
                print("Player 1 has won the game!")
                return True
        elif board.matrix[8][3].thereIsAnimal() and board.matrix[8][3].animal.player.number == 2:
                print("Player 2 has won the game!")
                return True
        else:
            return False

    def noPossibleMoveForPlayer(self, player: Player):
        for animal in player.animalCollection:
            if animal.isAlive:
                # there should be a function that is made on the single animal that test if he can move somewhere, the same function should be used also in isValidStartingPoint
                return True
        return False
