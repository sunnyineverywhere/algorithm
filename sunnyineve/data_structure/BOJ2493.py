'''
N개의 높이가 서로 다른 탑을 왼쪽부터 오른쪽 방향
레이저 송신기: 신호를 수평 직선 왼쪽 방향 발사
탑: 신호 수신

하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 탑 하나에서만 수신 가능
'''

n = int(input())
towers = list(map(int, (input().split(" "))))
s = [] # [인덱스, 타워 인덱스 값]
answer = []

for i in range(n):
    # 스택에 값이 존재할 때
    while s:
        # 마지막 스택 값이 현재 타워 높이보다 크면
        if s[-1][1] > towers[i]:
            answer.append(s[-1][0] + 1)
            break
        # 아닌 경우
        else:
            s.pop()
    # 스택에 값이 없는 경우
    if not s:
        answer.append(0)
    # 스택에 현재 타워 값 append
    s.append([i, towers[i]])

print(" ".join(map(str, answer)))