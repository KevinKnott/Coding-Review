# Pow(x, n): https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Uhm I feel like this is a super simple problem where you loop n times and multiply the result by n
# but that can't be the solution because it would be too easy
# I am willing to be that there is a math trick to this problem

class Solution:
    def myPow(self, x, n):
        # Basic math checks 0 * n is 0
        # x ^ 0 is always 1
        if x == 0:
            return 0
        if n == 0:
            return 1

        # If n is negative we must invert it because math
        if n < 0:
            x = 1/x
            n = -1 * n

        result = 1

        for i in range(n):
            result = x * result

        return result

# This runs in o(n) time and works apparently like I guessed this is not the solution as it is TLE in leetcode

# Thinking about this a little more you can actually improve this by cutting computation in half ie 2 ^ 2  + 2 ^ 2 = 2^4
# So if we use this to iterate over our n while halving the exponent as we go we should be able to solve this faster
    def myPow(self, x, n):
        # Basic math checks 0 * n is 0
        # x ^ 0 is always 1
        if x == 0:
            return 0
        if n == 0:
            return 1

        # If n is negative we must invert it because math
        if n < 0:
            x = 1/x
            n = -1 * n

        result = 1
        current = x
        index = n
        while index > 0:
            # If we are at an odd number we are at a 1 or 3 so we need to multiply one more time
            if (index % 2) == 1:
                result = result * current

            # After that check we can multiply together
            current = current * current

            index = index // 2

        return result

# The above is kind of a smart algorithm if that uses log(n) time to compute pow
# This is because 2 ^ 10 == 4 ^ 5 = 4 * 16 ^ 2 = 4 * 256 ^ 1 = 1024

# Score Card
# Did I need hints? Yes the optimal solution required a bit of math that I am shaky on
# Did you finish within 30 min? 3 min for first solution 30 for second
# Was the solution optimal? This is optimal for sure (the second one)
# Were there any bugs? Yea I initially forgot to check if we had an odd number at first
# 3 4 5 3 = 3.75
