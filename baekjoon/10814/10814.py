members = []
for i in range(int(input())):
    age, name = input().split()
    members.append([int(age), name])
members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)