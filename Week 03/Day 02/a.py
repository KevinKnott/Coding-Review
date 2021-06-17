# Number of Atoms: https://leetcode.com/problems/number-of-atoms/

# Given a chemical formula (given as a string), return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
# Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.


# My first thought is that we need a stack so that we can handle parenthesis (either with real stack or recursion)
# Then we shall parse letters as either One capital by itself or a Capital followed by a lower case
# Then parse numbers by getting an int unless there are two back to back elements like HMG
# We shall create a hash map of the results (or counter) that way we are finished and then we can sort the result as
# needed


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.index = 0

        # This techincally takes formula and will return a hashmap
        def evaluate():
            count = {}
            num = 0
            element = None
            while self.index < len(formula) and formula[self.index] != ')':
                # Get Element
                # To improve this I think I would use if char == '(' else it would look cleaner
                # Also the getting of the element and number could be improved as well
                # because technically we can combine the steps and reduce code
                if formula[self.index].isupper():
                    # I forgot that if the element is not there we need to handle it
                    # next time I am using a counter it solves this piece and looks cleaner
                    if element:
                        if element not in count:
                            count[element] = 1 if num == 0 else num
                        else:
                            count[element] += 1 if num == 0 else num
                        element = None
                        num = 0

                    if self.index + 1 < len(formula) and formula[self.index+1].islower():
                        element = formula[self.index: self.index+2]
                        self.index += 1
                    else:
                        element = formula[self.index]

                # Get Count
                elif formula[self.index].isdigit():
                    num = num * 10 + int(formula[self.index])
                # or recurse
                else:
                    if element:
                        if element not in count:
                            count[element] = 1 if num == 0 else num
                        else:
                            count[element] += 1 if num == 0 else num
                        element = None
                        num = 0

                    if formula[self.index] == '(':
                        self.index += 1
                        result = evaluate()

                        self.index += 1
                        start = self.index
                        while self.index < len(formula) and formula[self.index].isdigit():
                            self.index += 1

                        multiplicationFactor = int(
                            formula[start:self.index] or 1)

                        for i in result.keys():
                            if i not in count:
                                count[i] = 0
                            count[i] += result[i] * multiplicationFactor

                        continue
                self.index += 1

            if element:
                if element not in count:
                    count[element] = 1 if num == 0 else num
                else:
                    count[element] += 1 if num == 0 else num

            return count

        result = []
        count = evaluate()

        # I ran out of time to actually do this piece
        # This makes sure that we change Mg: 1 to Mg otherwise Mg: 2 to Mg2
        # and also makes sure we are in sorted order
        for name in sorted(count):
            result.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                result.append(str(multiplicity))

        return ''.join(result)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
