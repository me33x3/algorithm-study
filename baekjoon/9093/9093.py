for _ in range(int(input())):
    str = input()
    for word in str.split():
        print(word[::-1], end=' ')
    print()