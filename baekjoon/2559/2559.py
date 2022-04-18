n, k = map(int, input().split())
temps = list(map(int, input().split()))

sums = [sum(temps[:k])]
for i in range(1, n - k + 1):
    sums.append(sums[i - 1])
    sums[i] -= temps[i - 1]
    sums[i] += temps[i + k - 1]

i, j = 0, n - k
while i < j:
    if sums[i] > sums[j]:
        j -= 1
    else:
        i += 1

print(sums[j])