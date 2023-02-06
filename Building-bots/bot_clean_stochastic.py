"""A deterministic environment is one where the next state is completely determined by the current state of the environment and the task executed by the agent. If there is any randomness involved in determining the next state, the environment is stochastic.

The game Bot Clean took place in a deterministic environment. In this version, the bot is given 200 moves to clean as many dirty cells as possible. The grid initially has 1 dirty cell. When the bot cleans this cell, a new cell in the grid is made dirty. The new cell can be anywhere in the grid.

The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to appropriate dirty cell and clean it."""

def nextMove(posr, posc, board):
    bot_clean = (0,0)
    for i in range(len(board)):
        grid = board[i]
        if 'd' in grid:
            bot_clean = (i, grid.index('d'))
            break
    v, z = bot_clean
    if v > posr :
        print("DOWN")
        return
    elif v < posr:
        print("UP")
        return
    if z > posc :
        print("RIGHT")
        return
    elif z < posc :  
        print("LEFT")
        return
    if (v,z) == (posr, posc) :
        print("CLEAN")
        return
    
    print("")