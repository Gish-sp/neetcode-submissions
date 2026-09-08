'''
Truths:
Array = sorted
output -1 if not found 
output index if found
Assertions:
Array is sorted, so can try to guesstimate based on target num,
then halving the array skewed downwards if overshot, and upwards if undershot. 

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right: 
            middle = left +((right-left)//2)
            if nums[middle] >= target:
                right = middle
            elif nums[middle] < target:
                left = middle +1 
        return left if (left< len(nums) and nums[left] == target) else -1