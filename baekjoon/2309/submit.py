h = [int(input()) for _ in range(9)]
h.sort()
total = sum(h)
flag = False

for i in range(9):
    for j in range(i + 1, 9):
        if total - h[i] - h[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(h[k])
            flag = True
            break
    if flag:
        break