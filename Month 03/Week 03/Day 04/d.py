# Course Schedule II: https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

from types import List

# This problem is actually super easy once you know that it is a basic coloring algorithm. Basically we are searching for the order in which we should take
# classes given that this is a directed acyclic graph and that we cannot have cycles as prereqs must be taken before the class aka no cycles.
# Basically this becomes a dfs where we mark for completed taking or not seen if we see taking as part of our search it is an invalid path.

# The tricky part about this is we are actually returning a possible solution so we will actually need to take a backtracking dfs approach to this problem
# and record the path (I will be using a deque as our order will be reversed and I don't want to have to reverse afterwards)

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ourGraph = defaultdict(list)

        for toTake, isNeeded in prerequisites:
            ourGraph[isNeeded].append(toTake)

        visited = {}
        result = deque()

        # -1 is currently taking, 1 == completed, not in == not taken
        def topologicSort(node, visited):
            if node in visited:
                if visited[node] == -1:
                    return False

                if visited[node] == 1:
                    return True

            visited[node] = -1
            isValid = True

            for nextClass in ourGraph[node]:
                if isValid is False:
                    return False
                isValid = isValid and topologicSort(nextClass, visited)

            if isValid is False:
                return False

            visited[node] = 1
            result.appendleft(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not topologicSort(i, visited):
                    return []

        return result

# Badda bing badda boom
# This works like a charm I mean I made it a bit more convoluted by checking after every call if it is false in a weird way
# but regardless this runs in O(V+E) time and uses O(V) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 12
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
