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
        # if parentheses remain unpaired in the stack, return false
        return len(stack) == 0 
'''
time: o(n) -- traverses the s string
space: o(n) -- worst case is a string with only open parentheses, fills stack up to n

cute little connection with hashmaps
'''
