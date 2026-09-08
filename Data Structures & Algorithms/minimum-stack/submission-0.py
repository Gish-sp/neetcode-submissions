'''
Truths:
    Stacks are LIFO

Assertions: 
    getMin is the hardest function, need to track mins somehow. 
    can do this by keeping a running log number of size 1 across all functions and  
    update that number based on newer smaller numbers, but then that means  
    checking at each step if the number being operated on is the min num at each    
    other function, but then need to find restoration for n- pop operations in a    
    row. Will revisit this approach later for optimization, for now, proceeding
    with maintaining two stacks, one of mins, one being the true stack.

'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
