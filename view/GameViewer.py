class GameViewer:

    def showChoosingGameModeMenu(self):
        print(" Jungle Game\n")
        print("1- Player vs Player")
        print("2- Player vs Computer")
        print("3- Computer vs Computer")
        print("4. Research mode")
        return int(input("\n--> "))

    def showChoosingDifficultyMenu(self, number=""):
        print(" Choose difficulty level of computer " + number)
        print("1- Easy")
        print("2- Medium")
        print("3- Hard")
        return int(input("\n--> "))

    def showChoosingDepthMenu(self, number=""):
        print(" Choose depth level of computer " + number)
        return int(input("\n--> "))
