# Basic Calculator: https://leetcode.com/problems/basic-calculator/

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# My thoughts on this problem is that we can keep track of each piece and make this simpler
# If we use a dfs/stack we can compute a value by normal means pushing values onto the stack
# and then adding them together the end however we need to be careful to grab our values because
# if we have a double negative that is the same as adding and if we have subtraction we are
# adding a negative number


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        operand = 0

        # if we see a parenthesis pus our current result onto stack
        # other wise compute as we move along
        for index in range(len(s)):
            if s[index] != ' ':
                # Loop through the values and add it to result
                if s[index].isdigit():
                    operand = (operand * 10) + int(s[index])
                elif s[index] == '+':
                    result += sign * operand
                    sign = 1
                    operand = 0
                elif s[index] == '-':
                    result += sign * operand
                    sign = -1
                    operand = 0
                else:
                    if operand:
                        result += sign * operand

                    if s[index] == '(':
                        stack.append((result, sign))
                        result = 0
                        sign = 1
                        operand = 0
                    else:
                        temp, sign = stack.pop()
                        result = (result * sign) + temp
                        sign = 1
                        operand = 0

        if operand:
            result += sign * operand

        return result

# The above code works and is optimal it runs in O(N) and O(N) honestly I think I could optimize a bit but it is pretty solid


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? Yeah
# Were there any bugs? The only thing I forgot was that I need to handle when there is an operand at the end of computation
# i forgot to add it at first
# 5 5 5 3 = 4.5
