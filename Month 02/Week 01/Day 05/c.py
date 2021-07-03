# First Missing Positive: https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array nums, find the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.


# The brute force of this is to look through all of nums for each  1 -> k until you find the missing k
# this is quite bad as you will need to duplicate lots of work

# Alternatively you could sort the array and do the same thing as you know that you can quickly
# find the first missing by mobing i and left pointer across this is o(nlogn)

# The problem suggests that we could do this in o(n) with constant space and I believe the way to
# do this is to simply swap the value to negative if we have seen it and the first index that
# isn't negative is the one that is missing

class Solution:
    def firstMissingPositive(self, nums) -> int:

        # Check if we even have the start otherwise this doesn't matter
        hasOne = False

        # We also need to remove invalid values from our list aka negatives and 0s as they
        # Give us false positives
        for i in range(len(nums)):
            if nums[i] == 1:
                hasOne = True

            if nums[i] <= 0:
                # Since we already checked for one we can
                # Simply make all invalid numbers equal to one
                nums[i] = 1

        if not hasOne:
            return 1

        # Also check if we have just one
        if hasOne and len(nums) == 1:
            return 2

        for index in range(len(nums)):
            # get our current number and make sure it is the positive version
            curNumber = abs(nums[index])

            # If the location in the area is positive turn it to negative to mark that we have seen it
            if curNumber - 1 < len(nums) and nums[curNumber - 1] > 0:
                nums[curNumber - 1] = -nums[curNumber - 1]

        # Now that everything is marked we can run a for loop and find the first missing based off of the
        # first positive we see

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1

# My initial intuiton on this problem was correct there are a few weird things we want to take care of that I hadn't considered
# If we have 0 or a negative value we need to remove them but how do we do so?

# The answer is we check if we have one and then make all those values = to 1 so that we know what to add these values with

# Now is there other optimizations on this problem? For sure by using a set we can have an o(1) look up so just loop
# n times and add all numbers to a set and then simply loop from 1 -> k and see if it is in set which will run in o(k) time and o(n) space


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 30
# Was the solution optimal? See above
# Were there any bugs? i forgot to add a return that says len(nums) + 1 at the end in case we have every number from 1 -> len(nums)
#  5 3 5 3 = 4
