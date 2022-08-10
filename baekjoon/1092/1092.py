N = int(input())
cranes = sorted(map(int, input().split()), reverse=True)

M = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

cnt = 0

while boxes:
    if cranes[0] < boxes[0]:
        cnt = -1
        break

    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break

    cnt += 1

print(cnt)