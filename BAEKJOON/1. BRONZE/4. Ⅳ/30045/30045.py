N = int(input())
result = 0

for _ in range(N):
    S = input()
    if "01" in S or "OI" in S:
        result += 1

print(result)
