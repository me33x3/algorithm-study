def dfs(s, v):
    if len(s) == M:
        for num in s:
            print(num, end=' ')
        print()

    for i in range(1, N + 1):
        if i not in v and i > s[-1]:
            s.append(i)
            v.append(i)
            dfs(s, v)
            v.pop()
            s.pop()

N, M = map(int, input().split())
for i in range(1, N + 1):
    dfs([i], [i])