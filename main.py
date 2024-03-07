#minimax recursive algorithm

#implement: terminal(s)
#implement: utility(s)
#implement: succ(s)

class chessBot:

    def max_val(self, depth, h_func, s, bestmove):
        if terminal(s):
            return utility(s), bestmove
        
        if depth == 0:
            return h_func(s)
        
        max_val = float('-inf')
        current_bestmove = None

        for state in succ(s):
            val, pre_bestmove = min_val(depth-1, h_func, state, bestmove)

            if(val > max_val):
                max_val = val
                current_bestmove = state

        return max_val, current_bestmove
    
    def min_val(self, depth, h_func, s, bestmove):
        if terminal(s):
            return utility(s)
        
        if depth == 0:
            return h_func(s)
        
        min_val = float('+inf')
        current_bestmove = None

        for state in succ(s):
            val, pre_bestmove = max_val(depth-1, h_func, state, bestmove)

            if(val < min_val):
                min_val = val
                current_bestmove = state

        return min_val, current_bestmove


