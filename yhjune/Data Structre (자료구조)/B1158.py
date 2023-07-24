#https://www.acmicpc.net/problem/1158
# 출력 형식 시러용


import sys
import collections

queue = collections.deque()
answer = []

n, k = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    queue.append(i)

# 앞에서부터 집어 넣기
# 3번째 제거
# 3번째 이후부터 다음 라인으로 넘기기
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print('<', end='')
print(*answer, sep=', ',end='')
print('>', end='')