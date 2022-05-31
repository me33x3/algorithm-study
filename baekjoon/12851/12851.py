from collections import deque
INF = 10 ** 5

n, k = map(int, input().split())

sec, cnt = INF, 0
visited, dp = [-1] * (INF + 1), [0] * (INF + 1)
visited[n] = 0
dp[n] = 1
queue = deque([n])

while queue:
    curr = queue.popleft()

    for move in (curr + 1, curr - 1, curr *  2):
        if 0 <= move <= INF:
            if visited[move] == -1:
                visited[move] = visited[curr] + 1
                dp[move] = dp[curr]
                queue.append(move)
            elif visited[move] == visited[curr] + 1:
                dp[move] += dp[curr]

print(visited[k])
print(dp[k])