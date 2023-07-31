board = [list(map(int, input().split())) for _ in range(9)]

max_val = -1
x = -1
y = -1

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] > max_val:
            max_val = board[i][j]
            x, y = i+1, j+1

print(max_val)
print(str(x) + " " + str(y))