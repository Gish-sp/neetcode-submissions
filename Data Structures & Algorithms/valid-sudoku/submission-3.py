"""
Observations:
1: Checking for row and column is straight forward, iterative search
2: Can be optimized, if we search row, then column, then 3x3 box, there will 
    be overlap in the columns and rows with box 
Ideas:
1: 3 functions,
    a: checkRow(board, x, y) -> checks rows from x to y, if there are 2 of the same, return False
    b: checkColumn(board) -> if there are 2 of the same num in col, ret False
    c: checkBox(board, i_start, i_end, j_start, j_end) -> if there are dups in box ret False
2: REVISIT
    a. initially wrote the checkCols and checkRows functions for modularity with checkBox, 
        wont work that way.
    b. perhaps share a universal "seen" and this can be done with one function
"""
def checkBox(board, bi, bj):
    seen = set()
    for i in range(bi, bi+3):
        for j in range(bj, bj+3):
            v = board[i][j]
            if v == '.':
                continue
            if v in seen:
                return False
            seen.add(v)
    return True

def checkBoxes(board):
    for bi in range(0, 9, 3):
        for bj in range(0, 9, 3):
            if not checkBox(board, bi, bj):
                return False
    return True
def checkCols(board, x_start, x_end, y_start, y_end):
    seen = set()
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if board[i][j] == '.':
                continue
            if (j,board[i][j]) in seen:
                return False
            seen.add((j,board[i][j]))
    return True
def checkRows(board, x_start, x_end, y_start, y_end):
    seen = set()
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if board[i][j] == '.':
                continue
            if (i, board[i][j]) in seen:
                return False
            seen.add((i,board[i][j]))
    return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return checkRows(board,0,9,0,9) and checkCols(board,0,9,0,9) and checkBoxes(board)