import time

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
        elif mode == 4:
            self.researchMode()

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
        board.player2.depth = self.gameViewer.showChoosingDepthMenu()
        boardViewer.showBoard()
        state = State(board, board.player1, board.player2, board.player1, board.player2)

        while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board, True) == False):
            print("Turn of player" + str(state.currentPlayer.number))
            if state.currentPlayer.isABot:
                move = self.minMaxController.alpha_beta_cutoff_search(state, state.currentPlayer.difficulty, state.currentPlayer.depth)
                state.currentPlayer.lastMoves.addValue(move)
                self.computerController.round(state.board, move)
            else:
                self.humanRoundController.round(state.currentPlayer, state.board)
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
            if not self.endingGameController.noPossibleMoveForPlayer(state.currentPlayer, board):
                state.currentPlayer.alive = 0
        return

    def ComputerVsComputer(self):
        board = Board(True, True)
        boardViewer = BoardViewer(board)
        board.player1.difficulty = self.gameViewer.showChoosingDifficultyMenu("1")
        board.player1.depth = self.gameViewer.showChoosingDepthMenu("1")
        board.player2.difficulty = self.gameViewer.showChoosingDifficultyMenu("2")
        board.player2.depth = self.gameViewer.showChoosingDepthMenu("2")
        boardViewer.showBoard()
        state = State(board, board.player1, board.player2, board.player1, board.player2)
        turns = 0

        while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board, True) == False):
            print("Turn of player" + str(state.currentPlayer.number))

            turns += 1
            tic = time.perf_counter()
            move = self.minMaxController.alpha_beta_cutoff_search(state, state.currentPlayer.difficulty, state.currentPlayer.depth)
            toc = time.perf_counter()
            print(f"The computer has calculated the move in {toc - tic:0.4f} seconds!")
            state.currentPlayer.clock += (toc - tic)
            state.currentPlayer.nclock += 1
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
        print(str(turns))
        state.currentPlayer.showTimeInfo()
        state.opponentPlayer.showTimeInfo()
        return

    #In researchMode changing n we can change the number of games to test. In this way we can analyse much faster different difficulties/depths. At the end of the games the software gives us a
    #brief description of the games describing us number of wins, average number of rounds per game and average time for player 1 and for player 2.
    def researchMode(self):
        n = 100
        actual = 0
        nwins1 = 0
        nwins2 = 0
        avgTime1 = 0
        avgTime2 = 0
        avgTurns = 0
        difficultyp1 = self.gameViewer.showChoosingDifficultyMenu("1")
        depthp1 = self.gameViewer.showChoosingDepthMenu("1")
        difficultyp2 = self.gameViewer.showChoosingDifficultyMenu("2")
        depthp2 = self.gameViewer.showChoosingDepthMenu("2")
        while actual != n:
            board = Board(True, True)
            boardViewer = BoardViewer(board)
            board.player1.difficulty = difficultyp1
            board.player2.difficulty = difficultyp2
            board.player1.depth = depthp1
            board.player2.depth = depthp2
            boardViewer.showBoard()
            state = State(board, board.player1, board.player2, board.player1, board.player2)
            turns = 0

            while (self.endingGameController.testFinalGame(board.getPlayer1(), board.getPlayer2(), board,
                                                           True) == False):
                print("Turn of player" + str(state.currentPlayer.number))

                turns += 1
                tic = time.perf_counter()
                move = self.minMaxController.alpha_beta_cutoff_search(state, state.currentPlayer.difficulty, state.currentPlayer.depth)
                toc = time.perf_counter()
                print(f"The computer has calculated the move in {toc - tic:0.4f} seconds!")
                state.currentPlayer.clock += (toc - tic)
                state.currentPlayer.nclock += 1
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
            actual += 1
            print(str(turns))
            state.currentPlayer.showTimeInfo()
            state.opponentPlayer.showTimeInfo()
            if state.currentPlayer.number == 1:
                avgTime1 += (state.currentPlayer.clock / state.currentPlayer.nclock); avgTime2 += (
                            state.opponentPlayer.clock / state.opponentPlayer.nclock);
            else:
                avgTime2 += (state.currentPlayer.clock / state.currentPlayer.nclock); avgTime1 += (
                            state.opponentPlayer.clock / state.opponentPlayer.nclock);
            avgTurns += turns
            if state.currentPlayer.victories == 1:
                if state.currentPlayer.number == 1:
                    nwins1 += 1
                else:
                    nwins2 += 1
            if state.opponentPlayer.victories == 1:
                if state.opponentPlayer.number == 1:
                    nwins1 += 1
                else:
                    nwins2 += 1
        avgTime1 = avgTime1 / n
        avgTime2 = avgTime2 / n
        avgTurns = turns
        print("Games played: " + str(actual))
        print("Games won by player 1: " + str(nwins1))
        print("Average time for moving player 1: " + str(avgTime1))
        print("Games won by player 2: " + str(nwins2))
        print("Average time for moving player 2: " + str(avgTime2))
        print("Average number of turns in a game: " + str(avgTurns))

        return
