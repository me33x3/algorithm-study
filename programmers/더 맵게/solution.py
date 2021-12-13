import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        i = heapq.heappop(scoville)
        try:
            j = heapq.heappop(scoville)
        except:
            answer = -1
            break
        heapq.heappush(scoville, i + j * 2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2