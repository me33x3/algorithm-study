change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
i, answer = 0, 0

while change:
    t = change // coins[i]
    change -= t * coins[i]
    answer += t
    i += 1

print(answer)