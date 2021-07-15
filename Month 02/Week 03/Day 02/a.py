# Couples Holding Hands: https://leetcode.com/problems/couples-holding-hands/

# There are n couples sitting in 2n seats arranged in a row and want to hold hands.
# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

# This problem is kind of tricky the solution will call for us to create a mapping between 0 -> 1 and 1 <- 0 and then go through and find any unamtching pair
# and swap with the index of the partner exclusively going from left to right

from collections import defaultdict


class Solution:
    def minSwapsCouples(self, row) -> int:
        # We need to make a list of all partners
        couples = defaultdict(int)

        # We need to map partners together 0 -> 0,1 , 1 -> 2, 3
        for i in range(0, len(row), 2):
            couples[i] = i + 1
            couples[i+1] = i

        swap = 0
        # Now what we need to do is loop over the pairs and if i+1 doesn't equal the couple that is supposed to be there
        # we will swap those couples
        for i in range(0, len(row), 2):
            # Couples[row[i]] means if we have 0 that the couples is 1
            # If the don't match we need to count the swap and swap the value
            if couples[row[i]] != row[i+1]:
                swap += 1
                # I am cheating here and using a simple index search to find the correct value and swap it
                ourCouple = row.index(couples[row[i]])
                row[i+1], row[ourCouple] = row[ourCouple], row[i+1]

        return swap

# The above solution is something that I picked up the first time I tried this problem. The initial thought on this is that we need to use backtracking.
# However by taking advantage of the fact that we can always swap a correct partner in means that we will always get the correct answer
# It does take some time to get used to this solution. but this will run in o(N) and use o(N) space

# Also we could get rid of the couples array and reduce this to an o(N) and o(1)
    def minSwapsCouples(self, row) -> int:
        swap = 0
        # Now what we need to do is loop over the pairs and if i+1 doesn't equal the couple that is supposed to be there
        # we will swap those couples
        for i in range(0, len(row), 2):
            # 0 ^ 1 will be 1 and 1 ^ 0 = 1
            # This continues up as 11 ^ 01 will always flip the last bit which is a change of one to either one higher or lower
            partner = row[i] ^ 1
            # Couples[row[i]] means if we have 0 that the couples is 1
            # If the don't match we need to count the swap and swap the value
            if partner != row[i+1]:
                swap += 1
                # I am cheating here and using a simple index search to find the correct value and swap it
                ourCouple = row.index(partner)
                row[i+1], row[ourCouple] = row[ourCouple], row[i+1]

        return swap

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? Yuh
# Were there any bugs? Nope
# 5 5 5 5 = 5
