
## 백준 솔루션 템플릿
# 입력 형식 https://daebaq27.tistory.com/57

import sys

# 첫 줄에 7, 9 가 입력되고, 뒤의 숫자로 몇 번의 입력이 들어올지 정해지는 경우
n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

n,m = map(int, input().split())  # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
arr = []

for _ in range(m): # m번 loop을 돌면서 input을 arr에 append
    arr.append(list(map(int, input().split())))

# 반복가능한 객체
item = ["First", "Second", "Third"]
for i, val in enumerate(item):
    print("{} 번쨰 값은 {}입니다".format(i, val))
# 0 번쨰 값은 First입니다
# 1 번쨰 값은 Second입니다
# 2 번쨰 값은 Third입니다

answer.add(''.join(result))