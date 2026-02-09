from constants import *
from move import *
from piece import *

class State:

    def __init__(self, fen_string: str):
        self.board = [] # NOTE: List containing pieces indexed by row * 8 + col
        self.to_move = WHITE
        self.castling_rights = 0 # Ignore for now
        self.ep_file = -1 # Ignore for now
        self.half_moves = 0 # Ignore for now
        self.full_moves = 0 # Ignore for now
        self.piece_positions = [[] for _ in range(PIECE_COUNT)] # Ignore for now
        self.move_history = [] # Ignore for now


        # FEN PARSING FOR STARTING POSITION

        sections = fen_string.split()

        # board part
        board_part = sections[0]
        rank = 7
        file = 0
        for c in board_part:
            if (c == '/'):
                assert(rank != 0)

                rank -= 1
                file = 0
                continue
            elif (c.isdigit()):
                assert(1 <= int(c) <= 8)

                file += int(c)
                continue
            else:
                piece = piece_from_char(c)
                sq = rank * 8 + file

                assert(piece != NO_PIECE)
                assert(0 <= sq <= 63)

                self.board[sq] = piece
                self.piece_positions[piece].append(sq)
                file += 1

        # color to move
        color = sections[1]
        assert(color == 'w' or 'b')
        if (color == 'w'):
            self.to_move = WHITE
        else:
            self.to_move = BLACK
    

        # castling rights
        castling_rights = sections[2]
        assert(len(castling_rights) <= 4)
        self.castling_rights = CASTLING_NONE;
        if ('k' in castling_rights):
            self.castling_rights |= CASTLING_BLACK_KING
        elif ('q' in castling_rights):
            self.castling_rights |= CASTLING_BLACK_QUEEN
        elif ('K' in castling_rights):
            self.castling_rights |= CASTLING_WHITE_KING
        elif ('Q' in castling_rights):
            self.castling_rights |= CASTLING_WHITE_QUEEN
        # else should never happen

        # enpassant
        enpassant = sections[3];
        if (enpassant == '='):
            self.ep_file = 0
        else:
            self.ep_file = file_number_from_char(enpassant[0])

        # halfmoves
        half_moves = sections[4]
        self.half_moves = int(half_moves)

        # fullmoves
        full_moves = sections[5]
        self.full_moves = int(full_moves)

    def make_move(self, move: Move) -> None:
        
        # TODO: probably put castle and promotion case in quiet move case
        # Non capture
        if (move.is_quiet() and not move.is_castle() and not move.is_promotion()):
            start = move.start
            target = move.target
            piece = self.board[start]

            # Update board
            self.board[target] = self.board[start]
            self.board[start] = None

            # Update piece positions
            self.piece_positions[piece].remove(start)
            self.piece_positions[piece].append(target)

            # Update half move count
            self.half_moves += 1

            # Update castling rights
            if (piece_type(piece) == ROOK):
                if (piece_color(piece) == WHITE):
                    if (start == 0):
                        self.castling_rights &= ~CASTLING_WHITE_QUEEN
                    elif (start == 7):
                        self.castling_rights &= ~CASTLING_WHITE_KING
                else:
                    if (start == 56):
                        self.castling_rights &= ~CASTLING_BLACK_QUEEN
                    elif (start == 63):
                        self.castling_rights &= ~CASTLING_BLACK_KING
            elif (piece_type(piece) == KING):
                if (piece_color(piece) == WHITE):
                    self.castling_rights &= ~(CASTLING_WHITE_KING & CASTLING_WHITE_QUEEN)
                else:
                    self.castling_rights &= ~(CASTLING_BLACK_KING & CASTLING_BLACK_QUEEN)
            elif (piece_type(piece) == PAWN):
                self.half_moves = 0 # Pawn moves reset half move count

            # update enpassant file
            if (move.is_double_push()):
                self.ep_file = start & 7
            else:
                self.ep_file = NO_EP_FILE
        # TODO:
        # Move is a capture, castle, or promotion
        else:
            pass


        # Switch side to move and increment full move count
        if (self.to_move == WHITE):
            self.to_move = BLACK
        else:
            self.to_move = WHITE

        self.full_moves += 1
        pass

    def unmake_move(self, move: Move) -> None:
        pass

    def is_check(self) -> bool:
        return False

    def is_checkmate(self) -> bool:
        return False

    def is_draw(self) -> bool:
        return False

    def is_stalemate(self) -> bool:
        return False
