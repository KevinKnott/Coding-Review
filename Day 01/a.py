import heapq


class initial():
    def solution(self, nums, k):
        nums.sort()

        return nums[len(nums) - k] if len(nums) - k > 0 else -1


# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Initial thoughts
# We could  simply sort / (remove duplicates harder than I thought requires lots of work) in nlog(n) time
# and select kth element

# Test Case 1
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# Output should be 5

# Test Case 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
# Output should be 4

sol = initial()

print(sol.solution(nums, k))


# I got tripped up trying to select kth largest distinct element
# This initial solution is correct and runs in O(nlog(n)) time and o(n) space because it is sorting timesort

# If I were to improve this function we could use the properties of a max heap as we can take advantage of always having the max element at the top
#  which should use o(log(n)) time to heapify but only log(n) to pop


class better():
    def solution(self, nums, k):
        heapq._heapify_max(nums)
        result = None

        for _ in range(k):
            result = heapq._heappop_max(nums)

        return result


# Test Case 1
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# Output should be 5


# Test Case 2
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
# Output should be 4

sol = better()

print("Improved", sol.solution(nums, k))

# Score Card
# Did I need hints
# Did you finish within 30 min
# Was the solution optimal
# Were there any bugs
