#!/usr/bin/env python

# Pythonban a listát tudjuk használni sorként és veremként is.

# Sor (Queue) beépített listával
queue = []

# Adjunk hozzá elemeket a sorhoz! (enqueue)
print("Sor:", queue)  # [1, 2, 3]

# Távolítsunk el egy elemet a sor elejéről! (dequeue)
print("Kivett elem:", dequeued_item)  # 1
print("A sor kivétel után:", queue)  # [2, 3]

# Nézzük meg az első elemet! (peek)
print("Következő elem:")  # 2

# Verem (Stack) beépített listával
stack = []

# Adjunk hozzá elemeket a veremhez (push)
print("Verem:", stack)  # [1, 2, 3]

# Távolítsunk egy elemet a verem tetejéről (pop)
print("Kivett elem:", popped_item)  # 3
print("Verem kivétel után:", stack)  # [1, 2]

# Nézzük meg a verem legfelső elemét (peek)
print("Következő elem:")  # 2
