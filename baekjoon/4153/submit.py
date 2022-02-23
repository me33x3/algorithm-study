while True:
    legs = list(map(int, input().split()))

    if sum(legs) == 0:
        break

    legs.sort()
    print('right' if legs[0] ** 2 + legs[1] ** 2 == legs[2] ** 2 else 'wrong')