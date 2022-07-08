def dfs(curr, damage, a, p):
    global answer

    if damage + a + A[curr] > K:
        return

    a += A[curr]
    p += P[curr]
    damage += a
    answer = max(answer, p)

    for next in range(1, N + 1):
        if not visited[next]:
            visited[next] = 1
            dfs(next, damage, a, p)
            visited[next] = 0

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
P = [0] + list(map(int, input().split()))

visited = [0] * (N + 1)
answer = 0

dfs(0, 0, 0, 0)

print(answer)