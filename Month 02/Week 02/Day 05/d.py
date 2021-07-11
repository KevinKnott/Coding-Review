# Count of Smaller Numbers After Self: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# The quickest solution to this problem is to go through number by number and compare everything after in a n^2 solution
# The improvement on this problem is using dp or using merge sort to divide and conquer this problem

# This happens because for every value as we recombine we can see if a value on the right is taken over a value to the left
# So if we do this at every step and record the result as we go up we should have an answer

class Solution:
    def countSmaller(self, nums):
        # We will have exactly N results
        result = [0] * len(nums)

        # We need to convert nums to be a tuple of value and index so we can compare if it moves across
        nums = [[v, i] for i, v in enumerate(nums)]

        def divide(start=0, end=len(nums)):
            if end - start <= 1:
                return

            mid = start + (end - start) // 2

            divide(start, mid)
            divide(mid, end)
            conquer(start, mid, end)

        def conquer(start, mid, end):

            # Okay so now that we have each individual piece so now we have to update our result
            # This can be done by checking if something in the right piece is smaller than left
            left, right = start, mid
            temp = []

            while left < mid and right < end:
                # Check if the num on the left is less than the right
                if nums[left][0] <= nums[right][0]:
                    # Something moved to the right that is smaller so we update our result
                    result[nums[left][1]] += right - mid
                    temp.append(nums[left])
                    left += 1
                else:
                    # We just keep chugging as merge as result isn't updated
                    temp.append(nums[right])
                    right += 1

            # If there is anything left over because we can complete sort just one side first
            while left < mid:
                # Again we need to update result
                result[nums[left][1]] += right - mid
                temp.append(nums[left])
                left += 1
            while right < end:
                # If we end with just higher values on the right append
                temp.append(nums[right])
                right += 1

            # Now that we have our new sort we need to update the values in our nums array
            for i in range(start, end):
                nums[i] = temp[i - start]

        divide()
        return result

# This  solution works although it actually is quite cumbersome because honestly you can just use pointers and not use extra space to overwrite stuff
# It works in o(nlogn) and o(n) space though which is honestly pretty good according to the solution there may be some improvements but seeing as
# I haven't worked with the merge sort enough I am going to continue working on this solution until I speed it up

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 30
# Was the solution optimal? See blurb
# Were there any bugs? I accidently forgot to update the left variable to update to the new start which caused faulty list updating in the merge
# 3 5 3 3 = 3.5
