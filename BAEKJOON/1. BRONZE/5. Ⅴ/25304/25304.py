X = int(input())  # 영수증에 적힌 총 금액
N = int(input())  # 영수증에 적힌 구매한 물건의 종류의 수

price = 0  # 가격이 일치하는지 확인하기 위한 변수
for _ in range(N):
    a, b = map(int, input().split())  # 물건의 가격 a, 개수 b
    price += a * b

if X == price:
    print("Yes")
else:
    print("No")
