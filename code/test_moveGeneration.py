#Testing
import cProfile as cProfile

from board import Chessboard
import successor
import cProfile as benchmark #for profiling, delete in final version

def create_bitboards_from_fen(userInput):
    fenInput = userInput  #example: rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1
    fen = fenInput.split()

    boardPositions = fen[0]
    color_turn = fen[1]
    castlingRights = fen[2]
    enPassant = fen[3]
    halfmove = int(fen[4])
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
    chessboard = Chessboard(white_pawns, white_rooks, white_knights, white_bishops, white_queens, white_king,
                            black_pawns, black_rooks, black_knights, black_bishops, black_queens, black_king, color_turn)
    # chessboard.entireBoardPrinting()
    return chessboard

def create_bitboards_from_userInput():
    create_bitboards_from_fen(input("Enter FEN notation: "))

def Perft2():
    #Perft results
    D1_NODES = 48
    D2_NODES = 2039
    D3_NODES = 97862
    D4_NODES = 4085603
    D5_NODES = 193690690
    D6_NODES = 8031647685

    fen_notation = "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 1 1"
    chessboard = create_bitboards_from_fen(fen_notation)
    boardlist = successor.successors(chessboard)
    
    for m in boardlist:
        print("")
        m.entireBoardPrinting()
    
    if(len(boardlist) == D1_NODES):
        print("SUCCESSFULL")
        print(len(boardlist))
        print(D1_NODES)
    else:
        print("FUCK")
        print(len(boardlist))
        print(D1_NODES)

def Perft1():
    #Perft results
    D1_NODES = 20
    D2_NODES = 400
    D3_NODES = 8902
    D4_NODES = 197281
    D5_NODES = 4865609
    D6_NODES = 119060324

    chessboard = Chessboard()
    boardlist = successor.successors(chessboard)
    
    if(len(boardlist) == D1_NODES):
        print("SUCCESSFULL")
        print(len(boardlist))
        print(D1_NODES)
    else:
        print("FUCK")
        print(len(boardlist))
        print(D1_NODES)

    boardlist2 = []
    for b in boardlist:
        b.switchTurn()
        boardlist2.extend(successor.successors(b))

    if(len(boardlist2) == D2_NODES):
        print("SUCCESSFULL")
        print(len(boardlist2))
        print(D2_NODES)
    else:
        print("FUCK")
        print(len(boardlist2))
        print(D2_NODES)
    
    boardlist3 = []
    for b in boardlist2:
        b.switchTurn()
        boardlist3.extend(successor.successors(b))

    if(len(boardlist3) == D3_NODES):
        print("SUCCESSFULL")
        print(len(boardlist3))
        print(D3_NODES)
    else:
        print("FUCK")
        print(len(boardlist3))
        print(D3_NODES)
    
    boardlist4 = []
    for b in boardlist3:
        b.switchTurn()
        boardlist4.extend(successor.successors(b))

    if(len(boardlist4) == D4_NODES):
        print("SUCCESSFULL")
        print(len(boardlist4))
        print(D4_NODES)
    else:
        print("FUCK")
        print(len(boardlist4))
        print(D4_NODES)
    
    """  boardlist5 = []
    for b in boardlist4:
        b.switchTurn()
        boardlist4.extend(successor.successors(b))

    if(len(boardlist5) == D5_NODES):
        print("SUCCESSFULL")
        print(len(boardlist5))
        print(D5_NODES)
    else:
        print("FUCK")
        print(len(boardlist5))
        print(D5_NODES)
    
    """
    boardlist6 = []
    for b in boardlist5:
        b.switchTurn()
        boardlist5.extend(successor.successors(b))

    if(len(boardlist6) == D6_NODES):
        print("SUCCESSFULL")
        print(len(boardlist6))
        print(D6_NODES)
    else:
        print("FUCK")
        print(len(boardlist6))
        print(D6_NODES)
    """



benchmark.run("Perft1()")