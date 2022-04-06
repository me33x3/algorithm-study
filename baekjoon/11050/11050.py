N, K = map(int, input().split())

answer, fact = 1, 1
for i in range(2, N + 1):
    fact *= i
    if i == K:
        answer *= fact
    if i == N - K:
        answer *= fact

print(fact // answer)