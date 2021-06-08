# Next Greater Element I: https://leetcode.com/problems/next-greater-element-i/
# Given the root of a binary tree, invert the tree, and return its root.

# You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.


# The simplest solution is to sort nums2 and then binary search for the number and add index + 1 unless at the border
# So the problem description needed clarification from me it is asking for the next greater element passed its location in the second
# I misunderstood the problem
from collections import deque


class Solution:
    def nextGreaterElementOverall(self, nums1, nums2):
        nums2.sort()
        result = []

        for num in nums1:
            low, high = 0, len(nums2) - 1
            while low <= high:
                mid = low + (high - low) // 2

                if nums2[mid] < num:
                    low = mid + 1
                elif nums2[mid] > num:
                    high = mid - 1
                else:
                    if mid == len(nums2):
                        result.append(-1)
                    else:
                        result.append(nums2[mid+1])
                    break
        return result

    # The above gets the next highest value
    # The easiest solution is to go through nums2 until you find the number then go through everything after and append highest you find or -1
    def nextGreaterElementAfterNum(self, nums1, nums2):
        result = []

        # This ends up being an o(m*n) search where m is len(nums1) and n is len(nums2)
        for i in range(len(nums1)):
            target = nums1[i]
            next = False
            for j in range(len(nums2)):
                if nums2[j] == target:
                    next = True

                if next is True and nums2[j] > target:
                    result.append(nums2[j])

            if i == len(result):
                result.append(-1)

        return result

    # there is an even more optimal solution taking advantage of a stack where you push elements on one at a time and check if cur val is > then top
    def optimizeNextGreater(self, nums1, nums2):
        stack = deque()
        map = {}

        for target in nums2:
            if len(stack) != 0:
                while len(stack) != target > stack[-1]:
                    map[stack.pop()] = target
            else:
                stack.append(target)

        while stack:
            map[stack.pop()] = -1

        return [map[i] for i in nums1]


# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? Y
# Was the solution optimal? No the best answer actually used a stack and is super sick
# Were there any bugs? Yea I accidently used a peek instead of a pop for the last while loop for generating the mapping
#  3 5 3 2 = 3.25 - 2 = 1.25 (the minus two is for reading the problem wrong and wasting 10 minutes or so)
