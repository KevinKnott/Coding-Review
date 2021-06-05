# Two Sum: https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


#  Initial thought was to use a set but that will only work if I return the numbers not the index
class init():
    def twoSum(self, nums, k):
        seen = {}

        for i, num in enumerate(nums):
            target = k - num

            if target in seen:
                return [i, seen[target]] if i < seen[target] else [seen[target], i]

            seen[num] = i


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y O(N) Time and Space
# Were there any bugs? N
#  5 5 5 5 = 5

A = [2, 7, 11, 15]
k = 9
sol = init()
print(sol.twoSum(A, k))
