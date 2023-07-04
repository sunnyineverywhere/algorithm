'''
괄호를 제거해서 나올 수 있는 서로 다른 식의 개수
항상 쌍이 되는 괄호끼리 제거
'''

from itertools import combinations

str = input() # 리스트 형태로 input string
fomula = list(str)
s = [] # 괄호 표기할 스택
indices = [] # 괄호 쌍의 인덱스
answer = [] # 정답

# 괄호 쌍의 인덱스 번호 구함
# O(n)
for i in range(len(fomula)):
    if fomula[i] == '(':
        s.append(i)
    elif fomula[i] == ')':
        start = s[-1]
        s.pop()
        indices.append([start, i])

# 인덱스 쌍에 대한 `1 ~ index 개수` 만큼의 조합 생성
for i in range(1, len(indices) + 1):
    combi = (combinations(indices, i)) # 배열에 대해 i개만큼의 조합을 생성하는 라이브러리

    # 생성된 조합 만큼 반복문
    for c in combi:
        li = list(str)
        for k in c:
            start, end = k
            li[start] = ""
            li[end] = ""
        answer.append(''.join(li))

answer = set(answer) # set: 집합 자료형
for i in sorted(answer): # sorted: set 자료형의 값 백과사전 순 정렬
    print(i)