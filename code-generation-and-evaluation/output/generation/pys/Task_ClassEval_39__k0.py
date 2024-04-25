from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()

    def calculate(self, expression):
        transformed_expr = self.transform(expression)
        self.prepare(transformed_expr)
        return self._evaluate_postfix()

    def prepare(self, expression):
        self.postfix_stack.clear()
        # Code to convert infix expression to postfix and store in self.postfix_stack

    def is_operator(self, char):
        return char in ['+', '-', '*', '/']

    def compare(self, op1, op2):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence.get(op1, 0) >= precedence.get(op2, 0)

    def _calculate(self, operand1, operand2, operator):
        if operator == '+':
            return Decimal(operand1) + Decimal(operand2)
        elif operator == '-':
            return Decimal(operand1) - Decimal(operand2)
        elif operator == '*':
            return Decimal(operand1) * Decimal(operand2)
        elif operator == '/':
            return Decimal(operand1) / Decimal(operand2)

    def transform(self, expression):
        # Code to transform infix expression to a simplified form
        return expression

    def _evaluate_postfix(self):
        stack = []
        for token in self.postfix_stack:
            if token.isdigit():
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._calculate(operand1, operand2, token)
                stack.append(result)
        return float(stack[0])
