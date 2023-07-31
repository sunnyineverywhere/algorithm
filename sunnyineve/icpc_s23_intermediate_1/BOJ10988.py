word = list(input())
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False

if is_palindrome:
    print(1)
else:
    print(0)