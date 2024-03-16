
from board import Chessboard

#successor function
def successors(board: Chessboard):

    #calculate and return all possible next moves
    #run method legalMoves on every piece

    return
    

#calculates all truely legal moves for a piece
def legalMoves(board: Chessboard, numerical_position, piece):

    legal_moves = []

    match piece:
        case 'P':
            pass
        case 'B':
            pass
        case 'N':
            pass
        case 'R':
            pass
        case 'Q':
            pass
        case 'K':
            pass

    return legal_moves


# returns all squares that are seen by white pieces
def getWhitechecks(self):
    #TODO implement
    return
   
# returns all squares that are seen by black pieces
def getBlackchecks(self):
    #TODO implement
    return

# returns all possible pseudo pawn movements, given one position
def calcPseudoPawnAttacks(board: Chessboard, numerical_position):
    pawnattacks = 0
    pos = 1 << numerical_position
    b_pieces = board.getBlackpieces()
    w_pieces = board.getWhitepieces()
    
    if board.getColor() == board.c_WHITE: # white pawns
        if pos & board.T_BORDER == 0:
            if (pos << 8) & (w_pieces | b_pieces) == 0:
                pawnattacks = pawnattacks | (pos << 8) # single pawn push
            if pos & board.RANK_2 != 0 and (pos << 16) & (w_pieces | b_pieces) == 0:
                pawnattacks = pawnattacks | (pos << 16) # double pawn push
            if pos & board.L_BORDER == 0 and (pos << 9) & b_pieces != 0:
                pawnattacks = pawnattacks | (pos << 9) # left diagonal capture
            if pos & board.R_BORDER == 0 and (pos << 7) & b_pieces != 0:
                pawnattacks = pawnattacks | (pos << 7) # right diagonal capture
    else: # black pawns
        if pos & board.B_BORDER == 0:
            if (pos >> 8) & (w_pieces | b_pieces) == 0:
                pawnattacks = pawnattacks | (pos >> 8) # single pawn push
            if pos & board.RANK_7 != 0 and (pos >> 16) & (w_pieces | b_pieces) == 0:
                pawnattacks = pawnattacks | (pos >> 16) # double pawn push
            if pos & board.L_BORDER == 0 and (pos >> 7) & w_pieces != 0:
                pawnattacks = pawnattacks | (pos >> 7) # left diagonal capture
            if pos & board.R_BORDER == 0 and (pos >> 9) & w_pieces != 0:
                pawnattacks = pawnattacks | (pos >> 9) # right diagonal capture
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
