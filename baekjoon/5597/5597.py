nums = set(int(input()) for _ in range(28))
for i in range(1, 31):
    if i not in nums:
        print(i)