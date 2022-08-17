from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    keys = deque(stdin.readline().strip())

    left = list()
    right = list()
    for _ in range(len(keys)):
        key = keys.popleft()
        if key == '<':
            if left: right.append(left.pop())
        elif key == '>':
            if right: left.append(right.pop())
        elif key == '-':
            if left: left.pop()
        else:
            left.append(key)
    print(''.join(left + right[::-1]))