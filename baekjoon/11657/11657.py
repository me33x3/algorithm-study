INF = int(1e9)

def bf():
    dist[1  ] = 0
    for i in range(n):
        for a, b, c in edges:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c

                if i == n - 1:
                    return True
    return False

n, m = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

dist = [INF] * (n + 1)
if bf():
    print(-1)
else:
    for d in dist[2:]:
        print(d if d < INF else -1)