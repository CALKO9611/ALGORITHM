import sys

input = sys.stdin.readline
N, M = map(int, input().split())
package = []
piece = []
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)

min_pk = min(package)
min_pc = min(piece)

if N <= 6:  # 필요한 기타줄이 6개 이하
    result = min(min_pk, min_pc * N)
else:  # 그 외
    if N % 6 == 0:  # 필요한 기타줄이 6으로 나누어 떨어지는 지 판별
        tmp = N // 6
    else:
        tmp = (N // 6) + 1

    result = min(tmp * min_pk, N * min_pc)  # 패키지로만 구매, 낱개로만 구매의 최소값
    for i in range(1, tmp):  # 패키지, 낱개를 섞어서 샀을 때 최소값이 나오면 저장
        result = min(result, min_pk * i + (N - i * 6) * min_pc)

print(result)
