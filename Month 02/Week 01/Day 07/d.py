# Evaluate Division: https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# So my initial thought on this problem is that we can convert this to a simple graph problem
# there are a few trick things that we need to know though. The main one is one of the values
# we need to know isn't in the graph at all we return -1 other than that A/B = 2 means B/A = 1/2

from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        def backtrackDFS(node, target, ans, visited):
            # So this is a backtrack we try adding the cur node
            # otherwise we pop it off and continue

            visited.add(node)
            ret = -1.0
            neighbors = graph[node]
            if target in neighbors:
                ret = ans * neighbors[target]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrackDFS(neighbor, target, ans * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(node)
            return ret

        graph = defaultdict(defaultdict)

        # Create all relations
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # now that we have a graph we can do a dfs or if it isn't in
        #  our graph we can return -1
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0
            # Technically this should always be one
            elif dividend == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = backtrackDFS(dividend, divisor, 1, visited)

            results.append(ret)

        return results


# The above works although it took some time to complete I am not sure on the time complexity
# I think it runs in o(M*N) as we have to loop through all M quereies and N input equations
# The space will store all of the N input equations (technically 2n)

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 70
# Was the solution optimal? This is optimal I think
# Were there any bugs? No
# 2 2 3 5 = 3
