# Course Schedule II: https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# I know that this problem is a topological sort however I haven't coded one in  while
# The basic premise is to build a dfs where you visit all courses with a model of White (Unvisited) Grey (In Calc) and Black (Visited with no reqs)


class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    # O(V + E) we create a graph of vertex to edge and visit them all only once
    # o(V+E) since we have a ajdacency list of V and a stack of potentially E
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        color = {course: Solution.WHITE for course in range(numCourses)}
        topologicalOrder = []
        isPossible = True

        for dest, src in prerequisites:
            if src not in graph:
                graph[src] = []
            graph[src].append(dest)

        def topologicalSort(course):
            nonlocal isPossible

            if not isPossible:
                return False

            color[course] = Solution.GRAY
            if course in graph:
                for i in graph[course]:
                    if color[i] == Solution.WHITE:
                        topologicalSort(i)
                    elif color[i] == Solution.GRAY:
                        isPossible = False
                        return

            color[course] = Solution.BLACK
            topologicalOrder.append(course)

            return

        for course in range(numCourses):
            if color[course] == Solution.WHITE:
                topologicalSort(course)

        return topologicalOrder[::-1] if isPossible else []

# With a little bit of help I have been able to reproduce the algorithm
# But is there a more optimal way? I am not sure but I will have to look it up


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? N I didn't think of the quick select solution and I would still have to implement it
# Were there any bugs? Y my sorting took me a while to figure out my keys actually needed to be baseed off of count.get instead of count
#  4 3 3 2 = 3
