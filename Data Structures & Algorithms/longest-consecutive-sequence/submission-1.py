class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortednums = sorted(set(nums))
        resL = []
        res = 1
        if len(nums) >0:
            for i in range(len(sortednums)):
                if i == len(sortednums)-1:
                    resL.append(res)
                    break
                if sortednums[i] + 1 != sortednums[i+1]:
                    resL.append(res)
                    res = 1
                    continue
                res += 1
            print(sortednums)
            return max(resL)
        else:
            return 0