T = int(input())

for _ in range(T):
    A, B = input().split()

    correct_mul = int(A) * int(B)

    if len(A) < len(B):
        A = "1" * (len(B) - len(A)) + A
    elif len(A) > len(B):
        B = "1" * (len(A) - len(B)) + B

    wrong_mul = ""

    for i in range(len(A)):
        wrong_mul += str(int(A[i]) * int(B[i]))

    print(1 if correct_mul == int(wrong_mul) else 0)
