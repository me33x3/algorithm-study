from collections import deque

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append([x, y])

def bfs():
    queue.append([0, 0])  # A, B 물통의 남은 용량
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        z = C - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, B - y)
        pour(x - water, y + water)

        # x -> z
        water = min(x, C - z)
        pour(x - water, y)

        # y -> x
        water = min(y, A - x)
        pour(x + water, y - water)

        # y -> z
        water = min(y, C - z)
        pour(x, y - water)

        # z -> x
        water = min(z, A - x)
        pour(x + water, y)

        # z -> y
        water = min(z, B - y)
        pour(x, y + water)

A, B, C = map(int, input().split())

visited = [[False] * (B + 1) for _ in range(A + 1)]
queue = deque()
answer = []
bfs()

print(" ".join([str(i) for i in sorted(answer)]))