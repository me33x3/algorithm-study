res, answer = 1, 0
for i in range(1, int(input()) + 1):
    res *= i

for num in str(res)[::-1]:
    if num == '0':
        answer += 1
    else:
        break
print(answer)