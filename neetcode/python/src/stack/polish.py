from typing import List

class Solution:
    def __init__(self):
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                st.append(st.pop() + st.pop())
            elif token == "-":
                # op1 - op2 = -op2 + op1
                st.append(-st.pop() + st.pop())
            elif token == "*":
                st.append(st.pop() * st.pop())
            elif token == "/":
                # op1 / op2 = 1/op2 * op1
                st.append(int(1/st.pop() * st.pop()))
            else:
                st.append(int(token))
        return st[-1]
