# Kill Process: https://leetcode.com/problems/kill-process/

# You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.
# Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).
# When a process is killed, all of its children processes will also be killed.
# Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.

# I think that the brute force solution of this problem is to go through the loop killing node by node with a queue and go through until you delete everything


from collections import deque


class Solution:
    def killProcess(self, pid, ppid, kill):
        q = deque()
        q.appendleft(kill)

        result = []

        while q:
            remove = q.pop()
            result.append(remove)

            for index in range(len(pid)):
                if pid[index] in result:
                    continue
                if ppid[index] == remove:
                    q.appendleft(pid[index])

        return result

# This should work but is it optimal?  no because in worse case scenario you would have to go down o(n^n) potentiall possibilities
# So to improve this we could recreate the tree from pid and ppid and then delete the node which we could dfs/bfs down.
    # This is the dfs solution in case the order doesn't matter
    def killProcessDFS(self, pid, ppid, kill):
        ourTree = {}
        # Recreate tree
        for i in range(len(pid)):
            if ppid[i] not in ourTree:
                ourTree[ppid[i]] = []
            ourTree[ppid[i]].append(pid[i])

        # Visit from root down until you hit the result
        stack = []
        stack.append(kill)
        result = []

        while stack:
            kill = stack.pop()
            result.append(kill)

            if kill in ourTree:
                stack += ourTree[kill]

        return result

    def killProcessBFS(self, pid, ppid, kill):
        ourTree = {}
        # Recreate tree
        for i in range(len(pid)):
            if ppid[i] not in ourTree:
                ourTree[ppid[i]] = []
            ourTree[ppid[i]].append(pid[i])

        q = deque()
        q.appendleft(kill)
        result = []

        while q:
            kill = q.pop()
            result.append(kill)

            if kill in ourTree:
                for node in ourTree[kill]:
                    q.appendleft(node)

        return result


# This solution take o(N) and o(N) as we are storing the N nodes in a hash and iterating over in a standard DFS/BFS

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 27 min
# Was the solution optimal? This is optimal
# Were there any bugs? I accidentily forgot to initialize my hash correctly
# 5 5 5 5 = 5
