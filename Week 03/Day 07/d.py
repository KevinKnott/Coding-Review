#  First Bad Version: https://leetcode.com/problems/first-bad-version/

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Haha this problem is actually just like the last one it wants us to use a binary search to find the first bad version in a series
# I believe the slight variation to this problem is that you want to find the palce where it turns bad instead of a value

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n

        while True:

            mid = lo + (hi - lo) // 2

            result = isBadVersion(mid)
            next = isBadVersion(mid + 1)

            # If result is not bad we need to search mid + 1 -> end
            if not result and next:
                return mid + 1
            elif result and next:
                hi = mid
            else:
                lo = mid

# Booom nailed the problem down! is this optimal? It is because it runs in logn in the worst case and has o(1) space

    def firstBadVersion(self, n):
        lo, hi = 1, n

        while lo < hi:

            mid = lo + (hi - lo) // 2

            result = isBadVersion(mid)

            # If result is not bad we need to search mid + 1 -> end
            if result:
                hi = mid
            else:
                lo = mid + 1

        return lo

    # I realized that since we are checking for a swap I don't need to call the api twice so I could optimize a bit more
    # in this case we keep moving left and right together until they swap places aka the one on the right is true and the one on left is false
    # and we have our answer

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 20 min
# Was the solution optimal? Oh yea
# Were there any bugs? 0
# 5 5 5 5 = 5
