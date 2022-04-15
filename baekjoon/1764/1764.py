import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = set([input().strip() for _ in range(n)])
m_list = set([input().strip() for _ in range(n)])

dup = sorted(n_list & m_list)
print(len(dup))
for name in dup:
    print(name)