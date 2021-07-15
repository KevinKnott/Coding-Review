# Add Two Numbers II: https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Okay this problem seems difficult at first  as we actually need to reverse the numbers to get the right placement of digits
# We have two options then one reverse both linked list in O(N) and then calculate or calculate each number completey
# do the math and then create a new result which is also o(N). Honestly both these solutions run in o(N) space
# unless we overwrite one of the current lists

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0

        while l1:
            num1 = (num1 * 10) + l1.val
            l1 = l1.next

        while l2:
            num2 = (num2 * 10) + l2.val
            l2 = l2.next

        num1 += num2
        num1 = str(num1)
        result = ListNode()
        cur = result
        for i in range(len(num1)):
            temp = ListNode(int(num1[i]))
            cur.next = temp
            cur = cur.next

        return result.next

# The above is simple enough and works you could also potentially use a divmod to reduce the number by a factor of
# 10 and then reverse it.

    # This is the other solution by reversing both and then updating the nodes
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def reverse(self, l1):
        prev = None
        cur = l1

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

# A more optimal solution you could do is get both lengths and then add as you go
# then come back through and take any carry and move it in a second for loop
# Unfortunately I didn't have time to implement this

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 20
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(N) space
# Were there any bugs? None
# 5 5 4 5 = 4.75
