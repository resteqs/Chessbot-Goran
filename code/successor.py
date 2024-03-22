
from board import Chessboard
import movement as movement

# successor function, calculates all legal moves for the position
def successors(board: Chessboard):
    legal_moves = []

    rev_b_P = 0
    rev_b_B = 0
    rev_b_N = 0
    rev_b_R = 0
    rev_b_Q = 0
    rev_b_K = 0

    if board.getColor() == board.c_WHITE:
        b_P = bin(board.WHITE_PAWNS)[2:]
        rev_b_P = b_P[::-1]
        b_B = bin(board.WHITE_BISHOPS)[2:]
        rev_b_B = b_B[::-1]
        b_N = bin(board.WHITE_KNIGHTS)[2:]
        rev_b_N = b_N[::-1]
        b_R = bin(board.WHITE_ROOKS)[2:]
        rev_b_R = b_R[::-1]
        b_Q = bin(board.WHITE_QUEEN)[2:]
        rev_b_Q = b_Q[::-1]
        b_K = bin(board.WHITE_KING)[2:]
        rev_b_K = b_K[::-1]
    else:
        b_P = bin(board.BLACK_PAWNS)[2:]
        rev_b_P = b_P[::-1]
        b_B = bin(board.BLACK_BISHOPS)[2:]
        rev_b_B = b_B[::-1]
        b_N = bin(board.BLACK_KNIGHTS)[2:]
        rev_b_N = b_N[::-1]
        b_R = bin(board.BLACK_ROOKS)[2:]
        rev_b_R = b_R[::-1]
        b_Q = bin(board.BLACK_QUEEN)[2:]
        rev_b_Q = b_Q[::-1]
        b_K = bin(board.BLACK_KING)[2:]
        rev_b_K = b_K[::-1]
    
    for i, bit in enumerate(rev_b_P):
            if bit == '1':
                legal_moves.extend(legalMoves(board, i, 'P'))
    for i, bit in enumerate(rev_b_B):
            if bit == '1':
                legal_moves.extend(legalMoves(board, i, 'B'))
    for i, bit in enumerate(rev_b_N):
            if bit == '1':
                legal_moves.extend(legalMoves(board, i, 'N'))
    for i, bit in enumerate(rev_b_R):
            if bit == '1':
                legal_moves.extend(legalMoves(board, i, 'R'))
    for i, bit in enumerate(rev_b_Q):
            if bit == '1':
                legal_moves.extend(legalMoves(board, i, 'Q'))
    for i, bit in enumerate(rev_b_K):
            if bit == '1':
                legal_moves.extend(legalMoves(board, i, 'K'))

    return legal_moves
    

