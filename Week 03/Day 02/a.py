# Number of Atoms: https://leetcode.com/problems/number-of-atoms/

# Given a chemical formula (given as a string), return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
# Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        return

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Pretty well although there is a dynamic programming solution and there is even a o(n) with two pointers
# This actually kind of reminds of finding the fibonaci where it is based off the two previous answers
# Were there any bugs? My base cases need to be in a certain order and what I mentioned in the problem
#  3 3 1 3 = 2.5
