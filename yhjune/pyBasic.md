# Pyton Basic Grammer

## 목차
### [파이썬 공식 문서](https://docs.python.org/ko/3/)
1. [print](#print)
2. [Input/Output](#input/output)
3. [Transition](#transition)
4. [Calculate](#calculate)
5. [Condition](#condition)
6. [List](#list)

---
## Print
```python
print("hello") # hello
print("Hello world") # Hello World
print("hello","world") #hello World (, 사이 공백 출력)

# 줄 바꿔 출력
print("Hello")
print("World") 

#따옴표 출력
print("'Hello'") # 'Hello'
print('"Hello"') # "Hello"
print("\"C:\Download\\\'hello\'.py\"") # "C:\Download\'hello'.py"

# 줄바꿈 출력
print("print(\"Hello\\nWorld\")") # print("Hello\nWorld")
```

## Input/Output
```python
# 문자 1개 입력 받아 출력
c = input()
print(c)

# 정수 -> int 변환하여 출력 (입력값은 기본적으로 문자열로 인식)
n = input()
int_n = int(n)
print(int_n)

# 실수 출력
f = input()
f = float(f)
print(f)

# 공백을 기준으로 입력된 값 나누기 : input().split()
a,b = input().split()
print(a)
print(b)

# split("[문자]"), sep(seperator)
a,b = input().split(':') # ":" 로도 가능, : 기준으로 자름 
print(a,b,sep = ':') # ":"로도 가능 a, b 사이에 : 로 구분. 공백없이는 ""

# 단어 1개 나누어 출력
s = input() #Hello
print(s[0]) # H

#단어 잘라 출력
s = input() #200304
print(s[0:2]) #0번째 문자부터 2-1번째 문자까지 잘라냄

#단어 이어 붙여서 출력 (공백으로 구분되어 입력)
w1, w2 = input().split() # hello world
s = w1 + w2 #helloworld
print(s)
```

## Transition
```python
#10진수 -> 16진수 (대소문자 구분) %x %X
a =input()
n = int(a)
print('%x'%n) #소문자
print('%X'%n) #대문자

#16진수 -> 8진수
a =input()
n = int(a,16) #입력된 a를 16진수로
print('%o'%n) #소문자
print('%O'%n) #대문자

# 영문자 1개 -> 10진수 유니코드
n = ord(input()) #A
print(n) #65

# 10진수 정수 -> 유니코드 문자로
c = int(input())
print(chr(c))

# 실수 1개 -> 소수점 이하 2번째 자리까지 반올림한 값 : format([숫자],".[원하는자리까지]f")
a = float(input())
print(format(a,".2f"))

```

## Calculate

### 산술 연산
```python
# 단항 연산자 : 정수 부호 바꾸기
a = int(input())
print(-a)

# 문자 1개를 입력 받아 문자를 출력하기
c = ord(input())+1
print(chr(c))

#차이 계산
a,b = input().split()
c = int(a)-int(b)
print(c)

#곱 계산
a,b = input().split()
c = float(a)*float(b)
print(c)

# 거듭제곱 계산
c = a ** b

# 나누기 : /
a, b = input().split() # 10.0 3.0
c = float(a)/float(b) # 3.33333...
print(format(c, ".3f")) # 3.333

# 나눈 몫 : //
c = a//b # a를 b로 나눈 몫을 계산해줌

# 나눈 나머지 %
c = a % b

#여러 번 출력 : 문자열 * 정수 = 문자열을 정수 번 반복
w, n = input().split()
print(w*int(n))
```

### 비트시프트 연산
```python
컴퓨터 내부에 2진수 형태로 값이 저장되기 때문에 사용가능하다.
실수 값에 대한 비트 시프트 연산은 허용되지 않고 오류가 발생
n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.
```

### 비교 연산
```python
비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 
참 True 거짓 False (Boolean 값)

a,b = input().split()
a = int(a)
b = int(b)

print(a<b) # a<b True | a>b False

# 참 거짓 판별 bool() : 0의 경우 False 나머지 True
n = int(input()) #0
print(bool(n)) #False
```

### 논리 연산
```python
# not
print(not a) 

# and : t&t True | 나머지 Fasle
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#or : f&f False | 나머지 True
print(bool(int(a)) or bool(int(b)))

#xor : 두 불 값이 서로 다를 때에만 True
c = bool(int(c))
d = bool(int(d))
print((c and (not d)) or ((not c) and d))
```

### 비트단위 논리연산
```python
입력된 정수를 비트 단위로 참/거짓을 바꾼다.
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
# ~ : tilde, 틸드 , ^ : caret, 서컴플렉스/카릿

a,b = input().split()
a = int(a) # 3
b = int(b) # 5
print(a&b) # 1
```


### 3항 연산
```python
c = (a if(a>=b) else b) # 조건문이 참이면 a를 아니먄 b

a,b,c =input().split()
a = int(a)
b = int(b)
c = int(c)

temp = a if(a<=b) else b
ans = c if(c<=temp) else temp

print(int(ans))

```

## Condition
### 조건/선택 실행 구조
```python
if(a%2==0): 조건식
    실행1 
else:
    실행2

if(a%2==0): 조건식1
    실행1
elif 조건식2:
    실행2
else:
    실행3
```
### 반복 실행 구조
```python
while 조건식:
    실행

for i in range(1, n): # 0부터 n-1까지
    실행
    continue # 실행하지 않고 다음 반복 단계로 넘어감
```

## List
list comprehension
`[ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]`

```python
range(start, end, 증감) # 시작 수 포함, 끝 수 포함 안함
d = [[0 for j in range(20)] for i in range(20)] 

```
