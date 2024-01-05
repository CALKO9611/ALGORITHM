N, X = map(int, input().split())
barracks = list(map(int, input().split()))

if sum(barracks) % X == 0:
    print(1)
else:
    print(0)
