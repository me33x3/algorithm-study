from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def check():
    return sum(sum(row) for row in board)


def bfs():
    queue = deque([[0, 0]])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    t = 0

    while check():
        nq = deque()

        while queue:
            x, y = queue.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0 and not dp[nx][ny]:
                        dp[nx][ny] = 1
                        queue.append([nx, ny])
                    elif board[nx][ny] == 1 and dp[nx][ny] < 2:
                        if dp[nx][ny]:
                            nq.append([nx, ny])
                            board[nx][ny] = 0
                        dp[nx][ny] += 1
        t += 1
        queue = nq

    return t


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(bfs())