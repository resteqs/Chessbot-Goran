# specific defined chess notation:
# King K, Queen Q, Rook R, Bishop B, Knight N, Pawn P
# always carry piece char along and never add any additionals like '+' or 'x' for checks and takes
def inputMove(boardObject):
    print("\n")
    move_from = input("Please input starting position: ")
    move_to = input("Please input where the piece goes: ")
    piece = None

    # TODO: check if move is legal
    # checking if notation is correct is implemented

    ########################################
    #             castling                 #
    ########################################

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
    field_from_numeric = (7 - move_from_column +
                          ord('a')) + (move_from_row * 8)
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

    """legal_moves = boardObject.succ.legalMoves(boardObject.getBoard(), piece, field_from_numeric, boardObject.getColor())
        for move in legal_moves:
            if move == field_to_numeric:"""
    print(f"{boardObject.getColor()} {piece}: {
          field_from_numeric} to {field_to_numeric}")
    # boardObject.
    move(boardObject, piece, field_from_numeric, field_to_numeric)
    boardObject.entireBoardPrinting()
    return
    print(f"ERROR: Move not legal")


def move(boardObject, pieceChar, startField, endField):
    # switch cases checks which bitbboard will be changed due to the move. Additional function checkForTakes, checks if a piece was taken at removes it
    color = boardObject.getColor()
    if color == boardObject.c_WHITE:
        match pieceChar:
            case 'P':
                boardObject.WHITE_PAWNS = moveHelperFunction(
                    boardObject.WHITE_PAWNS, startField, endField)
            case 'N':
                boardObject.WHITE_KNIGHTS = moveHelperFunction(
                    boardObject.WHITE_KNIGHTS, startField, endField)
            case 'B':
                boardObject.WHITE_BISHOPS = moveHelperFunction(
                    boardObject.WHITE_BISHOPS, startField, endField)
            case 'R':
                boardObject.WHITE_ROOKS = moveHelperFunction(
                    boardObject.WHITE_ROOKS, startField, endField)
            case 'Q':
                boardObject.WHITE_QUEEN = moveHelperFunction(
                    boardObject.WHITE_QUEEN, startField, endField)
            case 'K':
                boardObject.WHITE_KING = moveHelperFunction(
                    boardObject.WHITE_KING, startField, endField)
    else:
        match pieceChar:
            case 'P':
                boardObject.BLACK_PAWNS = moveHelperFunction(
                    boardObject.BLACK_PAWNS, startField, endField)
            case 'N':
                boardObject.BLACK_KNIGHTS = moveHelperFunction(
                    boardObject.BLACK_KNIGHTS, startField, endField)
            case 'B':
                boardObject.BLACK_BISHOPS = moveHelperFunction(
                    boardObject.BLACK_BISHOPS, startField, endField)
            case 'R':
                boardObject.BLACK_ROOKS = moveHelperFunction(
                    boardObject.BLACK_ROOKS, startField, endField)
            case 'Q':
                boardObject.BLACK_QUEEN = moveHelperFunction(
                    boardObject.BLACK_QUEEN, startField, endField)
            case 'K':
                boardObject.BLACK_KING = moveHelperFunction(
                    boardObject.BLACK_KING, startField, endField)
    checkForTakes(boardObject, endField, color)
    boardObject.switchTurn()


def moveHelperFunction(bitboard, startField, endField):
    bitboard = bitboard & ~(1 << startField)
    return bitboard | (1 << endField)


# This method checks wheteher or not a user attacks a piece of the enemy ort not.
def checkForTakes(boardObject, endField, color):
    if color == boardObject.c_WHITE:
        if (boardObject.BLACK_PAWNS >> endField) & 1:  # Checks if a figure is at postion endfield
            boardObject.BLACK_PAWNS = boardObject.BLACK_PAWNS & ~(
                1 << endField)  # If so the figure gets removed
        elif (boardObject.BLACK_ROOKS >> endField) & 1:
            boardObject.BLACK_ROOKS = boardObject.BLACK_ROOKS & ~(
                1 << endField)
        elif (boardObject.BLACK_KNIGHTS >> endField) & 1:
            boardObject.BLACK_KNIGHTS = boardObject.BLACK_KNIGHTS & ~(
                1 << endField)
        elif (boardObject.BLACK_BISHOPS >> endField) & 1:
            boardObject.BLACK_BISHOPS = boardObject.BLACK_BISHOPS & ~(
                1 << endField)
        elif (boardObject.BLACK_QUEEN >> endField) & 1:
            boardObject.BLACK_QUEEN = boardObject.BLACK_QUEEN & ~(
                1 << endField)
        elif (boardObject.BLACK_KING >> endField) & 1:
            boardObject.BLACK_KING = boardObject.BLACK_KING & ~(1 << endField)
    else:
        if (boardObject.WHITE_PAWNS >> endField) & 1:
            boardObject.WHITE_PAWNS = boardObject.WHITE_PAWNS & ~(
                1 << endField)
        elif (boardObject.WHITE_ROOKS >> endField) & 1:
            boardObject.WHITE_ROOKS = boardObject.WHITE_ROOKS & ~(
                1 << endField)
        elif (boardObject.WHITE_KNIGHTS >> endField) & 1:
            boardObject.WHITE_KNIGHTS = boardObject.WHITE_KNIGHTS & ~(
                1 << endField)
        elif (boardObject.WHITE_BISHOPS >> endField) & 1:
            boardObject.WHITE_BISHOPS = boardObject.WHITE_BISHOPS & ~(
                1 << endField)
        elif (boardObject.WHITE_QUEEN >> endField) & 1:
            boardObject.WHITE_QUEEN = boardObject.WHITE_QUEEN & ~(
                1 << endField)
        elif (boardObject.WHITE_KING >> endField) & 1:
            boardObject.WHITE_KING = boardObject.WHITE_KING & ~(1 << endField)
