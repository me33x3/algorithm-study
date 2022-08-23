from collections import deque

S = int(input())
queue = deque([[1, 0]])
dp = [[-1] * (S+1) for _ in range(S+1)]
dp[1][0] = 0
answer = int(1e9)

while queue:
    s, c = queue.popleft()

    if s == S:
        answer = min(answer, dp[s][c])

    if dp[s][s] == -1:
        dp[s][s] = dp[s][c] + 1
        queue.append([s, s])
    if s+c <= S and dp[s+c][c] == -1:
        dp[s+c][c] = dp[s][c] + 1
        queue.append([s+c, c])
    if s > 0 and dp[s-1][c] == -1:
        dp[s-1][c] = dp[s][c] + 1
        queue.append([s-1, c])

print(answer)