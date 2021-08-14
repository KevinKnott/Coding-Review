# Add Two Numbers II: https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Also you could just reverse both, add them and reverse again

# So there are two approaches to this problem I can either convert both list into a integer and then add them together
# then parse it back into a string O(M+N) o(1) addditional space

#  Or I could do something a bit more complicated and parse them as is after counting to see which is larger. Then
#  calculating the carry and reverse them so the carry moves forward. At which point you return the result
#  this is also o(M+N) and o(1)


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1, num2 = 0, 0

        while l1:
            num1 = (num1 * 10) + int(l1.val)
            l1 = l1.next

        while l2:
            num2 = (num2 * 10) + int(l2.val)
            l2 = l2.next

        num1 += num2
        num1 = str(num1)

        head = ListNode()
        cur = head
        for i in range(len(num1)):
            cur.next = ListNode(num1[i])
            cur = cur.next

        return head.next

# The above works and is probably the easiest I explained all three solutions above
# I would normally do some of the other solutions for practice but I am low on time
# today


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal (see first blurbs of solutions)
# Were there any bugs? No bugs
# 5 5 5 5 = 5
