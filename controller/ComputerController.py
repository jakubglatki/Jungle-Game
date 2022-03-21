from controller.MovementController import MovementController
from model.Animal import Animal
from model.Board import Board
from model.Move import Move
from model.Player import Player
from model.State import State
from view.GameViewer import GameViewer


class ComputerController:

    def round(self, board: Board, move: Move):
        # first while for choosing a valid starting point
        movementController = MovementController()

        x1 = move.startingX
        y1 = move.startingY

        x2 = move.endingX
        y2 = move.endingY

        # The movement is valid, now we have just to make it and verify if, at the end of the movement, the player have eaten something off the other one
        # In case in the ending point there is another animal, kill it
        movementController.moveAnimal(board.matrix[x1][y1].animal, board, x2, y2)  # to do, simply move the animal from (x1,y1) to (x2,y2)
        print("The computer move is: "+move.animal.name+" in "+chr(move.endingY+97)+str(move.endingX+1)+ "\n")




    def chooseDifficultyForPlayerVsComputer(self):
        gameViewer = GameViewer()
        level = gameViewer.showChoosingDifficultyMenu()
        print("\n")

        if level == 1:
            return
        elif level == 2:
            return
        elif level == 3:
            return


    def chooseDifficultyForComputerVsComputer(self):
        gameViewer = GameViewer()
        level1 = gameViewer.showChoosingDifficultyMenu("1")
        level2 = gameViewer.showChoosingDifficultyMenu("2")
        print("\n")

        if level1 == 1:
            return
        elif level1 == 2:
            return
        elif level1 == 3:
            return
        if level2 == 1:
            return
        elif level2 == 2:
            return
        elif level2 == 3:
            return
