
# TODO implement detecting endgame



import board




# heuristic megafunction
def gogos_little_brain(gameState: board.Chessboard):
    if isDraw_heuristic(): #if a draw return 0
        return 0
    return (difference_of_pieces(gameState) + piece_tables(gameState))

def count_piecese(gameState: board.Chessboard):
    return (gameState.WHITE_PAWNS.bit_count(), gameState.WHITE_KNIGHTS.bit_count(), gameState.WHITE_BISHOPS.bit_count(),
            gameState.WHITE_ROOKS.bit_count(), gameState.WHITE_QUEEN.bit_count(),gameState.BLACK_PAWNS.bit_count(),
            gameState.BLACK_BISHOPS.bit_count(), gameState.BLACK_KNIGHTS.bit_count(), gameState.BLACK_ROOKS.bit_count(),
            gameState.BLACK_QUEEN.bit_count()
            )

#Here i store the number of each piece in the game (besides kings, but... yeah...)
w_pnum, w_knnum, w_bnum, w_rnum, w_qnum, b_pnum, b_knnum, b_bnum, b_rnum, b_qnum = count_piecese()

def difference_of_pieces(gameState: board.Chessboard):
    # sums the value of the pieces of each color and returns the difference
    # 100, 400, 410, 600, 1200 as in CentiPawns
    white_Value = w_pnum * 100 + w_knnum *400 + w_bnum *410 + w_rnum * 600 + w_qnum * 1200
    black_Value = b_pnum * 100 + b_knnum * 400 + b_bnum * 410 + b_rnum * 600 + b_qnum * 1200
    return white_Value - black_Value

def isEndgame(gameState: board.Chessboard):
    def isEndgame(gameState: board.Chessboard):
        if gameState.WHITE_PAWNS.bit_count() + gameState.WHITE_BISHOPS.bit_count() + gameState.WHITE_KNIGHTS.bit_count() + gameState.WHITE_ROOKS.bit_count() + gameState.WHITE_QUEEN.bit_count() + gameState.BLACK_PAWNS.bit_count() + gameState.BLACK_BISHOPS.bit_count() + gameState.BLACK_KNIGHTS.bit_count() + gameState.BLACK_ROOKS.bit_count() + gameState.BLACK_QUEEN.bit_count() < 10:
            return True
        else:
            return False


def piece_tables():
    return pieceTablesWhite(gameState) - pieceTablesBlack(gameState)


PST_PAWNS = (
    [   0,   0,   0,   0,   0,   0,  0,   0,
       98, 134,  61,  95,  68, 126, 34, -11,
       -6,   7,  26,  31,  65,  56, 25, -20,
      -14,  13,   6,  21,  23,  12, 17, -23,
      -27,  -2,  -5,  12,  17,   6, 10, -25,
      -26,  -4,  -4, -10,   3,   3, 33, -12,
      -35,  -1, -20, -23, -15,  24, 38, -22,
        0,   0,   0,   0,   0,   0,  0,   0]
    )
PST_KNIGHTS = (
    [-167, -89, -34, -49,  61, -97, -15,-107,
      -73, -41,  72,  36,  23,  62,   7, -17,
      -47,  60,  37,  65,  84, 129,  73,  44,
       -9,  17,  19,  53,  37,  69,  18,  22,
      -13,   4,  16,  13,  28,  19,  21,  -8,
      -23,  -9,  12,  10,  19,  17,  25, -16,
      -29, -53, -12,  -3,  -1,  18, -14, -19,
     -105, -21, -58, -33, -17, -28, -19, -23]
    )

PST_BISHOPS = (
    [ -29,   4, -82, -37, -25, -42,   7,  -8,
      -26,  16, -18, -13,  30,  59,  18, -47,
      -16,  37,  43,  40,  35,  50,  37,  -2,
       -4,   5,  19,  50,  37,  37,   7,  -2,
       -6,  13,  13,  26,  34,  12,  10,   4,
        0,  15,  15,  15,  14,  27,  18,  10,
        4,  15,  16,   0,   7,  21,  33,   1,
      -33,  -3, -14, -21, -13, -12, -39, -21]
    )

PST_ROOKS = (
    [  32,  42,  32,  51,  63,   9,  31,  43,
       27,  32,  58,  62,  80,  67,  26,  44,
       -5,  19,  26,  36,  17,  45,  61,  16,
      -24, -11,   7,  26,  24,  35,  -8, -20,
      -36, -26, -12,  -1,   9,  -7,   6, -23,
      -45, -25, -16, -17,   3,   0,  -5, -33,
      -44, -16, -20,  -9,  -1,  11,  -6, -71,
      -19, -13,   1,  17,  16,   7, -37, -26]
    )

