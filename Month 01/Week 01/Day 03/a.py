#  Basic Calculator: https://leetcode.com/problems/basic-calculator/
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Initial thought is to use a stack as I have done something similar before with postfix notation with reverse polish notation

# Look for hint as I can't figure out when to actually pop off of stack
# Technique is to reverse the string and parse


class initial():
    def calculate(self, s):
        stack = []
        n, operand = 0, 0

        for i in reversed(range(len(s))):
            cur = s[i]

            # print(cur, cur.isdigit())
            if cur.isdigit():
                # add digit to the write place
                operand = (10**n * int(cur)) + operand
                n += 1
            elif s[i] != ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0

                if cur == '(':
                    res = self.eval(stack)
                    # Remove ')'
                    stack.pop()

                    stack.append(res)
                else:
                    # If you are here we have + or -
                    stack.append(cur)

        if n:
            # Push whatever is currently half read onto stack
            stack.append(operand)

        return self.eval(stack)

    def eval(self, stack):
        # Since the eval has to be valid by rules we pop the first digit to get to the operation

        res = stack.pop() if stack else 0
        print(stack)
        while stack and stack[-1] != ')':
            # find the operation
            sign = stack.pop()
            # get next digit
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()

        return res

# Score Card
# Did I need hints? yes
# Did you finish within 30 min? No
# Was the solution optimal? I am unsure
# Were there any bugs? Yeah i took too long to figure out how to parse a number given a string and it took me a while to figure out
#  1 1 2 2 = 1.5


a = '1+2'
b = '1 + -2'  # '-1+2'
c = '(1+(4+5+2)-3)+(6+8)'
sol = initial()
print(sol.calculate(a))
print(sol.calculate(b))
print(sol.calculate(c))
