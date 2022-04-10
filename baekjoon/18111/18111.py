import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

high, low = max(map(max, board)), min(map(min, board))
t, height = INF, high

for i in range(high, low - 1, -1):
    fill, remove = 0, 0
    for j in range(n):
        for k in range(m):
            if i < board[j][k]:
                remove += board[j][k] - i
            elif i > board[j][k]:
                fill += i - board[j][k]

    if b + remove - fill >= 0:
        if t > 2 * remove + fill:
            t = 2 * remove + fill
            height = i

print(t, height)