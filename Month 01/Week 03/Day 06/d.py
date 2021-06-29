# Remove All Adjacent Duplicates in String II: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

# So if we take a string right and we use a stack we can count how many of the same letters we have in a row and if we end up with k in a row we can pop k - 1 off stack
# and then continue through the problem however this won't work if we don't know the k value  so we can use that on the stack as well
# Aka this problem is like having the min stack where you return the min value up to a point

class Solution:
    def removeDuplicates(self, s, k):
        if len(s) <= 1:
            return s

        stack = []

        for char in s:
            if len(stack) > 0:
                tempChar, count = stack[-1]

                if char == tempChar:
                    if count == k - 1:
                        for _ in range(k-1):
                            stack.pop()
                    else:
                        stack.append((char, count+1))
                else:
                    stack.append((char, 1))
            else:
                stack.append((char, 1))

        # unpack the stack that we created!
        result = ''
        for x in stack:
            result += x[0]
        return result

# This works but is it optimized? This will in worst case run through o(n) time and space can we do better
# I think it is possible to improve this by keeping track of indicies instead of counts but I am unsure.

# after looking at the solution it appears there is a slightly better algo that can reduce the space complexity
# by using two pointers and a stack you use the two pointers to compare the values and the stack to keep counts
# at the end you simply return the same string except you cut it at length of the slow pointer
    def removeDuplicatesOptimized(self, s, k):
        if k > len(s):
            return s
        stack = []
        j = 0
        result = list(s)

        for i in range(len(s)):
            # Make the value at fast pointer equal the slow pointer (we are modifying as we go)
            result[j] = result[i]
            # If we have a new char append the count to stack
            if j == 0 or result[j] != result[j - 1]:
                stack.append(1)
            else:
                # Check if the char is equal to k or increment by one
                count = stack.pop() + 1
                if count == k:
                    j = j - k
                else:
                    stack.append(count)

            j += 1

        temp = ''
        for i in range(j):
            temp += result[i]
        return temp


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? There was a interesting solution that had better space complexity but is more complicated
# Were there any bugs? Nope this was pretty straight forward
# 3 4 4 5 = 4
