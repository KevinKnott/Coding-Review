# Find the Town Judge: https://leetcode.com/problems/find-the-town-judge/

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:
#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


class Solution:
    def findJudge(self, n: int, trust) -> int:
        return

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(1) space
# Were there any bugs? None
# 5 5 5 5 = 5
