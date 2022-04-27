n, m, s = int(input()), int(input()), input()
i, cnt, res = 0, 0, 0

while i < m:
    if s[i:i + 3] == 'IOI':
        i += 2
        cnt += 1
        if n == cnt:
            res += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(res)