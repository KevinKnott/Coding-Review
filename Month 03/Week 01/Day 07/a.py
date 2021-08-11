# Basic Calculator II: https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# So for this problem we are moving across a string and on the fly we are evaluating this expression. This can be done because
# we only have the mdas part of pemdas. That means we can quickly evaluate any division and multiplcation on the spot
# and add any other values to be added on at the end. Also we dont have to worry about negative numbers except for as a solution


class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        operand, sign = 0, '+'
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char is not ' ':
                if char.isdigit():
                    operand = (operand * 10) + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    stack.append(stack.pop() * operand)
                else:
                    stack.append(int(stack.pop() / operand))

                operand = 0
                sign = char

        result = 0
        while stack:
            result += stack.pop()

        return result

# So in this problem the tricky part is the division as we can't just floor the int division we have to actually determine the proper float
# other than that the trick is that we need to keep the last sign so that we know whether or not to evaluate or simply add the value to the stack

# This runs in O(N) time and space. The question is 'Is this optimized' the answer should be no as we know that we could optimize futher on space
# based off of my last statement instead of keeping all of the addition on a stack and doing it later we can simply keep the last operation and current
# and when we go across we know that any + - (so two in a row) can be automatically calc or you do the * / immediately

    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        result = 0
        last = 0
        cur, sign = 0, '+'

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                cur = (cur * 10) + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    result += last
                    last = cur
                elif sign == '-':
                    result += last
                    last = -cur
                elif sign == '*':
                    last = last * cur
                else:
                    last = int(last / cur)

                cur = 0
                sign = char

        result += last

        return result

# This space optimized version is obviously identical and runs in O(N) but only uses O(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? Yes
# Were there any bugs? No bugs to squash
# 5 5 5 5 = 5
