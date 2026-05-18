'''
Observations:
need to look at everything, 
if a letter conflicts thats not the first one: stop and return the current string.


Thoughts:
sliding window? 
but then have to eval against every other item

Conclusion:
res = ""
Since i return an empty array if nothing matches, i can point at one letter,
check if all letters in the same position match for all str,
then if they dont, delete the previous letter if not the first index,
return res
if letters match:
    res.append(currently indexed letter)
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for word in range(len(strs)):
            letter = 0
            while letter < min(len(res), len(strs[word])):
                if res[letter] != strs[word][letter]:
                    break
                letter +=1
            res = res[:letter]
        return res