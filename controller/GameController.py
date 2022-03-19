from controller.MovementValidationController import MovementValidationController
from view.BoardViewer import BoardViewer
from view.GameViewer import GameViewer
from model.Player import Player
from model.Board import Board
from controller.HumanRoundController import HumanRoundController

WON_THE_GAME_1 = "Player 1 has won the game!"
WON_THE_GAME_2 = "Player 2 has won the game!"
WON_THE_GAME_1_NO_ANIMALS = WON_THE_GAME_1 + " Player 2 has no valid moves left"
WON_THE_GAME_2_NO_ANIMALS = WON_THE_GAME_2 + " Player 1 has no valid moves left"


class GameController:
    humanRoundController = HumanRoundController()
    movementValidationController = MovementValidationController()

    # 0- no winner, 1- Player1, 2- Player2
    def __init__(self, winner=0):
        self.winner = winner

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

        while (self.testFinalGame(board.getPlayer1(), board.getPlayer2(), board) == False):
            print("Turn of player" + str(actual.number))
            if not actual.isABot:
                self.humanRoundController.round(actual, board)
            if actual == board.getPlayer1():
                actual = board.getPlayer2()
            else:
                actual = board.getPlayer1()
            self.boardViewer.showBoard()
            if not self.noPossibleMoveForPlayer(actual, board):
                actual.alive = 0

        return

    def PlayerVsComputer(self):
        board = Board(True, False)
        boardViewer = BoardViewer(board)
        boardViewer.showBoard()
        return

    def ComputerVsComputer(self):
        board = Board(True, True)
        boardViewer = BoardViewer(board)
        boardViewer.showBoard()
        return

    def testFinalGame(self, p1: Player, p2: Player, board: Board):
        if p1.alive == 0:
            print(WON_THE_GAME_2_NO_ANIMALS)
            return True
        elif p2.alive == 0:
            self.winner = 1
            print(WON_THE_GAME_1_NO_ANIMALS)
            return True
        elif board.matrix[0][3].thereIsAnimal() and board.matrix[0][3].animal.player.number == 1:
            self.winner = 1
            print(WON_THE_GAME_1)
            return True
        elif board.matrix[8][3].thereIsAnimal() and board.matrix[8][3].animal.player.number == 2:
            self.winner = 2
            print(WON_THE_GAME_2)
            return True
        else:
            self.winner = 0
            return False

    def noPossibleMoveForPlayer(self, player: Player, board: Board):
        for animal in player.animalCollection:
            if animal.isAlive:
                if self.movementValidationController.checkIfAnimalHasAnyViableMoves(animal, board, animal.x, animal.y):
                    return True
        return False
