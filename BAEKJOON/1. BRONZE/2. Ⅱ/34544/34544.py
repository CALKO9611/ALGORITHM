N = int(input())
result = 1

for _ in range(N):
    A, B = map(int, input().split())

    if A < 0 and B > 0:
        result += B - A - 1
    elif A > 0 and B < 0:
        result += B - A + 1
    else:
        result += B - A

print(result if result > 0 else result - 1)
