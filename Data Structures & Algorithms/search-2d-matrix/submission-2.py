'''
Assertions:
    1 -> Brute force is trivial, m*n (not n^2 as there are two seperate lists)
    runtime where you return yet ifExists
    2 -> since the numbers are ordered, we can try something else. 
        We can guess where it is, and if the location we guessed is higher, than we 
        check the right side of the matrix, if smaller, the left side. 
        keep splitting until we find it. Basically binary search. 
Trials:
    1 -> Brute force proved trivial
    2 -> Binary search, things to look out for exceeding list size via indexing
        careful to stay within list bounds, check over the numbers selected
        when splitting to avoid double counting or missing items.
Conclusions:
    1 -> Brute force method does not produce the desired log(m*n) runtime, 
        trying a different method
    2 -> Binary search works with the time complexity contraints, because it
        progresses in logarithmic time. When doing it the way I've implemented, were 
        essentially just viewing the entire matrix as one giant array and then 
        splicing left and right from there.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols -1
        while left <= right:
            middle = left + (right - left) //2
            row, col = middle//cols, middle % cols
            if target > matrix[row][col]:
                left = middle + 1
            elif target < matrix[row][col]:
                right = middle -1
            else:
                return True
        return False
        