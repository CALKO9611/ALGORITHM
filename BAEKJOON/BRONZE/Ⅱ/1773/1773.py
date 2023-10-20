import sys

input = sys.stdin.readline
N, C = map(int, input().split())
firework = [0] * (C + 1)

for _ in range(N):
    time = int(input())
    if time == 1:
        print(C)
        exit()  # 출력 후 16번 째 print를 막기 위한 프로그램 종료
    else:
        for i in range(time, C + 1, time):
            firework[i] = 1

print(sum(firework))
