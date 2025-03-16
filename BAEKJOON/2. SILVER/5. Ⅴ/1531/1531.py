N, M = map(int, input().split())
paper = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2 + 1):
        for col in range(y1, y2 + 1):
            paper[row][col] += 1

# 보이지 않는 그림의 개수 세기
for p in paper:
    result += len([x for x in p if x > M])

print(result)
