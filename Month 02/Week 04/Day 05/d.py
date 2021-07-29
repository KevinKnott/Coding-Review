# Course Schedule II: https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# This problem is a more advanced implementation of the topological sorting coloring algorithm in which we store the path as we create it using the DFS

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        courses = defaultdict(list)

        for toTake, isNeeded in prerequisites:
            courses[isNeeded].append(toTake)

        visited = {}
        path = deque()

        # For topologic sort we need to check if we are currently visiting a node (-1)
        # or if it has been completed (1) otherwise we have not been to this node
        # so we check it all out
        def topologic(node):
            # We check for a cycle
            if node in visited and visited[node] == -1:
                return False
            # Check if we have already completed the search for this node
            if node in visited and visited[node] == 1:
                return True

            # Finally check if we can actually finish this node by trying every other possibility
            # but mark node as currently traversing
            visited[node] = -1

            isValid = True

            # Loop through possibilities of other classes
            for nextClass in courses[node]:
                if isValid is False:
                    break
                isValid = isValid and topologic(nextClass)

            if isValid is False:
                return False

            # If we get here we have checked all nodes and we needed
            # and can add this to our list so we mark it complete
            # and add it to the list
            visited[node] = 1
            path.appendleft(node)

            return True

        for i in range(numCourses):
            if i not in visited:
                if not topologic(i):
                    return []

        return path

# The above works and runs in O(V+E) time and space as we will visit every vertex and edge once and we
# we store the traversing information in a dictionary

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
