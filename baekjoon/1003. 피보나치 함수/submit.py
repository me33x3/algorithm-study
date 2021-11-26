for _ in range(int(input())):
    fibo = [[1, 0], [0, 1]]
    n = int(input())
    for i in range(2, n + 1):
        fibo.append([fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1]])
    print(fibo[n][0], fibo[n][1])