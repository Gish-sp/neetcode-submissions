'''
Truths:
    brackets can only be [] {} and ()
Assertions:
    can dismiss as false if starts with any closed type bracket ]})
Decisions:
    Attempt 1: 
            Treat input string like a stack, saves a second loop (O(n) time) by only having to iterate through string once.
Refinements:

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketSchema = {')' : '(', ']' : '[', '}' : '{'}
        for bracket in s:
            if bracket in bracketSchema:
                if stack and stack[-1] == bracketSchema[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False
