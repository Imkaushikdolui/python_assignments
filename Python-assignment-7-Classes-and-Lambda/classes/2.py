# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 

class ParenthesesValidator:
    def __init__(self):
        self.opening_brackets = '({['
        self.closing_brackets = ')}]'

    def is_valid(self, parentheses_string):
        stack = []
        for char in parentheses_string:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if not stack:
                    return False
                last_opening_bracket = stack.pop()
                if self.opening_brackets.index(last_opening_bracket) != self.closing_brackets.index(char):
                    return False
        return len(stack) == 0

validator = ParenthesesValidator()
input = input("enter the parentheses")
print(validator.is_valid(input))      
     
