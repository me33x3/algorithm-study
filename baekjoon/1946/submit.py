import sys
input = sys.stdin.readline

for _ in range(int(input())):
    rnk = []
    for _ in range(int(input())):
        rnk.append(list(map(int, input().split())))
    rnk.sort(key=lambda x: x[0])

    cnt, std = 1, rnk[0][1]
    for i in range(1, len(rnk)):
        if std > rnk[i][1]:
            std = rnk[i][1]
            cnt += 1

    print(cnt)
