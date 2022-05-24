INF = int(1e9)

def bellmanford():
    time = [INF] * (n + 1)
    time[1] = 0

    for i in range(1, n + 1):
        for s, e, t in edges:
            if time[e] > time[s] + t:
                time[e] = time[s] + t
                if i == n:
                    return True
    return False

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []

    M = [[0] * (m + 1) for _ in range(m + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    W = [[0] * (w + 1) for _ in range(w + 1)]
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print('YES' if bellmanford() else 'NO')