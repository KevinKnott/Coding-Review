# Task Scheduler: https://leetcode.com/problems/task-scheduler/

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# My initial thoughts on this problem are to run a simulation to do this we can use a queue
# and simply push whatever task we want to do first (if it isn't already in the q) and pop
# after n iterations. To keep track of what is not doable we can keep a set of tasks and
# check if it is in set or not

from collections import Counter, deque, OrderedDict


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        q = deque()
        tasks = Counter(tasks)
        impossible = set()
        count = 0

        # I need to actually sort the tasks by number of tasks greatest to shortest
        # so I am using Orderd dict
        tasks = OrderedDict(tasks.most_common())

        while len(tasks) > 0:
            # tasks = OrderedDict(tasks.most_common())
            count += 1
            if n < 0:
                lastFinished = q.pop()
                if lastFinished in impossible:
                    impossible.remove(lastFinished)

            ableToAdd = False
            for key in tasks.keys():
                if key not in impossible:
                    ableToAdd = True
                    impossible.add(key)
                    q.appendleft(key)
                    tasks[key] -= 1

                    if tasks[key] == 0:
                        del(tasks[key])
                    break

            if ableToAdd is False:
                q.appendleft('Idle')

            n -= 1

        return count

# So the above solution isn't actually fully complete I have a slight bug when to actually pop that I couldn't figure out
# However I am very close with it # That being saiid  it runs in o(N * k) where N  is nums and k is the delay and o(N)
# space for storing everything in a counter and Q

# So the main thing I am missing out on is that a wait time only occurs if there aren't enough elements to plug
# inbetween the wait period
    def leastIntervalOptimized(self, tasks, n: int) -> int:
        d = {}
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1
        max_freq = max(d.values())
        last_row = 0
        for k, v in d.items():
            if v == max_freq:
                last_row += 1

        return max((max_freq - 1) * (n + 1) + last_row, len(tasks))


# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? 45 min
# Was the solution optimal? My solution was not optimal
# Were there any bugs? See bug comment halfway down
# 3 2 3 3 = 2.75
