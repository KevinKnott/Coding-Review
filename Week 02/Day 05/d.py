# Basic Calculator: https://leetcode.com/problems/basic-calculator/
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# As I have already done this problem before I know that since we have a valid expression we can quickly do all math
# by using a stack to push on elements and compute once everything is pushed on or when have pushed all items and we need to evaluate the stack
# Part of this is because we know that + and - are at the same level so our reversal with the stack is not an issue


class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        prev, negative = None, False
        num = ''

        # We need to be careful that we actually add the numbers correctly as well since technically we can't solve  42 - -34 properly otherwise
        for c in s:

            if prev is None and c == '-' or prev == '-' and c == '-':
                negative = True

            if c.isdigit():
                num += c
            elif c != ' ':
                if num:
                    stack.append(self.getVal(num, negative))
                    num = ''
                    negative = None

                if c == ')':
                    self.evaluate(stack)

                else:
                    if prev == '-' and c == '-':
                        continue
                    stack.append(c)

            prev = c

        if len(num) > 0:
            stack.append(self.getVal(num, negative))

        self.evaluate(stack)

        return stack[-1]

    def getVal(self, num, negative):
        return -1 * int(num) if negative else int(num)

    def evaluate(self, stack):

        while len(stack) > 1 and stack[-2] != '(':
            # get second val
            second = stack.pop()
            # get operation
            ops = stack.pop()
            # get first val
            first = stack.pop()

            if ops == '-':
                stack.append(first - second)
            else:
                stack.append(first + second)

        # Pop the (
        if len(stack) > 1 and stack[-2]:
            res = stack.pop()
            stack.pop()
            stack.append(res)

        # ( 1 + ( 1 + 2))

# I am gettin closer to the answer however there is an edge case with 1 + 1 - - 2 which results in their solution wanting 0 for sign swaping even though it is a valid expression
# Also I think that I can stop some of my complication by changing my value to get the number in real time using num * 10 + int(num) instead of the method I am using
# because then I could use the negative operator to just swap if need be from 1 to -1 and add it if we have two - in a row 1 + - 2 and we can push on numbers any time we see a +/-


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N
# Was the solution optimal? It is optimal enough however I think I could make some slight improvements
# Were there any bugs? I am having issues with double negative values
# 5 1 3 3 = 3
