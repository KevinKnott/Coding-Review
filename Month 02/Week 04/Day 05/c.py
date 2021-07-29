# Evaluate Division: https://leetcode.com/problems/evaluate-division/


# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# So this problem is kinda convulated at first but what it boils down to is a simple dfs where you try and calculate these values
# The tricky part is figuring out that A/B = C also means that B/A = 1/C
# After the above trick all we need to do is find out if there is a path from X -> Y or return -1 unless X == Y
from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        ourMap = defaultdict(defaultdict)
        for (a, b), value in zip(equations, values):
            ourMap[a][b] = value
            ourMap[b][a] = 1 / value

        def dfs(cur, target, visited, value=1):
            # This is a backtracking solution so add cur to set try to find target
            # then remove it from our target
            visited.add(cur)
            res = -1
            neighbours = ourMap[cur]

            if target in neighbours:
                # Do math to get to target
                res = value * neighbours[target]
            else:
                for nei, val in neighbours.items():
                    # Don't go to a node we have seen
                    if nei in visited:
                        continue

                    # Otherwise travel down that path
                    res = dfs(nei, target, visited, value * val)

                    # If it isn't -1 we have found the solution so we just need to break out of backtracking
                    if res != -1.0:
                        break

            visited.remove(cur)
            return res

        result = []

        for src, dest in queries:
            if src not in ourMap or dest not in ourMap:
                result.append(-1.0)
            elif src == dest:
                result.append(1.0)
            else:
                # Create  a new set to track where we have been so we don't get cycles
                visited = set()
                result.append(dfs(src, dest, visited))

        return result

# This problem seems difficult but if you break it down into parts it is simply a dfs problem where you have weights
# on each path and you try backtracking to find a solution.

# Because this is backtracking we end up using o(VE) as we have to try every edge from every vertex
# and we store O(V) as we have V verticies to visit in the worst case

# A more optimal way to solve this is potentially using union find however I haven't implemented the version
# with weights


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 20
# Was the solution optimal? See above
# Were there any bugs? None
# 5 5 3 5 = 4.5
