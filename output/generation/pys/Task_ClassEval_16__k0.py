class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators '+', '-', '*', '/', and '^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        """
        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                operand_stack.append(float(num))
                i -= 1
            elif expression[i] in self.operators:
                while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(expression[i]):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[i])
            i += 1

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        if operand_stack:
            return operand_stack[-1]
        else:
            return None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment.
        The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator in ['^']:
            return 3
        elif operator in ['*', '/']:
            return 2
        elif operator in ['+', '-']:
            return 1
        else:
            return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack,
        and store the result at the top of the operand stack
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack and operator_stack
        """
        if len(operand_stack) < 2 or len(operator_stack) < 1:
            return

        num2 = operand_stack.pop()
        num1 = operand_stack.pop()
        operator = operator_stack.pop()

        if operator in self.operators:
            result = self.operators[operator](num1, num2)
            operand_stack.append(result)
