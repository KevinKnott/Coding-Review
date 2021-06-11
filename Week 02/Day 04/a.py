# Next Greater Element I:

# You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextHighest = {}
        currentVals = []

        for num in nums2:

            while len(currentVals) != 0 and num > currentVals[-1]:
                nextHighest[currentVals.pop()] = num

            currentVals.append(num)

        while len(currentVals) != 0:
            nextHighest[currentVals.pop()] = -1

        result = []

        for num in nums1:
            if num in nextHighest:
                result.append(nextHighest[num])
            else:
                result.append(-1)
        return result

# This is an o(n+m) time and o(n) space solution which is optimal for time
# You could technically do a more space efficient solution that is o(mn) where for each num in num1 you search for it
# in nums2 and then find the number that is after that is greater although I guess since we are creating the result list
# it would technically still be o(n) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? Forgot to return results
#  5 5 5 4 = 4.75
