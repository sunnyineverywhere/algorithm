'''
조건 만족
- 원의 중심 좌표가 x축 위에 존재해야 함 -> (x, 0) 형태
- 임의의 두 원 선택 시 교점 존재 X (외부 | 내부에 존재)
     -> 원 거리 계산 |ra - rb| <= d <= |ra + rb|
'''

from itertools import combinations

# 입력
n = int(input())
circles = [] # (i, x-r, x+r)
for i in range(n):
    x, r = map(int, input().split(" "))
    circles.append([x-r, i])
    circles.append([x+r, i])

# 좌표 왼쪽 순으로 정렬
circles.sort()

s = []
for i in range(len(circles)):
    cur, num = circles[i][0], circles[i][1]
    if s:
        if s[-1][1] == num:
            s.pop()
        else:
            s.append(circles[i])
    else:
        s.append(circles[i])

if s:
    print("NO")
else:
    print("YES")