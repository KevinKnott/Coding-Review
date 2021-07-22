# Basic Calculator: https://leetcode.com/problems/basic-calculator/

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# This solution is simple all we have to do is create a stack to store values if we see a paren
# then once this is done we simply convert the numbers to only use addition by changing the sign if we see a negative


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result, num, sign = 0, 0, 1

        for i in range(len(s)):

            if s[i] != ' ':

                if s[i].isdigit():
                    num = (num * 10) + int(s[i])
                elif s[i] == '-':
                    result += sign * num
                    sign = - 1
                    num = 0
                elif s[i] == '+':
                    result += sign * num
                    sign = 1
                    num = 0
                elif s[i] == '(':
                    stack.append(result)
                    stack.append(sign)

                    sign = 1
                    result = 0

                else:
                    result += sign * num
                    result *= stack.pop()
                    result += stack.pop()
                    num = 0

        return result + (sign * num)

# the above runs in O(N) time and space and is pretty basic

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Ohhhh yeaaa
# Were there any bugs?  Nope
# 5 5 5 5 = 5
