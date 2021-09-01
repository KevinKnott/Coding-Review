# Design Circular Queue: https://leetcode.com/problems/design-circular-queue/

# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implementation the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language.

# So for this problem we have to design a queue which is circular meaning that we can only use up to K spots

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        temp = Node(value)

        if self.size == 0:
            self.head = temp
            self.tail = self.head
        else:
            self.tail.next = temp
            self.tail = self.tail.next

        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# This works perfectly
# This solution is way more efficient than using say a list to accomplish the same thing. This will run in O(1) time
# and uses at max O(K) space


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
