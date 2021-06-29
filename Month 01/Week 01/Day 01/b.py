class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_a = []
        self.stack_b = []
        self.items = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_a.append(x)
        self.items += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return

        for _ in range(self.items):
            self.stack_b.append(self.stack_a.pop())

        print(self.stack_a, self.stack_b)
        result = self.stack_b.pop()
        self.items -= 1

        for _ in range(self.items):
            self.stack_a.append(self.stack_b.pop())

        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return

        for _ in range(self.items):
            self.stack_b.append(self.stack_a.pop())

        result = self.stack_b[-1]

        for _ in range(self.items):
            self.stack_a.append(self.stack_b.pop())

        return result

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.items == 0


# https://leetcode.com/problems/implement-queue-using-stacks/
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


# I solved initially but I forgot about poping from an empty array


# Score Card
# Did I need hints
# Did you finish within 30 min
# 19 minI spent rest of time trying to figure out amortization but didn't figure it out
# Was the solution optimal
# No I couldnt figure out how to amortize this to run in o(1) it turns out that my solution is consider an amortized o(1) however I need to update peek in order to always have the reference (can change later)
# Were there any bugs
# Forgot to check if people will pop an empty stack
# 5 5 4 5 = 4.75
