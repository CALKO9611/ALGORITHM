S = input()
result = [1]

for i in range(1, len(S)):
    if ord(S[i]) > ord(S[i - 1]):
        result.append(result[i - 1] + 1)
    else:
        result.append(1)

print(sum(result))
