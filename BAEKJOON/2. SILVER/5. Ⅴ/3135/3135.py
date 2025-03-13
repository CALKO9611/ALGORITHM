A, B = map(int, input().split())
N = int(input())
result = abs(A - B)

for _ in range(N):
    frequency = int(input())
    result = min(abs(frequency - B) + 1, result)

print(result)
