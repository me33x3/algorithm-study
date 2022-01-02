N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

w = []
for i in range(N):
    w.append(ropes[i] * (i + 1))

print(max(w))