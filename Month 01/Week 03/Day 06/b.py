# Add Two Numbers II: https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# First thought is actually to use a stack (recursion) because it handles getting the carry over to the previous value as well as getting to the last digit first
# Otherwise we could take an iterative approach using a stack or reversing all nodes and then solving the problem and reversing again
# Also another faster solution is actually to conver the ll into values add them and create a new ll which is actually the simplest code

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstValue = 0
        secondValue = 0

        while l1 is not None:
            firstValue = (firstValue * 10) + l1.val
            l1 = l1.next

        while l2 is not None:
            secondValue = (secondValue * 10) + l2.val
            l2 = l2.next

        result = str(firstValue + secondValue)

        dummy = ListNode(0)
        cur = dummy

        for value in result:
            cur.next = ListNode(int(value))
            cur = cur.next

        return dummy.next

# This solves the problem in o(n) where n is the length of the result l1 + l2 and same for the space
# Could we actually solve this in a better space complexity? I think so because if you consider the reverse operation to cost o(max(m,n))
# then you could actualy reverse both list due the normal math and then reverse the answer

    def addTwoNumbersSpaceEfficient(self, l1, l2):
        # Now that they are reversed we simply do the normal math!
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        result = ListNode(0)
        cur = result
        carry = 0

        while (l1 or l2) or carry:
            value = l1.val if l1 else 0
            value += l2.val if l2 else 0
            value += carry

            carry, value = divmod(value, 10)

            # I ran out of time for making this l1 or l2 or cary so I did it the easy way
            cur.next = ListNode(value)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverse(result.next)

    def reverse(l1):
        prev = None
        cur = l1

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    # If I had a bit more time I would change the above code to be more optimized for space because you could technically take l1 or l2 as your new node change the val and then continue
    # I just ran out of time for solving it that way. However is this the most optimal solution?
    # I don't think so because you are technically reversing the list twice which is a bit intensive according to the solution you can also find length which allows you to parse value
    # more efficiently and then you can do math and carry at the same time and do the above but I imagine it is just a slight improvement as it is still o(max(len(m), len(n)))

# Score Card
# Did I need hints? N
# Did you finish within 30 min? N
# Was the solution optimal? See above
# Were there any bugs? N
# 5 3 4 5 = 4.25
