import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs():
    queue = deque([[0, 0, 0, 0, 1]])
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, b, t, move = queue.popleft()

        if x == n - 1 and y == m - 1:
            return move

        nt = t ^ 1

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny]:
                    if k > b and not visited[nx][ny][b + 1]:
                        if t:
                            queue.append([x, y, b, nt, move + 1])
                        else:
                            visited[nx][ny][b + 1] = 1
                            queue.append([nx, ny, b + 1, nt, move + 1])
                else:
                    if not visited[nx][ny][b]:
                        visited[nx][ny][b] = 1
                        queue.append([nx, ny, b, nt, move + 1])

    return -1


n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())