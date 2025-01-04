import sys

input = sys.stdin.readline
N, M = map(int, input().split())
clap = [[0] * (M + 1)]
S = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    clap_row = [0] + list(map(int, input().split()))
    clap.append(clap_row)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + clap[i][j]


A = int(input())
max_result = 0

for i in range(len(S[-1]) - A):
    result = S[-1][i + A] - S[-1][i]
    max_result = max(result, max_result)

print(max_result)
