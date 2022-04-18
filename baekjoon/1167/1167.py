v = int(input())
tree = [[] for _ in range(v + 1)]

for _ in range(v):
    info = list(map(int, input().split()))
    node = info[0]

    for i in range(1, len(info), 2):
        if info[i] == -1:
            break
        tree[node].append([info[i], info[i + 1]])

result = [0 for _ in range(v + 1)]

def dfs(node):
    for vertex, edge in tree[node]:
        if result[vertex] == 0:
            result[vertex] += result[node] + edge
            dfs(vertex)

dfs(1)
result[1] = 0
idx, tmp = 0, 0
for i in range(2, v + 1):
    if tmp < result[i]:
        tmp = result[i]
        idx = i
    result[i] = 0

dfs(idx)
result[idx] = 0
print(max(result))