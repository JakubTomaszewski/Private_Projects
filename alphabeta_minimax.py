'''minimax algorythm, also known as alpha beta'''

def minimax(positions, depth, alpha, beta, PlayerMax):
    if depth == 0:
        if PlayerMax:
            print("Game over the winner is white")
        else:
            print("Game over the winner is NNN")
        return PlayerMax #wygrywa ten zawodnik, ktorego jest ruch

    if PlayerMax:
        max_eval = alpha
        for pos in positions:
            eval = minimax(pos, (depth-1), alpha, beta, not(PlayerMax))
            max_eval = max(eval, max_eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
            return max_eval

    else:
        max_eval = beta
        for pos in positions:
            eval = minimax(pos, (depth-1), alpha, beta, not(PlayerMax))
            min_eval = min(eval, max_eval)
            alpha = min(alpha, eval)
            if beta <= alpha:
                break
            return min_eval

alpha = -1000000
beta = 1000000
bialy = True #1
depth = 3

positions = []
for row in range(4):
    for col in range(4):
        positions.append([row,col])

print(positions)


minimax(positions, 3, alpha, beta, bialy)