# calculates all truely legal moves for one piece
def legalMoves(board: Chessboard, num_pos, piece):
    legal_moves = []
    all_boards = board.getBoard()
    color = 'w'
    if board.getColor() == board.c_BLACK:
        color = 'b'

    if piece == 'P':
        bitboard = calcPseudoPawnAttacks(board, num_pos, board.getColor()) | calcPseudoPawnCaptures(board, num_pos, board.getColor())
        b = bin(bitboard)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                succ = Chessboard(all_boards[0], all_boards[3], all_boards[2], all_boards[1], all_boards[4],  all_boards[5],
                                  all_boards[6], all_boards[9], all_boards[8], all_boards[7], all_boards[10], all_boards[11], color)
                movement.move(succ, 'P', num_pos, i)
                checks = getChecks(succ)
                if checks & (succ.BLACK_KING | succ.WHITE_KING) == 0: 
                    legal_moves.append(succ)
        
    elif piece == 'B':
        bitboard = calcPseudoBishopAttacks(board, num_pos)
        b = bin(bitboard)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                succ = Chessboard(all_boards[0], all_boards[3], all_boards[2], all_boards[1], all_boards[4],  all_boards[5],
                                  all_boards[6], all_boards[9], all_boards[8], all_boards[7], all_boards[10], all_boards[11], color)
                movement.move(succ, 'B', num_pos, i)
                checks = getChecks(succ)
                if checks & (succ.BLACK_KING | succ.WHITE_KING) == 0: 
                    legal_moves.append(succ)

    elif piece == 'N':
        bitboard = calcPseudoKnightAttacks(board, num_pos)
        b = bin(bitboard)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                succ = Chessboard(all_boards[0], all_boards[3], all_boards[2], all_boards[1], all_boards[4],  all_boards[5],
                                  all_boards[6], all_boards[9], all_boards[8], all_boards[7], all_boards[10], all_boards[11], color)
                movement.move(succ, 'N', num_pos, i)
                checks = getChecks(succ)
                if checks & (succ.BLACK_KING | succ.WHITE_KING) == 0: 
                    legal_moves.append(succ)

    elif piece == 'R':
        bitboard = calcPseudoRookAttacks(board, num_pos)
        b = bin(bitboard)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                succ = Chessboard(all_boards[0], all_boards[3], all_boards[2], all_boards[1], all_boards[4],  all_boards[5],
                                  all_boards[6], all_boards[9], all_boards[8], all_boards[7], all_boards[10], all_boards[11], color)
                movement.move(succ, 'R', num_pos, i)
                checks = getChecks(succ)
                if checks & (succ.BLACK_KING | succ.WHITE_KING) == 0: 
                    legal_moves.append(succ)

    elif piece == 'Q':
        bitboard = calcPseudoQueenAttacks(board, num_pos)
        b = bin(bitboard)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                succ = Chessboard(all_boards[0], all_boards[3], all_boards[2], all_boards[1], all_boards[4],  all_boards[5],
                                  all_boards[6], all_boards[9], all_boards[8], all_boards[7], all_boards[10], all_boards[11], color)
                movement.move(succ, 'Q', num_pos, i)
                checks = getChecks(succ)
                if checks & (succ.BLACK_KING | succ.WHITE_KING) == 0: 
                    legal_moves.append(succ)

    elif piece == 'K':
        bitboard = calcPseudoKingAttacks(board, num_pos)
        b = bin(bitboard)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                succ = Chessboard(all_boards[0], all_boards[3], all_boards[2], all_boards[1], all_boards[4],  all_boards[5],
                                  all_boards[6], all_boards[9], all_boards[8], all_boards[7], all_boards[10], all_boards[11], color)
                movement.move(succ, 'K', num_pos, i)
                checks = getChecks(succ)
                if checks & (succ.BLACK_KING | succ.WHITE_KING) == 0: 
                    legal_moves.append(succ)


    return legal_moves


