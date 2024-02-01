N = int(input())
d = N // 2  # 2로 나눈 몫

if N % 2 != 0:  # 홀수
    print("*" * N)  # 첫 번째 줄
    print(" " * d + "*")  # 두 번째 줄
    for i in range(d):  # 나머지 줄
        print(" " * (d - i - 1) + "*" + " " * (i * 2 + 1) + "*")
else:  # 짝수
    print("I LOVE CBNU")
