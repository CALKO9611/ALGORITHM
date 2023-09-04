N = int(input())
result = []

for _ in range(N):
    dices = list(map(int, input().split()))
    set_dices = list(set(dices))
    tmp = []
    for i in set_dices:
        tmp.append(dices.count(i))

    if len(set_dices) == 1:  # 1번 조건
        result.append(50000 + set_dices[0] * 5000)
    elif len(set_dices) == 2:  # 2, 3번 조건
        if len(tmp) == 2:  # 위에서 만든 tmp 리스트로 2, 3번 차이 판별
            if tmp[0] != tmp[1]:  # 2번 조건
                result.append(10000 + set_dices[tmp.index(max(tmp))] * 1000)
            else:  # 3번 조건
                result.append(2000 + set_dices[0] * 500 + set_dices[1] * 500)
    elif len(set_dices) == 3:  # 4번 조건
        result.append(1000 + set_dices[tmp.index(max(tmp))] * 100)
    elif len(set_dices) == 4:  # 5번 조건
        result.append(max(dices) * 100)

print(max(result))  # 최댓값 출력
