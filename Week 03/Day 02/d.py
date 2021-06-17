#  Remove All Adjacent Duplicates In String: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# My guess is that we should use a stack here as we can simply add a value and check if it equals last if it does
# pop off the stack other wise append
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if len(stack) > 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)

# Now is the above optimal I think so as this runs in O(n) time as we visit each letter once and o(n) space because we keep a stack that may be all different chars

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal although I suppose you could recurse which would be worse
# Were there any bugs? I forgot to check if node was null at the start
#  5 5 5 4 = 4.75
