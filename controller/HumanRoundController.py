from controller.MovementValidationController import MovementValidationController
from model.Animal import Animal
from model.Player import Player
from model.Board import Board
from controller.MovementController import MovementController


class HumanRoundController:
    movementController = MovementController()
    movementValidationController = MovementValidationController()

    def round(self, player: Player, board: Board):
        # first while for choosing a valid starting point
        movementController = MovementController()
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1
        tempAnimal = None
        flag = False
        while (flag == False):
            print("select starting point of your move: ")
            sp = str(input())
            # sp = "a7"
            x1 = int(sp[1]) - 1
            y1 = ord(sp[0].lower()) - 97
            if (self.movementValidationController.isValidStartingPoint(player, board, x1,
                                                                       y1)):  # In this test we see if in the selected area there is one of your animal and if he can move
                tempAnimal = board.matrix[x1][y1].animal
                flag = True
            else:
                print("You did not choose a valid starting point. The starting point has to contain your animal, "
                      "and it has to have available valid move.\n")
        # second while for chosing a valid ending point
        flag = False
        while (flag == False):
            print("select ending point of your move: ")
            ep = str(input())
            # ep="a6"
            x2 = int(ep[1]) - 1
            y2 = ord(ep[0].lower()) - 97
            if (self.movementValidationController.isValidEndingPoint(tempAnimal, board, x2, y2, x1,
                                                                     y1)):  # In this test we see if: the animal can go there, if there is another weaker opponent animal (in case of one of yours or in case of stronger you can't), if there is some special rule applied
                flag = True
            else:
                print("The selected ending point is incorrect.")

        # The movement is valid, now we have just to make it and verify if, at the end of the movement, the player have eaten something off the other one
        # In case in the ending point there is another animal, kill it
        movementController.killAnimal(board, x2, y2)
        movementController.moveAnimal(tempAnimal, board, x2,
                                      y2)  # to do, simply move the animal from (x1,y1) to (x2,y2)
