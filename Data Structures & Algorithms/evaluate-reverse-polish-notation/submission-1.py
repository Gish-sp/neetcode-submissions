'''
Assertions:
    Can break the input into two lists, one of nums, one of ops. 
    Have the first two nums handled by first op, then run through the rest of both
    lists, this way to use op then num. This would be O(N + M)


'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def recurse():
            current = tokens.pop()
            if current not in '+-*/':
                return int(current)
            right_side = recurse()
            left_side = recurse()

            if current == '+':
                return left_side + right_side
            elif current == '-':
                return left_side - right_side
            elif current == '*':
                return left_side * right_side
            elif current == '/':
                return int(left_side / right_side)
        return recurse()

            
            