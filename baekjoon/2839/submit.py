N = int(input())
answer = N

for i in range(N // 5 + 1):
    j = (N - 5 * i) // 3
    if N == 5 * i + 3 * j and answer > i + j:
        answer = i + j

print(answer if answer != N else -1)