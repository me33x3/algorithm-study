left, right = 0, int(input()) - 1
nums = sorted(map(int, input().split()))
x = int(input())

cnt = 0
while left != right:
    n = nums[left] + nums[right]

    if x < n:
        right -= 1
    else:
        left += 1
        if x == n:
            cnt += 1
print(cnt)
