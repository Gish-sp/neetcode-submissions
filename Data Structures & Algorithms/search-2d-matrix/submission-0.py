'''
Assertions:
    1 -> Brute force is trivial, n^2 run time where you return yet ifExists
Trials:
    1 -> Brute force proved trivial
Conclusions:
    1 -> Brute force method does not produce the desired lon(m*n) runtime, 
        trying a different method
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ifExists = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    print('happy')
                    return True
        return False