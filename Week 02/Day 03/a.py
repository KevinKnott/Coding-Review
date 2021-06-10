# Decode String: https://leetcode.com/problems/decode-string/
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].


class Solution:
    def decodeString(self, s: str) -> str:
        return

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Pretty well although there is a dynamic programming solution and there is even a o(n) with two pointers
# This actually kind of reminds of finding the fibonaci where it is based off the two previous answers
# Were there any bugs? My base cases need to be in a certain order and what I mentioned in the problem
#  3 3 1 3 = 2.5
