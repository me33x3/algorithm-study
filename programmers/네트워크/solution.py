from collections import deque

def solution(n, computers):
    network = []
    conn = dict(zip(list(range(n)), [[j for j, v in enumerate(com) if v == 1 and i != j] for i, com in enumerate(computers)]))

    while conn:
        queue = deque([list(conn.keys())[0]])
        net = []

        while queue:
            node = queue.popleft()

            if node not in net:
                queue += set(conn[node]) - set(net)
                del conn[node]
                net.append(node)

        network.append(net)

    return len(network)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))