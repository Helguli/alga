#!/usr/bin/env python

class StaticStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def __len__(self):
        return self.top + 1

    def push(self, item):
        if self.top == self.capacity - 1:
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def __str__(self):
        return str(self.stack[:self.top + 1])


# Példa használat
static_stack = StaticStack(5)
static_stack.push(1)
static_stack.push(2)
static_stack.push(3)
static_stack.push(4)
static_stack.push(5)
print(static_stack)  # [1, 2, 3, 4, 5]
print(static_stack.pop())  # 5
print(static_stack.peek())  # 4
static_stack.push(6)
print(static_stack)  # [1, 2, 3, 4, 6]
