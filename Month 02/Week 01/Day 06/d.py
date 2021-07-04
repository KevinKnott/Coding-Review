# Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# So this is a classic sliding window problem we will keep a set of values we have already seen
# while we expand to the right we check if the char has been seen if it has we pop off from the left until
# there are no more duplicatesand then we check for the longest array


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        result = 0

        seen = set()
        left = 0
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

            result = max(result, right - left + 1)

            seen.add(s[right])

        return result

# The above worked boo yeah and it runs in o(n) with o(1) although really it is o(k) where k is the longest interval
# but since this is capped at 26 it is o(1) space
# The question is "Is this optimal?"
# There is a slight optimization problem where instead of moving the left one at a time we can actually keep
# track of the index of the value we saw the duplicate and move to that spot + 1 to increase the effectiveness
# a little bit but still same complexity it is really o(2n) vs o(n)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
