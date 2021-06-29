# Couples Holding Hands: https://leetcode.com/problems/couples-holding-hands/

# There are n couples sitting in 2n seats arranged in a row and want to hold hands.
# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

# My initial thought for this problem is a backtracking problem you go through from left to right and swap
# any unhappy nodes (two options) and continue down that path until you find the result once there you save the minimum
# and go back. I think that this would run in O(N * 2^n) which I feel like is pretty bad

# That being said if you created a graph and check going from 0 -> n by two and count up the number of people
# that aren't next to their partner you should get correct answer as you can swap and fix every partner in real time

from collections import defaultdict


class Solution:
    def minSwapsCouples(self, row) -> int:
        result = 0
        couples = defaultdict(int)
        # create the graph of partners
        for i in range(0, len(row), 2):
            couples[i] = i+1
            couples[i+1] = i

        # Now we need to go through and swap any non matching person out
        for i in range(0, len(row), 2):
            # Check if they don't match partner
            if couples[row[i]] != row[i+1]:
                # if they don't increase count and swap them
                result += 1
                # Find the location of the couples partner (this is a log n operation )
                coupleLocation = row.index(couples[row[i]])
                row[i+1], row[coupleLocation] = row[coupleLocation], row[i+1]

        return result

# My intuition worked  but is the above optimal? this runs in o(n^2) and o(N) for the graph
# I think we could solve this without the graph though it just cleans up the code a bit
# I am almost positive this could be optimized so let us try

    def minSwapsCouplesOptimal(self, row) -> int:
        result = 0
        # No space will be used
        # couples = defaultdict(int)
        # # create the graph of partners
        # for i in range(0, len(row), 2):
        #     couples[i] = i+1
        #     couples[i+1] = i

        # Now we need to go through and swap any non matching person out
        for i in range(0, len(row), 2):
            # Check if they don't match partner
            # This is the part that will be complicated how do we match up the values?
            # So we can take the initial value and xor it with one to get i - 1
            target = row[i] ^ 1
            if target != row[i+1]:
                # if they don't increase count and swap them
                result += 1
                # Find the location of the couples partner (this is a log n operation )
                coupleLocation = row.index(target)
                row[i+1], row[coupleLocation] = row[coupleLocation], row[i+1]

        return result

# Score Card
# Did I need hints? Yup my initial thought was backtracking but knew that couldn't be right so I looked at the solution an coded it up
# Did you finish within 30 min? 30
# Was the solution optimal? Yeah at the end my solution runs in o(n^2) and o(1) space
# Were there any bugs? Not really
# 2 3 5 5 = 3.75
