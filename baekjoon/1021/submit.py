from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))

deq = deque(list(range(1, n + 1)))
answer = 0

for num in nums:
    i = deq.index(num)
    t = 0

    if i <= len(deq) // 2:
        t = i
        while i > 0:
            deq.append(deq.popleft())
            i -= 1
        deq.popleft()
    else:
        t = len(deq) - i
        while i < len(deq) - 1:
            deq.appendleft(deq.pop())
            i += 1
        deq.pop()

    answer += t

print(answer)