N = int(input())
timeTable = []
teacherTime = ""

for _ in range(N + 1):
    a, b = input().split()
    if b == "teacher":  # 선생님 도착 시간
        teacherTime = a
    else:  # 학생들 도착 시간
        timeTable.append(a)

startTime = input()  # 정해진 등교 시간

result = 0

for t in timeTable:
    if t >= startTime and t >= teacherTime:
        result += 1

print(result)
