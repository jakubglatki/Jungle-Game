import model
from Game.Player import Player
from model.Animal import Animal
from model.Board import Board

m1 = Animal("rat",1,1,6,6)
c1 = Animal("cat",2,1,7,1)
d1 = Animal("dog",3,1,7,5)
w1 = Animal("wolf",4,1,6,2)
p1 = Animal("panther",5,1,6,4)
t1 = Animal("tiger",6,1,8,0)
l1 = Animal("lion",7,1,8,6)
e1 = Animal("elephant",8,1,6,0)
m2 = Animal("rat",1,2,0,3)
c2 = Animal("cat",2,2,1,5)
d2 = Animal("dog",3,2,1,1)
w2 = Animal("wolf",4,2,2,4)
p2 = Animal("panther",5,2,2,2)
t2 = Animal("tiger",6,2,0,6)
l2 = Animal("lion",7,2,0,0)
e2 = Animal("elephant",8,2,2,6)

Animals1 = [m1, c1, d1, w1, p1, t1, l1, e1]
Animals2 = [m2, c2, d2, w2, p2, t2, l2, e2]

player1 = Player(1,Animals1)
player2 = Player(2,Animals2)
board = Board(Animals1, Animals2)
actual = player1

def testFinalGame():
    return True
def noPossibleMoveForPlayer(player: Player):
    return False


while(testFinalGame==True):
    print("Turn of player"+actual.number)
    print("")

    if(actual==player1):
        actual=player2
    else:
        actual=player1
    if(noPossibleMoveForPlayer(actual)==True):
        exit()






