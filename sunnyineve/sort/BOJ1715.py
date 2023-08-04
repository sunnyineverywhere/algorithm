import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
    a = int(input())
    heapq.heappush(card, a)

ans = 0
while len(card) > 1:
    pre = heapq.heappop(card)
    cur = heapq.heappop(card)
    ans += pre + cur
    heapq.heappush(card, pre + cur)

print(ans)
