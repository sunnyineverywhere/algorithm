n, s = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0


def bt(idx, total):
    global n, s, numbers, cnt
    if idx == n:
        return
    if total + numbers[idx] == s:
        cnt += 1
    bt(idx + 1, total)
    bt(idx + 1, total + numbers[idx])


bt(0, 0)
print(cnt)
