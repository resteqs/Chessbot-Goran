
"""
[x] Eine Methode die Eingabe vom USER holt und entscheidet welche FIGUR bewegt wurde und ändert die Bitmap
[] Eine M
[]
"""

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

        self.L_BORDER = 0b1000000010000000100000001000000010000000100000001000000010000000 #equals A file
        self.R_BORDER = 0b0000000100000001000000010000000100000001000000010000000100000001 #equals H file
        self.T_BORDER = 0b1111111100000000000000000000000000000000000000000000000000000000 #equals rank 8
        self.B_BORDER = 0b0000000000000000000000000000000000000000000000000000000011111111 #equals rank 1

        self.AB_FILE = 0b1100000011000000110000001100000011000000110000001100000011000000
        self.GH_FILE = 0b0000001100000011000000110000001100000011000000110000001100000011
        self.RANK_12 = 0b0000000000000000000000000000000000000000000000001111111111111111
        self.RANK_87 = 0b1111111111111111000000000000000000000000000000000000000000000000

    # python automatically passes the object as an argument to the function so I need the extra parameter 'self'
    def boardPrinting(self, bitboard):
        for bit in range(64, 0, -1):  # iterate from 64 (inclusive) to 0(exclusive) with step -1
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
        print(squareattacks)
        return squareattacks
    
    def calcKnightAttacks(self, numerical_position): #knight attacks
        knightattacks = 0
        pos = 1 << numerical_position
        knightattacks = knightattacks | (pos & ~(self.R_BORDER | self.RANK_87)) << 15 #NoNoEa
        knightattacks = knightattacks | (pos & ~(self.L_BORDER | self.RANK_87)) << 17 #NoNoWe
        knightattacks = knightattacks | (pos & ~(self.T_BORDER | self.AB_FILE)) << 10 #NoWeWe
        knightattacks = knightattacks | (pos & ~(self.B_BORDER | self.AB_FILE)) >> 6  #SoWeWe
        knightattacks = knightattacks | (pos & ~(self.L_BORDER | self.RANK_12)) >> 15 #SoSoWe
        knightattacks = knightattacks | (pos & ~(self.R_BORDER | self.RANK_12)) >> 17 #SoSoEa
        knightattacks = knightattacks | (pos & ~(self.B_BORDER | self.GH_FILE)) >> 10 #SoEaEa
        knightattacks = knightattacks | (pos & ~(self.T_BORDER | self.GH_FILE)) << 6  #NoEaEa
        return knightattacks


    def test(self, i):
        knight = (self.WHITE_KNIGHTS >> i) & 1
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS & ~(1 << i)
        knight = knight << 8
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS | (knight << i)

        self.boardPrinting(self.WHITE_KNIGHTS)


board = Chessboard()  # create a new board object
board.entireBoardPrinting()
board.getBoard()


for i in range(15):
    num = int(input("Square: "))
    board.calcVerticalRayattacks(num)

for i in range(30):
    gameInput.inputMove(board)
