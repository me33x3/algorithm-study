def tsp(curr, v):
    if v == VISITED_ALL:
        return graph[curr][START] or INF

    if not dp[curr][v]:
        dp[curr][v] = INF
        for next in range(n):
            if graph[curr][next] and not (v & (1 << next)):
                dp[curr][v] = min(dp[curr][v], tsp(next, v | (1 << next)) + graph[curr][next])

    return dp[curr][v]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (1 << n) for _ in range(n)]
START, VISITED_ALL, INF = 0, (1 << n) - 1, float('inf')

print(tsp(START, 1))