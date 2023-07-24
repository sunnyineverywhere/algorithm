# LIFO

import sys
from itertools import combinations

n = list(map(str, sys.stdin.readline().strip())) # 입력
answer = set() # 출력을 중복 없이 하기 위한 set()
stack = [] # 쌍이 되는 괄호 지점의 체크를 위해 스택을 사용함
bracket_idx = []

# 반복문을 통해 괄호 쌍을 저장
for idx, bracket in enumerate(n):
    if bracket == "(":
        stack.append(idx)
    elif bracket == ")":
        bracket_idx.append([stack.pop(), idx])

for i in range(1, len(bracket_idx) + 1):
    # combinations을 통해 모든 조합을 확인
    combi = combinations(bracket_idx, i)
    for j in combi:
        # 괄호 제거
        result = list(n)
        for k in j:
            result[k[0]] = ""
            result[k[1]] = ""
        answer.add(''.join(result))

print(*sorted(list(answer)))