n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
while i < n and j < m:
    if a[i] < b[j]:
        print(a[i], end=' ')
        i += 1
    else:
        print(b[j], end=' ')
        j += 1

if i < n:
    print(' '.join(map(str, a[i:])))
if j < m:
    print(' '.join(map(str, b[j:])))