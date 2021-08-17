# Number of Recent Calls: https://leetcode.com/problems/number-of-recent-calls/

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

#     RecentCounter() Initializes the counter with zero recent requests.
#     int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


class RecentCounter:

    def __init__(self):
        return

    def ping(self, t: int) -> int:
        return


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(1) space
# Were there any bugs? None
# 5 5 5 5 = 5
