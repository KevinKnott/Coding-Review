# Number of Recent Calls: https://leetcode.com/problems/number-of-recent-calls/

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
# Implement the RecentCounter class:
#     RecentCounter() Initializes the counter with zero recent requests.
#     int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# After reading the explanation this seems like a hash / bucketing problem
# Although we can also just keep a list of values and update it as we go using a q or any such list

from collections import deque


class RecentCounter:

    def __init__(self):
        self.window = deque()

    def ping(self, t: int) -> int:
        # Remove anything from window  from before the t - 3000
        while len(self.window) > 0 and self.window[0] < (t - 3000):
            self.window.popleft()

        # Then add our result
        self.window.append(t)

        return len(self.window)

# Boom solved in 7 minutes
# Okay the solution above is an o(n) operation as we have to go through potentially the whole q in worst case
# Although we also know that the operation will only have max of  3000 operations so it is really o(1)


# Can we do better?
# I don't think we can really do much better other than maybe creating a list and doing a binary search
# this may work because we actually are getting strictly increasing numbers which means we can search through the array
# for the first index that is lower than t-3000 and return everything to the right
# however this is way more complicated then the above and uses more space overall so in large n's it will be less effective
# Although thinking about it you could find the midpoint in a linked list and update that way and keep the new head


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y although you can read my blurb above about a potentially better solution it is rather complicated
# Were there any bugs? N
#  5 5 3 5 = 4.5
