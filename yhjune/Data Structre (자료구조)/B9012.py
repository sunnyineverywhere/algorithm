#https://www.acmicpc.net/problem/9012
#LIFO

import sys

input = sys.stdin.readline
n = int(input().strip())

for i in range(0,n):
    line = list(map(str, input().strip()))
    bracket = []
    for idx, word in enumerate(line):
        if word == '(':
            bracket.append(idx)
        elif word == ')':
            if not bracket:
                bracket.append("not")
                break
            else:
                bracket.pop()
    if not bracket:
        print("YES")
    else :
        print("NO")