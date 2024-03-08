
#successor function

class SuccessorFunction:
    def successors(self, state, color):

        #calculate and return all possible next moves
        #run method legal_moves on every piece

        return
    

    #calculates all legal moves for a piece
    def legalMoves(self, all_bitboards, piece, numerical_position, color):
        legal_moves = []

        white_pieces = 0
        for i in range(0, 6):
            white_pieces = white_pieces ^ all_bitboards[i]
        black_pieces = 0
        for i in range(6, 13):
            black_pieces = black_pieces ^ all_bitboards[i]

        if color == 1:  #white
            match piece:
                case 'P':
                    

        return legal_moves
