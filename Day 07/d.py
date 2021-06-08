# Number of Atoms: https://leetcode.com/problems/number-of-atoms/

# Given a chemical formula (given as a string), return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
# Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.


class Solution:
    def countOfAtoms(self, formula):
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N
# Was the solution optimal? Y
# Were there any bugs? Y
# Unfortunately I am tired and missed on a couple things in my partition I forgot that I need to make the slow index = to start as we are already
# seraching using binary search and don't need to do whole list
#  5 3 5 3 = 4
