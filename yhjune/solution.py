
## 백준 솔루션 템플릿
# 입력 형식 https://daebaq27.tistory.com/57

import sys

n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

n,m = map(int, input().split())  # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
arr = []

for _ in range(m): # m번 loop을 돌면서 input을 arr에 append
    arr.append(list(map(int, input().split())))