def dfs(depth, val):
    if depth == n:
        res.append(val)
        return

    for i in range(4):
        if op[i] == 0:
            continue

        op[i] -= 1

        if i == 0:
            dfs(depth + 1, val + A[depth])
        elif i == 1:
            dfs(depth + 1, val - A[depth])
        elif i == 2:
            dfs(depth + 1, val * A[depth])
        else:
            dfs(depth + 1, val * (-1 if val < 0 else 1) // A[depth] * (-1 if val < 0 else 1))

        op[i] += 1

n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

res = []
dfs(1, A[0])

print(max(res))
print(min(res))