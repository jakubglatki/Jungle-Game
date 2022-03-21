import math

from model.State import State



class EvaluationFunctionController:

#First evaluation function, it consider only the power of every animal and nothing else
    def evaluationFunction_onlyAnimalPower(self, state:State):
        value = 0
        for animal in state.currentPlayer.animalCollection:
            if animal.isAlive: value = value + animal.power
        for animal in state.opponentPlayer.animalCollection:
            if animal.isAlive: value = value - animal.power
        return value

    def evaluationFunction_firstEvaluationFunction(self, state:State):
        #Dojo control if I am player1
        if state.currentPlayer.number==1:
            if state.board.getDojo2().thereIsAnimal() and state.board.getDojo2().animal.player==1:
                value = math.inf
                return value
            if state.board.getDojo1().thereIsAnimal() and state.board.getDojo1().animal.player==2:
                value = -math.inf
                return value
        #Dojo control if I am player2
        else:
            if state.board.getDojo1().thereIsAnimal() and state.board.getDojo1().animal.player==2:
                value = math.inf
                return value
            if state.board.getDojo2().thereIsAnimal() and state.board.getDojo2().animal.player==1:
                value = -math.inf
                return value

        value = 0
        for animal in state.currentPlayer.animalCollection:
            if animal.isAlive:
                value = value + animal.power
                if animal.power==1: value = value + 5 #Mouse can stay in water and also eat Elephant, for sure has more value
                if animal.power==6 or animal.power==7: value + 2  #Tiger and Lion have special move, add to them some more value
        for animal in state.opponentPlayer.animalCollection:
            if animal.isAlive:
                value = value - animal.power
                if animal.power==1: value = value - 5 #Mouse can stay in water and also eat Elephant, for sure has more value
                if animal.power==6 or animal.power==7: value - 2  #Tiger and Lion have special move, add to them some more value
        return value

    #Now the idea is to give importance also in the positioning of each animal, creating some kind of "hot zone" in which some animals are stronger






