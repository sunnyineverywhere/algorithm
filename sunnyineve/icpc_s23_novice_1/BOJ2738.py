n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

c = []

for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(a[i][j] + b[i][j])
    c.append(tmp)

for i in range(n):
    for j in range(m):
        print(c[i][j], end=" ")
    print()