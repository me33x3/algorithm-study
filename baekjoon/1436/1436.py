n = int(input())
i, cnt = 666, 0

while True:
    if '666' in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break
    i += 1