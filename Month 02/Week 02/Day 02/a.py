# Task Scheduler: https://leetcode.com/problems/task-scheduler/

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Okay so my first thought is that we can create a simulation of this problem however I believe that we may have to intelligently pick our task to optimize so it would be using a backtrack which would be kind of challenging
# So what can we do instead?

# It looks like there is possibly a mathematical way to see how many idles we need by taking the largest count and multiplying it by the distance of idle time
# and then seeing how many matching element counts there are

from collections import Counter


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        if n == 0 or len(tasks) == 0:
            return len(tasks)

        count = Counter(tasks)
        count = count.most_common()

        # We need to take the max value that we see
        maxVal = count[0][1]
        # Then we need to count how many of these we have becasue that will continue the train
        nMax = 0
        for _, v in count:
            if v == maxVal:
                nMax += 1
            else:
                break

        # So the math is what the max count is  - 1 * (the space between reoccuring values) + how many over the pattern we go
        result = (maxVal - 1) * (n + 1) + nMax
        # Or we  return that the max is the number of elements if that is bigger (we have to use every element 1 time in base cases)
        return max(len(tasks), result)

# The above works and runs in o(n) time and o(1) space as there are max 26 tasks and we simply keep count in a dict of size 26
# The math part is kind of clever and took some time to think of but I did forget that we need to just use the len if we can loop
# through elements without having a cool down problem

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? Yes this is a simple math problem but see my above blurb
# Were there any bugs? See blurb
# 5 5 5 3 = 4.5
