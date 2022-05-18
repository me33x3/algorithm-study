n, m = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])

parties = []
for _ in range(m):
    parties.append(set(list(map(int, input().split()))[1:]))

for _ in range(m):
    for party in parties:
        if party & truth:
            truth |= party

cnt = 0
for party in parties:
    if not party & truth:
        cnt += 1

print(cnt)