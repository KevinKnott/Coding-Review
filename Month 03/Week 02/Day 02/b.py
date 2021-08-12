# Reconstruct Itinerary: https://leetcode.com/problems/reconstruct-itinerary/

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# Okay just looking at this problem I can see that it is a backtracking dfs problem as we have to try and complete the path of N tickets
# and also do it in the most lexographical way. To do this I will take two passes one to create a graph that stores all of the tickets
# in lexigraphical order and then another in which I do a simple backtracking dfs until I have used all N of the tickets

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        ourGraph = defaultdict(list)

        for src, dest in tickets:
            ourGraph[src].append(dest)

        # Now that we have everything in our list we need to sort and
        # setup the number of tickets we have in visited
        visited = {}
        for src, dest in ourGraph.items():
            dest.sort()
            visited[src] = [False] * len(dest)

        self.result = []

        # From here all we need is a backtracking dfs
        def backtrack(node='JFK', path=[]):
            if len(path) == len(tickets):
                self.result = path[:] + [node]

            for i, dest in enumerate(ourGraph[node]):
                # Dont use used tickets
                if len(self.result) == 0 and visited[node][i] is False:
                    visited[node][i] = True
                    backtrack(dest, path + [node])
                    visited[node][i] = False

        backtrack()
        return self.result

# Easy peasy problem basically this is a simple backtracking problem the hard part about this problem is that we
# have multiple tickets to the same place which makes this a bit more difficult. We get around this with sorting
# and also using a bitset for our visited so we know if we have used every ticket

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Yuh
# Were there any bugs? Nah
# 5 5 5 5 = 5
