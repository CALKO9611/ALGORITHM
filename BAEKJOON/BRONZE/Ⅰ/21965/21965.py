N = int(input())
A = list(map(int, input().split()))
check = True  # 산이 맞는지 아닌지 확인 변수
shape = True  # 올라가다 내려오고 다시 올라가는지 확인 변수

for i in range(N - 1):
    if A[i] < A[i + 1]:
        if shape == False:  # 올라가고 있으나 한 번 내려간 적이 있다면 break
            check = False
            break
    elif A[i] == A[i + 1]:  # 높이가 같으면 break
        check = False
        break
    else:  # 올라가다가 감소할 때
        shape = False

if check:  # 산이면 YES, 아니면 NO
    print("YES")
else:
    print("NO")
