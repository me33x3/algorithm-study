def tsp(curr, v):
    if v == VISITED_ALL:
        return graph[curr][START]

    if dp[curr][v] is not None:
        return dp[curr][v]

    dp[curr][v] = int(1e9)
    for next in range(n):
        if next != curr:
            dp[curr][v] = min(dp[curr][v], tsp(next, v | (1 << next)) + graph[curr][next])

    return dp[curr][v]

n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)]

graph = [[0] * n for _ in range(n)]
dp = [[None] * (1 << n) for _ in range(n)]
VISITED_ALL, START = (1 << n) - 1, 0

for i in range(n):
    for j in range(n):
        if i != j:
            cost = ((loc[i][0] - loc[j][0]) ** 2 + (loc[i][1] - loc[j][1]) ** 2) ** 0.5
            graph[i][j] = graph[j][i] = cost

print(tsp(0, 1))