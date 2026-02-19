import chess
import math
from timer import *

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0,
}

class Searcher:
    def __init__(self):
        self.max_depth = 5

        self.board = chess.Board()
        self.best_move = None

    def search(self):
        # How deep we search
        depth = self.max_depth
        if (self.board.turn):
            self.maxi(depth, -math.inf, math.inf)
        else:
            self.mini(depth, math.inf,- math.inf)

        return self.best_move 

    # White to move
    def maxi(self, depth: int, alpha: int, beta: int) -> int:
        #If the game ended
        if (depth == 0):
            return self.evaluate()

        if (self.board.is_checkmate()):
            return -math.inf
        elif (self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.is_repetition()):
            return 0

        max = -math.inf

        # Populate move array
        moves = self.board.generate_legal_moves()

        for move in moves:
            self.board.push(move)

            score = self.mini(depth - 1, alpha, beta)            
            
            self.board.pop()

            if (score > max):
                max = score
                # Update alpha, new best move
                if (score > alpha):
                    alpha = score

                if (depth == self.max_depth):
                    self.best_move = move

            # Beta cut-off
            if (score >= beta):
                return score
                
        return max

    
    # Black to move
    def mini(self, depth: int, alpha: int, beta: int) -> int:
        if (depth == 0):
            return self.evaluate()

        if (self.board.is_checkmate()):
            return math.inf
        elif (self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.is_repetition()):
            return 0

        min = math.inf         
        moves = []
        
        #Populate move array
        moves = self.board.generate_legal_moves()

        for move in moves:
            self.board.push(move)

            score = self.mini(depth - 1,alpha, beta)            
            
            self.board.pop()

            if (score < min):
                min = score

                if (score < alpha):
                    alpha = score

                if (depth == self.max_depth):
                    self.best_move = move 
            # Beta cut-off
            if (score <= beta):
                return score
        return min


    def evaluate(self) -> int:
        score = 0

        for piece_type, value in PIECE_VALUES.items():
            white_piece_score = len(self.board.pieces(piece_type, chess.WHITE))
            black_piece_score = len(self.board.pieces(piece_type, chess.BLACK))
            score += value * (white_piece_score - black_piece_score)

        return score
