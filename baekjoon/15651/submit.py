def dfs(s):
    if len(s) == M:
        for num in s:
            print(num, end=' ')
        print()
    else:
        for i in range(1, N + 1):
            s.append(i)
            dfs(s)
            s.pop()

N, M = map(int, input().split())
for i in range(1, N + 1):
    dfs([i])