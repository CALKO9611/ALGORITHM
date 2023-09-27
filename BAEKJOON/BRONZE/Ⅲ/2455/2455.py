result = 0  # 현재 탑승 사람 수
max_people = 0  # 최대 사람 수 저장할 변수
for _ in range(4):
    d, u = map(int, input().split())
    tmp = result - d + u  # 현재 사람 수 - 내리는 사람 + 탑승한 사람
    max_people = max(max_people, tmp)
    result = tmp  # 현재 탑승 사람 수 다시 저장

print(max_people)
