
# board class reworked as a numpy array

import numpy as np

import sys
from pympler import asizeof as pym


# indexing:
# wP, wB, wN, wR, wQ, wK, bP, bB, bN, bR, bQ, bK, turn color, castling, en passant
def createBoard():
    return np.empty(13, dtype=np.uint64)

# prints one given bitboard in binary
def boardPrinting(bitboard):
    for bit in range(64, 0, -1):  # iterate from 64 (inclusive) to 0 (exclusive) with step -1
        if bit % 8 == 0:
            print("")
        # performs bitshifting on the bitboard and checks wheter LSB is 1 or 0. & is a binary AND operator 1&1 = 1, 0&1 = 0
        curr_bit = (bitboard >> np.uint64(bit-1)) & np.uint64(1)
        if (curr_bit == np.uint64(1)):
            print("1", end=" ")
        else:
            print("·", end=" ")

# prints the entire chess board
def entireBoardPrinting(board):
    entireBoard = board[0] | board[1] | board[2] | board[3] | board[4] | board[5] | board[6] | board[7] | board[8] | board[9] | board[10] | board[11]
    for bit in range(64, 0, -1):
        if bit % 8 == 0:
            print("")
        curr_bit = (entireBoard >> np.uint64(bit-1)) & np.uint64(1)
        if (curr_bit == 1):
            if (curr_bit == (board[0] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("P", end=" ")
            elif (curr_bit == (board[1] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("B", end=" ")
            elif (curr_bit == (board[2] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("N", end=" ")
            elif (curr_bit == (board[3] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("R", end=" ")
            elif (curr_bit == (board[4] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("Q", end=" ")
            elif (curr_bit == (board[5] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("K", end=" ")
            elif (curr_bit == (board[6] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("p", end=" ")
            elif (curr_bit == (board[7] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("b", end=" ")
            elif (curr_bit == (board[8] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("n", end=" ")
            elif (curr_bit == (board[9] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("r", end=" ")
            elif (curr_bit == (board[10] >> np.uint64(bit - 1)) & np.uint64(1)):
                print("q", end=" ")
            else:  # else Black King
                print("k", end=" ")
        else:
            print("·", end=" ")
    
# returns all white pieces in one bitboard, making pieces undistinguishable
def getWhitepieces(board):
    return board[0] ^ board[1] ^ board[2] ^ board[3] ^ board[4] ^ board[5]
    
# returns all black pieces in one bitboard, making pieces undistinguishable
def getBlackpieces(board):
    return board[6] ^ board[7] ^ board[8] ^ board[9] ^ board[10] ^ board[11]
    
# switches turn color
def switchTurn(board):
    if board[12] == np.uint64(1):
        board[12] = np.uint64(0)
    else:
        board[12] = np.uint64(1)


"""
board = createBoard()
board[0] = 0b0000000000000000000000000000000000000000000000001111111100000000
board[1] = 0b0000000000000000000000000000000000000000000000000000000000100100
board[2] = 0b0000000000000000000000000000000000000000000000000000000001000010
board[3] = 0b0000000000000000000000000000000000000000000000000000000010000001
board[4] = 0b0000000000000000000000000000000000000000000000000000000000010000
board[5] = 0b0000000000000000000000000000000000000000000000000000000000001000
board[6] = 0b0000000011111111000000000000000000000000000000000000000000000000
board[7] = 0b0010010000000000000000000000000000000000000000000000000000000000
board[8] = 0b0100001000000000000000000000000000000000000000000000000000000000
board[9] = 0b1000000100000000000000000000000000000000000000000000000000000000
board[10] = 0b0001000000000000000000000000000000000000000000000000000000000000
board[11] = 0b0000100000000000000000000000000000000000000000000000000000000000
board[12] = 1

print(board)
print(board.dtype)
entireBoardPrinting(board)
boardPrinting(board[0])
boardPrinting(getBlackpieces(board))
boardPrinting(getWhitepieces(board))
print(board[12])
switchTurn(board)
print(board[12])

print(f"board size sys: {sys.getsizeof(board)}")
print(f"board size pym: {pym.asizeof(board)}")
print(f"board size np: {board.nbytes}")
"""