'''
N, K = map(int, input().split())

seq = []
people = list(range(1, N + 1))

i, j = 0, 0
while people:
    i += K - j - 1
    j += 1
    if len(people) <= i:
        i -= len(people)
        j = 0
    seq.append(people.pop(i))

print(seq)
'''