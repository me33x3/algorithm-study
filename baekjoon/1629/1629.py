def solve(n):
    if n == 1:
        return A % C
    temp = solve(n // 2)
    if n % 2:
        return temp * temp * A % C
    else:
        return temp * temp % C

A, B ,C = map(int, input().split())
print(solve(B))