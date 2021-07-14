# Pow(x, n): https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# This problem is pretty straight forward we simply iterate over the n times
# multiplying the input every time. The only tricky thing is that if we have
# a negative number we need to make sure to set it to 1/x before multiplying together

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0

        if n < 0:
            x = 1/x
            n *= -1

        result = 1
        for _ in range(n):
            result *= x

        return result

# The above works! The code runs in o(N)  steps and uses o(1) space the problem is this isn't the fastest we can do!
# This is based off of the math that 2 ^ 10 == 4 ^ 5 = 4 * 16 ^ 2 = 4 * 256 ^ 1 = 1024
# If you look at the above we can reduce n by half in every single iteration which means that we can have a resulting
# o(logn) solution

    def myPowOptimus(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0

        if n < 0:
            x = 1/x
            n *= -1

        result = 1.0
        current = x
        index = n
        while index > 0:
            # If we have an odd number we mutliply the result times the current factor so we can make our factor even
            # so we can multiply it by itslef to reduce to half
            if index % 2 == 1:
                result = result * current

            # Multiply current by current to reduce exponent in half
            current = current * current
            # Make sure our iterator is decreased by half
            index = index // 2

        return result

# Score Card
# Did I need hints? Yes because I forgot that I switched my index to equal n to make things more clear
# Did you finish within 30 min? 20
# Was the solution optimal? Oh yeah this runs in o(logn) and o(1)
# Were there any bugs? Yeah i forgot to make my odd exponent check use the right variable
# 3 5 5 3 = 4
