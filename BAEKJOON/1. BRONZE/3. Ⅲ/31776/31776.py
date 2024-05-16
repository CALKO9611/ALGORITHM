N = int(input())
result = 0

for _ in range(N):
    solve = list(map(int, input().split()))

    if sum(solve) == -3:  # 만약 모든 문제를 해결하지 않은 팀이라면 다음 팀으로 넘어감
        continue

    for i in range(3):  # 각 문제의 해결 시간이 -1이라면, 최대 시간으로 설정
        if solve[i] == -1:
            solve[i] = 121

    if solve[0] <= solve[1] <= solve[2]:
        result += 1

print(result)
