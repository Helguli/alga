#!/usr/bin/env python

class DynamicQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            raise Exception("Queue is empty")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


'''
# Példa használat
dynamic_queue = DynamicQueue()
dynamic_queue.enqueue(1)
dynamic_queue.enqueue(2)
dynamic_queue.enqueue(3)
dynamic_queue.enqueue(4)
dynamic_queue.enqueue(5)
print(dynamic_queue)  # [1, 2, 3, 4, 5]
print(dynamic_queue.dequeue())  # 1
dynamic_queue.enqueue(6)
dynamic_queue.enqueue(7)
print(dynamic_queue.peek())  # 2
print(dynamic_queue.dequeue())  # 2
print(dynamic_queue.dequeue())  # 3
print(dynamic_queue)  # [4, 5, 6]
'''
