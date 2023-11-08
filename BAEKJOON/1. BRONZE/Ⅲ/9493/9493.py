while 1:
    M, A, B = map(int, input().split())
    if M == A == B == 0:
        break
    time = round(abs(3600 * (M / A) - 3600 * (M / B)))

    s = time % 60
    time //= 60

    m = time % 60
    time //= 60

    print("{}:{:02}:{:02}".format(time, m, s))
