# Number of Recent Calls: https://leetcode.com/problems/number-of-recent-calls/

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

#     RecentCounter() Initializes the counter with zero recent requests.
#     int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# There is a simple way of solving this problem if you use a double ended queue you can simple push
# any values on and then pop off anything that is below t - 3000 then return the length


from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()
        return

    def ping(self, t: int) -> int:
        if t > 3000:
            while len(self.q) > 0 and self.q[-1] < (t - 3000):
                self.q.pop()

        self.q.appendleft(t)

        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# This problem is really simple and is just a basic deque usage honestly it is kind of like a window solution as well
# just using a ping instead of an array of nums this wil run in o(1) time and space as the t doesn't affect
# what is being added or removed we have an arbitrary number of values to remove

# To improve this code we could try to use an array and the bs throught he numbers since time is always sorted
# but we would run into space limitation constantly moving all the numbers in the array

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
