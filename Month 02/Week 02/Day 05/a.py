# Evaluate Division: https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# So my initial thoughts on this problem are that we need to create a simple graph that equates to the solution of  Ai/Bi and Bi/Ai as Ai/Bi = X then Bi/Ai = 1/x
# Then we need to see how we can complete the substitution to get to whatever is needed by the query. There is the exception of two things Ai/Ai always is one
# and then if we haven't seen Ai or Bi in our equations we cannot solve so it will always be -1

from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        # Create the equation graph from A/B = Value to B/A = 1/Value
        graph = defaultdict(defaultdict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1/value

        def dfs(cur, target, visited, cumProd=1):
            visited.add(cur)
            ret = -1.0
            neighbor = graph[cur]
            # So we have visited our node so we need to see if it connects to the divisor
            # if it does we can simply return the result
            if target in neighbor:
                ret = cumProd * neighbor[target]
            else:
                # Otherwise we need to dfs backtrack visiting all of our neighbors to find path
                # As well as update the value as we go down
                for nei, value in neighbor.items():
                    # Skip any node we have visted or are visiting
                    if neighbor in visited:
                        continue

                    # Check if we can find a path
                    ret = dfs(nei, target, visited, cumProd * value)

                    # If we have visted and can't find the path to a result we can just end the search
                    if ret == -1.0:
                        break

            visited.remove(cur)
            return ret

        result = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # Now that we have the above we can find out Cj/Dj in the following manner one there must exist a path from Ai - Cj then a path from Cj -> Dj
                # so if Cj/Dj are not in our graph we have no path so the result is -1
                ret = -1.0
            elif divisor == dividend:
                # From math we know that Ai/Ai will always be 1 4/4 = 1 5/5 = 1
                ret = 1.0
            else:
                # Otherwise we simply have our initial cumulative product and multiply it by the value of the path moving down and return when we find the answer (DFS)
                visited = set()
                ret = dfs(dividend, divisor, visited)

            result.append(ret)

        return result

# Hell yeah this problem is a bit tricky at first but honestly once you understand that you can convert this to a simple DFS you can see that it is quite easy.
# That being said this runs in o(M*N) as we have to create the graph and then traverse every possible path as for space it ends up only using o(N) for
# the graph, visited and stack space as we only visit each node once

# The question is "Is this optimal"? While I believe that this is pretty optimal it kind of reminds me of a union find problem although instead of having the root nodes
# being what is returned we actually use the weights when making a path from dividend to divisor I think that overall this could improve time as we can build a path
# and then anytime a query is already a part of a previous query we can reduce the time of the search. That being said I only recently learned about these and I  only
# have two minutes left

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? Y
# Was the solution optimal? I think there is a more optimal solution but mine is also pretty fast
# Were there any bugs? Nope
# 5 5 2 5 = 4.25
