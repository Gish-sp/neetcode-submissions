'''
Assertions:
    1 -> Brute force is trivial, m*n (not n^2 as there are two seperate lists)
    runtime where you return yet ifExists
Trials:
    1 -> Brute force proved trivial
Conclusions:
    1 -> Brute force method does not produce the desired log(m*n) runtime, 
        trying a different method
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    print('happy')
                    return True
        return False