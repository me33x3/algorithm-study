for _ in range(int(input())):
    A, B = map(int, input().split())
    mul = A * B

    if A < B:
        A, B = B, A

    while A % B:
        A, B = B, A % B

    print(mul // B)