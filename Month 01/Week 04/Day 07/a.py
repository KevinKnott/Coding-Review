# Decode String: https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:
        values = []
        strings = []

        index = 0
        curVal = 0
        curStr = ''
        result = ''

        while index < len(s):
            if s[index].isdigit():
                # Continue appending until we reach '['
                while s[index] != '[':
                    curVal = (10 * curVal) + int(s[index])
                    index += 1

                # Add our values
                values.append(curVal)
                strings.append(curStr)

                # Reset temp
                curVal = 0
                curStr = ''

            elif s[index] == ']':
                curStr = strings.pop() + (curStr * values.pop())
            else:
                curStr += s[index]

            index += 1

        if curStr:
            result += curStr

        return result

# My above solution works by using two stacks we can simplify this problem quite a bit in the grand scheme of things
# this will run in o(maxK * N) so the max k which is the int values in the values stack time and o(N+D) where D is the
# depth of nested values


# Is it possible to do better? I suppose that the recursion of this may actually be a bit better but under the hood
# I think the stack space will use just about the same amount of space.


# # Score Card
# Did I need hints? N
# Did you finish within 30 min? yes 27 min
# Was the solution optimal? Oh yea see my blurb above
# Were there any bugs? I had a slight confusion on how to return the string when we pop values off wher I switch cur string with a result string
# 5 5 5 3 = 4.5
