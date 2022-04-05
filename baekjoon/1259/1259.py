while True:
    s = input()

    if s == '0':
        break

    n = len(s)
    flag = True

    for i in range(n):
        if s[i] != s[n-i-1]:
            flag = False
            break

    print('yes' if flag else 'no')