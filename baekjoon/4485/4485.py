from heapq import heappush, heappop

INF = int(1e9)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dijkstra():
    heap = []
    heappush(heap, [board[0][0], 0, 0])

    while heap:
        curr_cost, x, y = heappop(heap)

        if x == n - 1 and y == n - 1:
            break

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < n:
                new_cost = curr_cost + board[mx][my]

                if new_cost < cost[mx][my]:
                    cost[mx][my] = new_cost
                    heappush(heap, [new_cost, mx, my])

t = 1
while True:
    n = int(input())

    if n == 0:
        break

    board = [list(map(int, input().split())) for _ in range(n)]
    cost = [[INF] * n for _ in range(n)]
    dijkstra()
    print(f'Problem {t}: {cost[-1][-1]}')
    t += 1