
# heuristic funtion

import board

gameState = board.Chessboard()


def __init__(self):

    # init magnitudes, magX

    return


# heuristic megafunction

def h_mega(gameState: board.Chessboard):
    h = (mag1 * self.h_sub1(gameState) + mag2 *
         self.h_sub2(gameState) + ... + magX * self.h_subX(gameState)) / X
    return h


# heuristic subfunctions

def h_sub1(gameState: board.Chessboard):
    return

# etc


def check_mate():
    # if YOUR King is check mate return -1
    # if Opponents King is check mate return 1
    return 0


def difference_of_pieces(gameState: board.Chessboard):
    white_Value = (gameState.WHITE_PAWNS.bit_count() +
                   gameState.WHITE_BISHOPS.bit_count() * 3 +
                   gameState.WHITE_KNIGHTS.bit_count() * 3 +
                   gameState.WHITE_ROOKS.bit_count() * 5 +
                   gameState.WHITE_QUEEN.bit_count() * 9)
    black_Value = (gameState.BLACK_PAWNS.bit_count() +
                   gameState.BLACK_BISHOPS.bit_count() * 3 +
                   gameState.BLACK_KNIGHTS.bit_count() * 3 +
                   gameState.BLACK_ROOKS.bit_count() * 5 +
                   gameState.BLACK_QUEEN.bit_count() * 9)
    
    