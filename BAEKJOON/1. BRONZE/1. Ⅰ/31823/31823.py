# https://www.acmicpc.net/problem/31823
# 31823번 악질검거 브론즈 1단계 / 블로그 및 깃허브 업로드 하기

N, M = map(int, input().split())
countStreak = set()  # 최대 리버스-스트릭
KPSC_List = []  # 최장 리버스-스트릭, 이름을 저장할 리스트

for _ in range(N):
    record = input().split()
    streak, name = record[:M], record[M]

    maxStreak = 0  # 최장 리버스 스트릭 확인
    tmp = 0
    for i in streak:
        if i == ".":  # 문제를 풀었으면
            tmp += 1  # tmp에 1을 더함
        else:  # 그렇지 않다면
            tmp = 0  # 0으로 초기화
        maxStreak = max(maxStreak, tmp)  # 최장 리버스스트릭 업데이트

    countStreak.add(maxStreak)  # 최대 리버스-스트릭을 set 집합에 추가
    KPSC_List.append([maxStreak, name])  # 최장 리버스-스트릭과 이름을 저장

print(len(countStreak))
for K in KPSC_List:
    print(*K)
