def check(x, y, n):
    base = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != base:
                return False
    return True

def dfs(x, y, n):
    if check(x, y, n):
        cnt[paper[x][y]] += 1
        return
    for i in range(x, x + n, n // 3):
        for j in range(y, y + n, n // 3):
            dfs(i, j, n // 3)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0, 0]
dfs(0, 0, n)

print(cnt[-1])
print(cnt[0])
print(cnt[1])