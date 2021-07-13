# Reconstruct Itinerary: https://leetcode.com/problems/reconstruct-itinerary/

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


# This problem is actually just a simple DFS problem with the exception being that we have a number of flights and
# we know we can have multiple tickets this means that instead of having a set we need to use a bitset or a counter

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for src, dest in tickets:
            graph[src].append(dest)

        # Now for the bitset
        visited = {}
        for src, dest in graph.items():
            # Now that we have all the tickets we need to alphabatize them as we need to return the lexographic best order
            dest.sort()
            visited[src] = [False] * len(dest)

        self.result = []
        # Now that we have our visited setup we simply need to travel through all of the tickets

        def dfs(node='JFK', path=[]):
            # Create the base case that if we have used every ticket we have completed our path
            if len(path) == len(tickets):
                self.result = path[:] + [node]
                return

            # Otherwise visit all nodes!
            for index, newDest in enumerate(graph[node]):
                if self.result == [] and visited[node][index] == False:
                    # Do a simple backtrack in the case we choose an incorrect option
                    visited[node][index] = True
                    dfs(newDest, path + [node])
                    visited[node][index] = False

        # make sure to travel down the dfs
        dfs()
        return self.result

# So this solution takes up O(E^d) where d is the number of flights from one airport and then space uses O(V+E) as we have to track every single ticket
# from every single airport

# I think that this is pretty optimal. I think the only other optimizations for this problem would add a lot of complexity

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 13
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
