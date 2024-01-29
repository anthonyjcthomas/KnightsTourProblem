# KnightsTourProblem
Give the problem statement:
"A knight's tour is a sequence of moves by a knight on a chessboard such that the knight visits every square exactly once. If the knight ends on a square that is one knight's move from the beginning square (so that it forms a closed tour), the tour is called a "closed tour", otherwise, it's an "open tour". Given an N×N chessboard, your task is to write a program to find a knight's tour starting from a specific square." 
I built this Recursive-Backtracking Algorithm. My approach to this was to try all possible paths the knight could take and check if the tour could be completed and print out the solution, otherwise, it backtracked and tried another move. 
The first function I programmed was "isSafe" which tells the knight whether or not it can move to a square:



def isSafe(x, y, board):

return (0 <= x < N and 0 <= y < N and board[x][y] == -1)

x: The x-coordinate(row)

y: The y-coordinate (column) 

board: The chessboard is represented as a 2D matrix or list of lists. Each cell of the board is either marked with -1 which means it hasn't visited that square or a non-negative integer which tells the knight it's been there and which turn it visited it.

returns: true if the x,y coordinate is within the board boundaries and the knight has not yet visited it and vice versa if false.



The second function I made was just a simple "printSolution" function.



def printSolution(n, board):

for i in range(n):

for j in range(n):

print(board[i][j], end=' ')

print()

n: size of the board

board: solution matrix again

prints out each cell of the board followed by a space



The third function I made was the "solveKTUtil"  a recursive function where all the magic happens.



def solveKTUtil(n, board, curr_x, curr_y, movei, xMove, yMove):

if movei == n**2:

return True



'#' Try all next moves from current coordinate x, y

for i in range(8):

next_x = curr_x + xMove[i]

next_y = curr_y + yMove[i]

if isSafe(next_x, next_y, board):

board[next_x][next_y] = movei

if solveKTUtil(n, board, next_x, next_y, movei + 1, xMove, yMove):

return True

board[next_x][next_y] = -1 # Backtracking



return False



if movei == n**2:  - If the number of moves equals the number of squares on the board, a solution is found.



for i in range(8) - tries each of the 8 possible moves of the knight.



next_x = curr_x + xMove[i] and next_y = curr_y + yMove[i] calculate the next position based on the current move.



if isSafe(next_x, next_y, board) - checks if the next move is safe



board[next_x][next_y] = movei - marks the board with the current move number



if solveKTUtil(n, board, next_x, next_y, movei + 1, xMove, yMove) - Recursively calls itself to try the next move, returns true if it finds the solution



board[next_x][next_y] = -1 - backtracks the square and tries the next move





The fourth function "solveKT" is the the main function that initiates the Knight's Tour solution.



def solveKT(n):

board = [[-1 for i in range(n)] for i in range(n)]



'#' xMove[] and yMove[] define next move of Knight

xMove = [2, 1, -1, -2, -2, -1, 1, 2]

yMove = [1, 2, 2, 1, -1, -2, -2, -1]



'x'Start from 0,0 and first move is to itself

board[0][0] = 0

if not solveKTUtil(n, board, 0, 0, 1, xMove, yMove):

print("Solution does not exist")

return False

else:

printSolution(n, board)

return True



board = [[-1 for i in range(n)] for i in range(n)] - Creates an n x n chessboard initialized with -1, indicating that no cell has been visited.



xMove and yMove arrays define the 8 possible moves of a knight on the chessboard.



board[0][0] = 0 - The knight starts at the top-left corner of the board, and this cell is marked 0



The solveKTUtil function is called with the initial parameters. If this function returns False, it means a solution doesn't exist, and it prints "Solution does not exist".



If it returns True, the printSolution function is called to print the completed tour.



And the final 2 lines of code are:

N = 8 - Sets the size of the chessboard.

solveKT(N) - Calls the solveKT function to find and print the Knight's Tour on an 8x8 chessboard.



When ran this was the final ouput:

0 59 38 33 30 17 8 63

37 34 31 60 9 62 29 16

58 1 36 39 32 27 18 7

35 48 41 26 61 10 15 28

42 57 2 49 40 23 6 19

47 50 45 54 25 20 11 14

56 43 52 3 22 13 24 5

51 46 55 44 53 4 21 12
