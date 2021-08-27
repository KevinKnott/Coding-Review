# Copy List with Random Pointer: https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list. For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list. The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# This problem has two separate solutions and each have their own merit the easier of the two is simply going through the list 3 times
# and using a hashmap to create copies of every node then assign the next and random on the next

# The optimal solution that saves space would be to use the properties of a list to know that you could create the list in place
# by going through adding a node next to the original that is a copy then going through and assigning the next as the original.next.next
# as the copy is besided and the same for the random this is optimal as we won't use any additional space other than the creation of the
# nodes

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return

        ourMap = {}

        cur = head
        while cur:
            ourMap[cur] = Node(cur.val)
            cur = cur.next

        # Now we have a hash map of all copied nodes we can go through and use them
        # for next and random
        cur = head
        while cur:
            copy = ourMap[cur]
            copy.next = ourMap[cur.next] if cur.next is not None else None
            copy.random = ourMap[cur.random] if cur.random is not None else None
            cur = cur.next

        return ourMap[head]

# If all nodes were unique we could reduce a bit of space instead  of storing whole list however that isnt possibe
# so what we need to do is the above except setting the copied nodes next to the original and then decoupling

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return

        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = cur.next.next

        # Since the random keeps getting messed up when I do them together I separated it out
        # even though we should be able to do it together
        cur = head
        while cur is not None:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # Now we have a hash map of all copied nodes we can go through and use them
        # for next and random
        cur = head
        newHead = cur.next
        copy = cur.next
        while cur:
            # cur.next.random = cur.random.next if cur.random else None
            cur.next = cur.next.next
            copy.next = copy.next.next if copy.next is not None else None
            cur = cur.next
            copy = copy.next

        return newHead

# Oh yeah O(N) and O(1)

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 6 minutes for easy 25 with the optimal
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
