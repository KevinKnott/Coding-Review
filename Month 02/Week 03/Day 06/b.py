# First Missing Positive: https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array nums, find the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# So this problem builds on another problem where you learn that you can store seen numbers as negatives
# however to do this the appropriate way we need to make sure we remove any invalid numbers aka any negative
# numbers and 0 then all we have to do is convert the number that is seen to make its appropriate index
# negative

class Solution:
    def firstMissingPositive(self, nums) -> int:
        # First thing we need to do is replace all negatives and 0 with one
        # but we also need to check if we have one so that we can ignore
        # all of these false positive ones
        hasOne = False
        for i in range(len(nums)):
            if nums[i] == 1:
                hasOne = True
            if nums[i] <= 0:
                nums[i] = 1

        if hasOne == False:
            return 1

        # Now we can loop through the list again and convert the i - 1 value to be negative
        for i in range(len(nums)):
            indexToChange = abs(nums[i]) - 1

            if indexToChange < len(nums) and nums[indexToChange] > 0:
                nums[indexToChange] *= -1

        # Now that we have all of our values as - if seen and posititve if not
        # we simply return the first missing positive minus index 0 as we already checked for one
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1


# The above works the only extra thing I didn't think about immediately was whether or not you have checked every number in the
# but it runs in o(N) and uses o(1) space because technically we are using our existing list for the dictionary.
# A little bit faster solution is using a real dictionary and looping until you don't find that number

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 18
# Was the solution optimal? yes see above
# Were there any bugs? I forgot to check for whether we find every number in the list from 1->n where n == len(nums)
# 5 5 5 5 = 5
