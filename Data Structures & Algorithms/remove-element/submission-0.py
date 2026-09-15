class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tracker = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[tracker] = nums[i]
                tracker +=1
        return tracker 
