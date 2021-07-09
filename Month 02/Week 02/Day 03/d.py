# Course Schedule: https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# So this is a graph coloring problem in fact I have done the harder version of this where you return a valid
# path. All we need to do is create a directed graph and traverse it in a dfs and if we see the traversing
# color we return false go back and try the next until we get to the very end

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = defaultdict(list)
        for toTake, isNeeded in prerequisites:
            graph[isNeeded].append(toTake)

        # Visited will be one of 3 states finished 1, searching -1 or empty of result
        visited = {}

        def dfs(node):
            if self.isPossible == False:
                return

            if node in visited:
                if visited[node] == -1:
                    self.isPossible = False
                    return
                if visited[node] == 1:
                    return

            # We have an unvisited node so mark it searching and continue down path
            visited[node] = -1

            for nextNode in graph[node]:
                dfs(nextNode)

            # If we have gotten here we have traversed as far as we can so we add this to result
            visited[node] = 1

        # So the only tricky thing is if we ever find a cycle we need a way to break out
        # So I used this class variable alternatively you can return True/False
        # and simply always check for it at every dfs call
        self.isPossible = True
        for i in range(numCourses):
            if i not in visited:
                dfs(i)

                if not self.isPossible:
                    break

        return self.isPossible

# Oh I forgot the time complexity this will run in o(V+E) time and space as we take E to create adj list
# then our traversal cover all V+E as for space we store all of the E in adj list and then we traverse
# using a stack whic means that we have V on the stack

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 15
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5= 5
