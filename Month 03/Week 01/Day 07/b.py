# Evaluate Division: https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# So in this problem what we have is basically a backtracking dfs problem where we convert these queries into A -> B costs value and B -> A costs 1/value
# then all we have to do is check if we can travel from A -> B assuming they are both in the graph that we create

from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        ourGraph = defaultdict(defaultdict)

        for (A, B), value in zip(equations, values):
            ourGraph[A][B] = value
            ourGraph[B][A] = 1/value

        def dfs(cur, target, visited, value=1):
            # Initialize result to -1 as we haven't found a solution
            res = -1

            # Add the value we are currently at as we don't want cycles
            visited.add(cur)
            neighbors = ourGraph[cur]

            if target in neighbors:
                res = value * neighbors[target]
            else:
                # Try moving down every neighbor
                for nei, val in neighbors.items():
                    # Skip anything we have seen before
                    if nei in visited:
                        continue

                    res = dfs(nei, target, visited, value * val)

                    # If the above finds the target skip everything else
                    if res != -1.0:
                        break

            # Since this is backtracking we need to remove our option
            visited.remove(cur)
            return res

        result = []
        for A, B in queries:
            if A not in ourGraph or B not in ourGraph:
                result.append(-1.0)
            elif A == B:
                result.append(1)
            else:
                visited = set()
                result.append(dfs(A, B, visited))

        return result


# Boo yeah! The above works as I expected it to there are a few tricks to this problem but it basically
# boils down to a backtracking problem over a simple graph without using cycles.

# This will run in O(V+E) and uses O(V + len(queries)) space for storage

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? I think this is pretty optimal although you may be able to use union find more effectively
# Were there any bugs?  I didn't really have any bugs
# 5 5 3 5 = 4.5
