def dfs():
    if len(seq) == m:
        print(*seq)
        return

    chk = set()
    for i in range(n):
        if not v[i] and nums[i] not in chk:
            v[i] = True
            chk.add(nums[i])
            seq.append(nums[i])
            dfs()
            seq.pop()
            v[i] = False

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
v = [False] * n
seq = []
dfs()