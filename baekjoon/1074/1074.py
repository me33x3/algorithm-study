def dfs(x, y, z):
    global cnt
    if z == 2:
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                if r == i and c == j:
                    print(cnt)
                    exit(0)
                cnt += 1
        return

    if not (x <= r < x + z and y <= c < c + z):
        cnt += z * z
        return

    for i in [x, x + z // 2]:
        for j in [y, y + z // 2]:
            dfs(i, j, z // 2)

n, r, c = map(int, input().split())
cnt = 0
dfs(0, 0, 2 ** n)