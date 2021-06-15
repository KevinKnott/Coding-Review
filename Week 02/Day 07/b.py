# Course Schedule II: https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


class Solution:
    def findOrder(self, numCourses, prerequisites):
        return

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? N I didn't think of the quick select solution and I would still have to implement it
# Were there any bugs? Y my sorting took me a while to figure out my keys actually needed to be baseed off of count.get instead of count
#  4 3 3 2 = 3
