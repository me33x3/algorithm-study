N, S = map(int, input().split())
seq = list(map(int, input().split()))

f, b = 0, 0
part = seq[0]
answer = float('inf')

while f < N:
    if part >= S:
        answer = min(answer, b - f + 1)
        part -= seq[f]
        f += 1
    else:
        b += 1
        if b == N:
            break
        part += seq[b]

print(0 if answer == float('inf') else answer)