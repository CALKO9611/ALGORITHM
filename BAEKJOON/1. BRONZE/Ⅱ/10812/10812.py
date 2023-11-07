N, M = map(int, input().split())
Basket = [i + 1 for i in range(N)]  # 1~N까지의 리스트

for _ in range(M):
    i, j, k = map(int, input().split())
    Basket[i - 1 : j] = Basket[k - 1 : j] + Basket[i - 1 : k - 1]

# print(*리스트명)을 통해 한 줄 출력
print(*Basket)
