answer, val = 0, 1
for i in list(input())[::-1]:
    if not i.isdigit():
        i = ord(i) - 55
    answer += int(i) * val
    val *= 16

print(answer)