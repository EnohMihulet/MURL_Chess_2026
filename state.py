from move import Move

class State:

    def __init__(self):
        self.board = [] # NOTE: List containing pieces indexed by row * 8 + col
        self.castling_rights = 0 # Ignore for now
        self.ep_file = -1 # Ignore for now
        self.piece_positions = [] # Ignore for now
        self.move_history = [] # Ignore for now
        return

    def make_move(self, move: Move):
        pass

    def unmake_move(self, move: Move):
        pass

    def is_check(self):
        pass

    def is_checkmate(self):
        pass

    def is_stalemate(self):
        pass
