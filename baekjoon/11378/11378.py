def dfs(x):
    for y in graph[x]:
        if visited[y]:
            continue
        visited[y] = True

        if w[y] == 0 or dfs(w[y]):
            w[y] = x
            return True
    return False

n, m, k = map(int, input().split())
graph = {}
for i in range(1, n + 1):
    graph[i] = list(map(int, input().split()))[1:]
w = {i: 0 for i in range(1, m + 1)}

cnt = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    cnt += 1 if dfs(i) else 0

for i in range(1, n + 1):
    while k > 0:
        if dfs(i):
            k -= 1
            cnt += 1
        else:
            break

print(cnt)