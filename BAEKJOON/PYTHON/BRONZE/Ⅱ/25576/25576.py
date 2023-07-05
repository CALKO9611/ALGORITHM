import sys

input = sys.stdin.readline
N, M = map(int, input().split())
streamer = list(map(int, input().split()))
cnt = 0

for _ in range(N - 1):
    bad = 0
    viewers = list(map(int, input().split()))
    for i in range(M):
        bad += abs(streamer[i] - viewers[i])
    if bad > 2000:
        cnt += 1

if (N - 1) / 2 <= cnt:
    print("YES")
else:
    print("NO")
