# Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Since we can't use extra space I think that we could solve this in o(n^2) where we compare every single value
# to every other value.

# That being said You could also take the fact that every other number is ues once and use negatives where
# 2 negatives = a positive

# That being said the problem also states that we cannot modify the existing array

class Solution:
    def findDuplicate(self, nums):
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return num

            nums[num - 1] *= -1

        return

# Now can we improve on this? I think that technically this ends up being  a graph problem as we
# dont want to visit the same node twice this means that we can use the floyd tortoise hare algo

    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]

        # Continue through path moving slow one time and fast two times
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # If the are equal we know that we have a cycle
            if slow == fast:
                break

        # At this point we know that we have a cycle
        # so we need to find where it starts (this is the duplicate)
        # to do this we know the distance from the cycle is equal to walking
        # through again (see my notes in person for this)

        fast = nums[0]

        while fast != slow:
            # We need to move both at the same time again see my notes for why
            slow = nums[slow]
            fast = nums[fast]

        return fast

# The above solution works it is an algo I have implemented a few times this will run in o(n) and o(1)
# This alogorithm is actually quite smart and I have spent some time on it. I think that it is hard to
# explain without the graphics. Basically because of the math of the distance we can compute that the
# distance from where we detect the cycle and restarting the fast pointer and moving one at a time
# is equal to the distance between o(n) and o(2n) meeting each other

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5
