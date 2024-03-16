from board import Chessboard

def create_bitboards_from_fen():
    fenInput = input("Enter FEN notation: ")  #example: rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1
    fen = fenInput.split()

    boardPositions = fen[0]
    color_turn = fen[1]
    castlingRights = fen[2]
    enPassant = fen[3]
    halmove = int(fen[4])
    fullmove = int(fen[5])

     # Initialize empty bitboards for each piece
    white_pawns = 0
    white_knights = 0
    white_bishops = 0
    white_rooks = 0
    white_queens = 0
    white_king = 0
    black_pawns = 0
    black_knights = 0
    black_bishops = 0
    black_rooks = 0
    black_queens = 0
    black_king = 0



    current_bit = 63
    for char in boardPositions:
        if char == '/':
            continue
        elif char.isdigit():
            current_bit -= int(char)
        elif char == 'p':
            bitmask = 1 << current_bit
            black_pawns |= bitmask
            current_bit -= 1
        elif char == 'r':
            bitmask = 1 << current_bit
            black_rooks |= bitmask
            current_bit -= 1
        elif char == 'n':
            bitmask = 1 << current_bit
            black_knights |= bitmask
            current_bit -= 1
        elif char == 'b':
            bitmask = 1 << current_bit
            black_bishops |= bitmask
            current_bit -= 1
        elif char == 'q':
            bitmask = 1 << current_bit
            black_queens |= bitmask
            current_bit -= 1
        elif char == 'k':
            bitmask = 1 << current_bit
            black_king |= bitmask
            current_bit -= 1
        elif char == 'P':
            bitmask = 1 << current_bit
            white_pawns |= bitmask
            current_bit -= 1
        elif char == 'R':
            bitmask = 1 << current_bit
            white_rooks |= bitmask
            current_bit -= 1
        elif char == 'N':
            bitmask = 1 << current_bit
            white_knights |= bitmask
            current_bit -= 1
        elif char == 'B':
            bitmask = 1 << current_bit
            white_bishops |= bitmask
            current_bit -= 1
        elif char == 'Q':
            bitmask = 1 << current_bit
            white_queens |= bitmask
            current_bit -= 1
        elif char == 'K':
            bitmask = 1 << current_bit
            white_king |= bitmask
            current_bit -= 1
   
    # Create a Chessboard object with the bitboards
    chessboard = Chessboard(white_pawns, white_knights, white_bishops, white_rooks, white_queens, white_king,
                            black_pawns, black_knights, black_bishops, black_rooks, black_queens, black_king)
    chessboard.entireBoardPrinting()


create_bitboards_from_fen()