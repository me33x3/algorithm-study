from heapq import heappush, heappop

def dijkstra():
    heap = []
    heappush(heap, [0, 0, sx, sy])
    visited[sx][sy] = 1

    while heap:
        a, b, x, y = heappop(heap)

        for d in range(4):
            mx, my = x + dx[d], y + dy[d]

            if 0 <= mx < N and 0 <= my < M and not visited[mx][my]:
                visited[mx][my] = 1

                if board[mx][my] == '.':
                    heappush(heap, [a, b, mx, my])
                elif board[mx][my] == 'g':
                    heappush(heap, [a + 1, b, mx, my])
                elif board[mx][my] == '!':
                    heappush(heap, [a, b + 1, mx, my])
                else:
                    return [a, b]

N, M = map(int, input().split())

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
sx, sy = 0, 0
fx, fy = 0, 0
board, G = [], []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    board.append(list(input()))

    for j in range(M):
        if board[i][j] == '.':
            continue
        elif board[i][j] == 'g':
            G.append([i, j])
        elif board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'F':
            fx, fy = i, j

for x, y in G:
    for d in range(4):
        mx, my = x + dx[d], y + dy[d]

        if 0 <= mx < N and 0 <= my < M and board[mx][my] == '.':
            board[mx][my] = '!'

print(*dijkstra())