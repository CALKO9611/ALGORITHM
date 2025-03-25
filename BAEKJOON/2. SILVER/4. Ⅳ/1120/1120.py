A, B = input().split()
N = len(B) - len(A) + 1
result = 51

for i in range(N):
    cnt = 0
    for x, y in zip(A, B[i : i + len(A)]):
        if x != y:
            cnt += 1

    result = min(result, cnt)

print(result)
