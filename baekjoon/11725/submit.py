from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs():
    parent = [-1] * (n + 1)
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parent[child] == -1:
                queue.append(child)
                parent[child] = node
    return parent

for i in bfs()[2:]:
    print(i)