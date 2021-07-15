# Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Okay so this problem is simply going to the halfway point and reversing the nodes from the halfway
# at that point we simply do a one to one check and if we ever find a mismatch return false else
# we return true


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True

        first, second = head, self.findMid(head)

        second = self.reverseLL(second)

        # Now we have a list that is split in half and we can compare the first half and second half
        while second is not None:
            if first is None and second is not None:
                return False
            if second is None and first is not None:
                return False

            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        self.reverseLL(self.findMid(head))
        return True

    def findMid(self, head):
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseLL(self, head):
        # How Slow is at the halfway point we need to reverse
        prev = None

        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

# This problem is simple enough if you can break it into its thre different steps. It runs in o(N) time and o(1) space
# as we simply only have two pointers at any given time

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
