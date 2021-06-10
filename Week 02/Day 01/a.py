# Number of Atoms: https://leetcode.com/problems/number-of-atoms/

# Given a chemical formula (given as a string), return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
# Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# My initial thought is that this is actually a stack problem because it is like a calculator problem (basic calc) you have Elements and how many there are then you have multiplication based off the level


from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Call dfs for our formula
        return self.dfsHelper(formula)

    def dfsHelper(self, formula):
        # Search for parens if you find some recurse with just that piece (must multiply answer by number after paren)
        if '(' in formula:
            start, end = 0, len(formula) - 1

            while start < len(formula):
                if formula[start] == '(':
                    break
                start += 1

            while end >= 0:
                if formula[end] == ')':
                    end += 1
                    break
                end -= 1

            multiply = formula[end] if end < len(formula) else 1
            result = self.dfsHelper(formula[start:end])
            for key, value in result:
                result[key] = value * multiply
            return result
        # otherwise create a hashmap and fill it in based off of the rules
        else:
            result = {}
            element = ''
            for i in range(len(formula)):
                # Check if there is an uppercase letter or digit
                if formula[i].isalpha():
                    if element.isupper() and formula[i].isupper() or len(element) > 1 and formula[i].isupper():
                        if element not in result:
                            result[element] = 0
                        result[element] += 1
                        element = ''
                    element += formula[i]

                else:
                    if element not in result:
                        result[element] = int(formula[i])
                    else:
                        result[element] += int(formula[i])
                    element = ''

            if element != '':
                result[element] = 1
        return result


# I realize that instead of using a straight dictionary we can use a counter (a subclass of dict) that allows us to just add values and ret 0 if they aren't there
# Next Day upsolving (since I was so close)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Call dfs for our formula
        def dfsParse():
            # Previously I had used an if statment to find the parens and pass it down which works minus the fact that we don't move
            # our index to the very end and that makes it a bit complicated. to combat this I am using the self.index to move my pointer

            count = Counter()
            # We need to loop over variables from 0 -> len(formula) or until we hit  a parne H2(OMg2)4  this will let us dive into parens
            # and multiply when we pass the end of them
            while self.index < len(formula) and formula[self.index] != ')':
                # If there is an open parenthesis increase our index and recurse
                if formula[self.index] == '(':
                    self.index += 1
                    # Recurse
                    for element, value in dfsParse().items():
                        count[element] += value
                else:
                    start = self.index
                    self.index += 1
                    # Get the Element
                    while self.index < len(formula) and formula[self.index].islower():
                        self.index += 1
                    element = formula[start:self.index]

                    # Get the count
                    start = self.index
                    while self.index < len(formula) and formula[self.index].isdigit():
                        self.index += 1
                    count[element] += int(formula[start:self.index] or 1)

            # Because we could end on a  ')' we need to increase the index
            self.index += 1

            # Handle possible multiplication
            start = self.index
            while self.index < len(formula) and formula[self.index].isdigit():
                self.index += 1

            if start < self.index:
                multiplicationFactor = int(formula[start:self.index] or 1)

                for element in count.keys():
                    count[element] *= multiplicationFactor
            return count

        self.index = 0
        result = []
        count = dfsParse()
        for element in sorted(count):
            result.append(element)
            elementCount = count[element]
            if elementCount > 1:
                result.append(str(elementCount))

        return ''.join(result)

# Unfortunately I wasn't able to finish this one. I was able to get it to parse with no parens and was working on expanding this

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Unkown
# Were there any bugs? Y  (no support for max heaps made me use negatives and I forgot to handle them properly)


#  To improve this code I think that i need to separate out the pieces that parse atoms and parse the amount of atoms
#  4 1 1 3 = 2.25
