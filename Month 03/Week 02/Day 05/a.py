# Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# So the naive solution here is to make a copy of the list and reverese it and then traverse down until you have finished
# and return the result this runs in O(N) but also uses o(N)

# The optimal solution for this problem is using a hare pointer to find the mid point and then reverse from the mid point
# until the end do the comparison and then reverse the reverse this will run in O(N) but uses O(1) extra space

class Solution:
    def reverseList(self, head):
        prev, cur = None, head

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def findMid(self, head):
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def isPalindrome(self, headListNode) -> bool:
        node1, node2 = headListNode, self.findMid(headListNode)
        node2 = self.reverseList(node2)

        while node2:
            if node1 is None and node2 is not None:
                return False
            if node2 is None and node1 is not None:
                return False
            if node1.val != node2.val:
                return False

            node1 = node1.next
            node2 = node2.next

        self.reverseList(self.findMid(headListNode))
        return True

# The above code works and is actually pretty clean you just take a couple of principles you have used before and rearrange them
# to make it cleaner I also abstracted a few methods (the only thing I haven't done is restore the list if it fails but w/e)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Optimal
# Were there any bugs? No bugs
# 5 5 5 5 = 5
