
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

        self.l_border = 0b1000000010000000100000001000000010000000100000001000000010000000
        self.r_border = 0b0000000100000001000000010000000100000001000000010000000100000001
        self.t_border = 0b1111111100000000000000000000000000000000000000000000000000000000
        self.b_border = 0b0000000000000000000000000000000000000000000000000000000011111111

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
    
    def calcBishopRayattacks(self, numerical_position):
        rayattacks = 0

        #NW ray
        i = 1 << numerical_position
        while i & self.t_border == 0 and i & self.l_border == 0:
            i <<= 9
            rayattacks = rayattacks | i
        #NE ray
        i = 1 << numerical_position
        while i & self.t_border == 0 and i & self.r_border == 0:
            i <<= 7
            rayattacks = rayattacks | i
        #SW ray
        i = 1 << numerical_position
        while i & self.b_border == 0 and i & self.l_border == 0:
            i >>= 7
            rayattacks = rayattacks | i
        #SE ray
        i = 1 << numerical_position
        while i & self.b_border == 0 and i & self.r_border == 0:
            i >>= 9
            rayattacks = rayattacks | i
    
        print(bin(rayattacks))

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
    board.calcBishopRayattacks(num)

for i in range(30):
    gameInput.inputMove(board)
