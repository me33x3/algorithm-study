a, b = input().split()
A = int(a.replace('6', '5')) + int(b.replace('6', '5'))
B = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(A, B)