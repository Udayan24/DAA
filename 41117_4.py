# 41117 - Udayan Chavan - P1
# Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens
# to generate the final n-queen

global N
N = 4

# To maintain remaining columns
cols = set([i for i in range(N)])

# Function to print the chess board
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# -------------------------------------------------------------
# Function to check if queen can be placed at i, j
def isSafe(board, row, col):
    # Check col wise in same row
    for i in range(col):    
        if board[row][i] == 1:
            return False

    i, j = row - 1, col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    i, j = row + 1, col + 1

    while i < N and j < N:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    i, j = row - 1, col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    i, j = row + 1, col - 1

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
        
    return True
# -------------------------------------------------------------
def NQUtil(board):
    if not cols:                # No cols remaining
        return True
    col = list(cols)[0]

    # Try placing queens in each row
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            cols.remove(col)    # Remove col from set if queen is placed
            if NQUtil(board) == True:
                return True
            cols.add(col)       # Add col back if solution was not found
            board[i][col] = 0
    return False
# -------------------------------------------------------------
def NQ():
    board = [ [0,0,1,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0] ]

    if NQUtil(board) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True
# -------------------------------------------------------------
NQ()