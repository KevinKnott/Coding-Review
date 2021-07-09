# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# So this problem is actually pretty neat! My initial intuition is to build a simple reverese function except looping until count = k
# After we have reveresed we need to update the nodes around the reversed ie head needing to swap and then pointing the prev to
# what we reversed


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while count < k and cur:
            cur = cur.next
            count += 1

        if k == count:
            # So this simply reverses our list from head to k ie in the case 1 2 3 4 5 k = 2 our result would be 2 1 None
            reversedHead = self.reverse(head, k)

            # So now that we have 2 -> 1 -> none how to point to next? from our head!
            # As it is still pointing to one so we then recurse down and continue from where we were so head is now  1 and will point to -> 3-> 4 -> 5 k = 2
            head.next = self.reverseKGroup(cur, k)
            return reversedHead

        # If we didn't to k elements that means we leave alone the end and buble back up
        return head

    # Simple method to reverse a linked list right
    def reverse(self, head, k):
        last, cur = None, head
        while k > 0:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp
            k -= 1

        return last


# I think the above solution works and is pretty nifty but is it optimal? It runs in o(N) (we loop over N twice) and uses o(N/k) calls of the stack space
# I think you could implement the above with an iterative solution that would use o(1) time but unfortunately I am out of time

# For the o(1) solution you could simply encase the reverseKGroup from above into a while loop until you hit the end
# Once that is done you simply update the head node and keep a separate node for its next pointer and then at the end

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? See above I was not optimal
# Were there any bugs? I initially had a bug where I thought that I needed another value to point to the next solution but
# I was able to use recursion to get around that
# 4 4 4 4 = 4
