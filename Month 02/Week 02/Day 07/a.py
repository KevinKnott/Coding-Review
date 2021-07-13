# Basic Calculator II: https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value.

# The integer division should truncate toward zero.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# So my best thought for this problem is that since we know they are in a valid expression we know we can simply use a stack
# and evaluate the expressions as we go leaving behind any values that is not being multiplied or divided as we can just
# add everything still on the stack afterwards.
#
# One of the tricky things about this is that we can get a negative number from our result which could mess up calculations

class Solution:
    def calculate(self, s: str) -> int:
        sign = '+'
        value = 0
        stack = []

        for index in range(len(s)):
            # We want to ignore all whitespace
            if s[index] != ' ' or index == len(s) - 1:

                if s[index].isdigit():
                    value = (value * 10) + int(s[index])

                # So we need to calculate if we hit a = - * / or if we are at the last char
                if s[index] in '+-/*' or index == len(s) - 1:

                    if sign == '+':
                        stack.append(value)
                    elif sign == '-':
                        stack.append(-value)
                    elif sign == '*':
                        stack.append(value * stack.pop())
                    else:
                        # So this is silly the problem doesn't say this but it doesn't want us to floor
                        # the value or top the value so we need to use int to properly round or the equivalent
                        # round()
                        stack.append(int(stack.pop() / value))

                    # Reset our values
                    sign = s[index]
                    value = 0

        # Now that we have done all multiplication we just need to sum the stack up for the result
        while len(stack) != 1:
            last = stack.pop()
            stack[-1] += last

        return stack[0]

# So the above is pretty simple as we know that negatives can be represented only by evalutation of something like 5 - 10
# Once that is out of the way and we know we have a straight forward expression we can simply check what sign is there
# and appropriately use the stack

# Now is it possible to do this in a more efficient way as this runs in o(N) and o(N)?
# Maybe it is possible if we do a two pass solution where we loop over once and do all multiplication and division
# and then do a round of addition but we would have to modify the existing array. Or if we just track what the last number
# was and if we see a M/D we can do the math other wise just move through

# I will have to try and do the alast paragraph on another day as I am out of time

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? I believe so we could make some slight optimization but overall the solution is pretty clean
# Were there any bugs? Nope
# 5 5 3 5 = 4.5
