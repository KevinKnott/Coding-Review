# Copy List with Random Pointer: https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# So to create a deep copy we can simply loop through the nodes once and create a copy of every node
# then we can loop through a second time and move through the random pointer and update with the location
# of the new node

# This solution will run in o(n) time and space

# Although that being said I think we may be able to reduce that space cost by simply creating the duplicates
# in the chain and then intelligently linking the nodes and then breaking the two lists apart but this is
# a bit more complicated

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        newNodes = {}

        cur = head
        while cur is not None:
            temp = Node(cur.val)
            newNodes[cur] = temp
            cur = cur.next

        # Now that all the nodes exist we simply link the two pointers to match the new nodes
        cur = head
        while cur is not None:
            if cur.next:
                newNodes[cur].next = newNodes[cur.next]
            if cur.random:
                newNodes[cur].random = newNodes[cur.random]
            cur = cur.next

        return newNodes[head]

# This solution works and like I said it runs in O(N) time and space and honestly is pretty simple
# now for the more improved version using O(N) time but o(1) space

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        # So we have three steps
        # Create the new nodes as the next pointer of the node
        cur = head
        while cur is not None:
            temp = Node(cur.val, cur.next, cur.random)
            cur.next = temp
            cur = cur.next.next

        # Using the fact that the next node is the new node we take the prev.random and assign its next
        # to our cur.random and then point cur to cur.next.next
        cur = head
        while cur is not None:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # Finally we need to separate the pointers and return the original list to its form
        cur = head
        newHead = cur.next
        curPrime = cur.next
        while cur is not None:
            # Update next
            cur.next = curPrime.next if curPrime.next else None
            curPrime.next = cur.next.next if cur.next else None

            cur = cur.next
            curPrime = curPrime.next

        return newHead

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Yeah
# Were there any bugs? I tried combining the two steps of adding the random as we know the random pointer at time of creating new node
# but I had a slight bug where I couldn't actually reassing the .random to .random.next as I ran out of time
# 5 5 5 4 = 4.75
