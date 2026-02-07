from constants import *


def piece_color(piece: int):
    if (piece > 5):
        return WHITE
    return BLACK

def piece_type(piece: int):
    return piece % 6
