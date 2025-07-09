import sys

input = sys.stdin.readline

N = int(input())
first_shooting = [list(map(int, input().split())) for _ in range(N)]
second_shooting = [list(map(int, input().split())) for _ in range(N)]

first_shooting.sort(key=lambda x: (x[0], x[1]))
second_shooting.sort(key=lambda x: (x[0], x[1]))

A = second_shooting[0][0] - first_shooting[0][0]
B = second_shooting[0][1] - first_shooting[0][1]

print(A, B)
