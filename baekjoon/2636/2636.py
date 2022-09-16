from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def count():
    return sum(sum(row) for row in board)


def bfs():
    queue = deque([[0, 0]])
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1

    cnt = count()
    t = 1

    while True:
        next = deque()

        while queue:
            x, y = queue.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if board[nx][ny]:
                        board[nx][ny] = 0
                        next.append([nx, ny])
                    else:
                        queue.append([nx, ny])
                    visited[nx][ny] = 1

        ncnt = count()
        if not ncnt:
            print(t)
            print(cnt)
            break

        cnt = ncnt
        queue = next
        t += 1


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
bfs()