n = int(input())
times = list(map(int, input().split()))
times.sort()

wait, res = 0, 0
for t in times:
    res += t + wait
    wait += t

print(res)