# Next Greater Element I: https://leetcode.com/problems/next-greater-element-i/

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


# The simple solution is to for each i in nums1 search for it in 2 and then find the first largest number after that this will run in o(N^2) and o(N) space as we have to append it to a result

# This is quite a tricky mouthful of a solution basically we need to create a dictionary of the next highest value of every number
# however to do this we will need to implement a stack. Luckily we can bulid this dict in o(N) time and using o(N) space so it ever so slightly optimized
# as we will not be evaluating the same two numbers twice

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        nextGreater = {}
        stack = []

        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                nextGreater[stack.pop()] = num

            stack.append(num)

        # while len(stack) > 0:
        #     nextGreater[stack.pop()] = -1

        result = []
        for num in nums1:
            result.append(nextGreater.get(num, -1))

        return result

# This is a super simple stack scanning solution because we can always see the number we are at and then you can check if the last n numbers were less than its value
# this solution will run in o(M+N) time and space as we will have to iterate through both nums array and store the result in a dict or in result


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Oh yea
# Were there any bugs?  None submitted with 0 issue first try
# 5 5 5 5 = 5
