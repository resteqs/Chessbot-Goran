"""
[] Eine Methode die Eingabe vom USER holt und entscheidet welche FIGUR bewegt wurde und ändert die Bitmap
[] Eine M
[]
"""
import movements

class Chessboard:
    c_WHITE = 1
    c_BLACK = 0

    turn_Color = c_WHITE

    def __init__(self): #Konstruktor. It sets the default values for the board
        self.WHITE_PAWNS =   0b0000000000000000000000000000000000000000000000001111111100000000
        self.WHITE_ROOKS =   0b0000000000000000000000000000000000000000000000000000000010000001
        self.WHITE_KNIGHTS = 0b0000000000000000000000000000000000000000000000000000000001000010
        self.WHITE_BISHOPS = 0b0000000000000000000000000000000000000000000000000000000000100100
        self.WHITE_QUEEN =   0b0000000000000000000000000000000000000000000000000000000000010000
        self.WHITE_KING =    0b0000000000000000000000000000000000000000000000000000000000001000
        self.BLACK_PAWNS =   0b0000000011111111000000000000000000000000000000000000000000000000
        self.BLACK_ROOKS =   0b1000000100000000000000000000000000000000000000000000000000000000
        self.BLACK_KNIGHTS = 0b0100001000000000000000000000000000000000000000000000000000000000
        self.BLACK_BISHOPS = 0b0010010000000000000000000000000000000000000000000000000000000000
        self.BLACK_QUEEN =   0b0001000000000000000000000000000000000000000000000000000000000000
        self.BLACK_KING =    0b0000100000000000000000000000000000000000000000000000000000000000
    def boardPrinting(self, bitboard): #python automatically passes the object as an argument to the function so i need an extra parameter self
        for bit in range(64, 0, -1): #iterate from 64 (inclusive) to 0(exclusive) with step -1
            if bit % 8 == 0:
                print("")
            curr_bit = (bitboard >> bit-1) & 1 #Performs bitshifting on the bitboard and checks wheter LSB is 1 or 0. & is a binary AND operator 1&1 = 1; 0&1 = 0
            if(curr_bit == 1):
                print(curr_bit, end = " ")
            else:
                print("·", end = " ")
    def entireBoardPrinting(self): #prints the entire chess board
        entireBoard = self.WHITE_PAWNS | self.WHITE_BISHOPS | self.WHITE_KING | self.WHITE_KNIGHTS | self.WHITE_ROOKS | self.WHITE_QUEEN | self.BLACK_PAWNS | self.BLACK_BISHOPS | self.BLACK_KNIGHTS | self.BLACK_KING | self.BLACK_QUEEN | self.BLACK_ROOKS
        for bit in range (64, 0, -1):
            if bit % 8 == 0:
                print("")
            curr_bit = (entireBoard >> bit-1) & 1
            if(curr_bit == 1):
                if(curr_bit == (self.WHITE_PAWNS >> bit - 1) & 1 ):
                    print("P", end = " ")
                elif(curr_bit == (self.WHITE_BISHOPS >> bit - 1) & 1):
                    print("B", end = " ")
                elif(curr_bit == (self.WHITE_KNIGHTS >> bit - 1) & 1):
                    print("N", end = " ")
                elif(curr_bit == (self.WHITE_ROOKS >> bit - 1) & 1):
                    print("R", end = " ")
                elif(curr_bit == (self.WHITE_QUEEN >> bit - 1) & 1):
                    print("Q", end = " ")
                elif(curr_bit == (self.WHITE_KING >> bit - 1) & 1):
                    print("K", end = " ")
                elif(curr_bit == (self.BLACK_PAWNS >> bit - 1) & 1):
                    print("p", end = " ")
                elif(curr_bit == (self.BLACK_BISHOPS >> bit - 1) & 1):
                    print("b", end = " ")
                elif(curr_bit == (self.BLACK_KNIGHTS >> bit - 1) & 1):
                    print("n", end = " ")
                elif(curr_bit == (self.BLACK_ROOKS >> bit - 1) & 1):
                    print("r", end = " ")
                elif(curr_bit == (self.BLACK_QUEEN >> bit - 1) & 1):
                    print("q", end = " ")
                else: #else Black King
                    print("k", end = " ")
            else:
                print("·", end = " ")

    def switchTurn(self):
        if self.turn_Color == self.c_WHITE:
            self.turn_Color == self.c_BLACK
        else:
            self.turn_Color = self.c_WHITE
    def inputMove(self):
        move_start = input("Please input starting position: ")
        move_end = input("Please input where the piece goes: ")
        #TODO: Is move valid? 
        #Specify the starting figure and point where it goes
        piece = move_start[0]
        field_start = move_start[1:]
        field_end = move_end[1:]

        field_start_numeric = (7 - ord(field_start[0]) - ord('a')) + (int(field_start[1]) - 1) * 8 #irgendwas ist hier falsch. ich möchte z.B f3 zu 18 übersetzen

        print(field_start_numeric)





    """
    << 1 moves left
    << 8 moves forward
    >> 1 moves right
    >> 8 moves backwards
    << 7 moves top right
    << 9 moves top left
    >> 7 moves bottom left
    >> 9 moves top right
              \ | /
           1  - 0 - 1
              / | 
    """
    def test(self, i):
        knight = (self.WHITE_KNIGHTS >> i) & 1
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS & ~(1 << i)
        knight = knight << 8
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS | (knight << i)


        self.boardPrinting(self.WHITE_KNIGHTS)




board = Chessboard() #create a new board object
board.entireBoardPrinting()
board.inputMove()