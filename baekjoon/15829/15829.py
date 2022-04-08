L = int(input())
S = input()

answer = 0
for i in range(L):
    answer += (ord(S[i]) - 96) * (31 ** i)
print(answer % 1234567891)