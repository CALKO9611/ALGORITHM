T = int(input())

for _ in range(T):
    expression = list(map(str, input().split()))

    if expression[1] == "+":
        result = int(expression[0]) + int(expression[2])
    elif expression[1] == "-":
        result = int(expression[0]) - int(expression[2])
    elif expression[1] == "*":
        result = int(expression[0]) * int(expression[2])
    elif expression[1] == "/":
        result = int(expression[0]) / int(expression[2])

    if result == int(expression[4]):
        print("correct")
    else:
        print("wrong answer")
