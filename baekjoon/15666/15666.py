def dfs(start):
    if len(seq) == m:
        print(*seq)
        return

    chk = set()
    for i in range(start, n):
        if nums[i] not in chk:
            chk.add(nums[i])
            seq.append(nums[i])
            dfs(i)
            seq.pop()

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
seq = []
dfs(0)