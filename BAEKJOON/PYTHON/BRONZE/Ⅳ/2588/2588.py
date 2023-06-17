num1 = int(input())
num2 = input()

res3 = num1 * int(num2[2])
res4 = num1 * int(num2[1])
res5 = num1 * int(num2[0])
res6 = num1 * int(num2)

print(res3, res4, res5, res6, sep="\n")  # sep="\n"로 줄바꿈