# returns a bitboard of all squares that are seen by the opposing turn color (eg. if it is white's turn, it will return black checks)
#! I am not that sure how efficient this method is, but ChatGPT says its O(log n) for every for-loop, so quite efficient
#! but of course their might be better ways of iterating through a bitboard and selecting 1-bits
def getChecks(board: Chessboard):
    checks = 0
    
    board.switchTurn()
    if board.getColor() == board.c_WHITE:
        b = bin(board.WHITE_PAWNS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoPawnCaptures(board, i, board.c_WHITE)
        b = bin(board.WHITE_BISHOPS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoBishopAttacks(board, i)
        b = bin(board.WHITE_KNIGHTS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoKnightAttacks(board, i)
        b = bin(board.WHITE_ROOKS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoRookAttacks(board, i)
        b = bin(board.WHITE_QUEEN)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoQueenAttacks(board, i)
        b = bin(board.WHITE_KING)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoKingAttacks(board, i)
    else:
        b = bin(board.BLACK_PAWNS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoPawnCaptures(board, i, board.c_BLACK)
        b = bin(board.BLACK_BISHOPS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoBishopAttacks(board, i)
        b = bin(board.BLACK_KNIGHTS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoKnightAttacks(board, i)
        b = bin(board.BLACK_ROOKS)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoRookAttacks(board, i)
        b = bin(board.BLACK_QUEEN)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoQueenAttacks(board, i)
        b = bin(board.BLACK_KING)[2:]
        rev_b = b[::-1]
        for i, bit in enumerate(rev_b):
            if bit == '1':
                checks = checks | calcPseudoKingAttacks(board, i)
    board.switchTurn()
    return checks

# returns all possible pseudo pawn movements, given one position
def calcPseudoPawnAttacks(board: Chessboard, numerical_position, color):
    pawnattacks = 0
    pos = 1 << numerical_position
    pieces = board.getBlackpieces() | board.getWhitepieces()
    
    if color == board.c_WHITE: # white pawns
        if pos & board.T_BORDER == 0:
            if (pos << 8) & pieces == 0:
                pawnattacks = pawnattacks | (pos << 8) # single pawn push
                if pos & board.RANK_2 != 0 and (pos << 16) & pieces == 0:
                    pawnattacks = pawnattacks | (pos << 16) # double pawn push
    else: # black pawns
        if pos & board.B_BORDER == 0:
            if (pos >> 8) & pieces == 0:
                pawnattacks = pawnattacks | (pos >> 8) # single pawn push
                if pos & board.RANK_7 != 0 and (pos >> 16) & pieces == 0:
                    pawnattacks = pawnattacks | (pos >> 16) # double pawn push
    return pawnattacks

# returns all possible pseudo pawn captures, given one position
def calcPseudoPawnCaptures(board: Chessboard, numerical_position, color):
    pawnattacks = 0
    pos = 1 << numerical_position

    if color == board.c_WHITE: # white, so we can capture black pieces
        opp_pieces = board.getBlackpieces()
        if pos & board.T_BORDER == 0:
            if pos & board.L_BORDER == 0 and (pos << 9) & opp_pieces != 0:
                pawnattacks = pawnattacks | (pos << 9) # left diagonal capture
            if pos & board.R_BORDER == 0 and (pos << 7) & opp_pieces != 0:
                pawnattacks = pawnattacks | (pos << 7) # right diagonal capture
    else: # black, so we can capture white pieces
        opp_pieces = board.getWhitepieces()
        if pos & board.B_BORDER == 0:
            if pos & board.R_BORDER == 0 and (pos >> 9) & opp_pieces != 0:
                pawnattacks = pawnattacks | (pos >> 9) # left diagonal capture
            if pos & board.L_BORDER == 0 and (pos >> 7) & opp_pieces != 0:
                pawnattacks = pawnattacks | (pos >> 7) # right diagonal capture
    return pawnattacks
    
# returns all possible pseudo bishop movements, given one position
def calcPseudoBishopAttacks(board: Chessboard, numerical_position):
    bishopattacks = 0
    pos = 1 << numerical_position

    if board.getColor() == board.c_WHITE:
        own_pieces = board.getWhitepieces()
        opp_pieces = board.getBlackpieces()
    else:
        own_pieces = board.getBlackpieces()
        opp_pieces = board.getWhitepieces()

    # NW ray
    i = pos
    while i & board.T_BORDER == 0 and i & board.L_BORDER == 0:
        i <<= 9
        if i & own_pieces != 0:
            break
        bishopattacks = bishopattacks | i
        if i & opp_pieces != 0:
            break
    # NE ray
    i = pos
    while i & board.T_BORDER == 0 and i & board.R_BORDER == 0:
        i <<= 7
        if i & own_pieces != 0:
            break
        bishopattacks = bishopattacks | i
        if i & opp_pieces != 0:
            break
    # SW ray
    i = pos
    while i & board.B_BORDER == 0 and i & board.L_BORDER == 0:
        i >>= 7
        if i & own_pieces != 0:
            break
        bishopattacks = bishopattacks | i
        if i & opp_pieces != 0:
            break
    # SE ray
    i = pos
    while i & board.B_BORDER == 0 and i & board.R_BORDER == 0:
        i >>= 9
        if i & own_pieces != 0:
            break
        bishopattacks = bishopattacks | i
        if i & opp_pieces != 0:
            break  
    return bishopattacks
    
# returns all possible pseudo knight movements, given one position
def calcPseudoKnightAttacks(board: Chessboard, numerical_position):
    knightattacks = 0
    pos = 1 << numerical_position

    if board.getColor() == board.c_WHITE:
        own_pieces = board.getWhitepieces()
    else:
        own_pieces = board.getBlackpieces()

    if pos & (board.T_BORDER | board.G_FILE | board.R_BORDER) == 0 and (pos << 6) & own_pieces == 0:
        knightattacks = knightattacks | pos << 6 # NoEaEa
    if pos & (board.R_BORDER | board.RANK_7 | board.T_BORDER) == 0 and (pos << 15) & own_pieces == 0:
        knightattacks = knightattacks | pos << 15 # NoNoEa
    if pos & (board.L_BORDER | board.RANK_7 | board.T_BORDER) == 0 and (pos << 17) & own_pieces == 0:
        knightattacks = knightattacks | pos << 17 # NoNoWe
    if pos & (board.T_BORDER | board.B_FILE | board.L_BORDER) == 0 and (pos << 10) & own_pieces == 0:
        knightattacks = knightattacks | pos << 10 # NoWeWe
    if pos & (board.B_BORDER | board.B_FILE | board.L_BORDER) == 0 and (pos >> 6) & own_pieces == 0:
        knightattacks = knightattacks | pos >> 6 # SoWeWe
    if pos & (board.L_BORDER | board.RANK_2 | board.B_BORDER) == 0 and (pos >> 15) & own_pieces == 0:
        knightattacks = knightattacks | pos >> 15 # SoSoWe
    if pos & (board.R_BORDER | board.RANK_2 | board.B_BORDER) == 0 and (pos >> 17) & own_pieces == 0:
        knightattacks = knightattacks | pos >> 17 # SoSoEa
    if pos & (board.B_BORDER | board.G_FILE | board.R_BORDER) == 0 and (pos >> 10) & own_pieces == 0:
        knightattacks = knightattacks | pos >> 10 # SoEaEa
    return knightattacks
    
# returns all possible pseudo rook movements, given one position
def calcPseudoRookAttacks(board: Chessboard, numerical_position):
    rookattacks = 0
    pos = 1 << numerical_position

    if board.getColor() == board.c_WHITE:
        own_pieces = board.getWhitepieces()
        opp_pieces = board.getBlackpieces()
    else:
        own_pieces = board.getBlackpieces()
        opp_pieces = board.getWhitepieces()

    # N ray
    i = pos
    while i & board.T_BORDER == 0:
        i <<= 8
        if i & own_pieces != 0:
            break
        rookattacks = rookattacks | i
        if i & opp_pieces != 0:
            break
    # E ray
    i = pos
    while i & board.R_BORDER == 0:
        i >>= 1
        if i & own_pieces != 0:
            break
        rookattacks = rookattacks | i
        if i & opp_pieces != 0:
            break
    # S ray
    i = pos
    while i & board.B_BORDER == 0:
        i >>= 8
        if i & own_pieces != 0:
            break
        rookattacks = rookattacks | i
        if i & opp_pieces != 0:
            break
    # W ray
    i = pos
    while i & board.L_BORDER == 0:
        i <<= 1
        if i & own_pieces != 0:
            break
        rookattacks = rookattacks | i
        if i & opp_pieces != 0:
            break
    return rookattacks
    
# returns all possible pseudo queen movements, given one position
def calcPseudoQueenAttacks(board: Chessboard, numerical_position):
    return calcPseudoRookAttacks(board, numerical_position) | calcPseudoBishopAttacks(board, numerical_position)
    
# returns all possible pseudo king movements, given one positon
def calcPseudoKingAttacks(board: Chessboard, numerical_position):
    kingattacks = 0
    pos = 1 << numerical_position

    if board.getColor() == board.c_WHITE:
        own_pieces = board.getWhitepieces()
    else:
        own_pieces = board.getBlackpieces()
        
    if pos & board.T_BORDER == 0:
        if (pos << 8) & own_pieces == 0:
            kingattacks = kingattacks | pos << 8 # No
        if pos & board.R_BORDER == 0 and (pos << 7) & own_pieces == 0:
            kingattacks = kingattacks | pos << 7 # NoEa
        if pos & board.L_BORDER == 0 and (pos << 9) & own_pieces == 0:
            kingattacks = kingattacks | pos << 9 # NoWe
    if pos & board.B_BORDER == 0:
        if (pos >> 8) & own_pieces == 0:
            kingattacks = kingattacks | pos >> 8 # So
        if pos & board.L_BORDER == 0 and (pos >> 7) & own_pieces == 0:
            kingattacks = kingattacks | pos >> 7 # SoWe
        if pos & board.R_BORDER == 0 and (pos >> 9) & own_pieces == 0:
            kingattacks = kingattacks | pos >> 9 # SoEa
    if pos & board.L_BORDER == 0 and (pos << 1) & own_pieces == 0:
        kingattacks = kingattacks | pos << 1 # We
    if pos & board.R_BORDER == 0 and (pos >> 1) & own_pieces == 0:
        kingattacks = kingattacks | pos >> 1 # Ea
    return kingattacks