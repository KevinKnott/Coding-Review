# Add Strings: https://leetcode.com/problems/add-strings/

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# I think the easiest way to solve this problem is to reverse the string and then as we move across
# create the new string values and keep track of the carry. After this is done we simply
# need to reverse the string again

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0

        len1, len2 = len(num1) - 1, len(num2) - 1

        while len1 >= 0 or len2 >= 0:
            if len1 >= 0:
                carry += ord(num1[len1]) - ord('0')
                len1 -= 1

            if len2 >= 0:
                carry += ord(num2[len2]) - ord('0')
                len2 -= 1

            result.append(str(carry % 10))
            carry = carry // 10

        if carry:
            result.append('1')

        return ''.join(result[::-1])


# The above works quite well as it runs in O(max(len(num1) , len(num2))) and uses o(N) addtional space
# I suppose you could technically overwrite the longer of num1 or num2 if you wanted to conserve more space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Yea
# Were there any bugs?  Nope
# 5 5 5 5 = 5
