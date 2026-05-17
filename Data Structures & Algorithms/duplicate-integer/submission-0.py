from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = Counter(nums)
        res = False
        for i in memo:
            if memo[i] > 1:
                res = True
        return res