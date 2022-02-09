n, m = map(int, input().split())
cards = sorted(map(int, input().split()))

answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = cards[i]+cards[j]+cards[k]
            if sum > m:
                break
            answer = max(answer, sum)

print(answer)