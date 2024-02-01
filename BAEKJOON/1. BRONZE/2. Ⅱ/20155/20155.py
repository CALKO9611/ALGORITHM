N, M = map(int, input().split())
brand = list(map(int, input().split()))
result = [0] * (M + 1)

for i in brand:
    result[i] += 1

print(max(result))
