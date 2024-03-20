def luckyStone(x, y):
    if y % x == 0:
        return y // x
    else:
        return y // x + 1


A_OP, A_LP = map(int, input().split())
B_OP, B_LP = map(int, input().split())

A, B = luckyStone(A_OP, B_LP), luckyStone(B_OP, A_LP)

if A < B:
    print("PLAYER A")
elif A > B:
    print("PLAYER B")
else:
    print("DRAW")
