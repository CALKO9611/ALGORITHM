N = int(input())
result = 0

for _ in range(N):
    name = input()
    if name[0] == "C":
        result += 1

print(result)
