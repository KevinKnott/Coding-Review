# Count of Smaller Numbers After Self: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# So this problem is quite challenging as the only way I can think of solving it is in the naive way where we simply go through the array and check all the numbers after it that are smaller
# I feel like we could do some intelligent caching with this

class Solution:
    def countSmaller(self, nums):
        result = []

        for i in range(len(nums)):
            result.append(0)
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    result[-1] += 1

        return result


# The above works but is a very slow N^2 algorithm that uses o(n) space as well
# after looking at the solution it seems you can use a segment tree or a
# binary indexed tree to solve this but I haven't used them before so I will
# be testing it out here

    # With this solution we will actually do what I suggested which is intelligent caching with a segment tree
    # we will parse for right to left and store how many of each value there is and then for every value
    # that exists to the left of the solution will end up being the result[i]


    def countSmaller(self, nums):

        def update(index, value, tree, size):
            index += size
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[(index * 2) + 1]

        def query(left, right, tree, size):
            result = 0
            left += size
            right += size
            while left < right:
                if left % 2 == 1:
                    result += tree[left]
                    left += 1

                left //= 2

                if right % 2 == 1:
                    right -= 1
                    result += tree[right]

                right //= 2

            return result

        # Create an offset so our range can include negative numbers
        offset = 10**4
        # Create a tree that can hold all possible values
        size = 2 * offset + 1
        tree = [0] * (2 * size)
        result = [0] * len(nums)

        for i in reversed(range(len(nums))):
            smaller = query(0, nums[i] + offset, tree, size)
            result[i] = smaller
            update(nums[i] + offset, 1, tree, size)

        return result

# So the above works and I understand the theory behind it but I need to figure out how to update a segment tree it seems pretty intuitive
# you use a tree in a list and simply conver to the parents and add up by taking your index and // 2 at each step then recompute the new
# sum

# As for the query we start at the leaf and simply and move up the tree until the parents match and add each value we see to our total result

# N is len of nums and M is dif between min and max values
# This solution runs in O(NlogM) as we spend log(M) to query for smaller number and log(m) but we have to do this for each element so it
# runs in O(Nlogm) and we are using O(m) space to store the segment tree


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 30
# Was the solution optimal? See blurb above
# Were there any bugs? No bugs
# 4 4 3 5 = 4
