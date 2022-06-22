def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x, y = find(x), find(y)

    if A[x] <= A[y]:
        root[y] = x
    else:
        root[x] = y

n, m, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
root = [i for i in range(n + 1)]

for i in range(m):
    union(*map(int, input().split()))

cost = 0
visited = set()
for i in range(1, n + 1):
    tmp = find(i)
    if tmp not in visited:
        visited.add(tmp)
        cost += A[tmp]

print(cost if k >= cost else 'Oh no')