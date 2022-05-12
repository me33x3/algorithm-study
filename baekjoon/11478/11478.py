S = input()
n = len(S)

sub = set()
while n > 0:
    for i in range(len(S) - n + 1):
        sub.add(S[i:i + n])
    n -= 1

print(len(sub))