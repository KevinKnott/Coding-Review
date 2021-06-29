# Evaluate Division: https://leetcode.com/problems/evaluate-division/
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Initial thoughts is that this is a system eq problem
# After 5 minutes I looked and it turns out this is a graph problem


from collections import defaultdict


class initial():
    def calcEq(self, equations, values, queries):
        graph = defaultdict(defaultdict)

        for (dividend, divisor), values in zip(equations, values):
            graph[dividend][divisor] = values
            graph[divisor][dividend] = 1/values

        return graph


equations, values, queries = [["a", "b"], ["b", "c"]],  [2.0, 3.0], [
    ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
sol = initial()
print(sol.calcEq(equations, values, queries))

# Score Card
# Did I need hints
# Did you finish within 30 min?
# 29 min for both
# Was the solution optimal
# Were there any bugs
# 1 1 1 1 = 1
# This problem i can't even wrap my head around and will need practice
