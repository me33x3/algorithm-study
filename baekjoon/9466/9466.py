import sys
sys.setrecursionlimit(10 ** 6)

def dfs(num):
    global students

    v[num] = True
    team.append(num)
    select = arr[num]

    if not v[select]:
        dfs(select)
    elif select in team:
        students -= set(team[team.index(select):])

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    students = set(range(1, n + 1))
    v = [False] * (n + 1)

    for i in range(1, n + 1):
        if not v[i]:
            team = []
            dfs(i)

    print(len(students))