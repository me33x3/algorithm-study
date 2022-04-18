N = int(input())
nums = sorted(map(int, input().split()), reverse=True)
composite = set({1})

for i in range(2, nums[0] + 1):
    if i not in composite:
        for j in range(i * i, nums[0] + 1, i):
            composite.add(j)

answer = 0
for n in nums:
    if n not in composite:
        answer += 1

print(answer)