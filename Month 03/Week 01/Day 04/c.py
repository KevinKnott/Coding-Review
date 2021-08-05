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

# So the clever thing about using two stacks to define is that you can simply move the whole stack 1 to stack 2 to get the correct order
# then we have x number of pops until we need to rebalance but moving stack 1 onto stack 2 this only occurs when stack 2 is empty

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()

        # The below would normally need an error check but since the problem said
        # the calls are always valid this is okay
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) != 0:
            return self.stack2[-1]

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) + len(self.stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Boo to the yeah so this will run in O(1) for all but peek and pop which would be an amortized o(1)
# as for space we obviously need o(N) space to store all the values

# Score Card
# Did I need hints? No
# Did you finish within 30 min? 12
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
