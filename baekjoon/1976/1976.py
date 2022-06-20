def find(num):
    if num != root[num]:
        root[num] = find(root[num])
    return root[num]

def union(x, y):
    if root[x] != root[y]:
        root_x, root_y = find(x), find(y)

        if root_x < root_y:
            root[root_y] = root_x
        else:
            root[root_x] = root_y

n = int(input())
m = int(input())
root = [i for i in range(n)]

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 1:
            union(i, j)

route = list(map(lambda x: int(x) - 1, input().split()))
base = root[route[0]]
answer = 'YES'

for num in route:
    if base != root[num]:
        answer = 'NO'
        break

print(answer)