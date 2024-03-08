
"""
[x] Eine Methode die Eingabe vom USER holt und entscheidet welche FIGUR bewegt wurde und ändert die Bitmap
[] Eine M
[]
"""

import movements

class Chessboard:
    c_WHITE = 1
    c_BLACK = 0

    turn_Color = c_WHITE


    #Constructor - sets the default values for the board

    def __init__(self):
        self.WHITE_PAWNS   = 0b0000000000000000000000000000000000000000000000001111111100000000
        self.WHITE_ROOKS   = 0b0000000000000000000000000000000000000000000000000000000010000001
        self.WHITE_KNIGHTS = 0b0000000000000000000000000000000000000000000000000000000001000010
        self.WHITE_BISHOPS = 0b0000000000000000000000000000000000000000000000000000000000100100
        self.WHITE_QUEEN   = 0b0000000000000000000000000000000000000000000000000000000000010000
        self.WHITE_KING    = 0b0000000000000000000000000000000000000000000000000000000000001000
        self.BLACK_PAWNS   = 0b0000000011111111000000000000000000000000000000000000000000000000
        self.BLACK_ROOKS   = 0b1000000100000000000000000000000000000000000000000000000000000000
        self.BLACK_KNIGHTS = 0b0100001000000000000000000000000000000000000000000000000000000000
        self.BLACK_BISHOPS = 0b0010010000000000000000000000000000000000000000000000000000000000
        self.BLACK_QUEEN   = 0b0001000000000000000000000000000000000000000000000000000000000000
        self.BLACK_KING    = 0b0000100000000000000000000000000000000000000000000000000000000000


    def boardPrinting(self, bitboard): #python automatically passes the object as an argument to the function so I need the extra parameter 'self'
        for bit in range(64, 0, -1): #iterate from 64 (inclusive) to 0(exclusive) with step -1
            if bit % 8 == 0:
                print("")
            curr_bit = (bitboard >> bit-1) & 1 #Performs bitshifting on the bitboard and checks wheter LSB is 1 or 0. & is a binary AND operator 1&1 = 1, 0&1 = 0
            if(curr_bit == 1):
                print(curr_bit, end = " ")
            else:
                print("·", end = " ")


    #prints the entire chess board

    def entireBoardPrinting(self):
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



    #specific defined chess notation:
    #King K, Queen Q, Rook R, Bishop B, Knight N, Pawn P
    #always carry piece char along and never add any additionals like '+' or 'x' for checks and takes
    
    def inputMove(self):
        move_from = input("Please input starting position: ")
        move_to = input("Please input where the piece goes: ")
        piece = None

        #TODO: check if move is legal
        #checking if notation is correct is implemented

        #check if notation has correct length
        if len(move_from) != 3 and len(move_to) != 3:
            print(f"ERROR: Notation wrong")
            return

        #check if first char (piece) is valid
        validChars = ["K", "Q", "R", "B", "N", "P"]
        for char in validChars:
            if char == move_from[0] and char == move_to[0]:
                piece = char
        if piece is None:
            print(f"ERROR: Notation wrong or piece moved not the same")
            return
        
        #check if second char (column) is valid
        move_from_column = ord(move_from[1])
        move_to_column = ord(move_to[1])
        if not(move_from_column >= 97 and move_from_column <= 104 and move_to_column >= 97 and move_to_column <= 104):
            print(f"ERROR: Notation wrong")
            return
        
        #check if third char (row) is valid, if char is a digit
        if not(move_from[2].isdigit() and move_to[2].isdigit()):
            print(f"ERROR: Notation wrong")
            return
        move_from_row = int(move_from[2])-1
        move_to_row = int(move_to[2])-1
        #check if third char (row) is valid, if char is in valid range
        if not(move_from_row >= 0 and move_from_row <= 7 and move_to_row >= 0 and move_to_row <= 7):
            print(f"ERROR: Notation wrong")
            return
      
        field_from_numeric = (7 - move_from_column + ord('a')) + (move_from_row * 8)
        field_to_numeric = (7 - move_to_column + ord('a')) + (move_to_row * 8)

        legal_moves = self.succ.legalMoves(state, piece, field_from_numeric)

        print(f"{piece}: {field_from_numeric} to {field_to_numeric}")


    def move(self, pieceChar, startField, endField, color):
        # switch cases checks which bitbboard will be changed due to the move
        if color == self.c_WHITE:
            match pieceChar:
                case 'P':
                    self.WHITE_PAWNS = self.moveHelperFunction(self.WHITE_PAWNS, startField, endField)
                case 'N':
                    self.WHITE_KNIGHTS = self.moveHelperFunction(self.WHITE_KNIGHTS, startField, endField)
                case 'B':
                    self.WHITE_BISHOPS = self.moveHelperFunction(self.WHITE_BISHOPS, startField, endField)
                case 'R':
                    self.WHITE_ROOKS = self.moveHelperFunction(self.WHITE_ROOKS, startField, endField)
                case 'Q':
                    self.WHITE_QUEEN = self.moveHelperFunction(self.WHITE_QUEEN, startField, endField)
                case 'K':
                    self.WHITE_KING = self.moveHelperFunction(self.WHITE_KING, startField, endField)
        else:
             match pieceChar:
                case 'P':
                    self.BLACK_PAWNS = self.moveHelperFunction(self.BLACK_PAWNS, startField, endField)
                case 'N':
                    self.BLACK_KNIGHTS = self.moveHelperFunction(self.BLACK_KNIGHTS, startField, endField)
                case 'B':
                    self.BLACK_BISHOPS = self.moveHelperFunction(self.BLACK_BISHOPS, startField, endField)
                case 'R':
                    self.BLACK_ROOKS = self.moveHelperFunction(self.BLACK_ROOKS, startField, endField)
                case 'Q':
                    self.BLACK_QUEEN = self.moveHelperFunction(self.BLACK_QUEEN, startField, endField)
                case 'K':
                    self.BLACK_KING = self.moveHelperFunction(self.BLACK_KING, startField, endField)
        
    def moveHelperFunction(bitboard, startField, endField):
        piece = (bitboard >> startField) & 1
        bitboard = bitboard & ~(1 << startField)

        moveDistance = endField - startField #check how much we should bitshift
        if moveDistance > 0:
            piece <<= moveDistance
        else:
            piece >>= moveDistance
        return bitboard | (piece << startField)
    
    def checkForTakes(self, endField, color): # This method checks wheteher or not a user attacks a piece of the enemy ort not.
        if color == self.c_WHITE:
            if (self.BLACK_PAWNS >> endField) & 1: #Checks if a figure is at postion endfield
                self.BLACK_PAWNS = self.BLACK_PAWNS & ~(1 << endField) #If so the figure gets removed
            elif (self.BLACK_ROOKS >> endField) & 1:
                self.BLACK_ROOKS = self.BLACK_ROOKS & ~(1 << endField)
            elif (self.BLACK_KNIGHTS >> endField) & 1:
                self.BLACK_KNIGHTS = self.BLACK_KNIGHTS & ~(1 << endField)
            elif (self.BLACK_BISHOPS >> endField) & 1:
                self.BLACK_BISHOPS = self.BLACK_BISHOPS & ~(1 << endField)
            elif (self.BLACK_QUEEN >> endField) & 1:
                 self.BLACK_QUEEN = self.BLACK_QUEEN & ~(1 << endField)
            elif (self.BLACK_KING >> endField) & 1:
                self.BLACK_KING = self.BLACK_KING & ~(1 << endField)
        else:
            if (self.WHITE_PAWNS >> endField) & 1:
             self.WHITE_PAWNS = self.WHITE_PAWNS & ~(1 << endField)
            elif (self.WHITE_ROOKS >> endField) & 1:
                self.WHITE_ROOKS = self.WHITE_ROOKS & ~(1 << endField)
            elif (self.WHITE_KNIGHTS >> endField) & 1:
             self.WHITE_KNIGHTS = self.WHITE_KNIGHTS & ~(1 << endField)
            elif (self.WHITE_BISHOPS >> endField) & 1:
             self.WHITE_BISHOPS = self.WHITE_BISHOPS & ~(1 << endField)
            elif (self.WHITE_QUEEN >> endField) & 1:
                self.WHITE_QUEEN = self.WHITE_QUEEN & ~(1 << endField)
            elif (self.WHITE_KING >> endField) & 1:
                self.WHITE_KING = self.WHITE_KING & ~(1 << endField)


    
    
    def test(self, i):
        knight = (self.WHITE_KNIGHTS >> i) & 1
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS & ~(1 << i)
        knight = knight << 8
        self.WHITE_KNIGHTS = self.WHITE_KNIGHTS | (knight << i)


        self.boardPrinting(self.WHITE_KNIGHTS)




board = Chessboard() #create a new board object
board.entireBoardPrinting()
print("")

for i in range(30):
    board.inputMove()