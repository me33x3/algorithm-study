def check(x, y, n):
    base = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if base != video[i][j]:
                return False
    return True

def dfs(x, y, n):
    global res
    if check(x, y, n):
        res += video[x][y]
    else:
        res += '('
        for i in range(x, x + n, n // 2):
            for j in range(y, y + n, n // 2):
                dfs(i, j, n // 2)
        res += ')'

n = int(input())
video = [[i for i in input()] for _ in range(n)]
res = ''
dfs(0, 0, n)
print(res)