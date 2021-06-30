# Reconstruct Itinerary: https://leetcode.com/problems/reconstruct-itinerary/

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# This seems like a simple dfs where we have a directed graph where we sort the neighbors by lexographical order
# also I would guess that we need to use a bit to keep track of the number of tickets if there were duplicates

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        ourGraph = defaultdict(list)

        for src, dest in tickets:
            ourGraph[src].append(dest)

        visited = {}
        # Take every list of possible solutions and sort it
        for src, dest in ourGraph.items():
            dest.sort()
            # Then create a bitmap so we know which ones we have visited
            visited[src] = [False] * len(dest)

        self.result = []

        def traverse(node='JFK', path=[]):
            # This is actually one of the harder parts we know that the stopping point is the first path
            # we find as we have already sorted the destination to make sure that we are only going
            # to use all of our tickets and be in lexographic order
            if len(path) == len(tickets):
                self.result = path[:] + [node]
                return

            for i, nextStop in enumerate(ourGraph[node]):
                # We have a check for if we have a result so we don't rewrite over it
                # and check whether or not we have used all of the tickets at our current
                # destination
                if self.result == [] and visited[node][i] is False:
                    # Then we backtrack mark as visited, visit and mark as unvisited
                    visited[node][i] = True
                    traverse(nextStop, path + [node])
                    visited[node][i] = False

        traverse()
        return self.result


# Overall this algorithm is just a simple backtracking dfs problem with a variation of having to create a bitmap to make sure
# that the number of tickets being used is correct.

# Now is this solution optimal I would say it isn't as this runs in o(E ^ D)  where d is the biggest number of flights from one airport
# and the space complexity would be o(V+E) as we are storing every edge that we have visited as well as every vertex + all of the edges again
# for the path

# That being said I am not sure of the optimal solution after taking a look it looks like the optimnal solution is hierholzers algo


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y although I messed up the thought process of how to solve the problem
# Were there any bugs?  I didn't really have any bugs
#  2 3 3 5 = 3.25
