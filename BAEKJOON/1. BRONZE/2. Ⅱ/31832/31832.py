# 알파벳 대문자, 알파벳 소문자, 숫자, 하이픈의 아스키코드는 각각 65-90, 97-122, 48-57, 45이다.


# 첫 번째 조건
def conditionOne(teamName):
    upperCase, lowerCase = 0, 0
    for i in teamName:
        if 65 <= ord(i) <= 90:
            upperCase += 1
        elif 97 <= ord(i) <= 122:
            lowerCase += 1

    return lowerCase >= upperCase


# 두 번째 조건
def conditionTwo(teamName):
    return len(teamName) <= 10


# 세 번째 조건
def conditionThree(teamName):
    letterCheck = False
    for i in teamName:
        if ord(i) < 48 or ord(i) > 57:
            letterCheck = True
    return letterCheck


N = int(input())
result = ""

for _ in range(N):
    S = input()

    if conditionOne(S) and conditionTwo(S) and conditionThree(S):  # 세 조건 모두 참이면
        result = S


print(result)
