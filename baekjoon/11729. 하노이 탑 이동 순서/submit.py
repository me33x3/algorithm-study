def hanoi(n, f, b, t):
    if n == 1:
        answer.append([f, t])
        return

    hanoi(n - 1, f, t, b)
    answer.append([f, t])
    hanoi(n - 1, b, f, t)

answer = []
hanoi(int(input()), 1, 2, 3)
print(len(answer))
for f, t in answer:
    print(f, t)