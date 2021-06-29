# All Nodes Distance K in Binary Tree: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# We are given a binary tree (with root node root), a target node, and an integer value k.
# Return a list of the values of all nodes that have a distance k from the target node.  The answer can be returned in any order.

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Honestly the simplist solution for me is to take the tree and level order sort it into an array
# then all we have to do is find the target is go up by k in both directions and append it to result


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        q = deque()
        q.appendleft(root)
        levels = []

        while q:
            count = len(q)
            temp = []

            while q:
                node = q.pop()
                if node == target:
                    self.targetLevel = 0

                temp.append(node)

                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                count -= 1
            levels.append(temp)

        return


# Unfortunately my initial thought for the level order won't work as I won't know which way to head down the
# tree to get the right result to get around this we can create a graph using a parent node and the tree
# and then do a bfs


    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        def labelParent(node, parent=None):
            if node:
                node.parent = parent
                labelParent(node.left, node)
                labelParent(node.right, node)

        labelParent(root)

        # Do a BFS (To know the distance from k and keep track of visited)
        q = deque()
        q.appendleft((target, 0))
        visited = set()
        result = []

        while q:
            node, distance = q.pop()
            if node.val not in visited:
                visited.add(node.val)

                if distance == k:
                    result.append(node.val)
                    continue

                for neighbor in (node.left, node.right, node.parent):
                    if neighbor is not None and neighbor not in visited:
                        q.appendleft((neighbor, distance + 1))

        return result

# The above works! and it runs in O(n) and o(n) which is pretty good. I think that it could be improved more
# however it is kind of late and I can't think of something better.


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 28
# Was the solution optimal? This is optimal (i think)
# Were there any bugs? No
# 4 5 3 5 = 4.25
