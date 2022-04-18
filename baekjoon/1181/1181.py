for word in sorted(set(input() for _ in range(int(input()))), key=lambda x:(len(x), x)):
    print(word)