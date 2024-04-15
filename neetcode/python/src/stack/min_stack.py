class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        return None

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.minStack[-1]
'''
Got inspiration from the monotonically decreasing deque.
This just contains the "window" of values that will 
potentially be minimums. We ignore values that are pushed in 
that are larger than the value on top of our minimum stack;
they will never be mins. We do push in smaller values, because 
they are actually mins -- monotonically decreasing stack.

Should create a link b/t this and the monotonically decreasing 
deque question I guess lol.

Would not have solved this if I didn't remember the monotonic 
deque pattern... tried a hashmap solution, that died fast

time: O(1) for each input 
space: O(1) for each input
'''
