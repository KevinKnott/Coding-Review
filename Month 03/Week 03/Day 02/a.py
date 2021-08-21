# Number of Atoms: https://leetcode.com/problems/number-of-atoms/

# Given a string formula representing a chemical formula, return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.
# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.
# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# In this problem we will be creating a counter system in which we add up values and then anytime we see a paren we will leverage a stack to place a newcount on top of the stack
# then we will parse and anytime we close a paren we wil go ahead grab the next number (unless it is a string) and multiply across
# once we have added and multiplied all the way we simply sort the counter by its items and return the sorted version

from typing import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        index = 0

        while index < len(formula):

            # 3 options (, a new atom, or )
            if formula[index] == '(':
                stack.append(Counter())
                index += 1

            elif formula[index].isupper():

                if index + 1 < len(formula) and formula[index + 1].islower():
                    element = formula[index:index + 2]
                    index += 2
                else:
                    element = formula[index]
                    index += 1

                # Get count
                value = 0
                while index < len(formula) and formula[index].isdigit():
                    value = (value * 10) + int(formula[index])
                    index += 1

                # H == H1
                if value == 0:
                    value = 1

                stack[-1][element] += value

            else:
                parenCounter = stack.pop()
                index += 1

                countMultiplier = 0
                while index < len(formula) and formula[index].isdigit():
                    countMultiplier = (countMultiplier * 10) + \
                        int(formula[index])
                    index += 1

                if countMultiplier == 0:
                    countMultiplier = 1

                for k, v in parenCounter.items():
                    stack[-1][k] += countMultiplier * v

        result = [element + str(stack[-1][element]) if stack[-1][element]
                  != 1 else element for element in sorted(stack[-1])]

        return ''.join(result)

# While this seems rather complicated it is just combining a basic stack with parsing of letters and numbers
# which I have done in many problem

# This runs in O(n^2) and O(N) as we have to multiply at every paren so we have to parse twice
# and o(N) for number of parens to add counter onto stack

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? Yeah
# Were there any bugs? Nope
# 5 5 5 5 = 5
