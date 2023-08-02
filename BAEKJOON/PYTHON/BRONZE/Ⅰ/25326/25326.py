n, m = map(int, input().split())
lst = []

for _ in range(n):  # 학생들의 선호도
    lst.append(input().split())

for _ in range(m):  # 질의
    sfc = input().split()
    cnt = 0
    for i in lst:
        check = 0
        for j in range(3):  # subject, fruit, color 일치 판별
            if sfc[j] == "-":
                check += 1
                continue
            if sfc[j] == i[j]:
                check += 1
        if check == 3:
            cnt += 1
    print(cnt)
