'''
heapq: 최소 힙
자바의 PriorityQueue와 비슷하다

heapq 호출시마다 리스트를 인자로 넘겨야 함
리스트를 heaq처럼 사용할 수 있게 해주는 것
'''
import heapq

n = int(input())
meetings = []
for i in range(n):
    s, e = map(int, input().split())
    meetings.append([s, e])

meetings.sort()

rooms = []
heapq.heappush(rooms, meetings[0][1])
# 제일 일찍 끝나는 시간이 위에 올라간다
# 최소 힙이니까... 2 4 이러고 3 이렇게 써야 하면 2 3 4 이렇게 될 것이고...

for i in range(1, n):
    if meetings[i][0] < rooms[0]:
        heapq.heappush(rooms, meetings[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, meetings[i][1])

print(len(rooms))
