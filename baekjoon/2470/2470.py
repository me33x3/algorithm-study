N = int(input())
sol = sorted(list(map(int, input().split())))
f, b = 0, N - 1
t_f, t_b = 0, N - 1

min = float('inf')
while f < b:
    mix = sol[f] + sol[b]

    if abs(mix) < min:
        min = abs(mix)
        t_f, t_b = f, b

    if mix < 0:
        f += 1
    elif mix > 0:
        b -= 1
    else:
        break

print(sol[t_f], sol[t_b])