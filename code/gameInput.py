

#! THE WORK ON THIS FILE IS TEMPORARILY PAUSED
#! this code is shit, needs some rework

"""

# specific defined chess notation:
# King K, Queen Q, Rook R, Bishop B, Knight N, Pawn P
# always carry piece char along and never add any additionals like '+' or 'x' for checks and takes
# castling with O-O and O-O-O as move_from and move_to

from successor import legalMoves

def inputMove(boardObject):
    print("\n")
    move_from = input("Please input starting position: ")
    move_to = input("Please input where the piece goes: ")
    piece = None
    field_from_numeric = 0
    field_to_numeric = 0

    # TODO: check if move is legal
    # checking if notation is correct is implemented

    ########################################
    #             castling                 #
    ########################################

    #Check if user has castling Rights?
    #Check if castle is possible. Checks, piece in between
    #Perform castling
    #Remove castling rights
    
    # specialized castling notation check, also specially handeled by the move and legalMoves functions
    if move_from == "O-O" and move_to == "O-O":
        board.
    elif move_from == "O-O-O" and move_to == "O-O-O":
        piece = 'K'
        field_from_numeric = -2
        field_to_numeric = -2
    
    # any other not castling move
    else:
        # check if notation has correct length
        if len(move_from) != 3 or len(move_to) != 3:
            print(f"ERROR: Notation wrong")
            return

        # check if first char (piece) is valid
        validChars = ['K', 'Q', 'R', 'B', 'N', 'P']
        for char in validChars:
            if char == move_from[0] and char == move_to[0]:
                piece = char
        if piece is None:
            print(f"ERROR: Notation wrong or piece moved not the same")
            return

        # check if second char (column) is valid
        move_from_column = ord(move_from[1])
        move_to_column = ord(move_to[1])
        if not (move_from_column >= 97 and move_from_column <= 104 and move_to_column >= 97 and move_to_column <= 104):
            print(f"ERROR: Notation wrong")
            return

        # check if third char (row) is valid, if char is a digit
        if not (move_from[2].isdigit() and move_to[2].isdigit()):
            print(f"ERROR: Notation wrong")
            return
        move_from_row = int(move_from[2])-1
        move_to_row = int(move_to[2])-1
        # check if third char (row) is valid, if char is in valid range
        if not (move_from_row >= 0 and move_from_row <= 7 and move_to_row >= 0 and move_to_row <= 7):
            print(f"ERROR: Notation wrong")
            return

        # calculate numeric positions, see FelderBitNummern.png
        field_from_numeric = (7 - move_from_column + ord('a')) + (move_from_row * 8)
        field_to_numeric = (7 - move_to_column + ord('a')) + (move_to_row * 8)

        # check if the piece actually exists on that square
        all_bitboards = boardObject.getBoard()
        if boardObject.getColor() == boardObject.c_WHITE:
            match piece:
                case 'P':
                    if not ((1 << field_from_numeric) & all_bitboards[0] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'B':
                    if not ((1 << field_from_numeric) & all_bitboards[1] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'N':
                    if not ((1 << field_from_numeric) & all_bitboards[2] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'R':
                    if not ((1 << field_from_numeric) & all_bitboards[3] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'Q':
                    if not ((1 << field_from_numeric) & all_bitboards[4] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'K':
                    if not ((1 << field_from_numeric) & all_bitboards[5] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
        else:
            match piece:
                case 'P':
                    if not ((1 << field_from_numeric) & all_bitboards[6] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'B':
                    if not ((1 << field_from_numeric) & all_bitboards[7] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'N':
                    if not ((1 << field_from_numeric) & all_bitboards[8] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'R':
                    if not ((1 << field_from_numeric) & all_bitboards[9] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'Q':
                    if not ((1 << field_from_numeric) & all_bitboards[10] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return
                case 'K':
                    if not ((1 << field_from_numeric) & all_bitboards[11] == (1 << field_from_numeric)):
                        print(f"ERROR: Piece does not exist at that position")
                        return

    # check if move legal and execute move

    legal_moves = legalMoves(boardObject.getBoard(), piece, field_from_numeric, boardObject.getColor())
    for move in legal_moves:
        if move == field_to_numeric:
            # TODO check specialized castling here
            # TODO also check promotion here
            # TODO and also gotta check en passant here
            print(f"{boardObject.getColor()} {piece}: {field_from_numeric} to {field_to_numeric}")
            move(boardObject, piece, field_from_numeric, field_to_numeric)
            boardObject.entireBoardPrinting()
            return
    print(f"ERROR: Move not legal")


"""
