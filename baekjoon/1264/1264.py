vowels = ('a', 'e', 'i', 'o', 'u')

while True:
    s = list(input())

    if s[0] == '#':
        break

    cnt = 0
    for ch in s:
        if ch.lower() in vowels:
            cnt += 1

    print(cnt)