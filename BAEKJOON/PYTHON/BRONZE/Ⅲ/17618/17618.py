N = int(input())
result = 0

for i in range(1, N + 1):
    tmp = 0
    for t in str(i):
        tmp += int(t)

    if i % tmp == 0:
        result += 1

print(result)
