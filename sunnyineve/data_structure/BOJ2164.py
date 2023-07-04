'''
N장의 카드
1번 카드가 제일 위에 / N번 카드가 제일 아래에
제일 위 카드 버림 => 제일 위 카드를 아래 카드 밑으로 옮김
'''

from collections import deque

n = int(input())
q = deque()
for i in range(n):
    q.append(i+1)

while len(q) != 1:
    q.popleft() # 제일 위의 카드를 버림
    if len(q) > 1: # 그 다음 카드를 아래로 보냄
        q.append(q[0])
        q.popleft()

print(q[0])