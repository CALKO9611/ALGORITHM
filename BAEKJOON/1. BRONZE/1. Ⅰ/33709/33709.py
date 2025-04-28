N = int(input())
slogan = input()
separator = ["|", ":", "#"]

for s in separator:
    slogan = slogan.replace(s, ".")

numberList = slogan.split(".")
result = 0

for n in numberList:
    result += int(n)

print(result)
