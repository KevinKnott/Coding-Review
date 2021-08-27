# Pow(x, n):  https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# This problem is initially quite difficult as the problem wants us to preferably do this in faster than
# O(N) time which is possible since we know that we can combine exponents together by going  through
# and squaring them aka  2 ^ 10 = 4 ^ 5 = 4 * (16 ^ 2) = 4 * (256) = 1024

# This will work for negative numbers in the exponent but we will need to be careful to invert our
# base to 1/x


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

# Perfect this works as I expected it to!
# This wil run in O(logn) and ueses O(1) extra space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
