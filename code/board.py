
#TODO: move legality, filtering illegal moves from attackpatterns generated on a imaginary empty board

import gameInput as gameInput

# The class stores all necessary information of the game, consisting of:
# pieces, turn color, castle rights, en passant squares and secondary information (like bitboards of the borders)
# additionally, the class has print methods, as well as getter, setter and switching turn color

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
                 white_pawns = 0b0000000000000000000000000000000000000000000000001111111100000000, 
                 white_rooks = 0b0000000000000000000000000000000000000000000000000000000010000001, 
                 white_knights = 0b0000000000000000000000000000000000000000000000000000000001000010, 
                 white_bishops = 0b0000000000000000000000000000000000000000000000000000000000100100, 
                 white_queen = 0b0000000000000000000000000000000000000000000000000000000000010000, 
                 white_king = 0b0000000000000000000000000000000000000000000000000000000000001000, 
                 black_pawns = 0b0000000011111111000000000000000000000000000000000000000000000000, 
                 black_rooks = 0b1000000100000000000000000000000000000000000000000000000000000000, 
                 black_knights = 0b0100001000000000000000000000000000000000000000000000000000000000, 
                 black_bishops = 0b0010010000000000000000000000000000000000000000000000000000000000, 
                 black_queen = 0b0001000000000000000000000000000000000000000000000000000000000000, 
                 black_king = 0b0000100000000000000000000000000000000000000000000000000000000000,
                 turn_Color = 'w'
                 # TODO: castling rights
                 # TODO: en passant
                 # TODO: halfclock and fullclock
                 ):
        
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
        if turn_Color == 'w':
            self.turn_Color = self.c_WHITE
        else:
            turn_Color = self.c_BLACK

    # prints one given bitboard in binary
    def boardPrinting(self, bitboard):
        for bit in range(64, 0, -1):  # iterate from 64 (inclusive) to 0 (exclusive) with step -1
            if bit % 8 == 0:
                print("")
            # performs bitshifting on the bitboard and checks wheter LSB is 1 or 0. & is a binary AND operator 1&1 = 1, 0&1 = 0
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
    
    # switches turn color
    def switchTurn(self):
        if self.turn_Color == self.c_WHITE:
            self.turn_Color = self.c_BLACK
        else:
            self.turn_Color = self.c_WHITE

    # returns current turn color
    def getColor(self):
        return self.turn_Color
    
