P = int(input())
N = int(input())
stone = [0] * 100

for _ in range(N):
    num, d = input().split()
    if d == "R":  # 방향이 오른쪽이면
        for i in range(int(num), len(stone)):
            stone[i] += 1
    if d == "L":  # 방향이 왼쪽이면
        for j in range(0, int(num) - 1):
            stone[j] += 1

blue = 0
red = 0
green = 0

for k in range(100):
    if stone[k] % 3 == 0:  # 나머지가 0이면
        blue += 1  # 파란돌 추가
    elif stone[k] % 3 == 1:  # 나머지가 1이면
        red += 1  # 빨간돌 추가
    else:  # 그 외
        green += 1  # 초록돌 추가

print("{:.2f}".format(P * (blue / 100)))
print("{:.2f}".format(P * (red / 100)))
print("{:.2f}".format(P * (green / 100)))
