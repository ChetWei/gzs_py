# -*- coding: utf-8 -*-

from collections import deque

q = deque(range(5))

q.pop()
print(q)

q.append(5)
print(q)

q.popleft()
print(q)

q.rotate(2)
print(q)


