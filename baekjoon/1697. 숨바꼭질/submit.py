from collections import deque

N, K = map(int, input().split())

MAX = 10 ** 5
dist = [0] * (MAX + 1)

queue = deque([N])
while True:
    n = queue.popleft()

    if n == K:
        print(dist[n])
        break

    for nx in (n - 1, n + 1, n * 2):
        if 0 <= nx <= MAX and not dist[nx]:
            dist[nx] = dist[n] + 1
            queue.append(nx)