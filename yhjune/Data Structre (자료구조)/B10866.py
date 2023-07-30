# https://www.acmicpc.net/problem/10866

import sys
import collections

n = int(sys.stdin.readline())
queue = collections.deque()

for _ in range(0,n):
    word = list(map(str,sys.stdin.readline().split()))
    case = word[0]

    if case == 'push_front':
        queue.appendleft(word[1])
    elif case == 'push_back':
        queue.append(word[1])
    elif case == 'pop_front':
        print(-1 if not queue else queue.popleft())
    elif case == 'pop_back':
        print(-1 if not queue else queue.pop())
    elif case == 'size':
        print(len(queue))
    elif case == 'empty':
        print(1 if not queue else 0)
    elif case == 'front':
        print(-1 if not queue else queue[0])
    elif case == 'back':
        print(-1 if not queue else queue[-1] )
    else: print("babo")


#list로 구현
from sys import stdin

input = stdin.readline


def solution() -> None:
    deque: list = []

    for _ in range(int(input())):
        commands = input().rstrip().split()
        op = commands[0]
        arg = commands[-1]

        if op == 'push_front':
            deque.insert(0, arg)
        elif op == 'push_back':
            deque.append(arg)
        elif op == 'pop_front':
            print(deque.pop(0) if deque else -1)
        elif op == 'pop_back':
            print(deque.pop() if deque else -1)
        elif op == 'size':
            print(len(deque))
        elif op == 'empty':
            print(0 if deque else 1)
        elif op == 'front':
            print(deque[0] if deque else -1)
        elif op == 'back':
            print(deque[-1] if deque else -1)


solution()



# 람다 식 짧은 표현
import sys
input = sys.stdin.readline


def sol():
    deck = []
    d = {
        "pop_front": lambda: deck.pop(-1) if deck else -1,
        "pop_back": lambda: deck.pop(0) if deck else -1,
        "size": lambda: len(deck),
        "empty": lambda: +(not deck),
        "front": lambda: deck[-1] if deck else -1,
        "back": lambda: deck[0] if deck else -1,
    }
    N = int(input())

    for _ in range(N):
        command = input().rstrip()
        if "push" in command:
            command, x = command.split()
            if command == "push_front":
                deck.append(x)
            else:
                deck.insert(0, x)
        else:
            print(d[command]())


sol()
