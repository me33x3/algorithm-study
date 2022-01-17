def star(n):
    t = n // 3
    print('***' * t)
    print('* *' * t)
    print('***' * t)

    if n == 1:
        return

    star(t)

    print('***' * t)
    print('* *' * t)
    print('***' * t)

n = int(input())
board = [[0] * n for _ in range(n)]
star(int(input()))