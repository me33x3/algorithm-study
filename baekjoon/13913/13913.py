from collections import deque


def bfs():
    q = deque([[n]])
    v = [0] * (k * 2 + 1)

    while q:
        route = q.popleft()
        a = route[-1]

        if a == k:
            return route

        for b in (a - 1, a + 1, a * 2):
            if 0 <= b <= k * 2 and not v[b]:
                v[b] = 1
                q.append(route + [b])


n, k = map(int, input().split())
res = bfs() if n < k else list(range(n, k-1, -1))
print(len(res) - 1)
print(*res)