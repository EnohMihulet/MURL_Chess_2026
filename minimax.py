from constants import *
from move import *
from piece import *
from state import *
from evaluator import *
from move_generator import *
import math

class Searcher:

    def __init__(self):
        self.evalutator = Evaluator()
        self.generator = Move_Generator()
        self.best_move = Move(0, 0, MOVE_FLAG_QUIET)
        self.max_depth = 3

    def search(self, state: State) -> Move:
        # How deep we search
        depth = self.max_depth
        if (state.to_move == WHITE):
            self.mini(state, depth)
        else:
            self.maxi(state, depth)

        return self.best_move 

    # White to move
    def maxi(self, state: State, depth: int) -> float:

        # Max depth reached
        if (depth == 0):
            return self.evalutator.evaluate(state, WHITE)

        # The game ended
        if (state.is_checkmate()):
            return -math.inf
        elif (state.is_draw()):
            return 0

        max = -math.inf
        moves = []

        #Populate move array
        self.generator.gen_moves(moves, WHITE)
        
        # Filter out illegal moves
        self.generator.filter_moves(moves, WHITE)

        for move in moves:
            state.make_move(move)

            score = self.mini(state, depth - 1)            
            
            state.unmake_move(move)

            if (score > max):
                max = score
                # At the root we set the best move
                if (depth == self.max_depth):
                    self.best_move = move

        return max

    
    # Black to move
    def mini(self, state: State, depth: int) -> float:
        if (depth == 0):
            return self.evalutator.evaluate(state, BLACK)

        if (state.is_checkmate()):
            return math.inf
        elif (state.is_draw()):
            return 0

        min = math.inf
        moves = []
        
        self.generator.gen_moves(moves, BLACK)
        self.generator.filter_moves(moves, BLACK)

        for move in moves:
            state.make_move(move)

            score = self.maxi(state, depth - 1)

            state.unmake_move(move)

            if (score < min):
                min = score
                if (depth == self.max_depth):
                    self.best_move = move 

        return min
