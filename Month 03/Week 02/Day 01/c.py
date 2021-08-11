# Intersection of Two Arrays II: https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# This problem is actually asking for an intersection of two sets you can complete this
# so if we can use memory all we have to do is iterate throught m+n and keep only the relevant
# possibilities. So you add to a hashmap if you find the solution in A and if you are searching
# through the second and it is in the hashmap you add it to the result.


class Solution:
    def intersect(self, nums1, nums2):
        result = []
        seen = {}

        for num in nums1:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1

        for num in nums2:
            if num in seen and seen[num] > 0:
                result.append(num)
                seen[num] -= 1

        return result

# This runs in O(m+n) and uses o(m) space

# Now for the optimization for this problem we can't use extra space
# so what we have to do is sort each list and move through the list

    def intersect(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result

# This runs in o(Nlogn) and uses o(1) space (depending on sorting algo used)


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 7
# Was the solution optimal? Yuh
# Were there any bugs? None
# 5 5 5 5 = 5
