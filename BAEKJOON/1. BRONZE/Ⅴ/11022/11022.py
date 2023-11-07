T = int(input())
for t in range(1, T + 1):  # Case 번호 출력을 위해 1부터 시작했다.
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(t, A, B, A + B))
