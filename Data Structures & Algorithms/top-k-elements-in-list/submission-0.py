'''
Observations:
if i just iterate through the list and map the values with a hash,
i can save time by not having to recount everything in the array
Counter library is helpful here

want to return an array
need to track the most frequent elements 
'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort the dict by values highest -> lowest
        memo = dict(sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True))
        res = []
        track = 0
        for val in memo:
            if track == k:
                break
            res.append(val)
            track += 1
        return res