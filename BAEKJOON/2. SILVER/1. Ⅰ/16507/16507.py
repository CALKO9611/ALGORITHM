import sys

input = sys.stdin.readline

R, C, Q = map(int, input().split())

A = [[0] * (C + 1)]
D = [[0] * (C + 1) for _ in range(R + 1)]

for _ in range(R):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, R + 1):
    for j in range(1, C + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    result = D[r2][c2] - D[r1 - 1][c2] - D[r2][c1 - 1] + D[r1 - 1][c1 - 1]
    print(result // cnt)
