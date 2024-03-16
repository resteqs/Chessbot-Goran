#MTD(f) code written in python for understanding it better
#not the code we want to use in the end



def iterativeDeepening(root, max_depth: int) -> int:

    #! innitial guess, set to 0
    f = 0

    #! run MTDF with depth 1, depth 2, ... until max depth reached
    #! this is the iterative deepining part
    for d in range(1, max_depth + 1, 1):
        f = MTDF(root, f, d)

        #! we can set a max execution time, so that every move selection always takes eg. 1 second at max
        if time_exhausted():
            break

    #! even though the desired max depth might have not been reached in the deepening process, we will just return the best guess we have
    #! this corresponds to the best guess we had at the depth of when our time was exhausted
    return f

#! root stores the game state, as well which turn it is; f is our first guess; d is our max depth for this deepening stage
def MTDF(root, f: int, d: int) -> int:

    #! writing our best guess from previous deepining stage to g
    g = f
    #! innitialization of upperbound and lowerbound, obviously
    #! upper and lowerbound creates an interval in which we will find our guess
    #! our main goal is to narrow this interval down until it only represents one value
    upperbound = float('+inf')
    lowerbound = float('-inf')

    #! run the loop until upper and lowerbound colide, meaning lowerbound == upperbound or lowerbound > upperbound
    #! this means are interval has been narrowed down to a singular value
    #! see miro.choppings inf MDTf for more info
    while lowerbound < upperbound:
        #! if we previously chopped off a piece from the left:
        #! we have to raise our beta for the AlphaBetaEnhanced call
        #! this creates a zero-window with [g, g+1] (basically the left-most window of our remaining interval)
        if g == lowerbound:
            beta = g + 1
        #! if we previously chopped off a piece from the right:
        #! we have to lower out beta for the AlphaBetaEnhanced call
        #! this creates a zero-window with [g-1, g] (basically the right-most window of our remaining interval)
        else:
            beta = g

        #! we run AlphaBetaEnhanced with beta-1 as lower bound (alpha) and beta as upper bound (beta) to create a zero-window
        #! this creates a super narrow search tree, resulting in alot of cuttings - NEED MORE INFO
        #! the call of the method will return a new guess based on the zero-window
        g = AlphaBetaEnhanced(root, beta - 1, beta, d)

        #! if the new guess is smaller than beta, we can decrease the upperbound to the new guess
        #! this decreases the right hand side of our interval (chopping off a piece on the right)
        if g < beta:
            upperbound = g
        #! else the new guess is bigger than beta, so we raise our lowerbound to g
        #! this decreases the left hand side of our interval (chopping off a piece on the left)
        else:
            lowerbound = g
    
    return g


#!very pseudo-code-ish beginning from here
#TODO complete annotations here

def AlphaBetaEnhanced(n, alpha, beta, d: int) -> int:

    #!transposition table lookup
    if node n in transposition table:
        #!return memorized values if node exists in transposition table
        if corresponding lowerbound to n >= beta:
            return corresponding lowerbound
        if corresponding upperbound to n <= alpha:
            return corresponding upperbound

    #!when max depth reached return heuristic value
    if d == 0:
        g = h_func(n)

    #!max recursive part
    if n == MAXNODE:
        g = float('-inf')
        a = alpha
        c = firstsuccessor of n

        while g < beta and c is truely a direct successor of n:
            g = max(g, AlphaBetaEnhanced(c, a, beta, d-1))
            a = max(a, g)
            c = nextsuccessor of n
    
    #!min recursive part
    else:
        g = float('+inf')
        b = beta
        c = firstsuccessor of n

        while g > alpha and c is truely a direct successor of n:
            g = min(g, AlphaBetaEnhanced(c, alpha, b, d-1))
            b = min(b, g)
            c = nextsuccessor of n
    
    #!storing values into transposition table
    if g <= alpha:
        upperbound of n = g
        store upperbound of n in transposition table
    
    if g > alpha and g < beta:
        lowerbound and upperbound of n = g
        store both bounds of n in transpostion table
    
    if g >= beta:
        lowerbound of n = g
        store lowerbound of n in transpostion table

    
    return g