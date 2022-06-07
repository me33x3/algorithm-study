def dfs(u):
    if not tree[u]:
        return 1

    cnt = 0
    for v in tree[u]:
        cnt += dfs(v)

    return cnt

n = int(input())

L = list(map(int, input().split()))
tree = {i: [] for i in range(n)}
root = -1
for u, v in enumerate(L):
    if v == -1:
        root = u
    else:
        tree[v].append(u)

target = int(input())

answer = 0
if L[target] != -1:
    tree[L[target]].remove(target)
    answer = dfs(root)
print(answer)