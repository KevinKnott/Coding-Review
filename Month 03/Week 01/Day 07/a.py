# Basic Calculator II: https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


class Solution:
    def calculate(self, s: str) -> int:
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
