import sys

input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
S = [0] * (N + 1)

for k in range(1, N + 1):
    S[k] = S[k - 1] + A[k]

M = int(input())

for _ in range(M):
    i, j = map(int, input().split())
    result = S[j] - S[i - 1]
    print(result)
