import sys

input = sys.stdin.readline
N = int(input())
A = [0]

for i in range(1, N + 1):
    time = sum(list(map(int, input().split()))[1:])
    A.append(time)

A.sort()
S1 = [0] * (N + 1)
S2 = [0] * (N + 1)

for j in range(1, N + 1):
    S1[j] = S1[j - 1] + A[j]
    S2[j] = S2[j - 1] + S1[j]

print(S2[-1])