PST_QUEEN = (
    [ -28,   0,  29,  12,  59,  44,  43,  45,
      -24, -39,  -5,   1, -16,  57,  28,  54,
      -13, -17,   7,   8,  29,  56,  47,  57,
      -27, -27, -16, -16,  -1,  17,  -2,   1,
       -9, -26,  -9, -10,  -2,  -4,   3,  -3,
      -14,   2, -11,  -2,  -5,   2,  14,   5,
      -35,  -8,  11,   2,   8,  15,  -3,   1,
       -1, -18,  -9,  10, -15, -25, -31, -50]
    )

PST_KING = (
    [ -65,  23,  16, -15, -56, -34,   2,  13,
       29,  -1, -20,  -7,  -8,  -4, -38, -29,
       -9,  24,   2, -16, -20,   6,  22, -22,
      -17, -20, -12, -27, -30, -25, -14, -36,
      -49,  -1, -27, -39, -46, -44, -33, -51,
      -14, -14, -22, -46, -44, -30, -15, -27,
        1,   7,  -8, -64, -43, -16,   9,   8,
      -15,  36,  12, -54,   8, -28,  24,  14]
    )


####################################################
# Endgame
####################################################


PST_PAWNS_EG = (
    [   0,   0,   0,   0,   0,   0,   0,   0,
      178, 173, 158, 134, 147, 132, 165, 187,
       94, 100,  85,  67,  56,  53,  82,  84,
       32,  24,  13,   5,  -2,   4,  17,  17,
       13,   9,  -3,  -7,  -7,  -8,   3,  -1,
        4,   7,  -6,   1,   0,  -5,  -1,  -8,
       13,   8,   8,  10,  13,   0,   2,  -7,
        0,   0,   0,   0,   0,   0,   0,   0]
)

PST_KNIGHTS_EG = (
    [ -58, -38, -13, -28, -31, -27, -63, -99,
      -25,  -8, -25,  -2,  -9, -25, -24, -52,
      -24, -20,  10,   9,  -1,  -9, -19, -41,
      -17,   3,  22,  22,  22,  11,   8, -18,
      -18,  -6,  16,  25,  16,  17,   4, -18,
      -23,  -3,  -1,  15,  10,  -3, -20, -22,
      -42, -20, -10,  -5,  -2, -20, -23, -44,
      -29, -51, -23, -15, -22, -18, -50, -64]
)

PST_BISHOPS_EG = (
    [ -14, -21, -11,  -8,  -7,  -9, -17, -24,
       -8,  -4,   7, -12,  -3, -13,  -4, -14,
        2,  -8,   0,  -1,  -2,   6,   0,   4,
       -3,   9,  12,   9,  14,  10,   3,   2,
       -6,   3,  13,  19,   7,  10,  -3,  -9,
      -12,  -3,   8,  10,  13,   3,  -7, -15,
      -14, -18,  -7,  -1,   4,  -9, -15, -27,
      -23,  -9, -23,  -5,  -9, -16,  -5, -17]
)

PST_ROOKS_EG = (
    [  13,  10,  18,  15,  12,  12,   8,   5,
       11,  13,  13,  11,  -3,   3,   8,   3,
        7,   7,   7,   5,   4,  -3,  -5,  -3,
        4,   3,  13,   1,   2,   1,  -1,   2,
        3,   5,   8,   4,  -5,  -6,  -8, -11,
       -4,   0,  -5,  -1,  -7, -12,  -8, -16,
       -6,  -6,   0,   2,  -9,  -9, -11,  -3,
       -9,   2,   3,  -1,  -5, -13,   4, -20]
)

PST_QUEEN_EG = (
    [  -9,  22,  22,  27,  27,  19,  10,  20,
      -17,  20,  32,  41,  58,  25,  30,   0,
      -20,   6,   9,  49,  47,  35,  19,   9,
        3,  22,  24,  45,  57,  40,  57,  36,
      -18,  28,  19,  47,  31,  34,  39,  23,
      -16, -27,  15,   6,   9,  17,  10,   5,
      -22, -23, -30, -16, -16, -23, -36, -32,
      -33, -28, -22, -43,  -5, -32, -20, -41]
)

PST_KING_EG = (
    [ -74, -35, -18, -18, -11,  15,   4, -17,
      -12,  17,  14,  17,  17,  38,  23,  11,
       10,  17,  23,  15,  20,  45,  44,  13,
       -8,  22,  24,  27,  26,  33,  26,   3,
      -18,  -4,  21,  24,  27,  23,   9, -11,
      -19,  -3,  11,  21,  23,  16,   7,  -9,
      -27, -11,   4,  13,  14,   4,  -5, -17,
      -53, -34, -21, -11, -28, -14, -24, -43]
)


