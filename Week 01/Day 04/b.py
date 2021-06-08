# Intersection of Two Arrays: https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

#  First thought is that this is a set problem so I will add everything to a set from one list and if I can find it I will add to result when parsing second list
class init():
    def intersection(self, nums1, nums2):
        return [x for x in set(nums1) and set(nums2)]

    def brute(self, nums1, nums2):
        temp = set()
        result = set()

        for num in nums1:
            temp.add(num)

        for num in nums2:
            if num in temp and num not in result:
                result.add(num)

        return list(result)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y (although not realistic for interview)
# Were there any bugs? N
#  5 5 5 5 = 5


A = [1, 2, 2, 1]
B = [2, 2]

sol = init()
print(sol.intersection(A, B))
