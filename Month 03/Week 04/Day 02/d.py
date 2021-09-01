# Evaluate Division: https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.


from collections import defaultdict
from types import List

# This problem is vary complicated at first but can be boiled down to a backtracking problem where we keep track of A -> B = val and B -> A = 1 / val
# This means we need to explore down every path and return the res if found or -1 if we cant find it


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ourMap = defaultdict(defaultdict)

        for (A, B), val in zip(equations, values):
            ourMap[A][B] = val
            ourMap[B][A] = 1 / val

        def backtrack(node, target, visited, value):
            res = -1

            # Try current node
            visited.add(node)
            neighbors = ourMap[node]

            # see if  target is B
            if target in neighbors:
                res = value * neighbors[target]
            # otherwise try all neighbors not in visited
            else:
                for nei in neighbors:
                    if nei not in visited:
                        res = backtrack(nei, target, visited,
                                        value * neighbors[nei])

                        if res != -1:
                            return res

            # remove this node from visited for backtrack
            visited.remove(node)
            return res

        result = []

        for A, B in queries:
            if A not in ourMap or B not in ourMap:
                result.append(-1)
            elif A == B:
                result.append(1)
            else:
                visited = set()
                result.append(backtrack(A, B, visited, 1))

        return result

# This runs in O(M * N) as for every A we may have to look through all nodes
# and this only uses o(N) space for our map and stack space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
