import sys

n, m = map(int, input().split())
nums = sorted([int(input()) for i in range(n)])

answer = sys.maxsize
left, right = 0, 1

while left < n and right < n:
    res = nums[right] - nums[left]

    if res == m:
        answer = res
        break
    elif res < m:
        right += 1
    else:
        left += 1
        answer = min(answer, res)

print(answer)