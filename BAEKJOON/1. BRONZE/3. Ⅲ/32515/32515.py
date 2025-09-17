N = int(input())
JB = list(input())  # Jeonghoon Basis
JK = list(input())  # Jeonghoon Key
IB = list(input())  # Ian Basis
IK = list(input())  # Ian Key

check = True
result = ""

for i in range(N):
    if JB[i] == IB[i]:
        if JK[i] != IK[i]:
            check = False
            break
        else:
            result += JK[i]

print(result if check else "htg!")
