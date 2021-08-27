# Evaluate Division: https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

from types import List
from collections import defaultdict
# In this problem we are taking a set of equations and values and creating a map to try and find some result  A/B = X
# To do this we will take a mapping from A -> B = V and B -> A = 1/V. Once our map is completed all we have to do is use
# a backtracking dfs to solve for the equations. Minus any equations where A or B is not in our map or  A == B which is
# always 1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ourMap = defaultdict(defaultdict)

        for (A, B), val in zip(equations, values):
            ourMap[A][B] = val
            ourMap[B][A] = 1 / val

        def backtrack(node, target, visited, value):
            res = -1
            visited.add(node)
            neighbors = ourMap[node]

            if target in neighbors:
                res = value * neighbors[target]
            else:

                for nei in neighbors:
                    if nei in visited:
                        continue

                    res = backtrack(nei, target, visited,
                                    value * neighbors[nei])

                    if res != -1:
                        break

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

# Oh yeah crushed this problem. This runs in a bad runtime complexity of O(V*E) and uses O(N) where N ends up being quite big as we build our map
# then we go through up to N calls of the stack

# The question to have is "is this optimal" and while I think that it is fairly optimal I think that if you used a disjoin union set you may be
# able to improve the performance although I haven't had a chance to build a weighted Union Find so I will need to practice this

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Yee
# Were there any bugs? Nee
# 5 5 4 5 = 4.75
