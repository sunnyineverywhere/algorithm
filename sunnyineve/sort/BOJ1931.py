n = int(input())
meetings = []
for i in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))
# print(meetings)

cnt = 1
tmp = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= tmp:
        cnt += 1
        tmp = meetings[i][1]

print(cnt)