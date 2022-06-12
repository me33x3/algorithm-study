def backtracking(n, sum):
    cnt = 0

    if n < N:
        sum += nums[n]

        if sum == S:
            cnt += 1

        cnt += backtracking(n + 1, sum - nums[n])
        cnt += backtracking(n + 1, sum)

    return cnt

N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(backtracking(0, 0))