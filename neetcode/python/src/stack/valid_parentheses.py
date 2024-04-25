class Solution:
    def isValid(s: str) -> bool:
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for p in s:
            # add open parentheses
            if p in pairs:
                stack.append(p)
            else:
                # check if matching open pair is on top of stack
                if stack and pairs[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
        # if any parentheses remain, it has not made a valid pair 
        return len(stack) == 0
