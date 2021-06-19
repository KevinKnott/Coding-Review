#  Find the Most Competitive Subsequence: https://leetcode.com/problems/find-the-most-competitive-subsequence/

# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

class Solution:
    def mostCompetitive(self, nums, k):
        return


# Score Card
# Did I need hints? N (But the second solution did)
# Did you finish within 30 min? Y
# Was the solution optimal? It is optimal enough, technically you can improve from o(E+V ) to o(e and the ackermanfunction(n)) and sapce could be just o(V) instead
# Were there any bugs? I did have one bug where I didn't add any nodes that were on there own like 0 in the example edges = [[2,3],[1,2],[1,3]]
# 4 5 3 3 =  3.75
