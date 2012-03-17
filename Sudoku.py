#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


def check_sudoku(sudoku):
        if len(sudoku) == len(sudoku[1]):
            check_part(sudoku)
        cols = []
        for i in range(0, len(sudoku)):
            cols.append([])
            for j in range(0, len(row)):
                cols[i].append(sudoku[j][i])
        return check_part(cols)
        else:
        return False

def check_part(part):
    for row in part:
        for i in range(1,len(row) + 1):
            if i not in row:
                return False
    return True

check_sudoku(correct)
