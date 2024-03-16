
#TODO: move legality, filtering illegal moves from attackpatterns generated on a imaginary empty board

import movements as movements
import gameInput as gameInput

#Die Klasse speichert den Zustand des Spiels. Es soll alle nötigen Bitboards selber bereitstellen. Es muss alle Bitboards selber berechenen können mit
#entsprechenden Funktionen. 
#All Black, All Whiite, All pieces, Rays of Attacks...

class Chessboard:
    c_WHITE = 1
    c_BLACK = 0

    L_BORDER = 0b1000000010000000100000001000000010000000100000001000000010000000 # equals A file
    R_BORDER = 0b0000000100000001000000010000000100000001000000010000000100000001 # equals H file
    T_BORDER = 0b1111111100000000000000000000000000000000000000000000000000000000 # equals rank 8
    B_BORDER = 0b0000000000000000000000000000000000000000000000000000000011111111 # equals rank 1

    B_FILE = 0b0100000001000000010000000100000001000000010000000100000001000000
    G_FILE = 0b0000001000000010000000100000001000000010000000100000001000000010
    RANK_2 = 0b0000000000000000000000000000000000000000000000001111111100000000
    RANK_7 = 0b0000000011111111000000000000000000000000000000000000000000000000

    # Constructor - sets the default values for the board
    def __init__(self, 
                 white_pawns=0b0000000000000000000000000000000000000000000000001111111100000000, 
                 white_rooks=0b0000000000000000000000000000000000000000000000000000000010000001, 
                 white_knights=0b0000000000000000000000000000000000000000000000000000000001000010, 
                 white_bishops=0b0000000000000000000000000000000000000000000000000000000000100100, 
                 white_queen=0b0000000000000000000000000000000000000000000000000000000000010000, 
                 white_king=0b0000000000000000000000000000000000000000000000000000000000001000, 
                 black_pawns=0b0000000011111111000000000000000000000000000000000000000000000000, 
                 black_rooks=0b1000000100000000000000000000000000000000000000000000000000000000, 
                 black_knights=0b0100001000000000000000000000000000000000000000000000000000000000, 
                 black_bishops=0b0010010000000000000000000000000000000000000000000000000000000000, 
                 black_queen=0b0001000000000000000000000000000000000000000000000000000000000000, 
                 black_king=0b0000100000000000000000000000000000000000000000000000000000000000):
        self.WHITE_PAWNS = white_pawns
        self.WHITE_ROOKS = white_rooks
        self.WHITE_KNIGHTS = white_knights
        self.WHITE_BISHOPS = white_bishops
        self.WHITE_QUEEN = white_queen
        self.WHITE_KING = white_king
        self.BLACK_PAWNS = black_pawns
        self.BLACK_ROOKS = black_rooks
        self.BLACK_KNIGHTS = black_knights
        self.BLACK_BISHOPS = black_bishops
        self.BLACK_QUEEN = black_queen
        self.BLACK_KING = black_king
        self.turn_Color = self.c_WHITE # possibly let this be set by a parameter given for flexibility

    # prints one given bitboard in binary
    def boardPrinting(self, bitboard):
        for bit in range(64, 0, -1):  # iterate from 64 (inclusive) to 0 (exclusive) with step -1
            if bit % 8 == 0:
                print("")
            # Performs bitshifting on the bitboard and checks wheter LSB is 1 or 0. & is a binary AND operator 1&1 = 1, 0&1 = 0
            curr_bit = (bitboard >> bit-1) & 1
            if (curr_bit == 1):
                print(curr_bit, end=" ")
            else:
                print("·", end=" ")

    # prints the entire chess board
    def entireBoardPrinting(self):
        entireBoard = self.WHITE_PAWNS | self.WHITE_BISHOPS | self.WHITE_KING | self.WHITE_KNIGHTS | self.WHITE_ROOKS | self.WHITE_QUEEN | self.BLACK_PAWNS | self.BLACK_BISHOPS | self.BLACK_KNIGHTS | self.BLACK_KING | self.BLACK_QUEEN | self.BLACK_ROOKS
        for bit in range(64, 0, -1):
            if bit % 8 == 0:
                print("")
            curr_bit = (entireBoard >> bit-1) & 1
            if (curr_bit == 1):
                if (curr_bit == (self.WHITE_PAWNS >> bit - 1) & 1):
                    print("P", end=" ")
                elif (curr_bit == (self.WHITE_BISHOPS >> bit - 1) & 1):
                    print("B", end=" ")
                elif (curr_bit == (self.WHITE_KNIGHTS >> bit - 1) & 1):
                    print("N", end=" ")
                elif (curr_bit == (self.WHITE_ROOKS >> bit - 1) & 1):
                    print("R", end=" ")
                elif (curr_bit == (self.WHITE_QUEEN >> bit - 1) & 1):
                    print("Q", end=" ")
                elif (curr_bit == (self.WHITE_KING >> bit - 1) & 1):
                    print("K", end=" ")
                elif (curr_bit == (self.BLACK_PAWNS >> bit - 1) & 1):
                    print("p", end=" ")
                elif (curr_bit == (self.BLACK_BISHOPS >> bit - 1) & 1):
                    print("b", end=" ")
                elif (curr_bit == (self.BLACK_KNIGHTS >> bit - 1) & 1):
                    print("n", end=" ")
                elif (curr_bit == (self.BLACK_ROOKS >> bit - 1) & 1):
                    print("r", end=" ")
                elif (curr_bit == (self.BLACK_QUEEN >> bit - 1) & 1):
                    print("q", end=" ")
                else:  # else Black King
                    print("k", end=" ")
            else:
                print("·", end=" ")

    # returns all bitboards in a list
    def getBoard(self):
        all_bitboards = [self.WHITE_PAWNS, self.WHITE_BISHOPS, self.WHITE_KNIGHTS, self.WHITE_ROOKS, self.WHITE_QUEEN, self.WHITE_KING,
                         self.BLACK_PAWNS, self.BLACK_BISHOPS, self.BLACK_KNIGHTS, self.BLACK_ROOKS, self.BLACK_QUEEN, self.BLACK_KING]
        return all_bitboards
    
    # returns all white pieces in one bitboard, making pieces undistinguishable
    def getWhitepieces(self):
        pieces = 0
        all_bitboards = self.getBoard()
        for i in range(0, 6):
            pieces = pieces ^ all_bitboards[i]
        return pieces
    
    # returns all black pieces in one bitboard, making pieces undistinguishable
    def getBlackpieces(self):
        pieces = 0
        all_bitboards = self.getBoard()
        for i in range(6, 12):
            pieces = pieces ^ all_bitboards[i]
        return pieces
    
    # returns all squares that are seen by white pieces
    def getWhitechecks(self):
        #TODO implement
        return
    
    # returns all squares that are seen by black pieces
    def getBlackchecks(self):
        #TODO implement
        return
    
    # switches turn color
    def switchTurn(self):
        if self.turn_Color == self.c_WHITE:
            self.turn_Color = self.c_BLACK
        else:
            self.turn_Color = self.c_WHITE

    # returns current turn color
    def getColor(self):
        return self.turn_Color
    
    # returns all possible pseudo pawn movements, given one position and color
    def calcPseudoPawnAttacks(self, numerical_position, color):
        pawnattacks = 0
        pos = 1 << numerical_position
        b_pieces = self.getBlackpieces
        w_pieces = self.getWhitepieces

        if color == self.c_WHITE: # white pawns
            if pos & self.T_BORDER == 0:
                if (pos << 8) & (w_pieces | b_pieces) == 0:
                    pawnattacks = pawnattacks | (pos << 8) # single pawn push
                if pos & self.RANK_2 != 0 and (pos << 16) & (w_pieces | b_pieces) == 0:
                    pawnattacks = pawnattacks | (pos << 16) # double pawn push
                if pos & self.L_BORDER == 0 and (pos << 9) & b_pieces != 0:
                    pawnattacks = pawnattacks | (pos << 9) # left diagonal capture
                if pos & self.R_BORDER == 0 and (pos << 7) & b_pieces != 0:
                    pawnattacks = pawnattacks | (pos << 7) # right diagonal capture
        else: # black pawns
            if pos & self.B_BORDER == 0:
                if (pos >> 8) & (w_pieces | b_pieces) == 0:
                    pawnattacks = pawnattacks | (pos >> 8) # single pawn push
                if pos & self.RANK_7 != 0 and (pos >> 16) & (w_pieces | b_pieces) == 0:
                    pawnattacks = pawnattacks | (pos >> 16) # double pawn push
                if pos & self.L_BORDER == 0 and (pos >> 7) & w_pieces != 0:
                    pawnattacks = pawnattacks | (pos >> 7) # left diagonal capture
                if pos & self.R_BORDER == 0 and (pos >> 9) & w_pieces != 0:
                    pawnattacks = pawnattacks | (pos >> 9) # right diagonal capture
        return pawnattacks
    
    # returns all possible pseudo bishop movements, given one position and color
    def calcPseudoBishopAttacks(self, numerical_position, color):
        bishopattacks = 0
        pos = 1 << numerical_position

        if color == self.c_WHITE:
            own_pieces = self.getWhitepieces
            opp_pieces = self.getBlackpieces
        else:
            own_pieces = self.getBlackpieces
            opp_pieces = self.getWhitepieces

        # NW ray
        i = pos
        while i & self.T_BORDER == 0 and i & self.L_BORDER == 0:
            i <<= 9
            if i & own_pieces != 0:
                break
            bishopattacks = bishopattacks | i
            if i & opp_pieces != 0:
                break
        # NE ray
        i = pos
        while i & self.T_BORDER == 0 and i & self.R_BORDER == 0:
            i <<= 7
            if i & own_pieces != 0:
                break
            bishopattacks = bishopattacks | i
            if i & opp_pieces != 0:
                break
        # SW ray
        i = pos
        while i & self.B_BORDER == 0 and i & self.L_BORDER == 0:
            i >>= 7
            if i & own_pieces != 0:
                break
            bishopattacks = bishopattacks | i
            if i & opp_pieces != 0:
                break
        # SE ray
        i = pos
        while i & self.B_BORDER == 0 and i & self.R_BORDER == 0:
            i >>= 9
            if i & own_pieces != 0:
                break
            bishopattacks = bishopattacks | i
            if i & opp_pieces != 0:
                break  
        return bishopattacks
    
    # returns all possible pseudo knight movements, given one position and color
    def calcPseudoKnightAttacks(self, numerical_position, color):
        knightattacks = 0
        pos = 1 << numerical_position

        if color == self.c_WHITE:
            own_pieces = self.getWhitepieces
        else:
            own_pieces = self.getBlackpieces

        if pos & (self.T_BORDER | self.G_FILE | self.R_BORDER) == 0 and (pos << 6) & own_pieces == 0:
            knightattacks = knightattacks | pos << 6 # NoEaEa
        if pos & (self.R_BORDER | self.RANK_7 | self.T_BORDER) == 0 and (pos << 15) & own_pieces == 0:
            knightattacks = knightattacks | pos << 15 # NoNoEa
        if pos & (self.L_BORDER | self.RANK_7 | self.T_BORDER) == 0 and (pos << 17) & own_pieces == 0:
            knightattacks = knightattacks | pos << 17 # NoNoWe
        if pos & (self.T_BORDER | self.B_FILE | self.L_BORDER) == 0 and (pos << 10) & own_pieces == 0:
            knightattacks = knightattacks | pos << 10 # NoWeWe
        if pos & (self.B_BORDER | self.B_FILE | self.L_BORDER) == 0 and (pos >> 6) & own_pieces == 0:
            knightattacks = knightattacks | pos >> 6 # SoWeWe
        if pos & (self.L_BORDER | self.RANK_2 | self.B_BORDER) == 0 and (pos >> 15) & own_pieces == 0:
            knightattacks = knightattacks | pos >> 15 # SoSoWe
        if pos & (self.R_BORDER | self.RANK_2 | self.B_BORDER) == 0 and (pos >> 17) & own_pieces == 0:
            knightattacks = knightattacks | pos >> 17 # SoSoEa
        if pos & (self.B_BORDER | self.G_FILE | self.R_BORDER) == 0 and (pos >> 10) & own_pieces == 0:
            knightattacks = knightattacks | pos >> 10 # SoEaEa
        return knightattacks
    
    # returns all possible pseudo rook movements, given one position and color
    def calcPsedoRookAttacks(self, numerical_position, color):
        rookattacks = 0
        pos = 1 << numerical_position

        if color == self.c_WHITE:
            own_pieces = self.getWhitepieces
            opp_pieces = self.getBlackpieces
        else:
            own_pieces = self.getBlackpieces
            opp_pieces = self.getWhitepieces

        # N ray
        i = pos
        while i & self.T_BORDER == 0:
            i <<= 8
            if i & own_pieces != 0:
                break
            rookattacks = rookattacks | i
            if i & opp_pieces != 0:
                break
        # E ray
        i = pos
        while i & self.R_BORDER == 0:
            i >>= 1
            if i & own_pieces != 0:
                break
            rookattacks = rookattacks | i
            if i & opp_pieces != 0:
                break
        # S ray
        i = pos
        while i & self.B_BORDER == 0:
            i >>= 8
            if i & own_pieces != 0:
                break
            rookattacks = rookattacks | i
            if i & opp_pieces != 0:
                break
        # W ray
        i = pos
        while i & self.L_BORDER == 0:
            i <<= 1
            if i & own_pieces != 0:
                break
            rookattacks = rookattacks | i
            if i & opp_pieces != 0:
                break
        return rookattacks
    
    # returns all possible pseudo queen movements, given one position and color
    def calcPseudoQueenAttacks(self, numerical_position, color):
        return self.calcPsedoRookAttacks(numerical_position, color) | self.calcPseudoBishopAttacks(numerical_position, color)
    
    # returns all possible pseudo king movements, given one positon and color
    def calcPseudoKingAttacks(self, numerical_position, color):
        kingattacks = 0
        pos = 1 << numerical_position

        if color == self.c_WHITE:
            own_pieces = self.getWhitepieces
        else:
            own_pieces = self.getBlackpieces
        
        if pos & self.T_BORDER == 0:
            if (pos << 8) & own_pieces == 0:
                kingattacks = kingattacks | pos << 8 # No
            if pos & self.R_BORDER == 0 and (pos << 7) & own_pieces == 0:
                kingattacks = kingattacks | pos << 7 # NoEa
            if pos & self.L_BORDER == 0 and (pos << 9) & own_pieces == 0:
                kingattacks = kingattacks | pos << 9 # NoWe
        if pos & self.B_BORDER == 0:
            if (pos >> 8) & own_pieces == 0:
                kingattacks = kingattacks | pos >> 8 # So
            if pos & self.L_BORDER == 0 and (pos >> 7) & own_pieces == 0:
                kingattacks = kingattacks | pos >> 7 # SoWe
            if pos & self.R_BORDER == 0 and (pos >> 9) & own_pieces == 0:
                kingattacks = kingattacks | pos >> 9 # SoEa
        if pos & self.L_BORDER == 0 and (pos << 1) & own_pieces == 0:
            kingattacks = kingattacks | pos << 1 # We
        if pos & self.R_BORDER == 0 and (pos >> 1) & own_pieces == 0:
            kingattacks = kingattacks | pos >> 1 # Ea
        return kingattacks
    

#!
#! below here only temporary testing code
#!
