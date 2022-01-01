N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min = float('inf')
answer = 0
for i in range(N - 1):
    if min > price[i]:
        min = price[i]
    answer += min * dist[i]

print(answer)