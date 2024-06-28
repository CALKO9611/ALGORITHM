N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = sum(a)

for i in b:
    if i == 0:
        continue
    result *= i

print(result)
