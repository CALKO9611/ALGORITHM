T = int(input())

for _ in range(T):
    K = int(input())  # 수강생 수
    K_Number = list(map(int, input().split()))  # 수강생의 참가 번호
    N = int(input())  # 대회 참가자 수

    record_time = 1441  # 24시간 정도의 최대값 설정
    receive_certificate = 0

    for _ in range(N):
        n, h, m = map(int, input().split())

        if h == m == -1:  # 대회를 중간에 포기한 경우는 continue
            continue

        record = (h * 60) + m  # 분으로 통일

        if n in K_Number and record <= 360:
            receive_certificate += 1

            if record < record_time:
                recorder = n  # 기록 좋은 수강생의 참가 번호 저장
                record_time = record  # 기록 갱신

    print(recorder, receive_certificate)
