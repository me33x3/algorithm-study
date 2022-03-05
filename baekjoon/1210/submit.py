n, m = map(int, input().split())
start, end = map(int, input().split())
cost = [0] + [int(input()) for _ in range(n)]
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(cost)
print(graph)