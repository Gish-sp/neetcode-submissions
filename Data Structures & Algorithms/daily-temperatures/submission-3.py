'''
Assertions:
    Going about this using with a reference return list may be easier than doing 
    edits in place. 
    Intution says recursion may be the end goal here, lets try a brute force first.
    Recursion probably not the main goal, trying to view as stack instead.
Attempts:
    First -> Try and iterate over the list for each until you find a hotter day 
    and add that to a list per item. O(n^2) -> can be reduced 
    Second -> Attempt to view as stack, keep removing from stack to find next temp
Results:
    First -> As expected, O(n^2) timed out the submission for one of the longer 
    entries. Retrying again with rescursion.
    Second -> Worked much better when viewed as a stack, enumerating over the list
    and adding the stack to store temp and indecies that havnet found a day yet, then 
    iterating over the stack to fill res made sense.
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t,i))
        return res
