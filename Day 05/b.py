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
