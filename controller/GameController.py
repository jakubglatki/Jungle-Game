from controller.ComputerController import ComputerController
from controller.EndingGameController import EndingGameController
from controller.MinimaxController import MinimaxController
from controller.MovementValidationController import MovementValidationController
from model.LastMoves import LastMoves
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
    gameViewer = GameViewer()


    def chooseGameMode(self):
        mode = self.gameViewer.showChoosingGameModeMenu()
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
        board = Board(False, True)
        boardViewer = BoardViewer(board)
        board.player2.difficulty = self.gameViewer.showChoosingDifficultyMenu()
        boardViewer.showBoard()
        state = State(board, board.player1, board.player2, board.player1, board.player2)

        while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board, True) == False):
            print("Turn of player" + str(state.currentPlayer.number))
            if state.currentPlayer.isABot:
                move = self.minMaxController.alpha_beta_cutoff_search(state)
                state.currentPlayer.lastMoves.addValue(move)
                self.computerController.round(state.board, move)
            else: self.humanRoundController.round(state.currentPlayer, state.board)
            if state.currentPlayer == state.board.getPlayer1():
                state.currentPlayer = state.board.getPlayer2()
                state.opponentPlayer = state.board.getPlayer1()
            else:
                state.currentPlayer = state.board.getPlayer1()
                state.opponentPlayer = state.board.getPlayer2()
            boardViewer.showBoard()
            if not self.endingGameController.noPossibleMoveForPlayer(state.currentPlayer, board):
                state.currentPlayer.alive = 0
        return

    def ComputerVsComputer(self):
        board = Board(True, True)
        boardViewer = BoardViewer(board)
        board.player1.difficulty = self.gameViewer.showChoosingDifficultyMenu("1")
        board.player2.difficulty = self.gameViewer.showChoosingDifficultyMenu("2")
        boardViewer.showBoard()
        state = State(board, board.player1, board.player2, board.player1, board.player2)

        while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board, True) == False):
            print("Turn of player" + str(state.currentPlayer.number))
            move = self.minMaxController.alpha_beta_cutoff_search(state, state.currentPlayer.difficulty)
            self.computerController.round(board, move)
            state.currentPlayer.lastMoves.addValue(move)
            if state.currentPlayer == state.board.getPlayer1():
                state.currentPlayer = state.board.getPlayer2()
                state.opponentPlayer = state.board.getPlayer1()
                state.playerWhoMoves = state.currentPlayer
                state.playerWhoNotMoves = state.opponentPlayer
            else:
                state.currentPlayer = state.board.getPlayer1()
                state.opponentPlayer = state.board.getPlayer2()
                state.playerWhoMoves = state.currentPlayer
                state.playerWhoNotMoves = state.opponentPlayer
            boardViewer.showBoard()
            if not self.endingGameController.noPossibleMoveForPlayer(state.playerWhoMoves, state.board):
                state.playerWhoMoves.alive = 0
        return

