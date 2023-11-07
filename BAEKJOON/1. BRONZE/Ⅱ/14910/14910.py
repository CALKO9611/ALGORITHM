N = list(map(int, input().split()))
tmp = sorted(N)

if N == tmp:
    print("Good")
else:
    print("Bad")