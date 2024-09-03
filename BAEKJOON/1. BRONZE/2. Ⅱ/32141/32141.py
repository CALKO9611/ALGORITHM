N, H = map(int, input().split())
d = [0] + list(map(int, input().split()))
S = [0] * (N + 1)  # 공격력 누적합 배열

for k in range(1, N + 1):
    S[k] = S[k - 1] + d[k]

if H > S[-1]:
    print(-1)
else:
    for i in range(1, N + 1):
        if H <= S[i]:
            print(i)
            break
