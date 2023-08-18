colors = set()

for _ in range(2):
    parents = input().split()
    for p in parents:
        colors.add(p)

birdColor_lst = sorted(list(colors))  # 사전 순 정렬

for i in birdColor_lst:
    for j in birdColor_lst:
        print(i, j)
