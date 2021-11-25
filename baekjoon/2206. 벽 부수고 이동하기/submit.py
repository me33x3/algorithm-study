from collections import deque
import math, sys
input = sys.stdin.readline

N, M = map(int, input().split())

board, move = [], []
for _ in range(N):
    board.append(list(map(int,input().rstrip())))
    move.append([float('inf') for _ in range(M)])

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
queue = deque([[0, 0, False]])
move[0][0] = 1

while queue:
    n, m, b = queue.popleft()

    for x, y in zip(dx, dy):
        mx, my = m + x, n + y

        if 0 <= mx < M and 0 <= my < N:
            if not board[my][mx] or (board[my][mx] and not b):
                if move[my][mx] >= move[n][m] + 1:
                    move[my][mx] = move[n][m] + 1
                    queue.append([my, mx, True if board[my][mx] else b])

print(-1 if math.isinf(move[-1][-1]) else move[-1][-1])