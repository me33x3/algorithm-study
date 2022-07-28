n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = n

for i in range(n):
    tmp = A[i] - B if A[i] - B > 0 else 0
    q, r = divmod(tmp, C)
    answer += q + (1 if r else 0)

print(answer)