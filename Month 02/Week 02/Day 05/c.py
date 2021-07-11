# Remove All Adjacent Duplicates in String II: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

# This seems like a simple stack problem where you keep the value of how many you have seen and if you add up to k in a row
# you pop them off the string. There may be some edge cases that I have missed though

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:

            if len(stack) != 0 and char == stack[-1][0]:
                # We have a repeated char now we need to update the stack to have one more
                stack[-1][1] += 1

                # Check if we have k repeated
                if stack[-1][1] == k:
                    # Pop them off
                    stack.pop()
            else:
                stack.append([char, 1])

        result = ''

        for char, count in stack:
            result += char * count

        return result

# So this works and runs in o(N) time and uses o(N) space as we are potentially adding everything into our stack
# and then adding it to our resulting string

# Can we improve this?  There is actually a pretty nifty way we could probably improve this so the premise of reconstructing
# the string can help because we can use a fast pointer and a slow pointer and potentially update the string in real time
# This would reduce our time by not having to recreate another string. However the it still runs in o(n) and o(n) as we
# need a stack still to keep just the count

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 16
# Was the solution optimal? See above
# Were there any bugs? I accidently used a tuple for my counts which you can't update pretty silly mistake honestly
# 5 5 5 5 = 5
