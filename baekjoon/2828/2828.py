N, M = map(int, input().split())
J = int(input())

answer, curr = 0, 1
for _ in range(J):
    next = int(input())

    if curr < next:
        temp = (next - curr) - (M - 1)
    else:
        temp = curr - next

    if temp > 0:
        answer += temp
        curr += temp if curr < next else -temp

print(answer)