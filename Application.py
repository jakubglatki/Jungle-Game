import model
from Game.Player import Player
from model.Animal import Animal

m1 = Animal("rat",1,1)
c1 = Animal("cat",2,1)
d1 = Animal("dog",3,1)
w1 = Animal("wolf",4,1)
l1 = Animal("leopard",5,1)
t1 = Animal("tiger",6,1)
li1 = Animal("lion",7,1)
e1 = Animal("elephant",8,1)
m2 = Animal("rat",1,2)
c2 = Animal("cat",2,2)
d2 = Animal("dog",3,2)
w2 = Animal("wolf",4,2)
l2 = Animal("leopard",5,2)
t2 = Animal("tiger",6,2)
li2 = Animal("lion",7,2)
e2 = Animal("elephant",8,2)

Animals1 = {m1, c1, d1, w1, l1, t1, li1, e1}
Animals2 = {m2, c2, d2, w2, l2, t2, li2, e2}

p1 = Player(1,Animals1)
p2 = Player(2,Animals2)


