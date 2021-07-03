# Random Pick with Weight: https://leetcode.com/problems/random-pick-with-weight/

# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
# More formally, the probability of picking index i is w[i] / sum(w).

class Solution:

    def __init__(self, w):
        return

    def pickIndex(self) -> int:
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
