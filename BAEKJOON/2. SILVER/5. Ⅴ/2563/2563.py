import sys

input = sys.stdin.readline

# 가로, 세로의 크기가 100인 도화지 2차원 배열 A
A = [[0] * 101 for _ in range(101)]
N = int(input())  # 색종이의 수

for _ in range(N):
    x, y = map(int, input().split())

    for row in range(x, x + 10):
        for col in range(y, y + 10):
            A[row][col] = 1

result = 0
for a in A:
    result += a.count(1)

print(result)
