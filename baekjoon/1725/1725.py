n = int(input())
data = [int(input()) for _ in range(n)]
stack = []
answer = 0

for i in range(n):
    while stack and data[stack[-1]] > data[i]:
        width, height = i, data[stack[-1]]
        stack.pop()
        if stack:
            width -= stack[-1] + 1
        answer = max(answer, width * height)
    stack.append(i)

while stack:
    width, height = n, data[stack[-1]]
    stack.pop()
    if stack:
        width -= stack[-1] + 1
    answer = max(answer, width * height)

print(answer)