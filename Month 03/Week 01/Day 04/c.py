# Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:

#     You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#     Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

    def peek(self) -> int:
        """
        Get the front element.
        """

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(1) space
# Were there any bugs? None
# 5 5 5 5 = 5
