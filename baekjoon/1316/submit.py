n = int(input())

for _ in range(n):
    word = input()

    chk = []
    for c in word:
        if c in chk:
            if chk[-1] != c:
                n -= 1
                break
        else:
            chk.append(c)

print(n)