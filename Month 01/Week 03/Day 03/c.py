#  Add Strings: https://leetcode.com/problems/add-strings/

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Super easy just loop through the number and multiply number by 10 ^ index going through backwards
# we can convert number with char values

from collections import deque


class Solution:
    # So my solution is to do this but since we cant use int we will have to use ord()
    # also instead of getting both numbers together I think we aren't allowed to use
    # + straight out
    def addStrings(self, num1: str, num2: str) -> str:
        val1 = 0
        val2 = 0

        for i in reversed(range(len(num1))):
            val1 += int(num1) * (10**i)

        for i in reversed(range(len(num2))):
            val2 += int(num2) * (10**i)

        return val1 + val2

    def addStringsOptimal(self, num1, num2):
        result = deque()

        numOneIndex = len(num1) - 1
        numTwoIndex = len(num2) - 1
        carry = 0

        # Loop through values from their first digit
        while numOneIndex >= 0 or numTwoIndex >= 0 or carry:
            val1 = ord(num1[numOneIndex]) - ord('0') if numOneIndex >= 0 else 0
            val2 = ord(num2[numTwoIndex]) - ord('0') if numTwoIndex >= 0 else 0

            val = val1 + val2 + carry
            carry, val = divmod(val, 10)

            result.appendleft(str(val))
            numOneIndex -= 1
            numTwoIndex -= 1

        return ''.join(result)


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 12
# Was the solution optimal? Yes this is an o(max(len(m), len(n)) time and space in the worst case
# Were there any bugs? None :D
#  5 5 5 5 = 5
