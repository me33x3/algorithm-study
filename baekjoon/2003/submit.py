n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
i, j = 0, 0
while j <= n:
    res = sum(nums[i:j])
    if res >= m:
        i += 1
        answer += 1 if res == m else 0
    else:
        j += 1
print(answer)