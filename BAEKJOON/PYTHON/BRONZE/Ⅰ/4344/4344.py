for _ in range(int(input())):
    score = list(map(int, input().split()))
    N = score[0]
    score = score[1:]

    avg = sum(score) / N
    student = 0
    for i in score:
        if i > avg:
            student += 1

    rate = student / N * 100
    print("{:.3f}%".format(rate))
