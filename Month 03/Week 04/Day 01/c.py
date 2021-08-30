# Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# In order to solve this problem we can go through the list with a sliding windowand take a count of every char
# then we can simply reduce this down everytime that we have a char twice and then check for the longest answer
# while this is pretty much optimal there is a slight optimization you can make by keeping track
# of what index you saw the char at so you can quickly jump over and not have to manually remove all the chars
# up to that index you can just check if they are at a higher index


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            result = max(result, right - left + 1)

            seen.add(s[right])

        return result

# This solution is super easy and actually runs in O(N) time could be O(1) if we are only considering
# the alphabet but could become as large as O(len(alphabet))

# Now this is pretty optimal but like I said you could make a small change to quickly jump until the
# next time you see the char and ignore any chars that are of a lower index
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        result = 0
        left = 0
        seen = {}

        for right in range(len(s)):
            char = s[right]
            # Basically move left if that char is still valid other wise
            # keep the other left max that we have seen
            if char in seen and seen[char] >= left and seen[char] < right:
                left = seen[char] + 1

            result = max(result, right - left + 1)

            seen[char] = right

        return result

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 15
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
