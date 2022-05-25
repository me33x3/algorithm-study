MAX, MIN = int(1e9), -int(1e9)

def bf(start):
    money[start] = earn[start]

    for i in range(n * 2):
        for a, b, c in bus:
            if money[a] == MAX:
                money[b] = MAX
            elif money[a] != MIN and money[b] < money[a] - c + earn[b]:
                money[b] = money[a] - c + earn[b]
                if i == n - 1:
                    money[b] = MAX

n, s, e, m = map(int, input().split())
bus = [list(map(int, input().split())) for _ in range(m)]
earn = list(map(int, input().split()))

money = [MIN] * n
bf(s)
print('Gee' if money[e] == MAX else ('gg' if money[e] == MIN else money[e]))