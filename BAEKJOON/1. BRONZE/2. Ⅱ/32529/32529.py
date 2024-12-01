import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list((map(int, input().split())))[::-1]
PrefixSum = [0] * (N + 1)  # 누적합 리스트

for i in range(1, N + 1):
    PrefixSum[i] = PrefixSum[i - 1] + A[i]

if PrefixSum[-1] < M:
    print(-1)
else:
    for i in range(1, N + 1):
        if PrefixSum[i] >= M:
            print(N - i + 1)
            break
