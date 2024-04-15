class Solution:
    def isValid(s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            if p in pairs.values(): 
                stack.append(p)
            else:
                # no matching open parenthesis found
                if not stack or stack[-1] != pairs[p]:
                    return False
                else:
                    stack.pop()
        # if parentheses remain unmatched, return false
        return len(stack) == 0 
