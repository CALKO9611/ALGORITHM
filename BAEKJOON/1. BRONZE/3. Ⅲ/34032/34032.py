N = int(input())
S = list(input())
half = N // 2

if N % 2 != 0:
    half += 1

if S.count("O") >= half:
    print("Yes")
else:
    print("No")
