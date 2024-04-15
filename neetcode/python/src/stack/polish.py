from typing import List

class Solution:
    def __init__(self):
        pass

    def calculate(self, operand2: int, operator: str, operand1: int) -> int:
        value = 0
        if operator == "+":
            value = operand1 + operand2
        elif operator == "-":
            value = operand1 - operand2
        elif operator == "*":
            value = operand1 * operand2
        else:
            value = int(operand1 / operand2)
        return value

    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = set(["+", "-", "*", "/"])
        for ops in tokens:
            if ops in operators:
                value = self.calculate(operands.pop(), ops, operands.pop())
                operands.append(value)
            else:
                operands.append(int(ops))
        return operands[-1]
'''
like dijkstra's but easier since polish postfix notation is built to make this 
stuff easy.
time : o(n) -- to traverse the string
space : o(n) -- worst case n/2 operands in the stack with n/2 -1 operators
'''
