from view.BoardViewer import BoardViewer
from view.GameViewer import GameViewer


class GameController:

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
