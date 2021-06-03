#  Decode Ways: https://leetcode.com/problems/decode-ways/
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.

# initial thought is to decode this string using a version of backtracking. You can either pop off two digits and form 1-26 (no leading zeroes) or pop one and decode 1-9. once you are all the way through add to count.


class initial():
    def decode(self, s):
        self.memo = {}
        return self.helper(s)

    def helper(self, s, index=0):
        if index in self.memo:
            return self.memo[index]

        if index == len(s):
            return 1

        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        count = self.helper(s, index+1)
        temp = s[index:index+2]
        if int(temp) <= 26:
            count += self.helper(s, index+2)

        self.memo[index] = count
        return count


s = '2326'
sol = initial()
print(sol.decode(s))

# I had a hard time decoding this problem i ended up getting a similar solution to the dfs problem but I need to add memoization because there is potentially a lot of extra work being done
# that being said there is also a dp and a iterative solution that I didn't even get close to

# Score Card
# Did I need hints? y
# Did you finish within 30 min? n
# Was the solution optimal? n
# Were there any bugs? n
# 1 1 1 1 = 1
