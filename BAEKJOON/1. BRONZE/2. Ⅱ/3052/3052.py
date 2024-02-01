lst = []
result = []
for _ in range(10):
    lst.append(int(input()))
for i in lst:
    result.append(i % 42)

result = set(result)

print(len(result))
