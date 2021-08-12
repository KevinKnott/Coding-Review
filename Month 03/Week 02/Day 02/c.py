# Next Greater Element I: https://leetcode.com/problems/next-greater-element-i/

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# In this problem we are searching for the next greater element after self in in the second nums array
# normally we would do a heavy n^2 and for every number in num1 find its location in num2 and find the number after it
# we can do a little better than that if we try and use a hashmap and a stack to find the next number that will be higher
# than it. This is because with stacks we can easily parse a number and do something for the previous number(s) while parsing

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        nextHighest = {}
        stack = []

        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                nextHighest[stack.pop()] = num

            stack.append(num)

        # Anything still on the stack has nothing higher after it so we put a -1 there
        while stack:
            nextHighest[stack.pop()] = -1

        result = []

        for num in nums1:
            if num in nextHighest:
                result.append(nextHighest[num])
            else:
                result.append(-1)

        return result

# Another day another easy problem. Basically I did exactly what I said in previous blurb.
# This will run in O(N + M) time and o(N) space

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? Yeah
# Were there any bugs? None
# 5 5 5 5 = 5