def pieceTablesBlack(gameState: board.Chessboard):
    # PAWNS
    score = 0
    if isEndgame() == False:
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_PAWNS >> bit - 1) & 1
            if (curr_bit == 1):
                score += PST_PAWNS[bit - 1]
        # KNIGHTS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_KNIGHTS >> bit - 1) & 1
            if (curr_bit == 1):
                score += PST_KNIGHTS[bit - 1]
        # BISHOPS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_BISHOPS >> bit - 1) & 1
            if (curr_bit == 1):
                score += PST_BISHOPS[bit - 1]
        # ROOKS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_ROOKS >> bit - 1) & 1
            if (curr_bit == 1):
                score += PST_ROOKS[bit - 1]
        # QUEEN
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_QUEEN >> bit - 1) & 1
            if (curr_bit == 1):
                score += PST_QUEEN[bit - 1]
        # KING
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_KING >> bit - 1) & 1
            if (curr_bit == 1):
                score += PST_KING[bit - 1]
    else:
        # PAWNS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_PAWNS >> bit - 1) & 1
            if curr_bit == 1:
                score += PST_PAWNS_EG[bit - 1]
        # KNIGHTS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_KNIGHTS >> bit - 1) & 1
            if curr_bit == 1:
                score += PST_KNIGHTS_EG[bit - 1]
        # BISHOPS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_BISHOPS >> bit - 1) & 1
            if curr_bit == 1:
                score += PST_BISHOPS_EG[bit - 1]
        # ROOKS
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_ROOKS >> bit - 1) & 1
            if curr_bit == 1:
                score += PST_ROOKS_EG[bit - 1]
        # QUEEN
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_QUEEN >> bit - 1) & 1
            if curr_bit == 1:
                score += PST_QUEEN_EG[bit - 1]
        # KING
        for bit in range(1, 65):
            curr_bit = (gameState.BLACK_KING >> bit - 1) & 1
            if curr_bit == 1:
                score += PST_KING_EG[bit - 1]
    return score

def pieceTablesWhite(gameState: board.Chessboard):
        # PAWNS
        score = 0
        if isEndgame() == False:
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_PAWNS >> bit - 1) & 1
                if (curr_bit == 1):
                    score += PST_PAWNS[64-bit]
            # KNIGHTS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_KNIGHTS >> bit - 1) & 1
                if (curr_bit == 1):
                    score += PST_KNIGHTS[64-bit]
            # BISHOPS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_BISHOPS >> bit - 1) & 1
                if (curr_bit == 1):
                    score += PST_BISHOPS[64-bit]
            # ROOKS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_ROOKS >> bit - 1) & 1
                if (curr_bit == 1):
                    score += PST_ROOKS[64-bit]
            # QUEEN
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_QUEEN >> bit - 1) & 1
                if (curr_bit == 1):
                    score += PST_QUEEN[64-bit]
            # KING
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_KING >> bit - 1) & 1
                if (curr_bit == 1):
                    score += PST_KING[64-bit]
        else:
            #PAWNS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_PAWNS >> bit - 1) & 1
                if curr_bit == 1:
                    score += PST_PAWNS_EG[64 - bit]
            # KNIGHTS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_KNIGHTS >> bit - 1) & 1
                if curr_bit == 1:
                    score += PST_KNIGHTS_EG[64 - bit]
            # BISHOPS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_BISHOPS >> bit - 1) & 1
                if curr_bit == 1:
                    score += PST_BISHOPS_EG[64 - bit]
            # ROOKS
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_ROOKS >> bit - 1) & 1
                if curr_bit == 1:
                    score += PST_ROOKS_EG[64 - bit]
            # QUEEN
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_QUEEN >> bit - 1) & 1
                if curr_bit == 1:
                    score += PST_QUEEN_EG[64 - bit]
            # KING
            for bit in range(1, 65):
                curr_bit = (gameState.WHITE_KING >> bit - 1) & 1
                if curr_bit == 1:
                    score += PST_KING_EG[64 - bit]
            return score
        return score

def isDraw_heuristic(gameState: board.Chessboard):
    #1. Test insufficient material
    # sum all pieces
    sum = w_pnum + w_knnum +  w_bnum +  w_rnum + w_qnum + b_pnum + b_knnum + b_bnum + b_rnum + b_qnum
    if sum == 1 and (w_knnum == 1 or b_knnum == 1 or b_bnum or w_bnum):
        #draw
        pass
    elif sum == 2 and (w_knnum == 2 or b_knnum == 2):
        #draw
        pass
        #!The following are "almost" draws. They are cituations were the chance of either side to win is nearly 0
        #!My idea is to simplify them into draws so that we try to avoid the situations just in case
    elif sum == 2 and ((w_knnum == 1 and w_knnum == 1) or (w_knnum == 1 and b_bnum == 1) or (w_bnum == 1 or b_knnum == 1)):
        #almost draw
        pass




        
