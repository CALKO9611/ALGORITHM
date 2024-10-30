woodCarving = list(map(int, input().split()))

while woodCarving != [1, 2, 3, 4, 5]:
    for i in range(4):
        if woodCarving[i] > woodCarving[i + 1]:
            woodCarving[i], woodCarving[i + 1] = woodCarving[i + 1], woodCarving[i]
            print(*woodCarving)  # 리스트 한 줄 출력
