import sys
INF = sys.maxsize

n = int(input())
solutions = list(map(int, input().split()))

i, j = 0, n - 1
val = INF
answer = []

while i < j:
    tmp = solutions[i] + solutions[j]

    if val >= abs(tmp):
        val = abs(tmp)
        answer = [solutions[i], solutions[j]]

    if tmp < 0:
        i += 1
    elif tmp > 0:
        j -= 1
    else:
        break

print(answer[0], answer[1])