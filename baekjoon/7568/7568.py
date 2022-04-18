    n = int(input())

    group = []
    for _ in range(n):
        group.append(list(map(int, input().split())))

    for p1 in group:
        rnk = 1
        for p2 in group:
            if p1[0] < p2[0] and p1[1] < p2[1]:
                rnk += 1
        print(rnk, end=' ')