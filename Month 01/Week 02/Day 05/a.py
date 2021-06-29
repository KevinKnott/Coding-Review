# Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


class Solution:
    def findDuplicate(self, nums):
        # If we could use extra space we could just use a set since the numbers are unique in range 1->n
        # Also because of this we could technically change the values in the array i-1 to negative if we have seen it
        # This is still wrong as we aren't allowed to modify
        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            if nums[num] < 0:
                return abs(num) + 1

            nums[num] *= -1

    # The brute force solution is for every number loop through the rest to see if you find a match
    def findDuplicateBrute(self, nums):
        # If we could use extra space we could just use a set since the numbers are unique in range 1->n
        # Also because of this we could technically change the values in the array i-1 to negative if we have seen it
        # This is still wrong as we aren't allowed to modify
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

    # how do we improve we do what we did in the first solution
    # If there is only one numbe repeated twice we know that one number is missing so if we use the nums array like a graph we could technically find a loop!
    # So if we sort the two numbers will be next to each other nlogn but we arne't really allowed to modify the array
    def findDuplicateCycle(self, nums):
        # Setup initial with slow and fast
        slow, fast = nums[0], nums[0]
        # Jump to next val slow = slow.next fast = fast.next (one jump and two jumps)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # The duplicated value will actually end up where we started so we can go till we know there is a cycle set slow to start and fast to be at the same spot
        slow = nums[0]

        # Loop until we are at the same point and boom you have an answer (this is based off of a math proof)
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Score Card
# Did I need hints? Yes for the loop detection I didn't think about it
# Did you finish within 30 min? Y
# Was the solution optimal? Yes for time but my original solutions all modified the array
# Were there any bugs? N
#  2 4 2 5 = 3.25
