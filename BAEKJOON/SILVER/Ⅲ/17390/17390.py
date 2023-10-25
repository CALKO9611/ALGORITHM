import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
S = [0] * (N + 1)
A.sort()

for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    result = S[R] - S[L - 1]
    print(result)
