import chess
from minimax import *



if __name__ == "__main__":
    print("Hello World!")
    searcher = Searcher()
    searcher.board.set_fen("4k3/4p3/8/3RKQ2/8/8/8/8 w KQkq - 0 0")

    move_count = 0
    while (not searcher.board.is_game_over()):
        move = searcher.search()
        move_count += 1
        searcher.board.push(move)
        print("Move made: ", move)
        print("Move Count: ", move_count)
        print("Current position: ")
        print(searcher.board)

    print("Game over.")