def dfs():
    global answer

    if sum(visited) == n:
        res = 0
        for j in range(n - 1):
            res += abs(stack[j] - stack[j + 1])
        answer = max(answer, res)

    for i, val in enumerate(a):
        if not visited[i]:
            visited[i] = True
            stack.append(val)
            dfs()
            stack.pop()
            visited[i] = False

n = int(input())
a = list(map(int, input().split()))

stack = []
visited = [False] * n
answer = 0
dfs()

print(answer)