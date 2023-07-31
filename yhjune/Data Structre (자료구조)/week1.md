# Week 1 스택, 큐, 덱
## [문제집 바로가기](https://github.com/tony9402/baekjoon/tree/main/data_structure)

## Stack
1. **LIFO** 를 알아차리자
2. push, pop, top, peek
3. 원소들이 **늘** 같은 end 에서 더해지거나 제거됨

```python
# 스택 선언
stack = []

# push
stack.append(1)

# pop
stack.pop()

# stack empty check
not stack # False (비어있지 않으면)

# stack 의 top 확인
stack[-1] 

# stack 사이즈 확인
len(stack)
```


## Queue
1. FIFO
2. enqueue, dequeue
3. python `collections.deque` 사용

```python
# 큐 선언
import collections
queue = collections.deque()

# 특정 값과 함께 선언
queue = collections.deque([1, 2, 3])

# enque
queue.append(4)

# Dequeue
queue.popleft() 

# 큐에서 가장 앞에 있는 원소 체크 (제거될 다음 원소)
queue[0] 

# 큐 사이즈 체크
len(queue)
```

## Dequeue
1. double-ended queue의 줄임말
2. 양 끝에서 enqueue, dequeue 모두 가능