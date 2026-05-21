'''
Once again, haskmaps really seem like a power tool here
I can just make a dictionary, associating the number as the key, and its
number of occurances as the vals, then return the highest val.
'''
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = Counter(nums)
        highestNum = 0
        biggestAmnt = 0
        for i in memo: 
            if memo[i] > biggestAmnt:
                highestNum = i
                biggestAmnt = memo[i]
        return highestNum