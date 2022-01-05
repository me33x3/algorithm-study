while True:
    n = int(input())

    if not n:
        break

    composite = set({1})
    answer = 0

    for i in range(2, n * 2 + 1):
        if i in composite:
            continue

        for j in range(i * i, n * 2 + 1, i):
            composite.add(j)

    for k in range(n + 1, n * 2 + 1):
        if k not in composite:
            answer += 1

    print(answer)