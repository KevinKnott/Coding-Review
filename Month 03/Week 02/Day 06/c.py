# Number of Recent Calls: https://leetcode.com/problems/number-of-recent-calls/

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

#     RecentCounter() Initializes the counter with zero recent requests.
#     int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# This is a basic q problem you pop off anything with the time  before t - 3000 at every ping and return the len of the q

from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        if t > 3000:
            while self.q and self.q[-1] < t - 3000:
                self.q.pop()

        self.q.appendleft(t)

        return len(self.q)

# Easy q problem super straight forward O(1) time and space


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
