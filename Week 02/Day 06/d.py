# Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a palindrome.

# My initial thought is to go in to the half point using a fast and slow pointer
# Once you are there reverse the second half
# loop through both and check if one is out of order

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        if head.next is None:
            return True

        first = head
        second = self.reverse(self.findMid(head))

        result = True
        # Loop through the second as we know the half will alwasy be <= the len of the whole
        # go through until we have looped the whole second half
        while result and second is not None:
            # If the numbers ever mismatch return false
            if first.val != second.val:
                result = False

            first = first.next
            second = second.next

        # Restore the second halfs
        self.reverse(self.findMid(head))
        return result

    #   Simple way to find midpoint using fast and slow pointer
    def findMid(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

    # simple reverse function
    def reverse(self, head):
        prev = None
        while head is not None:
            save = head.next
            head.next = prev
            prev = head
            head = save

        # One bug I had was not returning the previous which was pointing to None
        return prev


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N
# Was the solution optimal? It is optimal enough however I think I could make some slight improvements
# Were there any bugs? I am having issues with double negative values
# 5 5 5 3 = 4.5
