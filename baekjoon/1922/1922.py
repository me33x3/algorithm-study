def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

n = int(input())
m = int(input())

root = [i for i in range(n + 1)]
net = [list(map(int, input().split())) for _ in range(m)]
net.sort(key=lambda x: x[-1])

answer = 0
for a, b, c in net:
    ra, rb = find(a), find(b)

    if ra != rb:
        if ra > rb:
            root[ra] = rb
        else:
            root[rb] = ra
        answer += c

print(answer)