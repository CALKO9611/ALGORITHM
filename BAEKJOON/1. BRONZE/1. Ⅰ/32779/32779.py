Q = int(input())

for _ in range(Q):
    a, m = map(int, input().split())
    # 상수 0.00176을 사용하여 계산
    cost = int(a * m * 0.00176)
    print(cost)
