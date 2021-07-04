# Intersection of Two Arrays II: https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many
# times as it shows in both arrays and you may return the result in any order.

# Since there are duplicates we can't really use a set to do this problem
# My initial thought here is that we could sort both of these lists and have two pointers to loop through each
# and create a new list with the results

# Alternatively we can create a dictionary and add all values from one and then loop through 2 and remove values as we go
# If the number is > 0 while we remove we add it to our result this will be an o (m+n) and o(m+n)

from collections import defaultdict


class Solution:
    def intersect(self, nums1, nums2):
        potentialValues = defaultdict(int)

        for num in nums1:
            potentialValues[num] += 1

        result = []
        for num in nums2:
            if num in potentialValues and potentialValues[num] > 0:
                potentialValues[num] -= 1
                result.append(num)

        return result

# This solution is O(m+n) for time and space and is probably optimal in terms of time
# however if we were to optimize this for space we could simply loop sort the numbers
# and then remove by swaping the element with the end and poping if the number isn't
# in the other but it would also have to swap values that are valid in the second
# list to the front so we can ignore them if they have already been used
# overall this is way more complicated than above

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 9 min
# Was the solution optimal? See blurb
# Were there any bugs? None
# 5 5 5 5 = 5
