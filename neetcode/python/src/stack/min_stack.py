class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    # never called on empty stack
    def pop(self) -> None:
        if self.minStack[-1] == self.stack.pop():
            self.minStack.pop()

    # never called on empty stack
    def top(self) -> int:
        return self.stack[-1] 

    # never called on empty stack
    def getMin(self) -> int:
        return self.minStack[-1]
