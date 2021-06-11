# . Find the Town Judge: https://leetcode.com/problems/find-the-town-judge/
# In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
#  This is actually close however you can't check outbound connections
#  This makes me think we actually have a Graph problem

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # Since it is from 1 -> N we create an inbound and outbound array and check if there exists a element with no outbound and n-1 inbound
        trusts = [0] * (n+1)
        trusted = [0] * (n+1)

        for person, trustee in trust:
            trusts[trustee] += 1
            trusted[person] += 1

        for i in range(1, n+1):
            if trusted[i] == 0 and trusts[i] == n-1:
                return i
        return -1

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? I actually had two bugs one was not considering that I need to check incoming/outgoing connections
# and two my indexs start at 0 and the positions start at 1 should of caught it but I didn't do an example first
#  3 4 3 3 = 3.25
