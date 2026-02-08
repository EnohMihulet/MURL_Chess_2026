from constants import *


class Move:

    def __init__(self, start: int, target: int, flag: int):
        self.start = start
        self.target = target
        self.flag = flag # NOTE: Will be used to store info about move type (capture, enpassant, castling, etc.)
        return

    def is_quiet(self) -> bool:
        return self.flag == MOVE_FLAG_QUIET

    def is_capture(self) -> bool:
        return self.flag == MOVE_FLAG_CAPTURE

    def is_double_push(self) -> bool:
        return self.flag == MOVE_FLAG_DOUBLE_PAWN_PUSH

    def is_enpassant(self) -> bool:
        return self.flag == MOVE_FLAG_EN_PASSANT

    def is_castle(self) -> bool:
        return self.flag == MOVE_FLAG_CASTLE

    def is_promotion(self) -> bool:
        return self.flag == MOVE_FLAG_PROMOTION

    def is_null_move(self) -> bool:
        if (self.start == self.start == 0):
            return True
        return False


FILE_NUM_FROM_CHAR = [NO_EP_FILE] * 128
FILE_NUM_FROM_CHAR[ord('a')] = 0
FILE_NUM_FROM_CHAR[ord('b')] = 1
FILE_NUM_FROM_CHAR[ord('c')] = 2
FILE_NUM_FROM_CHAR[ord('d')] = 3
FILE_NUM_FROM_CHAR[ord('e')] = 4
FILE_NUM_FROM_CHAR[ord('f')] = 5
FILE_NUM_FROM_CHAR[ord('g')] = 6
FILE_NUM_FROM_CHAR[ord('h')] = 7

def file_number_from_char(file_char: str):
    assert(len(file_char) == 1)
    return FILE_NUM_FROM_CHAR[ord(file_char)]
