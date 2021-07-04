# Course Schedule II: https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# So my thought is that this problem is a finding a cycle in a directed graph
# We should take the prerequisites and convert them into an adjacency list and then we can do a simple bfs/dfs in which
# we color nodes to make sure that we dont reach a node that we are currently  investigating the path

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):

        # preReq is [a, b] where b -> a
        # Also note that we need to populate adjacency list for things not including prereqs
        # as some classes may not have prereqs
        graph = defaultdict(list)

        for toTake, isNeeded in prerequisites:
            graph[isNeeded].append(toTake)

        # So our visited in this case will have three "Colors" In path, Visiting , unvisited
        # If we ever find a node that we are currently still visiting we have no solution
        visited = {}
        path = []

        def dfs(node):
            if node in visited and visited[node] == -1:
                return False

            if node in visited and visited[node] == 1:
                return True

            # Mark that we are visiting this node currently
            visited[node] = -1

            # Check what this node is needed for and traverse down that path
            isValid = True

            for nextClass in graph[node]:
                temp = dfs(nextClass)
                isValid = isValid and temp

            if not isValid:
                return False

            visited[node] = 1
            path.append(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        return path[::-1]

# So the above works and is a simple DFS that involves coloring of nodes it runs o(V+E) time and o(V+E) space
# Can we do better? There is an algorithm that is better for cycle detection but since it is July 4th I won't
# be looking at it right now

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20 min
# Was the solution optimal? See above!
# Were there any bugs?  No bugs on this today!
# 5 5 3 5 = 4.5
