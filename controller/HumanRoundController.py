class HumanRoundController:

    def round(self, player: Player, board: Board):
        # first while for chosing a valid starting point
        while ():
            print("select starting point of your move: ")
            sp = str(input())
            x1 = ord(sp[0].lower()) - 97
            y1 = sp[1]-1
            if (isValid(x1,y1)):  # In this test we see if in the selected area there is one of your animal and if he can move
                exit;
            else:
                print("The starting point selected is not fine.")
        # second while for chosing a valid ending point
        while ():
            print("select ending point of your move: ")
            ep = str(input())
            x2 = ord(ep[0].lower()) - 97
            y2 = ep[1]-1
            if (isValid2(tempAnimal,x2,y2)):  # In this test we see if: the animal can go there, if there is another weaker opponent animal (in case of one of yours or in case of stronger you can't), if there is some special rule applied
                exit;
            else:
                print("The ending point selected is not fine.")

        # The movement is valid, now we have just to make it and verify if, at the end of the movement, the player have eaten something off the other one
        # In case in the ending point there is another animal, kill it
        board.killAnimal(x2, y2)
        board.moveAnimal()  # to do, simply move the animal from (x1,y1) to (x2,y2)
