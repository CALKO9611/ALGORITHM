N = int(input())
Bus = []
# result1 → 진주로 가는 교통편의 요금
# result2 → 진주로 가는 교통편보다 비싼 교통편의 개수
result1 = result2 = 0

for _ in range(N):
    D, C = input().split()
    Bus.append([D, int(C)])
    if D == "jinju":
        result1 = int(C)

for i in Bus:
    if i[1] > result1:
        result2 += 1

print(result1)
print(result2)
