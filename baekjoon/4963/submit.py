dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())

    if w and h:
        land, visited = [], []

        for _ in range(h):
            land.append(list(map(int, input().split())))
            visited.append([False for _ in range(w)])

        cnt = 0

        for i in range(h):
            for j in range(w):
                if land[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    stack = [[i, j]]

                    while stack:
                        loc = stack.pop()

                        for x, y in zip(dx, dy):
                            mx, my = loc[1] + x, loc[0] + y

                            if mx > -1 and mx < w and my > -1 and my < h:
                                if land[my][mx] and not visited[my][mx]:
                                    visited[my][mx] = True
                                    stack.append([my, mx])
                    cnt += 1
        print(cnt)

    else:
        break