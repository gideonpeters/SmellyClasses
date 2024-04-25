class BalancedBrackets:
    def __init__(self, expr):
        self.expr = expr

    def clear_expr(self):
        stack = []
        for char in self.expr:
            if char in ['(', ')', '[', ']', '{', '}']:
                stack.append(char)
        self.expr = ''.join(stack)

    def check_balanced_brackets(self):
        stack = []
        opening_brackets = ['(', '[', '{']
        closing_brackets = [')', ']', '}']
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}

        for char in self.expr:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or bracket_pairs[stack.pop()] != char:
                    return False

        return len(stack) == 0
