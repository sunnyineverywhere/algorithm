"""
1: (0, 0) -> (0, 1) -> (1, 0) -> (1, 1)

2: ... => (0, 2) ... => (2, 0) ... => (2, 2)

3: (0,0) => ... => (0, 4) ... => (4, 0)

입력 N
r, c를 몇번째로 방문했는가?

0   1   4   5
2   3   6   7
8   9   12  13
10  11  14  15

0 % 2 = 0
1 % 2 = 1


"""

n, r, c = map(int, input().split())

def solution(n, r, c):
    if n == 0:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * solution(n-1, int(r/2), int(c/2))

print(solution(n, r, c))