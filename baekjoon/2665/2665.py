import sys, heapq
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

heap = []
heapq.heappush(heap, [0, 0, 0])

while heap:
    cnt, x, y = heapq.heappop(heap)

    if x == n - 1 and y == n - 1:
        print(cnt)
        break

    for nx, ny in zip(dx, dy):
        mx, my = x + nx, y + ny

        if 0 <= mx < n and 0 <= my < n and not visited[mx][my]:
            visited[mx][my] ^= 1

            if board[mx][my]:
                heapq.heappush(heap, [cnt, mx, my])
            else:
                heapq.heappush(heap, [cnt + 1, mx, my])