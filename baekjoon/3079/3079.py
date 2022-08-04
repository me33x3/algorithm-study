import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]

left, right = 1, M * max(T)

answer = 0
while left <= right:
    mid = (left + right) // 2
    total = 0

    for t in T:
        total += mid // t

    if total < M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)