k = int(input())
signs = list(input().split())
res = []
visited = [False] * 10

def chk(x, y, sign):
    if sign == '<':
        return x < y
    else:
        return x > y

def dfs(s):
    idx = len(s)
    if idx == k + 1:
        res.append(s)
        return

    for i in range(10):
        if not visited[i]:
            if idx == 0 or chk(int(s[-1]), i, signs[idx - 1]):
                visited[i] = True
                dfs(s + str(i))
                visited[i] = False

dfs('')
print(res[-1])
print(res[0])