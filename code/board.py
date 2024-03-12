
#TODO: move legality, filtering illegal moves from attackpatterns generated on a imaginary empty board

import movements as movements
import gameInput as gameInput
import successor as successor

#Die Klasse speichert den Zustand des Spiels. Es soll alle nötigen Bitboards selber bereitstellen. Es muss alle Bitboards selber berechenen können mit
#entsprechenden Funktionen. 
#All Black, All Whiite, All pieces, Rays of Attacks...

class Chessboard:
    c_WHITE = 1
    c_BLACK = 0

    turn_Color = c_WHITE

    L_BORDER = 0b1000000010000000100000001000000010000000100000001000000010000000 #equals A file
    R_BORDER = 0b0000000100000001000000010000000100000001000000010000000100000001 #equals H file
    T_BORDER = 0b1111111100000000000000000000000000000000000000000000000000000000 #equals rank 8
    B_BORDER = 0b0000000000000000000000000000000000000000000000000000000011111111 #equals rank 1

    B_FILE = 0b0100000001000000010000000100000001000000010000000100000001000000
    G_FILE = 0b0000001000000010000000100000001000000010000000100000001000000010
    RANK_2 = 0b0000000000000000000000000000000000000000000000001111111100000000
    RANK_7 = 0b0000000011111111000000000000000000000000000000000000000000000000

    # Constructor - sets the default values for the board
    def __init__(self):
        self.WHITE_PAWNS = 0b0000000000000000000000000000000000000000000000001111111100000000
        self.WHITE_ROOKS = 0b0000000000000000000000000000000000000000000000000000000010000001
        self.WHITE_KNIGHTS = 0b0000000000000000000000000000000000000000000000000000000001000010
        self.WHITE_BISHOPS = 0b0000000000000000000000000000000000000000000000000000000000100100
        self.WHITE_QUEEN = 0b0000000000000000000000000000000000000000000000000000000000010000
        self.WHITE_KING = 0b0000000000000000000000000000000000000000000000000000000000001000
        self.BLACK_PAWNS = 0b0000000011111111000000000000000000000000000000000000000000000000
        self.BLACK_ROOKS = 0b1000000100000000000000000000000000000000000000000000000000000000
        self.BLACK_KNIGHTS = 0b0100001000000000000000000000000000000000000000000000000000000000
        self.BLACK_BISHOPS = 0b0010010000000000000000000000000000000000000000000000000000000000
        self.BLACK_QUEEN = 0b0001000000000000000000000000000000000000000000000000000000000000
        self.BLACK_KING = 0b0000100000000000000000000000000000000000000000000000000000000000

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

    def getBoard(self):
        all_bitboards = [self.WHITE_PAWNS, self.WHITE_BISHOPS, self.WHITE_KNIGHTS, self.WHITE_ROOKS, self.WHITE_QUEEN, self.WHITE_KING,
                         self.BLACK_PAWNS, self.BLACK_BISHOPS, self.BLACK_KNIGHTS, self.BLACK_ROOKS, self.BLACK_QUEEN, self.BLACK_KING]
        return all_bitboards
    
    #returns all white pieces in one bitboard, making pieces undistinguishable
    def getWhitepieces(self):
        pieces = 0
        all_bitboards = self.getBoard()
        for i in range(0, 6):
            pieces = pieces ^ all_bitboards[i]
        return pieces
    
    #returns all black pieces in one bitboard, making pieces undistinguishable
    def getBlackpieces(self):
        pieces = 0
        all_bitboards = self.getBoard()
        for i in range(6, 12):
            pieces = pieces ^ all_bitboards[i]
        return pieces
    
    #returns all squares that are seen by white pieces
    def getWhitechecks(self):

        return
    
    #returns all squares that are seen by black pieces
    def getBlackchecks(self):
        return

    def switchTurn(self):
        if self.turn_Color == self.c_WHITE:
            self.turn_Color = self.c_BLACK
        else:
            self.turn_Color = self.c_WHITE

    def getColor(self):
        return self.turn_Color
    
    def calcDiagRayattacks(self, numerical_position): #basically bishop attacks
        rayattacks = 0
        pos = 1 << numerical_position
        #NW ray
        i = pos
        while i & self.T_BORDER == 0 and i & self.L_BORDER == 0:
            i <<= 9
            rayattacks = rayattacks | i
        #NE ray
        i = pos
        while i & self.T_BORDER == 0 and i & self.R_BORDER == 0:
            i <<= 7
            rayattacks = rayattacks | i
        #SW ray
        i = pos
        while i & self.B_BORDER == 0 and i & self.L_BORDER == 0:
            i >>= 7
            rayattacks = rayattacks | i
        #SE ray
        i = pos
        while i & self.B_BORDER == 0 and i & self.R_BORDER == 0:
            i >>= 9
            rayattacks = rayattacks | i
        return rayattacks
    
    def calcVerticalRayattacks(self, numerical_position): #basically rook attacks
        rayattacks = 0
        pos = 1 << numerical_position
        #N ray
        i = pos
        while i & self.T_BORDER == 0:
            i <<= 8
            rayattacks = rayattacks | i
        #E ray
        i = pos
        while i & self.R_BORDER == 0:
            i >>= 1
            rayattacks = rayattacks | i
        #S ray
        i = pos
        while i & self.B_BORDER == 0:
            i >>= 8
            rayattacks = rayattacks | i
        #W ray
        i = pos
        while i & self.L_BORDER == 0:
            i <<= 1
            rayattacks = rayattacks | i
        print(rayattacks)
        return rayattacks
    
    def calcSquareAttacks(self, numerical_position): #basically king attacks
        squareattacks = 0
        pos = 1 << numerical_position
        squareattacks = squareattacks | (pos & ~self.T_BORDER) << 8 #No
        squareattacks = squareattacks | (pos & ~(self.T_BORDER | self.L_BORDER)) << 9 #NoWe
        squareattacks = squareattacks | (pos & ~self.L_BORDER) << 1 #We
        squareattacks = squareattacks | (pos & ~(self.B_BORDER | self.L_BORDER)) >> 7 #SoWe
        squareattacks = squareattacks | (pos & ~self.B_BORDER) >> 8 #So
        squareattacks = squareattacks | (pos & ~(self.B_BORDER | self.R_BORDER)) >> 9 #SoEa
        squareattacks = squareattacks | (pos & ~self.R_BORDER) >> 1 #Ea
        squareattacks = squareattacks | (pos & ~(self.T_BORDER | self.R_BORDER)) << 7 #NoEa
        return squareattacks
    
    def calcPawnAttacks(self, numerical_position, color): #pawn attacks, independant if capturing or moving
        pawnattacks = 0
        pos = 1 << numerical_position 
        if color == self.c_WHITE:
            pawnattacks = pawnattacks | (pos & self.RANK_2) << 16 #double push
            pawnattacks = pawnattacks | (pos & ~self.T_BORDER) << 8 #single push
            pawnattacks = pawnattacks | (pos & ~(self.L_BORDER | self.T_BORDER)) << 9 #left diagonal capture
            pawnattacks = pawnattacks | (pos & ~(self.R_BORDER | self.T_BORDER)) << 7 #right diagonal capture
        else:
            pawnattacks = pawnattacks | (pos & self.RANK_7) >> 16 #double push
            pawnattacks = pawnattacks | (pos & ~self.B_BORDER) >> 8 #single push
            pawnattacks = pawnattacks | (pos & ~(self.L_BORDER | self.B_BORDER)) >> 7 #left diagonal capture
            pawnattacks = pawnattacks | (pos & ~(self.R_BORDER | self.B_BORDER)) >> 9 #right diagonal capture

        print(pawnattacks)
        return pawnattacks

    
    def calcKnightAttacks(self, numerical_position): #knight attacks
        knightattacks = 0
        pos = 1 << numerical_position
        knightattacks = knightattacks | (pos & ~(self.R_BORDER | self.RANK_7 | self.T_BORDER)) << 15 #NoNoEa
        knightattacks = knightattacks | (pos & ~(self.L_BORDER | self.RANK_7 | self.T_BORDER)) << 17 #NoNoWe
        knightattacks = knightattacks | (pos & ~(self.T_BORDER | self.B_FILE | self.L_BORDER)) << 10 #NoWeWe
        knightattacks = knightattacks | (pos & ~(self.B_BORDER | self.B_FILE | self.L_BORDER)) >> 6  #SoWeWe
        knightattacks = knightattacks | (pos & ~(self.L_BORDER | self.RANK_2 | self.B_BORDER)) >> 15 #SoSoWe
        knightattacks = knightattacks | (pos & ~(self.R_BORDER | self.RANK_2 | self.B_BORDER)) >> 17 #SoSoEa
        knightattacks = knightattacks | (pos & ~(self.B_BORDER | self.G_FILE | self.R_BORDER)) >> 10 #SoEaEa
        knightattacks = knightattacks | (pos & ~(self.T_BORDER | self.G_FILE | self.R_BORDER)) << 6  #NoEaEa
        return knightattacks
    

    def test(self, i):
        knight = (self.WHITE_KNIGHTS >> i) & 1
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS & ~(1 << i)
        knight = knight << 8
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS | (knight << i)

        self.boardPrinting(self.WHITE_KNIGHTS)



#!
#! below here only temporary testing code
#!

board = Chessboard()  # create a new board object
board.entireBoardPrinting()
board.getBoard()


for i in range(15):
    num = int(input("Square: "))
    board.calcKnightAttacks(num)

for i in range(30):
    gameInput.inputMove(board)