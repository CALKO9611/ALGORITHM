N = int(input())

result_1 = 0  # 1부터 N까지 수의 합
result_2 = 0  # 1부터 N까지 수의 세제곱의 합

for i in range(1, N + 1):
    result_1 += i
    result_2 += i**3

print(result_1)
print(result_1**2)  # 1부터 N까지 수의 합을 제곱한 수
print(result_2)
