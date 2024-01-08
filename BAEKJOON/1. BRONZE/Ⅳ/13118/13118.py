pos = list(map(int, input().split()))
apple = list(map(int, input().split()))

if apple[0] in pos:
    print(pos.index(apple[0]) + 1)
else:
    print(0)
