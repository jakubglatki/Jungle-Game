import math

from controller.ComputerMovesController import ComputerMovesController
from controller.GameController import GameController
from controller.StateController import StateController


class MinimaxController:
    computerMovesController = ComputerMovesController()
    gameController = GameController()


    def alpha_beta_cutoff_search(self, state, game, d=5, cutoff_test=None, eval_fn=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

        player = state.currentPlayer

        # Functions used by alpha_beta
        def max_value(state, alpha, beta, depth):
            if cutoff_test(state, depth):
                return eval_fn(state)
            value = -math.inf
            for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
                value = max(value, min_value(game.result(state, action), alpha, beta, depth + 1))
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            return value

        def min_value(state, alpha, beta, depth):
            if cutoff_test(state, depth):
                return eval_fn(state)
            value = math.inf
            for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
                value = min(value, max_value(game.result(state, action), alpha, beta, depth + 1))
                if value <= alpha:
                    return value
                beta = min(beta, value)
            return value

        # Body of alpha_beta_cutoff_search starts here:
        # The default test cuts off at depth d or at a terminal state
        cutoff_test = (cutoff_test or (lambda state, depth: depth > d or
                                self.gameController.testFinalGame(state.currentPlayer, state.opponentPlayer, state.board)))
        eval_fn = eval_fn or (lambda state: state.checkWinner())
        best_score = -math.inf
        beta = math.inf
        best_action = None
        for action in self.computerMovesController.listOfPossibleMoves(state.currentPlayer, state.board):
            value = min_value(game.result(state, action), best_score, beta, 1)
            if value > best_score:
                best_score = value
                best_action = action
        return best_action