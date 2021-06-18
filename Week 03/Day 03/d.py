#  Reconstruct Itinerary: https://leetcode.com/problems/reconstruct-itinerary/
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


# This is a dfs graph problem in which you sort the adjaceny list
from collections import defaultdict


class Solution:
    # This was my solution and it seems to work however I forgot you could have multiple tickets to the same spot
    def findItinerary(self, tickets):
        graph = {}
        visited = set()
        self.result = []

        for src, dest in tickets:
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []

            # we should sort this actually and do an insertion sort but I am going to use
            graph[src].append(dest)
            graph[src].sort()

        def traverse(code, path=[]):
            if len(visited) == len(tickets):
                self.result = path[:] + [code]

            for i in graph[code]:
                if self.result == [] and (code, i) not in visited:
                    visited.add((code, i))
                    traverse(i, path + [code])
                    visited.remove((code, i))

        traverse('JFK')
        return self.result

    def findItineraryMultiSameTicket(self, tickets):
        graph = defaultdict(list)
        visited = set()
        self.result = []

        for src, dest in tickets:
            graph[src].append(dest)

            # # we should sort this actually and do an insertion sort but I am going to use
            # graph[src].append(dest)
            # graph[src].sort()

        visited = {}

        # Sort once we have everything
        for src, dests in graph.items():
            dests.sort()
            visited[src] = [False] * len(dests)

        def traverse(code, path=[]):
            if len(path) == len(tickets):
                self.result = path[:] + [code]

            for i, nextDest in enumerate(graph[code]):
                if self.result == [] and visited[code][i] is False:
                    visited[code][i] = True
                    traverse(nextDest, path + [code])
                    visited[code][i] = False

        traverse('JFK')
        return self.result

# After reviewing the solution (I was really close to having the naive solution)
# My other thought for doing the visited where you pop off flights and reappend them
# was close to a famous algo Eulerian Path which is actually a bit more optimal


# Score Card
# Did I need hints? Kinda I had the right solution but I had one bug
# Did you finish within 30 min? 45
# Was the solution optimal? I am not sure the current solution runs in O(|E| ^ d) where is the number of total flights and d
# is the number of destinations from one airport and spacec is O(|V| + |E|) where v is the # of airports and E is the number of flights
# Were there any bugs? I was using a set to keep track of my flights however when they adde multiple of the same flights it broke my code
#  3 1 2 1 = 1.75
