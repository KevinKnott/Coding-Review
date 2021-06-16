# Random Pick with Weight: https://leetcode.com/problems/random-pick-with-weight/

# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
# More formally, the probability of picking index i is w[i] / sum(w).


class Solution:

    def __init__(self, w):
        return

    def pickIndex(self):
        return
# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y (there isn't really too much optimization as this is building a standard data structure)
# Were there any bugs? Not a bug but initially I didn't create a Bucket class but it makes things more complicated
#  4 5 5 3 = 4.25
