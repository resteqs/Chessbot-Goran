
#successor function

class SuccessorFunction:
    def successors(self, state, color):

        #calculate and return all possible next moves
        #run method legal_moves on every piece

        return
    

    #calculates all (pseudo, so not checking if checks) legal moves for a piece

    def legalMoves(self, all_bitboards, piece, numerical_position, color):

        legal_moves = []

        #some initializations for code efficiency
        white_pieces = 0
        for i in range(0, 6):
            white_pieces = white_pieces ^ all_bitboards[i]
        black_pieces = 0
        for i in range(6, 12):
            black_pieces = black_pieces ^ all_bitboards[i]


        if color == 1:  #white
            match piece:
                case 'P':
                    if numerical_position >= 8 and numerical_position <= 15:
                        if ((white_pieces | black_pieces) & (1 << numerical_position << 16) == 0):
                            legal_moves.append(numerical_position + 16)
                    if numerical_position + 8 <= 63:
                        if (white_pieces | black_pieces) & (1 << numerical_position << 8) == 0:
                            legal_moves.append(numerical_position + 8)
                    if numerical_position + 8 <= 63 and numerical_position % 8 != 7:        
                        if black_pieces & (1 << numerical_position << 9) != 0:
                            legal_moves.append(numerical_position + 9)
                    if numerical_position + 8 <= 63 and numerical_position % 8 != 0:
                        if black_pieces & (1 << numerical_position << 7) != 0:
                            legal_moves.append(numerical_position + 7)


                    

        return legal_moves
