# Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# This problem boils down to a simple sliding window solution like the first problem of the night
# and in fact it does the same thing I mentioned in the last about negative numbers
# you can use a hashmap to skip to the next time you see a removed letter to make it more optimal


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, left = 0, 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Right for the right most value, left + 1 as we moved 1 passed the solution
            result = max(result, right - left + 1)

            seen.add(s[right])

        return result

# So the above works but can we optimize it? The answer is yes because we know we can skip
# over the pieces we have already parsed by using our set as a dict instead

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        result, left = 0, 0
        seen = {}

        for right in range(len(s)):
            char = s[right]
            # Check if our chars new char is between left and right so we can use it
            # basically this cuts out extra work by automagically moving to the last
            # place we saw this char + 1
            if char in seen and seen[char] >= left and seen[char] < right:
                left = seen[char] + 1

            # Right for the right most value, left + 1 as we moved 1 passed the solution
            result = max(result, right - left + 1)

            seen[char] = right

        return result


# So this is lightly more optimized than above they both run in O(N) and o(min(m,n)) but the second solution
# would be ever so slightly faster and if you used a charset instead of a dict you could reduce this to
# a straight O(M) because you have the exact char set size of whatever the len of letters are

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 25
# Was the solution optimal? Oh hell yea
# Were there any bugs? none
# 5 5 5 5 = 5
