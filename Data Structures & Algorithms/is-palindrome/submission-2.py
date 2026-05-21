'''
Observations:
python feels like cheating here
Ideas:
1: strip the text of non alphanumericals '.join(filter(isalnum,s))
2: force lowercase 
3: return stripped == reverse(stripped)

Optimize:
Revisit later, can probably make this faster by just using two pointers 
one init at index 0 and one init at len(s) -1
Have them work into each other, if they are their values are the same the whole way
through, then return true, else false.
For odd numbers, remember that they can be the same index. Have them stop iterating when
they visit an index the other has visited
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join(filter(str.isalnum, s)).lower()
        rev_stripped = stripped[::-1]
        return stripped == rev_stripped