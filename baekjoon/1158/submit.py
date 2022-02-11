N, K = map(int, input().split())
arr = list(range(1, N + 1))
i, answer = 0, []

for _ in range(N):
    i += K - 1
    if i >= len(arr):
        i %= len(arr)
    answer.append(arr.pop(i))

print('<', ', '.join(map(str, answer)), '>', sep='')