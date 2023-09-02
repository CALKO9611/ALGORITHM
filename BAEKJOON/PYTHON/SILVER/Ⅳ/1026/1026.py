N = int(input())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

A_lst = sorted(A_lst, reverse=True)  # 내림차순 정렬
B_lst.sort()  # 오름차순 정렬

result = 0
for i in range(N):
    result += A_lst[i] * B_lst[i]
print(result)
