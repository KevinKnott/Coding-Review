# Decode String: https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# For this problem we are parsing through a string and are tracking what values need to be multiplied. The optimal solution
# probably involves taking two stacks and recording the number to multiply and the current string while you parse new strings
# and then doing the math to return the result

class Solution:
    def decodeString(self, s: str) -> str:
        result = ''
        stack, strStack = [], []

        index = 0

        while index < len(s):
            if s[index].isdigit():
                val = 0
                while s[index].isdigit():
                    val = (val * 10) + int(s[index])
                    index += 1

                stack.append(val)
                strStack.append(result)
                result = ''
            elif s[index] == ']':
                result = strStack.pop() + (result * stack.pop())
            else:
                result += s[index]

            index += 1

        return result

# Oh yeah the above works and runs in O(maxK * N) time where k is the val of the repeated str and uses o(M+N) space
# where M is len of val stack and N is the len of strStack
# I solved in 8 min

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Oh yea
# Were there any bugs?  No bugs for me
# 5 5 5 5 = 5
