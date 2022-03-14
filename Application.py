import model
from game.Player import Player
from model.Animal import Animal
from model.Board import Board
from view.BoardViewer import BoardViewer

player1 = Player(1, "human")
player2 = Player(2, "human")
m1 = Animal("rat", "M1", 1, player1, 6, 6)
c1 = Animal("cat", "C1", 2, player1, 7, 1)
d1 = Animal("dog", "D1", 3, player1, 7, 5)
w1 = Animal("wolf", "W1", 4, player1, 6, 2)
p1 = Animal("panther", "P1", 5, player1, 6, 4)
t1 = Animal("tiger", "T1", 6, player1, 8, 0)
l1 = Animal("lion", "L1", 7, player1, 8, 6)
e1 = Animal("elephant", "E1", 8, player1, 6, 0)
m2 = Animal("rat", "M2", 1, player2, 3, 0)
c2 = Animal("cat", "C2", 2, player2, 1, 5)
d2 = Animal("dog", "D2", 3, player2, 1, 1)
w2 = Animal("wolf", "W2", 4, player2, 2, 4)
p2 = Animal("panther", "P2", 5, player2, 2, 2)
t2 = Animal("tiger", "T2", 6, player2, 0, 6)
l2 = Animal("lion", "L2", 7, player2, 0, 0)
e2 = Animal("elephant", "E2", 8, player2, 2, 6)

Animals1 = [m1, c1, d1, w1, p1, t1, l1, e1]
Animals2 = [m2, c2, d2, w2, p2, t2, l2, e2]

player1.animalCollection = Animals1
player2.animalCollection = Animals2

board = Board(Animals1, Animals2)
actual = player1

boardViewer = BoardViewer(board)
boardViewer.showBoard()


def testFinalGame():
    return True


def noPossibleMoveForPlayer(player: Player):
    return False


while (testFinalGame == True):
    print("Turn of player" + actual.number)
    if (actual.isABot == False):
        # first while for chosing a valid starting point
        while ():
            print("select starting point of your move: ")
            sp = str(input())
            x1 = ord(sp[0].lower()) - 97
            y1 = sp[1]
            if (isValid(x1,
                        y1)):  # In this test we see if in the selected area there is one of your animal and if he can move
                exit
            else:
                print("The starting point selected is not fine.")
        # second while for chosing a valid ending point
        while ():
            print("select ending point of your move: ")
            ep = str(input())
            x2 = ord(ep[0].lower()) - 97
            y2 = ep[1]
            if (isValid2(
                    ep)):  # In this test we see if: the animal can go there, if there is another weaker opponent animal (in case of one of yours or in case of stronger you can't), if there is some special rule applied
                exit
            else:
                print("The ending point selected is not fine.")

    # The movement is valid, now we have just to make it and verify if, at the end of the movement, the player have eaten something off the other one
    # In case in the ending point there is another animal, kill it
    board.killAnimal(x2, y2)
    board.moveAnimal()  # to do, simply move the animal from (x1,y1) to (x2,y2)

    if (actual == player1):
        actual = player2
    else:
        actual = player1
    if (noPossibleMoveForPlayer(actual) == True):
        exit()
