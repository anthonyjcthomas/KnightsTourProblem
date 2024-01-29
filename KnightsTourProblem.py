def isSafe(x, y, board):
    return (0 <= x < N and 0 <= y < N and board[x][y] == -1)

def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solveKT(n):
    board = [[-1 for i in range(n)] for i in range(n)]

    # xMove[] and yMove[] define next move of Knight
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]

    # Start from 0,0 and first move is to itself
    board[0][0] = 0
    if not solveKTUtil(n, board, 0, 0, 1, xMove, yMove):
        print("Solution does not exist")
        return False
    else:
        printSolution(n, board)
        return True

def solveKTUtil(n, board, curr_x, curr_y, movei, xMove, yMove):
    if movei == n**2:
        return True

    # Try all next moves from current coordinate x, y
    for i in range(8):
        next_x = curr_x + xMove[i]
        next_y = curr_y + yMove[i]
        if isSafe(next_x, next_y, board):
            board[next_x][next_y] = movei
            if solveKTUtil(n, board, next_x, next_y, movei + 1, xMove, yMove):
                return True
            board[next_x][next_y] = -1  # Backtracking

    return False

N = 8  # Change N based on your requirement
solveKT(N)
