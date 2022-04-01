import copy
import math
from random import randint

from controller.ComputerMovesController import ComputerMovesController
from controller.EndingGameController import EndingGameController
from controller.EvaluationFunctionController import EvaluationFunctionController
from controller.MovementController import MovementController
from model.LastMoves import LastMoves
from model.Move import Move
from model.State import State


class MinimaxController:
    computerMovesController = ComputerMovesController()
    movementController = MovementController()
    evaluationFunctionController = EvaluationFunctionController()
    endingGameController = EndingGameController()

    def alpha_beta_cutoff_search(self, state, difficulty, d, cutoff_test=None, eval_fn=None):

        def max_value(state, alpha, beta, depth, minimaxLastMoves):
            if cutoff_test(state, depth):  #test if we are at the maximum depth selected or if we are in a endgame situation (0 animals or dojo conquered)
                return eval_fn(state) #return value of the evaluation function
            value = -math.inf
            if depth > minimaxLastMoves.depth: minimaxLastMoves.depth = depth  #This is to count the number of moves that must be made to reach the state. The function is only useful in case the player is close to winning, in this way he will go to choose the set of moves that leads him faster to victory.
            for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board): #Generate all possible moves that a player can do
                minimaxLastMoves.max += 1
                #MinimaxLastMoves saves the last moves that are made in the CURRENT subtree that we are analysing at the moment.
                #isARecentMove saves the last 5 moves that the active player has made, made for avoiding loops (considering also that usually make the opposite move is not worth)
                if state.currentPlayer.lastMoves.isARecentMove(action) == False and minimaxLastMoves.isARecentMove(
                        action) == False: #Second pruning, if the moving player has already made that move recently or within the branch we are analyzing the player makes a move that brings him back to the initial state, let's eliminate that move since it is certainly not convenient.
                    minimaxLastMoves.push(action)
                    value = max(value, min_value(self.result(state, action), alpha, beta, depth + 1, minimaxLastMoves))
                    minimaxLastMoves.pop()
                    #alpha-beta cuts pruning
                    if value >= beta:
                        return value
                    alpha = max(alpha, value)
            return value

        def min_value(state, alpha, beta, depth, minimaxLastMoves):
            if cutoff_test(state, depth):
                return eval_fn(state)
            value = math.inf
            if depth > minimaxLastMoves.depth: minimaxLastMoves.depth = depth
            for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
                minimaxLastMoves.max += 1
                if state.currentPlayer.lastMoves.isARecentMove(action) == False and minimaxLastMoves.isARecentMove(
                        action) == False:
                    minimaxLastMoves.push(action)
                    value = min(value, max_value(self.result(state, action), alpha, beta, depth + 1, minimaxLastMoves))
                    minimaxLastMoves.pop()
                    if value <= alpha:
                        return value
                    beta = min(beta, value)
            return value

        cutoff_test = (cutoff_test or (lambda state, depth: depth > d or
                                                            self.endingGameController.testFinalGame(state.currentPlayer,
                                                                                                    state.opponentPlayer,
                                                                                                    state.board, False)
                                                            or not self.endingGameController.noPossibleMoveForPlayer(
            state.currentPlayer, state.board)))
        eval_fn = eval_fn or (
            lambda state: self.evaluationFunctionController.evaluationFunctionWithIsMenacedFunctionWithoutEnemyDiminuition(state, difficulty))
        minimaxLastMoves = LastMoves(d)  #we generate the stack with the right dimension (==depth)
        best_score = -math.inf
        beta = math.inf
        best_action = None
        for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
            if state.currentPlayer.lastMoves.isARecentMove(action) == False and minimaxLastMoves.isARecentMove(
                    action) == False:
                minimaxLastMoves.push(action)
                value = min_value(self.result(state, action), best_score, beta, 1, minimaxLastMoves)
                action.depth = minimaxLastMoves.depth
                minimaxLastMoves.depth = 0
                minimaxLastMoves.pop()
                random = randint(0, 100)
                if value > best_score or (value == best_score and random > 80) or best_action is None or (
                        value == math.inf and action.depth == 0):
                    best_score = value
                    best_action = action
                    if best_action.depth == 0 and best_score == math.inf: #Win in 1 move, useless to continue to search
                        return best_action

        print("Number of different nodes analyzed: " + str(minimaxLastMoves.max))
        return best_action

    def result(self, state: State, action: Move):  #This function generate the new state of the game
        tempState = copy.deepcopy(state)
        self.movementController.moveAnimal(tempState.board.matrix[action.startingX][action.startingY].animal,
                                           tempState.board,
                                           action.endingX, action.endingY)
        tempPlayer = tempState.currentPlayer
        tempState.currentPlayer = tempState.opponentPlayer
        tempState.opponentPlayer = tempPlayer
        return tempState
