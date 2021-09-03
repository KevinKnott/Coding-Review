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

# This problem comes down to using a stack to parse through the parenthesis and otherwise we can parse every element. Then at the we need to
# sort and return the result

from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        index = 0

        while index < len(formula):

            if formula[index] == '(':
                stack.append(Counter())
                index += 1
            elif formula[index].isupper():

                if index + 1 < len(formula) and formula[index + 1].islower():
                    element = formula[index:index+2]
                    index += 2
                else:
                    element = formula[index]
                    index += 1

                value = 0
                while index < len(formula) and formula[index].isdigit():
                    value = (value * 10) + int(formula[index])
                    index += 1

                if value == 0:
                    value = 1

                stack[-1][element] += value

            else:
                parent = stack.pop()
                index += 1

                multFactor = 0
                while index < len(formula) and formula[index].isdigit():
                    multFactor = (multFactor * 10) + int(formula[index])
                    index += 1

                if multFactor == 0:
                    multFactor = 1

                for element, v in parent.items():
                    stack[-1][element] += v * multFactor

        last = sorted(stack[-1])
        result = []

        for element in last:
            result.append(
                element + str(stack[-1][element]) if stack[-1][element] != 1 else element)

        return ''.join(result)


# Eyyyy lezzgo this is great
# It runs in O(N^2) as for every paren we have to loop through an extra time to multiply values
# and for space it simply uses o(N)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 17
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
