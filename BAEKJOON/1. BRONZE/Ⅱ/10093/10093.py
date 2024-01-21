A, B = map(int, input().split())

if A > B:
    A, B = B, A

result = [i for i in range(A + 1, B)]

print(len(result))  # 리스트 개수 출력
print(*result)  # 리스트 한 줄 출력
