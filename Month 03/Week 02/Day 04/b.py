# Remove All Adjacent Duplicates in String II: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

# This problem basically screams to use a stack. Basically we can add letters as we parse along with the count of how many there are
# once we reach k we can pop it off otherwise we leave it alone. Then at the end we parse through the string of pairs and construct
# the valid string

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if len(stack) > 0 and stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    # Remove a char that has k element
                    stack.pop()
            else:
                stack.append([char, 1])

        result = ''
        for i in range(len(stack)):
            char, count = stack[i]
            result += char * count

        return result

# The above works and is pretty efficient it uses o(N) time and space the question is can we do better?
# I think that we could probably solve this slightly more efficiently with a two pointer solution
# keeping track of what is kept and what we have parsed but at the same time it would still require
# us to keep a stack of counts and is probably a bit more confusing

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Mine is optimal
# Were there any bugs?  I didn't really have any bugs
# 5 5 5 5 = 5
