# Kill Process: https: // leetcode.com/problems/kill-process/

# You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.
# Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process(the root of the tree).
# When a process is killed, all of its children processes will also be killed.
# Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.


class Solution:
    def killProcess(self, pid, ppid, kill):
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
