'''
Observations:
1: I can just sort the array in place to preserve TC
Ideas:
1: sort array,  
2: iterate through the array with a global counter initialized at 1.
    compare every number to the counter, if its equal to it, then increment the counter
    by 1, other wise dont.
    return counter
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1 
        for n in nums:
            if counter == n:
                counter += 1
        return counter 