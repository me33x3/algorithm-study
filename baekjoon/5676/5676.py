import sys
from math import ceil, log2
input = sys.stdin.readline


def check(num):
    if num > 0:
        num = 1
    elif num <0:
        num = -1
    return num


def init(start, end, node):
    if start == end:
        tree[node] = num_list[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] * tree[node * 2 + 1]


def update(start, end, node, index):
    if not start <= index <= end:
        return

    if start == end:
        tree[node] = num_list[index]
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, index)
    update(mid + 1, end, node * 2 + 1, index)
    tree[node] = tree[node * 2] * tree[node * 2 + 1]


def query(start, end, node, left, right):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) * query(mid + 1, end, node * 2 + 1, left, right)


while True:
    try :
        n, k = map(int, input().split())
        num_list = [0]

        for num in list(map(int, input().split())):
            num_list.append(check(num))

        answer = ''
        tree = [0] * 2 ** (ceil(log2(n)) + 1)
        init(1, n, 1)

        for _ in range(k):
            cmd, a, b = input().split()
            a, b = int(a), int(b)

            if cmd[0] == 'C':
                b = check(b)
                if b != num_list[a]:
                    num_list[a] = b
                    update(1, n, 1, a)
            else:
                x = query(1, n, 1, a, b)
                if x > 0: answer += '+'
                elif x < 0: answer += '-'
                else: answer += '0'
        print(answer)
    except Exception:
        break