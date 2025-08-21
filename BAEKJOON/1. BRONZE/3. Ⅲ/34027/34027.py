T = int(input())

for _ in range(T):
    N = int(input())

    if (N**0.5) % 1 == 0:
        print(1)
    else:
        print(0)
