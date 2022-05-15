def get_stat(num, s):
    res = 0
    for i in s:
        res += S[i][num] + S[num][i]
    return res

def dfs(depth, start_stat, link_stat):
    global answer

    if depth == n // 2:
        temp = []

        r = 0
        for i in range(start[-1] + 1, n):
            r += get_stat(i, link + temp)
            temp.append(i)

        answer = min(answer, abs(start_stat - (link_stat + r)))

        return

    for i in range(start[-1] + 1, n):
        stat = get_stat(i, start)
        start.append(i)
        start_stat += stat

        dfs(depth + 1, start_stat, link_stat)

        start.pop()
        start_stat -= stat
        link_stat += get_stat(i, link)
        link.append(i)

    for i in range(start[-1] + 1, n):
        link.remove(i)

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

start, link = [0], []
answer = float('inf')

dfs(1, 0, 0)

print(answer)