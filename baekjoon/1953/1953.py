def dfs(u, t):
    for v in hate[u]:
        if not visited[v]:
            visited[v] = 1
            team[t ^ 1].append(v)
            dfs(v, t ^ 1)

n = int(input())

hate = {i: list(map(int, input().split()))[1:] for i in range(1, n + 1)}

team =[[], []]
visited = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = 1
        team[0].append(i)
        dfs(i, 0)

for t in team:
    print(len(t))
    print(*sorted(t))