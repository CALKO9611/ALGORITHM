# 백준 34552번 디딤돌 장학금
# 깃헙 및 블로그 업로드하자
# https://www.acmicpc.net/problem/34552

scholarship = list(map(int, input().split()))
N = int(input())
result = 0

for _ in range(N):
    B, L, S = input().split()

    if float(L) >= 2 and int(S) >= 17:
        result += scholarship[int(B)]

print(result)
