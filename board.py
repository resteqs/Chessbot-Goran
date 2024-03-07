def mainMethod():
    WHITE_PAWNS = 0b0000000000000000000000000000000000000000000000001111111100000000
    boardPrinting(WHITE_PAWNS)

def boardPrinting(bitboard):
    for bit in range(64):
        if bit % 8 == 0:
            print("")
        curr_bit = (bitboard >> bit) & 1
        if(curr_bit == 1):
            print(curr_bit, end = " ")
        else:
            print("·", end = " ")





mainMethod()