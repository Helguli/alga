#!/usr/bin/env python

class StaticQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, item):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return str([self.queue[(self.front + i) % self.capacity] for i in range(self.size)])


'''
# Példa használat
static_queue = StaticQueue(5)
static_queue.enqueue(1)
static_queue.enqueue(2)
static_queue.enqueue(3)
static_queue.enqueue(4)
static_queue.enqueue(5)
print(static_queue)  # [1, 2, 3, 4, 5]
print(static_queue.dequeue())  # 1
static_queue.enqueue(6)
#static_queue.enqueue(7)
print(static_queue.peek())  # 2
print(static_queue.dequeue())  # 2
print(static_queue.dequeue())  # 3
print(static_queue)  # [4, 5, 6]
'''
