# 정수, 소수 판별 함수
def numChange(x):
    if "." in x:
        return float(x)
    else:
        return int(x)


calculation = input().split()
result = numChange(calculation[0])

# 계산기 작동
for i in range(1, len(calculation), 2):
    operator = calculation[i]
    operand = numChange(calculation[i + 1])

    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/":
        result /= operand


# 결과 소수점 셋째 자리까지 반올림
result_str = "{:.3f}".format(result)


# 계산기 출력
print("=================")
print("|SASA CALCULATOR|")
print("|" + " " * (15 - len(result_str)) + result_str + "|")
print("-----------------")
print("|               |")
print("| AC         /  |")
print("| 7  8  9    *  |")
print("| 4  5  6    -  |")
print("| 1  2  3    +  |")
print("|    0  .    =  |")
print("=================")
