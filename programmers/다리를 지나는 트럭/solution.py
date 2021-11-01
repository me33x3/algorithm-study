def solution(bridgth_length, weight, truck_weights):
    sec, curr_weight = 1, truck_weights.pop(0)
    on_bridge, move = [curr_weight], [1]

    while on_bridge:
        if move:
            for i in range(len(move)):
                move[i] += 1

            if move[0] > bridgth_length:
                move.pop(0)
                curr_weight -= on_bridge.pop(0)

        if truck_weights:
            if (weight - curr_weight) >= truck_weights[0]:
                on_bridge.append(truck_weights.pop(0))
                curr_weight += on_bridge[-1]
                move.append(1)

        sec += 1

    return sec

print(solution(2, 10, [7,4,5,6])) # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # 110