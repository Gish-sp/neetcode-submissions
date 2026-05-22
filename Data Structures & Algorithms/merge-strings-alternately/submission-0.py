"""
Observations:
cant exceed the index size, but need to do this in one loop -> use a while 
always has to come from word1 first, if it exists, then word2
Ideas:
1: have a counter for both words
2: Prio word 1, add its val to the list, then word 2
3: if the counter for either of the words exceeds its indices, dont append
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        count1 = 0
        count2 = 0
        while count1 < len(word1) or count2 < len(word2):
            if count1 < len(word1):
                res.append(word1[count1])
            if count2 < len(word2):
                res.append(word2[count2])
            count1 += 1
            count2 += 1
        
        return ''.join(res)