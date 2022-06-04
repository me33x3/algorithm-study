n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = {i: set() for i in range(1, k + 1)}
make_num = [False] * (nums[-1] * k + 1)
make_num[0] = True
for num in nums:
    dp[1].add(num)
    make_num[num] = True

for i in range(1, k):
    for j in dp[i]:
        for num in nums:
            dp[i + 1].add(j + num)
            make_num[j + num] = True

for i, make in enumerate(make_num):
    if not make:
        print(('jjaksoon' if i % 2 else 'holsoon') + ' win at ' + str(i))
        break