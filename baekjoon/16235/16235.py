from collections import deque

dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
board = [[5] * n for _ in range(n)]

trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(k):
    for r in range(n):
        for c in range(n):
            len_t = len(trees[r][c])

            for k in range(len_t):
                if board[r][c] < trees[r][c][k]:
                    for _ in range(k, len_t):
                        board[r][c] += trees[r][c].pop() // 2
                    break
                else:
                    board[r][c] -= trees[r][c][k]
                    trees[r][c][k] += 1

    for r in range(n):
        for c in range(n):
            for k in trees[r][c]:
                if k % 5 == 0:
                    for d in range(8):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n:
                            trees[nr][nc].appendleft(1)

            board[r][c] += a[r][c]

answer = 0
for r in range(n):
    for c in range(n):
        answer += len(trees[r][c])

print(answer)