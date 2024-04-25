class Calculator:
    def calculate(self, expression):
        if not expression:
            return None
        operand_stack = []
        operator_stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                operand_stack.append(float(num))
                continue
            elif expression[i] in precedence:
                while operator_stack and precedence[operator_stack[-1]] >= precedence[expression[i]]:
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[i])
            i += 1
        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)
        return operand_stack[0]

    def precedence(self, operator):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        if len(operand_stack) < 2 or not operator_stack:
            return
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        if operator == '+':
            operand_stack.append(operand1 + operand2)
        elif operator == '-':
            operand_stack.append(operand1 - operand2)
        elif operator == '*':
            operand_stack.append(operand1 * operand2)
        elif operator == '/':
            operand_stack.append(operand1 / operand2)
        elif operator == '^':
            operand_stack.append(operand1 ** operand2)
