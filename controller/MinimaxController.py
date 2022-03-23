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

    def alpha_beta_cutoff_search(self, state, d=3, cutoff_test=None, eval_fn=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

        # Functions used by alpha_beta
        def max_value(state, alpha, beta, depth, minimaxlastMoves):
            #DA TESTARE COSA FA SUL CUTOFF, CI METTE TROPPO TEMPO ANCHE QUANDO SONO DAVANTI AL DOJO, NON HA SENSO
            if cutoff_test(state, depth):
                return eval_fn(state)
                # return self.evaluationFunctionController.evaluationFunction_firstEvaluationFunction(state)
            value = -math.inf
            for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
                if state.currentPlayer.lastMoves.isARecentMove(action) == False and minimaxLastMoves.isARecentMove(
                        action) == False:
                    minimaxLastMoves.push(action)
                    value = max(value, min_value(self.result(state, action), alpha, beta, depth + 1, minimaxLastMoves))
                    minimaxLastMoves.pop()
                    if value >= beta:
                        return value
                    alpha = max(alpha, value)
            return value

        def min_value(state, alpha, beta, depth, minimaxlastMoves):
            if cutoff_test(state, depth):
                return eval_fn(state)
                # return self.evaluationFunctionController.evaluationFunction_firstEvaluationFunction(state)
            value = math.inf
            for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
                if state.currentPlayer.lastMoves.isARecentMove(action) == False and minimaxLastMoves.isARecentMove(
                        action) == False:
                    minimaxLastMoves.push(action)
                    value = min(value, max_value(self.result(state, action), alpha, beta, depth + 1, minimaxLastMoves))
                    minimaxLastMoves.pop()
                    if value <= alpha:
                        return value
                    beta = min(beta, value)
            return value

        # Body of alpha_beta_cutoff_search starts here:
        # The default test cuts off at depth d or at a terminal state
        cutoff_test = (cutoff_test or (lambda state, depth: depth > d or
                                                            self.endingGameController.testFinalGame(state.currentPlayer,
                                                                                                    state.opponentPlayer,
                                                                                                    state.board, False)
                                                            or not self.endingGameController.noPossibleMoveForPlayer(
            state.currentPlayer, state.board)))
        eval_fn = eval_fn or (
            lambda state: self.evaluationFunctionController.evaluationFunctionWithMeaningfulDistanceToDojo(state))
        minimaxLastMoves = LastMoves(d)
        best_score = -math.inf
        beta = math.inf
        best_action = None
        for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
            if state.currentPlayer.lastMoves.isARecentMove(action) == False and minimaxLastMoves.isARecentMove(
                    action) == False:
                minimaxLastMoves.push(action)
                value = min_value(self.result(state, action), best_score, beta, 1, minimaxLastMoves)
                action.depth = minimaxLastMoves.actual
                minimaxLastMoves.pop()
                random = randint(0, 100)
                if value > best_score or (value == best_score and random >= 80) or best_action==None or (value == best_score and action.depth<best_action.depth):
                    best_score = value
                    best_action = action
        return best_action

    def result(self, state: State, action: Move):
        # We are sure that the move is legal, so we have just to apply it to the state
        tempState = copy.deepcopy(state)
        self.movementController.moveAnimal(tempState.board.matrix[action.startingX][action.startingY].animal,
                                           tempState.board,
                                           action.endingX, action.endingY)
        tempPlayer = tempState.currentPlayer
        tempState.currentPlayer = tempState.opponentPlayer
        tempState.opponentPlayer = tempPlayer
        return tempState
