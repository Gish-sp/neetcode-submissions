'''
Observations:
python feels like cheating here
Ideas:
1: strip the text of non alphanumericals '.join(filter(isalnum,s))
2: force lowercase 
3: return stripped == reverse(stripped)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join(filter(str.isalnum, s)).lower()
        rev_stripped = stripped[::-1]
        return stripped == rev_stripped