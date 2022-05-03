for _ in range(int(input())):
    n = int(input())
    cloth_list = {}

    for _ in range(n):
        _, kind = input().split()
        if kind in cloth_list:
            cloth_list[kind] += 1
        else:
            cloth_list[kind] = 1

    res = 1
    for val in cloth_list.values():
        res *= (val + 1)
    print(res - 1)