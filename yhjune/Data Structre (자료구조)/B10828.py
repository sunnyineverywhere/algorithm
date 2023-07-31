# https://www.acmicpc.net/problem/10828

import sys
answer = []

n = int(sys.stdin.readline())

for i in range(0,n):
    word = str(sys.stdin.readline().strip())
    if word == "pop":
        if not answer:
            print(-1) # 비어있음
        else:
            print(answer.pop())
    elif word == "size":
        print(len(answer))
    elif word == "empty":
        if not answer:
            print(1) # 비어있음
        else:
            print(0)
    elif word == "top":
        if not answer:
            print(-1) # 비어있음
        else :
            print(answer[-1])
    elif word.startswith('push'):
        _, item = word.split()
        answer.append(int(item))
    else:
        pass



# 간편한 풀이
import sys
input=sys.stdin.readline

s = []
n = int(input().rstrip())

for _ in range(n):
    op = list(map(str, input().split()))
    if op[0] == 'push':
        s.append(int(op[1]))
    elif op[0] == 'pop':
        print(s[-1] if len(s) else -1)
        s = s[:-1]
    elif op[0] == 'size':
        print(len(s))
    elif op[0] == 'empty':
        print(0 if len(s) else 1)
    elif op[0] == 'top':
        print(s[-1] if len(s) else -1)
