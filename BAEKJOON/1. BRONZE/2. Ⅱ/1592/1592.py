N, M, L = map(int, input().split())
ball = [1] + [0] * (N - 1)
idx = 0

if M == 1:
    print(0)
else:
    while 1:
        if ball[idx] % 2 == 1:  # 공을 받은 횟수 : 홀수
            idx += L
        else:  # 공을 받은 횟수 : 짝수
            idx -= L

        # 원형 순환을 위한 idx 값 조절
        if idx >= N:
            idx %= N
        elif idx < 0:
            idx += N

        ball[idx] += 1

        if ball[idx] == M:
            break

    print(sum(ball) - 1)
