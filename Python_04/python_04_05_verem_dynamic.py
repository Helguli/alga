#!/usr/bin/env python

class DynamicStack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

'''
# Példa használat
dynamic_stack = DynamicStack()
dynamic_stack.push(1)
dynamic_stack.push(2)
dynamic_stack.push(3)
dynamic_stack.push(4)
dynamic_stack.push(5)
print(dynamic_stack)  # [1, 2, 3, 4, 5]
print(dynamic_stack.pop())  # 5
print(dynamic_stack.peek())  # 4
dynamic_stack.push(6)
print(dynamic_stack)  # [1, 2, 3, 4, 6]
'''
