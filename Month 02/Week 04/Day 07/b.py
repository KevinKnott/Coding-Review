# Pow(x, n): https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# The initial problem would simply to do an o(n) operation and simply multiply the number
# as we go up the whole way however since we know some math about logs we know that
# we can multiply the values by n to use a log.

# This is because 2 ^ 8 = 2 ^ 4 * 2 ^ 4 = etc etc the only difference is if you have an odd number
# you need to simply multiply on whatever the base is at

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        # If an exponent is negative we have 1/exponent
        if n < 0:
            x = 1/x
            # Make the number not negative
            n = -1 * n

        result = 1
        current = x
        index = n
        while index > 0:
            if (index % 2) == 1:
                result = result * current

            current = current * current
            index //= 2

        return result

# The above works but you actually have to know a bit about the math behind it
# It runs in o(nlogn) and o(1) sapce

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? See above
# Were there any bugs?  No
# 5 5 5 5 = 5
