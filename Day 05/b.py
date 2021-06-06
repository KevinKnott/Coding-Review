# https://leetcode.com/contest/weekly-contest-244/problems/reduction-operations-to-make-the-array-elements-equal/
# First solution physically transforms the array one at a time n^2 the second solutions sorts and then creates a hash
# and removes elements down one at a time to incrase performance

from collections import defaultdict


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = 0
        isReduced = False

        while not isReduced:
            firstNum = nums[0]
            # print(nums)
            for num in nums:
                if num != firstNum:
                    self.reduction(nums)
                    count += 1
                    isReduced = False
                    break

                isReduced = True

        return count

    def reduction(self, nums):
        largest = 0

        for i in range(len(nums)):
            if nums[i] > nums[largest]:
                largest = i

        maxVal = -float('inf')
        secondLargest = None

        for i in range(len(nums)):
            if nums[i] > maxVal:
                if nums[i] != nums[largest]:
                    maxVal = nums[i]
                    secondLargest = i

        nums[largest] = nums[secondLargest]
        return nums


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = 0
        values = defaultdict(int)
        nums.sort()

        for num in nums:
            values[num] += 1

        while len(values) != 1:
            key = values.keys()[-1]
            count += values[-1]
            del(values[key])

        print(values)
        return count


class OptimalSolution:
    def reductionOperations(self, nums: List[int]) -> int:
        # In order to do this we will do what I did in the above but in reverse
        nums.sort()

        # Basically this is a dp problem so i set my dp array
        count = [0] * len(nums)

        # Go through the array and either if values are the same keep count the same
        # otherwise increase the count by 1 for all values to the right (you have to swap all values one more time)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count[i] = count[i-1]
            else:
                count[i] = count[i-1] + 1

        # Once you are done you sum all of these changes
        result = 0
        for num in count:
            result += num

        return result
