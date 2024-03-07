

#implement: h_func(s)
#implement: succ(s)
#implement: terminal(s)
#implement: utility(s)


class chessBot:

    #minimax recursive algorithm with alpha-beta pruning and heuristics
    #call minimax with 'depth' set to desired max search depth and alpha = -inf, beta = +inf
    #returns utility of predicted final state and optimal next move

    #alpha-beta-pruning might be flawed

    def max_val(self, depth, h_func, s, bestmove, alpha, beta):
        #check if state is terminal state
        if self.terminal(s):
            return self.utility(s), bestmove
        
        #break when max depth reached and return its heuristic value and state
        if depth == 0:
            return h_func(s), s
        
        max_val = alpha
        current_bestmove = None

        #branch successors
        for state in self.succ(s):
            val, pre_bestmove = self.min_val(depth-1, h_func, state, bestmove, max_val, beta)

            if val > max_val:
                max_val = val
                current_bestmove = state
            
            #beta pruning
            if max_val >= beta:
                return beta, pre_bestmove

        return max_val, current_bestmove
    
    def min_val(self, depth, h_func, s, bestmove, alpha, beta):
        #check if state is terminal state
        if self.terminal(s):
            return self.utility(s), bestmove
        
        #break when max depth reached and return its heuristic value and state
        if depth == 0:
            return h_func(s)
        
        min_val = beta
        current_bestmove = None

        #branch successors
        for state in self.succ(s):
            val, pre_bestmove = self.max_val(depth-1, h_func, state, bestmove, alpha, min_val)

            if(val < min_val):
                min_val = val
                current_bestmove = state

            #alpha pruning
            if min_val <= alpha:
                return alpha, pre_bestmove

        return min_val, current_bestmove
    

    #heuristic function
    #DOING - IMPLEMENT

    def h_func(self, state) -> int:
        h = 0

        #calculate heuristic

        return h
    
    
    #successor function
    #DOING - IMPLEMENT

    def succ(self, state):
        
        #return list of successors

        return
    

    #terminal function
    #DOING - IMPLEMENT 

    def terminal(self, state) -> bool:

        #return true if terminal state

        return


    #utility function
    #DOING - IMPLEMENT

    def utility(self, state) -> int:

        #return winner: -1, 0, 1

        return

