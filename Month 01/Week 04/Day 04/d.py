# First Unique Character in a String: https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

# This problem is actually pretty straight forward if we loop through the array
# and keep a hashtable or list of the alphabet and keep count (or use counter)
# we can simply count and then look for the first value that has a count of 1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for char in s:
            if char not in seen:
                seen[char] = 0
            seen[char] += 1

        for index in range(len(s)):
            if seen[s[index]] == 1:
                return index

        return -1

# Could we possibly do better? I think not as we are simply building a counter (the actuall counter class may slightly be faster)
# but never the less this will run in o(n) and o(1) times where n is the length of the string also it is o(1) space as there
# is actually only 26 (or 52) letters that could be used total and any value that is of a constant size will be o(1)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 4
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
