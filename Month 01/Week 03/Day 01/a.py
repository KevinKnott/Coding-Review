# Basic Calculator: https://leetcode.com/problems/basic-calculator/

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# The initial thought here is that we can move across the string and keep track of everything within the stack
# For simple calculation it is easy 1 + 2 + 3 is a calc where you pop thre elements and push one on
# It gets more complicated when you add parenthesis because we need to push those on as a stoping point
# After that the only concern is negative numbers as we will need to change the sign when we see them


class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        # Value for keeping track of multi digit number
        value = 0
        # Sign for keeping track of whether we have a positive or a negative
        sign = 1
        leadingZero = False

        def evaluate(stack):

            while len(stack) > 1 and stack[-2] != '(':
                result = stack.pop() + stack.pop()
                stack.append(result)

            # Remove extra parenthesis as we no longer need it
            if len(stack) > 1:
                result = stack.pop()
                stack.pop()
                sign = stack.pop()

                stack.append(result * sign)

        for char in s:

            if char == ' ':
                continue
            elif char.isdigit():
                if value == 0 and leadingZero is False:
                    leadingZero = True
                value = value * 10 + int(char)
            else:
                if value or leadingZero:
                    # If we hit anything other than a number we need to add the value to the stack
                    stack.append(value * sign)
                    # And then reset it
                    leadingZero = False
                    value = 0
                    sign = 1

                if char == ')':
                    evaluate(stack)
                elif char in '+-':
                    sign = 1 if char == '+' else -1
                else:
                    stack.append(sign)
                    stack.append(char)
                    sign = 1

        if value:
            stack.append(value * sign)

        evaluate(stack)
        return stack[-1] if len(stack) > 0 else 0

# With this problem I think I could optimize it further because honestly since I am tracking the sign all I really need to do is add values every time
# Unless there is a ( and then we could actually push the value onto the stack and keep going and pop when we get to )


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N 50 or so
# Was the solution optimal? Y
# Were there any bugs? Y (I forgot about handling leading 0 since I was using if value and value could be 0)
#  4 1 4 2 = 2.75
