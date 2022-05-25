dividend, divisor = 0, 0
score = dict(zip(['A', 'B', 'C', 'D', 'F'], [4, 3, 2, 1, 0]))

for _ in range(20):
    sub, credit, grade = input().split()
    credit = float(credit)

    if grade == 'P':
        continue

    if grade != 'F':
        p, q = list(grade)
        dividend += credit * (score[p] + (0.5 if q == '+' else 0))

    divisor += credit

print(dividend / divisor)