# Task Scheduler: https://leetcode.com/problems/task-scheduler/

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.


# Okay so this problem is kind of tricky but what it boils down to is the fact that we need to find the most frequent element
# and calculate how long it will take to complete this taks with just the most frequent ie max(task) * n then we need
# to take every other possible element and try and add it to the idle time from above this should give us our answer
# the only awkward situations should be if we have multiple of the max value


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # Create a map of 26 values
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()

        # Now that we have the most frequent (it actually doesn't matter if we have the correct task order)
        maxFreq = freq.pop()
        # Idle time doens't include anything after last placement so f - 1
        idleTime = (maxFreq - 1) * n

        # Now we try to place elements until our cool down is empty meaning we have to place x after it
        while freq and idleTime > 0:
            # Here we will
            idleTime -= min(maxFreq - 1, freq.pop())

        # make sure idle time is above 0
        idleTime = max(0, idleTime)

        return idleTime + len(tasks)

# This will run in O(N) time and O(1) space which is pretty optimal

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Yee Yee
# Were there any bugs?  I forgot to make the idle Time positive
# 5 5 5 5 = 5
