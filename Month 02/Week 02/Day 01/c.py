# Count of Smaller Numbers After Self: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# Okay my initial thought is you can simply do an n^2 count and add the result to a list which seems pretty simple but is not optimal
# My second thought is that we can move right to left through the array and probably compute this value by storing the result in our
# list it is initialized to 0 and then you check if the cur num is < the prev if so you keep the previous answer other wise
# you would increase the value by the prev value

class Solution:
    def countSmaller(self, nums):
        result = []

        for i in range(len(nums)):
            count = 0
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            result.append(count)

        return result

# Like I said the above works and is quite simple it runs in o(n^2) and o(n) space
# Can we do better? Apparently so using a segment tree which I have never used or we can
# a merge sort where we simply keep dividing the array in half and sort the nodes as normal
# once we are done we can loop through one more time over the interval and get the count
# of how many are less than our mid point (we need to check indicies for being initially to the right)

    def countSmallerMerge(self, nums):
        arr = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * len(nums)

        def merge_sort(left=0, right=len(arr)):
            # merge sort [left, right) from small to large, in place
            if right - left <= 1:
                return
            mid = right + (left - right) // 2

            # Sort left side
            merge_sort(left, mid)
            # Sort right side
            merge_sort(mid, right)

            # Combine both pieces together
            merge(left, right, mid)

        def merge(left, right, mid):
            # merge [left, mid) and [mid, right)
            i = left  # current index for the left array
            j = mid  # current index for the right array
            # use temp to temporarily store sorted array
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # when one of the subarrays is empty
            while i < mid:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort()

        return result

# This code works (although I took the easy apporach and create the new list adding another o(N) instead of realtime swapping)
# The tricky part about this problem is the intuition behind trying to solve this problem. We know that since we are starting
# with an array of length 1 at position 0 that we can keep track of weather or not as we move across if a node moves from the
# right of a number and to the left (aka smaller but after) honestly after looking at the solutions we could write simpler code
# since we aren't trying to just do merge sort

    # This is a way simpler code that behaves just like merge sort but is way easier
    def countSmallerMergeSimple(self, nums):
        arr = list(enumerate(nums))  # record value and index
        result = [0] * len(nums)

        def merge_sort(arr):
            mid = len(arr) // 2
            if mid:
                left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
                # Loop through the range backwards
                for i in reversed(range(len(arr))):
                    # if we move the value from the right to the left we increase our result
                    if not right or left and left[-1][1] > right[-1][1]:
                        result[left[-1][0]] += len(right)
                        arr[i] = left.pop()
                    else:
                        # Here we just have a larger number to the right so w/e
                        arr[i] = right.pop()
            return arr

        merge_sort(arr)

        return result

# Score Card
# Did I need hints? Oh yea
# Did you finish within 30 min? 50 min
# Was the solution optimal? See my blurb above
# Were there any bugs? Merge sort is difficult and I messed up the counts for some of the math
# 1 1 5 3 = 2.5
