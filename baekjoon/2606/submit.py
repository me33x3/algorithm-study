from collections import deque

N = int(input())
conn = int(input())

network = [[] for _ in range(N)]
for i in range(conn):
    com1, com2 = map(int, input().split())
    network[com1 - 1].append(com2)
    network[com2 - 1].append(com1)

def bfs():
    infection = [1]
    queue = deque(infection)

    while queue:
        com = queue.popleft()
        for c in network[com-1]:
            if c not in infection:
                queue.append(c)
                infection.append(c)

    print(len(infection) - 1)

bfs()