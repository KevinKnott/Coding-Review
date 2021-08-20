# Evaluate Division: https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# This problem is kind of difficult to understand but basically it ends up being a backtracking dfs as we are creating a graph to get from A->B with a cost of value[i]
# because of this we can do a simple backtrack to do a dfs through our graph and see if we find the solution if not return -1

from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        ourGraph = defaultdict(defaultdict)

        for (A, B), value in zip(equations, values):
            ourGraph[A][B] = value
            ourGraph[B][A] = 1 / value

        def backtracking(node, target, visited, value):
            res = -1.0
            visited.add(node)
            neighbors = ourGraph[node]

            if target in neighbors:
                res = value * neighbors[target]
            else:
                for nei in neighbors:
                    if nei in visited:
                        continue

                    res = backtracking(nei, target, visited,
                                       value * neighbors[nei])

                    # If we found answer continue
                    if res != -1.0:
                        break

            visited.remove(node)
            return res

        result = []
        for A, B in queries:
            if A not in ourGraph or B not in ourGraph:
                result.append(-1.0)
            elif A == B:
                result.append(1.0)
            else:
                visited = set()
                result.append(backtracking(A, B, visited, 1))

        return result

# This is exactly what I stated and it runs in O(V * E) and uses O(N) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
