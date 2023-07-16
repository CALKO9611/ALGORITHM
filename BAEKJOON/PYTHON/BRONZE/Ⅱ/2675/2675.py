for _ in range(int(input())):
    R, S = input().split()
    result = ""
    for i in S:
        result += i * int(R)
    print(result)
