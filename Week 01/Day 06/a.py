# Binary Tree Right Side View: https://leetcode.com/problems/binary-tree-right-side-view/
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#  Initial solution is pretty simple you just do a depth level traversal with a bst and append the last element you see on that level
from collections import deque


#  20 min
# This solution is o(n) time and o(D) space where d is the diameter of the largest level
class Solution:
    def rightSideView(self, root):
        result = []

        if root is None:
            return []

        q = deque([[root, 0]])
        last = [root, 0]
        # When the level goes up 1 append last to result
        while q:
            node, level = q.pop()
            if last[1] != level:
                result.append(node.val)

            last = [node, level]

            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))

        # The last time you go through the tree you can't see the next level
        # So we have to check if end on a new level where we need to append the last val
        if len(result) == level:
            result.append(last[0].val)

        return result

# After reviewing the solution there is actually another solution that I wanted to implement it is similar
# however it uses two queues to figure out the last element basically whenever the first q is empty
# you have reached the end of the level. Then you move the second q to the first

# So after testing this solution it looks like this solution is slower than my initial mainly because it has slightly more computations
#  that being said the overall complexity is the same and this is a simpler solution


class Solution2:
    def rightSideView(self, root):
        result = []
        if root is None:
            return []

        nextLevel = deque()
        nextLevel.appendleft(root)

        while nextLevel:
            curLevel = nextLevel
            nextLevel = deque()

            while curLevel:
                node = curLevel.pop()

                if(node.left):
                    nextLevel.appendleft(node.left)
                if(node.right):
                    nextLevel.appendleft(node.right)

            result.append(node.val)

        return result

# Score Card
# Did I need hints?
# Did you finish within 30 min?
# Was the solution optimal?
# Were there any bugs?
#  4 5 5 3 = 4.25
