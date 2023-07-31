n, k = map(int, input().split())

def factorial(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * factorial(i-1)

print(factorial(n) // (factorial(n-k) * factorial(k)))