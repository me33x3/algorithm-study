from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    queue = deque([[0, 0, False]])
    move[0][0] = 1

    while queue:
        n, m, b = queue.popleft()

        if n == N - 1 and m == M - 1:
            return move[-1][-1]

        for x, y in zip(dx, dy):
            mx, my = m + x, n + y

            if 0 <= mx < M and 0 <= my < N:
                if (not board[my][mx] and b) or (board[my][mx] and not b):
                    if move[my][mx] >= move[n][m] + 1:
                        move[my][mx] = move[n][m] + 1
                        queue.append([my, mx, True if board[my][mx] else b])
    return -1

N, M = map(int, input().split())
board, move = [], []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))
    move.append([float('inf') for _ in range(M)])
print(bfs())