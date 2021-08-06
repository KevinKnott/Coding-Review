# Kill Process: https: // leetcode.com/problems/kill-process/

# You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.
# Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process(the root of the tree).
# When a process is killed, all of its children processes will also be killed.
# Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.

# This problem can be simplified if we go ahead and do an iteration where setup a tree and make sure that this new class includes a parent id.
# once we do that we simply do a bfs from the node we are killing and wallah we have an easy o(N) solution

from collections import defaultdict, deque


class Solution:
    def killProcess(self, pid, ppid, kill):
        if kill == 0:
            return pid

        ourGraph = defaultdict(list)

        # Basically since pid and ppid are linked we can
        # zip them together and for every ppid append the pid as a child
        for node, parent in zip(pid, ppid):
            ourGraph[parent].append(node)

        # Now all we have to do is create a queue that starts at kill and move our way down
        q = deque()
        q.appendleft(kill)

        result = []
        while q:
            node = q.pop()
            result.append(node)

            for child in ourGraph[node]:
                q.appendleft(child)

        return result


# This solution actually helps us a lot in the avg case as we can remove anything outside the scope of a tree rooted at kill
# this means it is more efficient the deeper the depth. However in worst case we still have to iterate over the whole tree
# this runs in O(N) time and space because of this (and creating the tree itself)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Awwwww yeet
# Were there any bugs? Negative there were no bugs to squash
# 5 5 5 5 = 5
