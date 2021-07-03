# Number of Atoms: https://leetcode.com/problems/number-of-atoms/


# Given a chemical formula (given as a string), return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
# Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# My first thought with this problem is that we should use a stack and push on the count and when we get out of the loop add the counts together
# Other than that we simply need to parse the formula

# There are a few special things that we need to take note of
# 1. We need to separate every level when we see a ( or close them and get the count when we see )
# 2. We Can add leters automagically when we see them
# 3. and get count for when we see them (we can probably combine 2/3)

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
# Did I need hints? No
# Did you finish within 30 min? 35
# Was the solution optimal? Yes this is optimal it runs in o(n) and it doesn't use the builtin stack but an o(N * K) stack where K is the number of parenthesis
# Were there any bugs?  I needed to add a check to make sure my index doesn't run out of bounds for the way I am getting numbers
# 5 4 5 4 = 4.5
