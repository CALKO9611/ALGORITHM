Q = int(input())
result = 0
check = True

while Q:
    a, b = map(int, input().split())
    if a == 1:
        result += b
    elif a == 2:
        result -= b

    if result < 0:
        check = False

    Q -= 1

if check:
    print("See you next month")
else:
    print("Adios")
