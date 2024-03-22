
# Moves a piece from one square to another, does not check if that pieces exists nor if the move legal is
def move(boardObject, pieceChar, startField, endField):
    
    # Switch cases checks which bitbboard will be changed due to the move
    # Additional function checkForTakes, checks if a piece was taken at removes it
    color = boardObject.getColor()
    if color == boardObject.c_WHITE:
        if pieceChar == 'P':
            boardObject.WHITE_PAWNS = moveHelperFunction(
                boardObject.WHITE_PAWNS, startField, endField)
        elif pieceChar == 'N':
            boardObject.WHITE_KNIGHTS = moveHelperFunction(
                boardObject.WHITE_KNIGHTS, startField, endField)
        elif pieceChar == 'B':
            boardObject.WHITE_BISHOPS = moveHelperFunction(
                boardObject.WHITE_BISHOPS, startField, endField)
        elif pieceChar == 'R':
            boardObject.WHITE_ROOKS = moveHelperFunction(
                boardObject.WHITE_ROOKS, startField, endField)
        elif pieceChar == 'Q':
            boardObject.WHITE_QUEEN = moveHelperFunction(
                boardObject.WHITE_QUEEN, startField, endField)
        elif pieceChar == 'K':
            boardObject.WHITE_KING = moveHelperFunction(
                boardObject.WHITE_KING, startField, endField)
    else:
        if pieceChar == 'P':
            boardObject.BLACK_PAWNS = moveHelperFunction(
                boardObject.BLACK_PAWNS, startField, endField)
        elif pieceChar == 'N':
            boardObject.BLACK_KNIGHTS = moveHelperFunction(
                boardObject.BLACK_KNIGHTS, startField, endField)
        elif pieceChar == 'B':
            boardObject.BLACK_BISHOPS = moveHelperFunction(
                boardObject.BLACK_BISHOPS, startField, endField)
        elif pieceChar == 'R':
            boardObject.BLACK_ROOKS = moveHelperFunction(
                boardObject.BLACK_ROOKS, startField, endField)
        elif pieceChar == 'Q':
            boardObject.BLACK_QUEEN = moveHelperFunction(
                boardObject.BLACK_QUEEN, startField, endField)
        elif pieceChar == 'K':
            boardObject.BLACK_KING = moveHelperFunction(
                boardObject.BLACK_KING, startField, endField)
    checkForTakes(boardObject, endField, color)

# Helper function for clean code
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
