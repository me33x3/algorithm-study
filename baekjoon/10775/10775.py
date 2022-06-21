import sys
input = sys.stdin.readline

G, P = int(input()), int(input())
root = [g for g in range(G + 1)]
planes = []

for _ in range(P):
    planes.append(int(input()))

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

answer = 0
for plane in planes:
    docking = find(plane)

    if docking == 0:
        break

    answer += 1
    root[docking] = root[docking - 1]

print(answer)