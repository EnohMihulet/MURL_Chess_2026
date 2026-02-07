

class Move:

    def __init__(self, start: int, target: int, flag: int):
        self.start = start
        self.target = target
        self.flag = flag # NOTE: Will be used to store info about move type (capture, enpassant, castling, etc.)
        return

    def is_capture(self):
        pass

    def is_enpassant(self):
        pass

    def is_castle(self):
        pass

    def is_promotion(self):
        pass
