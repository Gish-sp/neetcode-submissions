'''
Idea:
1: count the amount of times any element appears in the list
    if it occur more than len(nums) // 3, add it to a list res, return res
'''
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counted = Counter(nums) # dict with keys = num, values = num count
        res = []

        for val in counted:
            if counted[val]  > len(nums) // 3:
                res.append(val)
                
        return res