N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
M_lst = list(map(int, input().split()))

for i in range(N):
    tmp = []
    x = N_lst[i]
    for j in range(M):
        if x == M_lst[j]:  # 같으면
            x = 0  # 노란색 꽃
            tmp.append(x)
        else:  # 다르면
            x = 1  # 빨간색 꽃
            tmp.append(x)
    M_lst = tmp  # tmp에 저장된 값을 M에 저장

print(M_lst[-1])  # 맨 마지막에 심어진 꽃의 색을 출력
