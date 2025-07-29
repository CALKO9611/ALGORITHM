N, M = map(int, input().split())
bus_number = list(map(int, input().split()))
bus_cost = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(M - 1):
    S, E = bus_number[i], bus_number[i + 1]
    result += bus_cost[S - 1][E - 1]  # 0번째 인덱스를 고려한 -1

print(result)
