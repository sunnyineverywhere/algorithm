#https://www.acmicpc.net/problem/18258

import sys
import collections

queue = collections.deque()

n = int(sys.stdin.readline().strip())

for _ in range(0,n):
    line = list(sys.stdin.readline().split())
    word = line[0].strip()

    if word == 'push':
        queue.append(line[1])
    elif word == 'pop':
        if not queue:
            print(-1)
        else: print(queue.popleft())
    elif word == 'size':
        print(len(queue))
    elif word == 'empty':
        if not queue:
            print(1)
        else : print(0)
    elif word == 'front':
        if not queue : print(-1)
        else : print(queue[0])
    elif word == 'back':
        if not queue : print(-1)
        else:
            print(queue[-1])


# 더 간단하게
queue = collections.deque()

n = int(sys.stdin.readline().strip())

for _ in range(0,n):
    line = list(sys.stdin.readline().split())
    word = line[0].strip()

    if word == 'push':
        queue.append(line[1])
    elif word == 'pop':
        print(-1 if not queue else queue.popleft())
    elif word == 'size':
        print(len(queue))
    elif word == 'empty':
        print(1 if not queue else 0)
    elif word == 'front':
        print(-1 if not queue else queue[0])
    elif word == 'back':
        print(-1 if not queue else queue[-1])