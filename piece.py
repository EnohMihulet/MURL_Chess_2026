from constants import *

# Look-up table for piece char to piece integer value
PIECE_FROM_CHAR = [NO_PIECE] * 128
PIECE_FROM_CHAR[ord('p')] = B_PAWN
PIECE_FROM_CHAR[ord('P')] = W_PAWN
PIECE_FROM_CHAR[ord('n')] = B_KNIGHT
PIECE_FROM_CHAR[ord('N')] = W_KNIGHT
PIECE_FROM_CHAR[ord('b')] = B_BISHOP
PIECE_FROM_CHAR[ord('B')] = W_BISHOP
PIECE_FROM_CHAR[ord('r')] = B_ROOK
PIECE_FROM_CHAR[ord('R')] = W_ROOK
PIECE_FROM_CHAR[ord('q')] = B_QUEEN
PIECE_FROM_CHAR[ord('Q')] = W_QUEEN
PIECE_FROM_CHAR[ord('k')] = B_KING
PIECE_FROM_CHAR[ord('K')] = W_KING

def piece_color(piece: int):
    if (piece > 5):
        return WHITE
    return BLACK

def piece_type(piece: int):
    return piece % 6

def piece_from_char(piece_char: str):
    assert(len(piece_char) == 1)
    return PIECE_FROM_CHAR[ord(piece_char)]
