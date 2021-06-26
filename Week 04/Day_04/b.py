# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# So this problem seems like we need to put in a for loop counting up to k and then reverse from start to k
# I think that we can probably pass the sort to another function to keep this code ab it clean


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head

        # Check to see if k is smaller than the length of the list
        while count < k and cur:
            cur = cur.next
            count += 1

        if count == k:

            # Reverse from head to k
            reversedList = self.reverse(head, k)

            # Recursively call down the stack
            head.next = self.reverseKGroup(cur, k)
            return reversedList

        # Otherwise we just return the list as is
        return head

        return

    def reverse(self, head, k):
        prev = None
        cur = head

        while k:
            # Keep track of the node after k
            ourNext = cur.next

            cur.next = prev
            prev = cur

            cur = ourNext

            k -= 1

        return prev

# So the above works, what happens is that we call recursively down the list swapping k elements at a time and if there is more
# we call the function itself if we loop through the list and we don't reach k we are at the end and we start returning the list
# The bonus is that we assign the reversed k and keep them on the stack as we come up which really simplifies the problem

# This runs in o(n) and o(n/k) as we visit each node and store the value of n/k on the stack until we reach n

# Can we do better? I think so I know that we can recursively call through the list so I think that if we approach this problem
# as we go across from 0 -> n checking for index % k we can find the point where we need to end the reverse from! Then all we
# need is to call our reverse function like we did above and we should be good.

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        # We need to check for the node that we point to from as it can't always be none
        lastTail = None

        # The new head
        result = None

        while cur:
            count = 0

            cur = head

            # Loop over the values like before
            while count < k and cur:
                cur = cur.next
                count += 1

            # If we need to reverse keep track of the reversed list
            if count == k:
                reversedList = self.reverse(head, k)

                # If we reveresed the first k update the new head
                if not result:
                    result = reversedList

                # if we have a node that is pointing to our start
                # we need to point it to the new head
                if lastTail:
                    lastTail.next = reversedList

                # we need to update head to the cur pointer (to mirror the recursion)
                lastTail = head
                head = cur

        # Even if we have gone through if we haven't pointed the last node to the new head
        # we need to do that agin
        if lastTail:
            lastTail.next = head

        # return either new head or the old head depending if k is in the length of the linked list
        return result if result else head


# So the iterative step is the same thing like I explained there is a little bit of extra to handle if you have a node
# before you start reveresing. The difference is that this will run in o(n) and o(1) space as we are changing the result
# as we go along

# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? n 45
# Was the solution optimal? The initial solution I though of definitely wasn't but when I got to thinking I solved in optimal
# improving on the intial
# Were there any bugs?  Nope
#  3 3 3 4 = 3.25
