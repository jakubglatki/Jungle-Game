from view.BoardViewer import BoardViewer


class GameController:

    def __init__(self, boardViewer: BoardViewer):
        self.boardViewer = boardViewer

    def chooseGameMode(self):
        print(" Jungle Game\n")
        print("1- Player vs Player")
        print("2- Player vs Computer")
        print("3- Computer vs Computer")
        op = int(input("\n--> "))
        print("\n")

        if op == 1:
            self.PlayerVsPlayer()
        elif op == 2:
            self.PlayerVsComputer()
        elif op == 3:
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
