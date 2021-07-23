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

# This is another parsing problem which we will use a stack the are a few more things that make this complicated like determining whether or
# not we have a single element with a count of 1 or a element of len 2 with multiplicity. On top of that we neeed to use a stack to keep up
# with all of the cuonts

from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        index = 0
        stack = [Counter()]

        while index < len(formula):

            # If we see an open paren we need to push a new count onto the stack
            if formula[index] == '(':
                stack.append(Counter())
                index += 1

            # If we have a letter we need to check if the next char is a lowercase letter
            # then we can try to see if the next after that is a num parse it and potentially
            # add it
            elif formula[index].isupper():

                # Get H vs He
                if index + 1 < len(formula) and formula[index + 1].islower():
                    element = formula[index: index + 2]
                    index += 2
                else:
                    element = formula[index]
                    index += 1

                # Get the count H vs H3
                value = 0
                while index < len(formula) and formula[index].isdigit():
                    value = (value * 10) + int(formula[index])
                    index += 1

                # Default value to one in the case there is a example like HHe3
                if value == 0:
                    value = 1

                # Add the value onto the current stack
                stack[-1][element] += value

            # Finally if we get a closing bracket we need to pop off our current count
            # Get the multiplicity and add it to the top of the stack
            else:
                parenCounter = stack.pop()
                index += 1

                # Get our value (which should just be a method since we are reusing it)
                multiplicity = 0
                while index < len(formula) and formula[index].isdigit():
                    multiplicity = (multiplicity * 10) + int(formula[index])
                    index += 1

                if multiplicity == 0:
                    multiplicity = 1

                # Go through every item and multiply its value and add it to the top of our stack
                for k, v in parenCounter.items():
                    stack[-1][k] += multiplicity * v

        # Once we are full through our whole entire algo we can sort the values so they are in the "correct" order
        # So we need to convert 1 -> H and 2 -> H2
        result = [element + str(stack[-1][element]) if stack[-1][element]
                  != 1 else element for element in sorted(stack[-1])]

        return ''.join(result)

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 25
# Was the solution optimal? This runs in o(N^2) and o(n) as we have potentiall for () and we need to keep track of the stackking solution
# Were there any bugs? None
# 5 4 5 5 = 4.75
