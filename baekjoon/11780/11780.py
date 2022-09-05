import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
cost = [[inf] * (n+1) for _ in range(n+1)]
dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)
    dp[a][b] = [a, b]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                dp[i][j] = dp[i][k] + dp[k][j][1:]

for i in range(n+1):
    for j in range(n+1):
        if cost[i][j] == inf:
            cost[i][j] = 0

for data in cost[1:]:
    print(*data[1:])

for routes in dp[1:]:
    for route in routes[1:]:
        print(len(route), *route)