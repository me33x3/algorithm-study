from collections import deque

for _ in range(int(input())):
    n, i = map(int, input().split())
    work = list(map(int, input().split()))
    queue = deque(work)
    t = 0

    while queue:
        document = queue.popleft()

        if document == max(work):
            work.remove(document)
            t += 1
            if i == 0:
                break
        else:
            queue.append(document)

        i = n - t -1 if i == 0 else i - 1

    print(t)