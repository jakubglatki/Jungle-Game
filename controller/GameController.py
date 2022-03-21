from controller.ComputerController import ComputerController
from controller.EndingGameController import EndingGameController
from controller.MinimaxController import MinimaxController
from controller.MovementValidationController import MovementValidationController
from model.State import State
from view.BoardViewer import BoardViewer
from view.GameViewer import GameViewer
from model.Board import Board
from controller.HumanRoundController import HumanRoundController


class GameController:
    humanRoundController = HumanRoundController()
    movementValidationController = MovementValidationController()
    computerController = ComputerController()
    endingGameController = EndingGameController()
    minMaxController = MinimaxController()

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
        board = Board(False, False)
        actual = board.getPlayer1()
        boardViewer = BoardViewer(board)
        boardViewer.showBoard()

        while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board, True) == False):
            print("Turn of player" + str(actual.number))
            if not actual.isABot:
                self.humanRoundController.round(actual, board)
            if actual == board.getPlayer1():
                actual = board.getPlayer2()
            else:
                actual = board.getPlayer1()
            boardViewer.showBoard()
            if not self.endingGameController.noPossibleMoveForPlayer(actual, board):
                actual.alive = 0

        return

    def PlayerVsComputer(self):
        board = Board(True, False)
        actual = board.getPlayer1()
        boardViewer = BoardViewer(board)
        boardViewer.showBoard()
        return

    def ComputerVsComputer(self):
        board = Board(True, True)
        actual = board.getPlayer1()
        boardViewer = BoardViewer(board)
        boardViewer.showBoard()
        state = State(board, board.player1, board.player2)

        while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board, True) == False):
            print("Turn of player" + str(actual.number))
            if actual.isABot:
                move = self.minMaxController.alpha_beta_cutoff_search(state)
                self.computerController.round(board, move)
            if actual == board.getPlayer1():
                actual = board.getPlayer2()
            else:
                actual = board.getPlayer1()
            boardViewer.showBoard()
            if not self.endingGameController.noPossibleMoveForPlayer(actual, board):
                actual.alive = 0
        return

